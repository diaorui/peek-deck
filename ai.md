---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-16T13:15:39.754199+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 16, 2026 at 13:15 UTC  
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

**[Will access to AI compute become a real competitive advantage for startups?](https://www.reddit.com/r/artificial/comments/1rv7tr5/will_access_to_ai_compute_become_a_real/)**

Lately I’ve been thinking about how AI infrastructure spending is starting to feel less like normal cloud usage and more like long-term capital investment (similar to energy or telecom sectors). Big tech companies are already locking in massive compute capacity to support AI agents and large-scale inference workloads. If this trend continues, just having reliable access to compute could become a serious competitive advantage not just a backend technical detail. It also makes me wonder if startup funding dynamics could change. In the future, investors might care not only about product and model quality, but also about whether a startup has secured long-term compute access to scale safely. Of course, there’s also the other side of the argument. Hardware innovation is moving fast, new fabs are being built, and historically GPU shortages have been cyclical. So maybe this becomes less of a problem over time. But if AI agent usage grows really fast and demand explodes, maybe compute access will matter more than we expect. Curious to hear your thoughts: If you were building an AI startup today, would you focus more on improving model capability first, or on making sure you have long-term compute independence?

58m ago

---

**[ChatGPT ads still exclusive to the United States, OpenAI says no to global rollout just yet](https://www.reddit.com/r/artificial/comments/1rv69kf/chatgpt_ads_still_exclusive_to_the_united_states/)**

OpenAI introduced ads to ChatGPT last month, exclusive to users in the United States. Users online suspect a global rollout is coming soon.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/chatgpt-ads-still-exclusive-to-the-united-states-openai-says-no-to-global-rollout-just-yet/) • 2h ago

---

**[The bottleneck flipped: AI made execution fast and exposed everything around it that isn't](https://www.reddit.com/r/artificial/comments/1rusgb2/the_bottleneck_flipped_ai_made_execution_fast_and/)**

I've been tracking AI-driven layoffs for the past few months and something doesn't add up. Block cut 4,000 people (40% of workforce). Atlassian cut 1,600. Shopify told employees to prove AI can't do their job before asking for headcount. The script is always the same: CEO cites AI, stock ticks up. But then you look at the numbers. S&P Global found 42% of companies abandoned their AI initiatives in 2025, up from 17% the year before. A separate survey found 55% of CEOs who fired people "because of AI" already regret it. Klarna bragged AI could replace 700 employees, then quietly started hiring humans back when quality tanked. What I keep seeing across the research is that AI compressed execution speed dramatically; prototyping that took weeks now takes hours. But the coordination layer (approval chains, quarterly planning, review cycles) didn't speed up at all. The bottleneck flipped from "can we build it fast enough" to "does leadership know what to build and can they keep up with the teams building it." Companies are cutting the people who got faster while leaving the layer that didn't speed up intact. Monday.com is an interesting counter-example. Lost 80% of market value, automated 100 SDRs with AI, but redeployed them instead of firing them. Their CEO's reasoning: "Every time we eliminate one bottleneck, a new one emerges." I pulled together ten independent sources on this — engineers, economists, survey data, executives — and wrote it up here if anyone wants the full analysis with sources: https://news.future-shock.ai/ai-didnt-replace-workers-it-outran-their-managers/ Curious if anyone else is seeing this pattern in their orgs. Is the management layer adapting or just cutting headcount and calling it an AI strategy?

14h ago

---

**[Does anyone actually switch between AI models mid-conversation? And if so, what happens to your context?](https://www.reddit.com/r/artificial/comments/1rv6tfi/does_anyone_actually_switch_between_ai_models/)**

I want to ask something specific that came out of my auto-routing thread earlier. A lot of people said they prefer manual model selection over automation — fair enough. But that raised a question I haven't seen discussed much: When you manually switch from say ChatGPT to Claude mid-task, what actually happens to your conversation? Do you copy-paste the context across? Start fresh and re-explain everything? Or do you just not switch at all because it's too much friction? Because here's the thing — none of the major AI providers have any incentive to solve this problem. OpenAI isn't going to build a feature that seamlessly hands your conversation to Claude. Anthropic isn't going to make it easy to continue in Grok. They're competitors. The cross-model continuity problem exists precisely because no single provider can solve it. I've been building a platform where every model — GPT, Claude, Grok, Gemini, DeepSeek — shares the same conversation thread. I just tested it by asking GPT-5.2 a question about computing, then switched manually to Grok 4 and typed "anything else important." Three words. No context. Grok 4 picked up exactly where GPT-5.2 left off without missing a beat. My question for this community is genuinely whether that's a problem people actually experience. Do you find yourself wanting to switch models mid-task but not doing it because of the context loss? Or do most people just pick one model and stay there regardless? Trying to understand whether cross-model continuity is a real pain point or just something that sounds useful in theory.

1h ago

---

**[Kimi introduce Attention Residuals: replaces fixed residual connections with softmax attention](https://www.reddit.com/r/artificial/comments/1rv7k29/kimi_introduce_attention_residuals_replaces_fixed/)**

Introducing Attention Residuals: Rethinking depth-wise aggregation. Residual connections have long relied on fixed, uniform accumulation. Inspired by the duality of time and depth, Kimi introduce Attention Residuals, replacing standard depth-wise recurrence with learned, input-dependent attention over preceding layers. Enables networks to selectively retrieve past representations, naturally mitigating dilution and hidden-state growth. Introduces Block AttnRes, partitioning layers into compressed blocks to make cross-layer attention practical at scale. Serves as an efficient drop-in replacement, demonstrating a 1.25x compute advantage with negligible (<2%) inference latency overhead. Validated on the Kimi Linear architecture (48B total, 3B activated parameters), delivering consistent downstream performance gains. Paper link: https://github.com/MoonshotAI/Attention-Residuals/blob/master/Attention_Residuals.pdf

1h ago

---

**[I don't quite understand how useful AI is if conversations get long and have to be ended. Can someone help me figure out how to make this sustainable for myself? Using Claude Sonnet 4.6.](https://www.reddit.com/r/artificial/comments/1rv79uz/i_dont_quite_understand_how_useful_ai_is_if/)**

First, please tell me if there's a better forum to go to for newbies. I don't want to drag anyone down with basics. I'm starting to use AI more in my personal life, but the first problem I'm encountering is the conversations gets long and have to be compacted all the time, and eventually it isn't useful because compacting takes so damn long. I also don't want to start a new conversation because, I assume, that means I lose everything learned in the last one. (Or maybe this is where I'm wrong?) For a relatively simple example like below, how would I get around this? Let's suppose I want to feed in my regular bloodwork and any other low level complexity medical results and lay out some basic things to address, like getting my cholesterol a little lower and improving my gut health. I want the AI to be a companion helping me with my weekly meal planning and grocery shopping list. Maybe I tell it how much time I have to cook each day, what meals I'm thinking about/craving, or even suggest a menu that I like. AI would help me refine it around my nutritional goals and build my weekly grocery list. Every 24 hours I will feed it basic information, like how well my guts are performing, how well I sleep, how often I feel low energy, etc. Every few months I might add new test results. How do I do this, but not lose information every time the conversation gets long?

1h ago

---

**[WiFi-DensePose: AI Can Track Body Positions Through Walls](https://www.reddit.com/r/artificial/comments/1ruzmks/wifidensepose_ai_can_track_body_positions_through/)**

WiFi-DensePose: AI Can Track Body Positions Through Walls: Researchers have developed a system using standard WiFi signals to reconstruct full-body positions in real-time, through walls and in the dark, offering potential for privacy-preserving fall detection and health monitoring

8h ago

---

**[Anyone Else Have Those Weird Dreams Where Sobbing Future Generations Beg You To Change Course?](https://www.reddit.com/r/artificial/comments/1ruok4v/anyone_else_have_those_weird_dreams_where_sobbing/)**

The human subconscious is such an interesting thing. No matter how much you think you’ve got it figured out, it’ll always spit out the most random stuff. Take me, for example. After coming home from a long day at the world’s most groundbreaking artificial intelligence organization, I’ll go to bed and have the weirdest dreams where people from the future are sobbing and begging me to change course. Anyone else ever have these?

🔗 [The Onion](https://theonion.com/anyone-else-have-those-weird-dreams-where-sobbing-future-generations-beg-you-to-change-course/) • 16h ago

---

**[Building a multi-model AI platform with auto-routing — does automatic model selection actually appeal to users or do people always want manual control?](https://www.reddit.com/r/artificial/comments/1ruvk79/building_a_multimodel_ai_platform_with/)**

Been working on a personal project for a few months that has now launched — I can't share details to adhere to subreddit rules and I'm not here to advertise. I'm here to get genuine feedback from people who actually use AI daily. The core idea is auto-routing. Instead of choosing which model to use yourself, the system analyses your prompt and automatically sends it to the right model. Here's how I've mapped it: Grok for anything needing real-time or live data GPT-5.2 for coding tasks Gemini for image and audio analysis Claude for long documents and writing DeepSeek R1 for complex reasoning problems I've also built in a dropdown so users can turn auto-routing off completely and manually pick whichever model they want. So it works both ways. One thing I haven't seen discussed much elsewhere — because all models share the same conversation thread, you can actually use them together consecutively. Ask Gemini to write a prompt, switch to GPT for deep reasoning on it, switch to Claude for the long-form output — and the full context carries across all of them. No copy-pasting between tabs. ChatGPT remembers within ChatGPT. Claude remembers within Claude. But here every model has access to the same conversation history. I'm curious whether that kind of cross-model continuity is something people actually want or whether most users just pick one model and stick with it. On features — I've already implemented most of what the big platforms are now making announcements about: persistent memory, knowledge base, vision to code, photo editing, music generation, and video generation using top models. So I'm genuinely not sure what's missing. What would make you switch from whatever you're currently using? Is there something you wish existed that none of the major platforms have shipped yet? A few other things I'd love opinions on: Input limit is set to 200,000 characters, which safely fits within the context windows of all supported models. For large inputs the router automatically directs to Claude or Gemini which handle long context best. Is 200k enough or do people genuinely need more? I've also added UI features I haven't seen elsewhere — 26 language options for the entire interface, multiple themes, and live wallpapers. Does that kind of thing matter to anyone or do people just want raw model performance and the interface is irrelevant?

12h ago

---

**[Consultants Are Cashing in on the AI Boom - Tech News Briefing - WSJ Podcasts](https://www.reddit.com/r/artificial/comments/1rue9qr/consultants_are_cashing_in_on_the_ai_boom_tech/)**

🔗 [wsj.com](https://www.wsj.com/podcasts/tech-news-briefing/consultants-are-cashing-in-on-the-ai-boom/e9eaf7be-171e-4e25-9faa-33d8bb2ea786?gaa_at=eafs&gaa_n=AWEtsqfdTyvWaFP8EfWuBrGOod5F9GRFcSzxcEHqOEAYwDmKE6xeFnP31JmAzsh3SsE%3D&gaa_ts=69b6b7da&gaa_sig=OPtT9zqUPeLMNc4DiaE9pndX0S1npatSl4fjzt3RjCbRWxbY64Z5j0ODyk5msYHze2XhkS1AkVFl9a8m738_5Q%3D%3D) • 23h ago

---

---

## Google News: "ai"

**[Is this product 'human-made'? The race to establish an AI-free logo](https://www.bbc.com/news/articles/cj0d6el50ppo)**

The backlash to the growing use of the tech has led to an explosion in attempts to come up with 'AI-Free' logo that could be used globally.

BBC • 12h ago

---

**[Google scraps AI search feature that crowdsourced amateur medical advice](https://www.theguardian.com/technology/2026/mar/16/google-scraps-ai-search-feature-that-crowdsourced-amateur-medical-advice)**

Exclusive: Revelation comes as company faces mounting scrutiny over use of AI to provide health tips

The Guardian • 4h ago

---

**[Mayor Wilson pauses city employees’ sanctioned use of AI](https://www.seattletimes.com/seattle-news/politics/mayor-wilson-pauses-city-employees-sanctioned-use-of-ai/)**

The Seattle Times • 15m ago

---

**[One of world's largest AI conferences kicks off in San Jose](https://www.ktvu.com/news/one-worlds-largest-ai-conferences-kicks-off-san-jose)**

One of the world's largest artificial intelligence conferences is underway in San Jose this week, drawing an estimated 30,000 developers, researchers and business leaders to the city for Nvidia's annual GTC Conference.

KTVU • 17m ago

---

**[AI is spreading disinformation in war and markets](https://www.ft.com/content/ceb33440-e0bd-46da-9be0-d4ac27d5a19a)**

How can countries force the tech platforms to take more responsibility for the circulation of deep fakes?

Financial Times • 15m ago

---

**[See which jobs are most threatened by AI, and who may be able to adapt](https://www.washingtonpost.com/technology/interactive/2026/jobs-most-affected-ai-automation/)**

Look up which jobs are most at risk from artificial intelligence and who is most likely to be able to adapt, according to a new analysis.

The Washington Post • 1h ago

---

**[Meta up nearly 3% in premarket as it plans mass layoff to offset increased AI spending](https://www.cnbc.com/2026/03/16/meta-ai-costs-mass-layoffs-20percent-up-premarket.html)**

Meta is planning capital expenditure of up to $135 billion in AI-related costs in 2026, which raised investors' fears around unsustainable spending.

CNBC • 2h ago

---

**[Tech companies are blaming massive layoffs on AI. What’s really going on?](https://theconversation.com/tech-companies-are-blaming-massive-layoffs-on-ai-whats-really-going-on-278314)**

Amazon, Block and Atlassian have announced AI-driven job cuts, and Meta is reportedly planning its own – but all may not be as it seems.

The Conversation • 10h ago

---

**[Breakingviews - China tech's old guard lose their AI thunder](https://www.reuters.com/commentary/breakingviews/china-techs-old-guard-lose-their-ai-thunder-2026-03-16/)**

Reuters • 10h ago

---

**[Nebius signs AI infrastructure deals with Meta worth up to $27 billion over 5 years](https://finance.yahoo.com/news/nebius-signs-ai-capacity-deal-100907683.html)**

By Aditya Soni and Toby Sterling March 16 (Reuters) - Amsterdam-based AI infrastructure firm Nebius Group said Monday it has signed a five-year deal with Meta Platforms to provide the social media

Yahoo Finance • 1h ago

---

---

## HackerNews: "ai"

**[Elon Musk pushes out more xAI founders as AI coding effort falters](https://news.ycombinator.com/item?id=47366666)**

Tesla and SpaceX managers sent in to review work as billionaire’s start-up struggles to keep pace with rivals

⬆️ 516 • 💬 812 • 2d ago • [ft.com](https://www.ft.com/content/e5fbc6c2-d5a6-4b97-a105-6a96ea849de5)

---

**[$96 3D-printed rocket that recalculates its mid-air trajectory using a $5 sensor](https://news.ycombinator.com/item?id=47385935)**

Contribute to novatic14/MANPADS-System-Launcher-and-Rocket development by creating an account on GitHub.

⬆️ 411 • 💬 366 • 1d ago • [GitHub](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket)

---

**[John Carmack about open source and anti-AI activists](https://news.ycombinator.com/item?id=47367463)**

⬆️ 370 • 💬 486 • 2d ago • [X (formerly Twitter)](https://twitter.com/id_aa_carmack/status/2032460578669691171)

---

**[The Appalling Stupidity of Spotify's AI DJ](https://news.ycombinator.com/item?id=47385272)**

Am I naïve in expecting Artificial Intelligence to be smart? Is my interpretation of the word “intelligence” too literal? And when an AI behaves stupidly, who’s to blame? The programmers or the AI entity itself? Is it even proper to make a distinction between the two? Or does the AI work in so mysterious a way that the programmers need no longer take responsibility?

⬆️ 359 • 💬 292 • 1d ago • [charlespetzold.com](https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html)

---

**[Ask HN: How is AI-assisted coding going for you professionally?](https://news.ycombinator.com/item?id=47388646)**

⬆️ 328 • 💬 522 • 21h ago

---

**[Airbus is preparing two uncrewed combat aircraft](https://news.ycombinator.com/item?id=47382277)**

Airbus is working at full throttle to offer the German Air Force an operational Uncrewed Collaborative Combat Aircraft (UCCA) system by 2029.

⬆️ 180 • 💬 128 • 1d ago • [Airbus](https://www.airbus.com/en/newsroom/press-releases/2026-03-airbus-is-preparing-two-uncrewed-combat-aircraft-from-kratos-for-first-flight-with-a-european)

---

**[Show HN: GitAgent – An open standard that turns any Git repo into an AI agent](https://news.ycombinator.com/item?id=47376584)**

Define, version, and run AI agents natively in git. GitAgent is the open AI agent standard — framework-agnostic, works with Claude, OpenAI, CrewAI, Lyzr, and more.

⬆️ 139 • 💬 35 • 1d ago • [GitAgent](https://www.gitagent.sh/)

---

**[AI didn't simplify software engineering: It just made bad engineering easier](https://news.ycombinator.com/item?id=47377262)**

⬆️ 128 • 💬 111 • 1d ago • [robenglander.com](https://robenglander.com/writing/ai-did-not-simplify/)

---

**[Launch HN: Spine Swarm (YC S23) – AI agents that collaborate on a visual canvas](https://news.ycombinator.com/item?id=47364116)**

Spine is the world's first truly agentic platform designed to manage and orchestrate the next generation of AI.

⬆️ 109 • 💬 69 • 2d ago • [getspine.ai](https://www.getspine.ai/)

---

**[Meta planning layoffs as AI costs mount](https://news.ycombinator.com/item?id=47372249)**

⬆️ 100 • 💬 22 • 2d ago • [reuters.com](https://www.reuters.com/business/world-at-work/meta-planning-sweeping-layoffs-ai-costs-mount-2026-03-14/)

---

---

## YouTube Videos: "ai"

**[Daniel Priestley: AI Will Make Plumbers Earn More Than Lawyers! (2029 PREDICTION)](https://www.youtube.com/watch?v=fpETS6q1Hww)**

What is financial freedom? The Business Strategist Daniel Priestley on why AI makes lifestyle businesses easy. Daniel Priestley is ...

📺 The Diary Of A CEO

👁️ 93K • 👍 4K • 💬 869 • ⏱️ 2:02:37 • 5h ago

---

**[What&#39;s really going on with AI, Expert weighs in | TheStandup](https://www.youtube.com/watch?v=TtX3jDaZG8Y)**

ssh terminal.shop CHECK OUT THEIR NEW PODCAST ON CASEY'S YOUTUBE: @MollyRocket AI researcher Dimitri joins the ...

📺 The PrimeTime

👁️ 120K • 👍 3K • 💬 643 • ⏱️ 42:21 • 2d ago

---

**[Meta to Fire 20% of its Workforce? (AI Takeover)](https://www.youtube.com/watch?v=K5CxBze4BeI)**

Meta is preparing for the largest layoffs in company history, potentially firing 20% of its workforce (16000 jobs). Get updated: ...

📺 Mark Savant

👁️ 8K • 👍 268 • 💬 101 • ⏱️ 15:54 • 1d ago

---

**[Palantir CTO: &quot;You&#39;re Being Lied to About AI&quot; | Official Preview](https://www.youtube.com/watch?v=gTP9_WTqFWE)**

Join this channel to get access to perks: https://www.youtube.com/channel/UCkoujZQZatbqy4KGcgjpVxQ/join In this episode of ...

📺 Shawn Ryan Show

👁️ 97K • 👍 3K • 💬 546 • ⏱️ 3:28 • 2d ago

---

**[Netanyahu &#39;DEAD&#39; BREAKING:  New ‘FAKE AI’ Coffee Video Released? Grok Says Israeli PM Is Dead?](https://www.youtube.com/watch?v=ZPgLki4x3xc)**

A viral video shows Israeli Prime Minister Benjamin Netanyahu sitting in a Tel Aviv café, seemingly dismissing death claims.

📺 Oneindia News

👁️ 7K • 👍 86 • 💬 44 • ⏱️ 3:02 • 6h ago

---

**[AI News: They All Launched the Same Thing!](https://www.youtube.com/watch?v=syx_8UlEWlA)**

Here's the AI News you probably missed this week. Head to http://hostinger.com/mattopenclaw and use the coupon code ...

📺 Matt Wolfe

👁️ 84K • 👍 3K • 💬 234 • ⏱️ 33:33 • 2d ago

---

**[Cute or Creepy? AI Fruit Babies 🍓👶 | The Strangely Satisfying AI ASMR](https://www.youtube.com/watch?v=f_gcmtfLBIk)**

Cute Fruit Babies Eating Fruit | Oddly Satisfying AI Welcome to a strange but relaxing AI world with @AI_DREAM_ASMRR.

📺 AI DREAM ASMR

👁️ 77K • 👍 5K • 💬 314 • ⏱️ 2:34 • 2d ago

---

**[Digital Optimus: Elon Musk Reveals the First True AI Worker](https://www.youtube.com/watch?v=OzXqJh6yOj4)**

Elon Musk just dropped bombshell after bombshell at the Abundance Summit — and honestly? The future of work may never look ...

📺 The AI Nexus

👁️ 12K • 👍 405 • 💬 33 • ⏱️ 18:24 • 2d ago

---

**[Claude Code, Paperclip, &amp; The Rise of &quot;AI Agent Companies&quot;](https://www.youtube.com/watch?v=Rgb-Kx-kkaA)**

Master Claude Code, Build Your Agency, Land Your First Client⚡ https://www.skool.com/chase-ai FREE community + GWS ...

📺 Chase AI

👁️ 18K • 👍 512 • 💬 45 • ⏱️ 8:51 • 14h ago

---

**[This hotel uses AI instead of humans and then LIES about it. 🥴](https://www.youtube.com/watch?v=iK5mTjCCBdc)**

📺 Maggie McGaugh

👁️ 273K • 👍 14K • 💬 671 • ⏱️ 2:30 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 5,412 • ❤️ 505 • 4d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 67,573 • ❤️ 737 • 8d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 86,706 • ❤️ 294 • 5d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 237,719 • ❤️ 477 • 12d ago

---

**[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)**

*Lightricks*

LTX-2.3 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs, including images and text. It offers improved visual and audio quality, enhanced prompt adherence, and supports local execution with open weights.

`image-to-video`

⬇️ 596,747 • ❤️ 639 • 20h ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 2,111,532 • ❤️ 863 • 14d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 7,340 • ❤️ 234 • 3d ago

---

**[NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Super-120B-A12B-BF16 is a 120B parameter LLM with a LatentMoE architecture, supporting up to 1M tokens context. It excels at agentic workflows, long-context reasoning, and high-volume tasks like IT automation, with configurable reasoning modes.

`text-generation` `123.6B`

⬇️ 27,263 • ❤️ 219 • 1d ago

---

**[tada-1b](https://huggingface.co/HumeAI/tada-1b)**

*Hume AI*

TADA-1B is a text-to-speech model that uses a novel 1:1 text-acoustic alignment for high-fidelity speech synthesis with reduced computational overhead. It enables dynamic duration synthesis and dual-stream generation, making it efficient for generating natural-sounding speech.

`text-to-speech` `2.2B`

⬇️ 21,467 • ❤️ 202 • 2d ago

---

**[LocoTrainer-4B](https://huggingface.co/LocoreMind/LocoTrainer-4B)**

*LocoreMind*

LocoTrainer-4B is a 4B parameter text-generation model specialized for MS-SWIFT codebase analysis. It excels at multi-turn tool-calling for tasks like code navigation and report generation, leveraging a 32K context window for in-depth analysis.

`text-generation` `4.0B`

⬇️ 1,343 • ❤️ 170 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 13 • 💬 0 • ⭐ 34,808 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 26 • 💬 2 • ⭐ 27,748 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 102 • 💬 5 • ⭐ 3,071 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 163 • 💬 3 • ⭐ 7,136 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 24 • 💬 1 • ⭐ 32,315 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 48 • 💬 2 • ⭐ 49,972 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 46 • 💬 1 • ⭐ 73,274 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 12 • 💬 1 • ⭐ 9,735 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[TADA: A Generative Framework for Speech Modeling via Text-Acoustic Dual Alignment](https://huggingface.co/papers/2602.23068)**

*Trung Dang, Sharath Rao, Ananya Gupta et al. (9 authors)*

🏢 Hume AI

A novel tokenization scheme synchronizes acoustic features with text tokens in TTS systems, enabling unified modeling and reduced hallucinations through flow matching and text-only guidance.

▲ 6 • 💬 0 • ⭐ 734 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2602.23068) • [💻 code](https://github.com/HumeAI/tada) • [🔗 project](https://www.hume.ai/blog/opensource-tada)

---

**[OASIS: Open Agent Social Interaction Simulations with One Million Agents](https://huggingface.co/papers/2411.11581)**

*Ziyi Yang, Zaibin Zhang, Zirui Zheng et al. (23 authors)*

OASIS is a scalable and generalizable social media simulator that models large-scale user interactions and replicates complex social phenomena across platforms.

▲ 1 • 💬 0 • ⭐ 3,263 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2411.11581) • [💻 code](https://github.com/camel-ai/oasis)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 37.6k • 🔱 5.2k • 5d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 20.8k • 🔱 965 • 2d ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 12.2k • 🔱 1.5k • 15m ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 10.0k • 🔱 906 • 20h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 9.5k • 🔱 685 • 2h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`HTML` `agency` `agent` `pip` `pua`

⭐ 7.9k • 🔱 372 • 4h ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"

`Python`

⭐ 7.2k • 🔱 921 • 12d ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 6.4k • 🔱 752 • 10h ago

---

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**

Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop" 

`agent` `ai` `coding` `lowcode` `nocode`

⭐ 3.0k • 🔱 193 • 14h ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 2.8k • 🔱 91 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
