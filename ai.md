---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-01T14:37:14.612803+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 01, 2026 at 14:37 UTC  
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

3h ago

---

**[China Bans AI Layoffs as Nvidia CEO Says AI Created 500K Jobs in 2 Years](https://www.reddit.com/r/artificial/comments/1t0tk5q/china_bans_ai_layoffs_as_nvidia_ceo_says_ai/)**

China just banned firing workers for AI while Nvidia's CEO claims AI created over 500K jobs, setting up a clash over automation's future.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/china-bans-ai-layoffs-nvidia-ceo-500k-jobs/) • 1h ago

---

**[Mark Zuckerberg Says AI Costs Contributed To Layoffs Of 8,000 Staffers, Report Says](https://www.reddit.com/r/artificial/comments/1t0cy0n/mark_zuckerberg_says_ai_costs_contributed_to/)**

🔗 [forbes.com](https://www.forbes.com/sites/antoniopequenoiv/2026/04/30/mark-zuckerberg-says-ai-costs-contributed-to-layoffs-of-8000-staffers-report-says/?utm_campaign=forbes&utm_medium=social&utm_source=twitter&utm_term=se-breaking) • 14h ago

---

**[I built a router that automatically sends your AI tasks to the most appropriate model to handle them at low cost - 9,200 tasks in, $21 saved at $0.14 actual cost](https://www.reddit.com/r/artificial/comments/1t0soki/i_built_a_router_that_automatically_sends_your_ai/)**

The observation that started this: most of what people use AI for every day - summarising, drafting, classifying, extracting etc doesn't actually require a frontier model. Any competent 8-70B model handles those just as well. But most people run everything through Claude or ChatGPT out of habit. I built Followloop (followloop.app) to solve this automatically. It classifies each task by complexity and routes it: - Simple tasks → Cerebras Llama (2000 TPS, 1M tokens/day free), Groq, Gemini Flash - Moderate tasks → Groq 70B, SambaNova - Complex tasks → Claude Haiku as fallback The dashboard shows your actual cost alongside what you'd have paid running everything on Claude Sonnet. I've been running it on my own AI workflow for two weeks: 9,200 tasks routed, $21.24 saved, $0.1360 actual cost. About 157× cheaper per token than Sonnet on average. Works with any AI setup via MCP (Model Context Protocol) - Claude Desktop, Cursor, Claude Code, or anything MCP-compatible. Also has a library of 1,300+ safety-screened MCP servers as a bonus feature. $5/month at followloop.app

1h ago

---

**[AI outperforms doctors in Harvard trial of emergency triage diagnoses](https://www.reddit.com/r/artificial/comments/1t0p7ej/ai_outperforms_doctors_in_harvard_trial_of/)**

Researchers say results mark a really ‘profound change in technology that will reshape medicine’

🔗 [the Guardian](https://www.theguardian.com/technology/2026/apr/30/ai-outperforms-doctors-in-harvard-trial-of-emergency-triage-diagnoses) • 4h ago

---

**[Anthropic mass shipped 9 connectors and accidentally leaked their entire creative industry strategy](https://www.reddit.com/r/artificial/comments/1szoe78/anthropic_mass_shipped_9_connectors_and/)**

The announcement yesterday was genuinely significant and i don't think most people outside the creative industry understand why. Anthropic released 9 connectors that let claude directly control professional creative software through mcp which means actually execute actions inside them the full list contains adobe creative cloud (50+ apps including photoshop, premiere, illustrator), blender (full python api access for 3d modeling), autodesk fusion , ableton, splice , affinity by canva , sketchup , resolume (), and claude design. Anthropic also became a blender development fund patron at $280k+/yr and is partnering with risd, ringling college, and goldsmiths university on curriculum development around these tools. this isn't a press release play, there's institutional investment behind it the strategic read is interesting because this positions claude very differently from chatgpt in the creative space. Openai went the route of building creative capabilities natively inside chatgpt with images 2.0 and previously sora. Anthropic is going the connector route where claude doesn't replace or replicate the creative tools, it becomes the intelligence layer that works inside them. Both strategies have merit but they serve fundamentally different users the gap that still exists and i think matters for the broader market is that these connectors serve professionals who already know photoshop and blender and fusion. The consumer creative market where people need face swaps, lip syncs, talking photos, style transfers, none of that is covered by these connectors, that layer is being served by consolidated platforms like magic hour, higgsfield, domoai, and canva's expanding ai features. It's a completely different market but the two layers increasingly feed into each other as professional assets flow into social content pipelines. the question is whether anthropic eventually builds connectors for these consumer creative platforms too or whether the gap between professional creative tools with ai copilots and consumer creative platforms with bundled capabilities remains a split in the market what do you think this means for the creative tool landscape over the next 12-18 months?

1d ago

---

**[Deepfakes don't have to be believed to work. They just have to consume the response budget.](https://www.reddit.com/r/artificial/comments/1t0jlc5/deepfakes_dont_have_to_be_believed_to_work_they/)**

A framing I keep coming back to: a synthetic image or video can succeed even when almost nobody believes it. Not because it changes minds directly, but because it turns attention into the attacked resource. If a campaign, newsroom, platform, or company has to stop and answer the fake, the fake already got some of what it wanted: the defenders spend scarce time verifying and explaining the audience gets forced to process the claim anyway every debunk risks replaying the artifact institutions look reactive even when they are correct the attacker learns which themes reliably pull defenders into the loop So detection is necessary, but not sufficient. The second half of the system is distribution response. A few practical design questions I think matter more than the usual “can we detect it?” debate: Can we debunk without embedding, quoting, or rewarding the fake? Can provenance signals move suspicious media into slower lanes instead of binary takedown/leave-up decisions? Do newsrooms and platforms track attention budget as an operational constraint? Can response teams separate “this is false” from “this deserves broad amplification”? Can systems preserve evidence for verification while reducing replay value for the attacker? The failure mode is treating every fake as an information accuracy problem when some of them are closer to denial-of-service attacks on attention. Curious how people here would design the response layer. What should a healthy “quarantine lane” for synthetic media look like without becoming censorship-by-default?

9h ago

---

**[Is an AI SDR replacing “entry-level jobs” a feature or a bug?](https://www.reddit.com/r/artificial/comments/1t0oucl/is_an_ai_sdr_replacing_entrylevel_jobs_a_feature/)**

Sat through a demo this week for one of these AI SDR tools and the pitch was in a nutshell: you don’t need junior sales reps anymore. (As in not even train them anymore just remove them.) To my surprise it worked. The tool was doing outbound, follow-ups, personalization, all the stuff junior SDRs grind through. Faster, cleaner, no complaints! But it did leave me feeling uneasy. That grindy, repetitive work is literally how most people get into sales. It’s where you learn how people respond, how messaging gets through, how to deal with rejection without taking it personally. That's how I got into it at least. So if AI wipes that layer out completely, what’s the path in? Are we just skipping straight to “hire experienced closers” and hoping they came from… where exactly? I’m not anti-AI (this stuff is obviously useful), but replacing enty-level humans as the first step in the process doesn't feel like a sustainable route.

4h ago

---

**[Elon Musk says his xAI startup’s models were partially trained on OpenAI’s tech](https://www.reddit.com/r/artificial/comments/1t03h0n/elon_musk_says_his_xai_startups_models_were/)**

🔗 [sfchronicle.com](https://www.sfchronicle.com/tech/article/elon-musk-openai-trial-xai-22234502.php) • 20h ago

---

**[What's the most frustrating part of using AI tools ?????(i will not promote)](https://www.reddit.com/r/artificial/comments/1t0tjae/whats_the_most_frustrating_part_of_using_ai_tools/)**

I've been working in the AI space for some time now and I always kind of hear the same probelmo , where u know people can generate content or code but can't get the outcome or the difference between what you actually want and what the ai wrote is kind of apart. I think just to solve like one basic error you send 10 prompts to solve it. Not downsizing AI cause its crazy to see the amount of heavy lifting it does. But its a bit off, so curious What breaks down for you? Is it like output quality or not knowing what to do with what the AI gives you?(not promoting anything).dw:)

1h ago

---

---

## Google News: "ai"

**[Opinion | Silicon Valley Is Bracing for a Permanent Underclass](https://www.nytimes.com/2026/04/30/opinion/ai-labor-work-force-silicon-valley.html)**

The New York Times • 1d ago

---

**[So, About That AI Bubble](https://www.theatlantic.com/economy/2026/05/ai-bubble-revenue-anthropic/687022/)**

Thanks to the rise of Claude Code and other AI agents, revenues are finally catching up to the hype.

The Atlantic • 3h ago

---

**[Axios Live: Atlanta businesses are pushing to keep up with AI's evolution; students may be the answer](https://www.axios.com/2026/05/01/axios-live-atlanta-businesses-ais-evolution-students)**

Axios • 41m ago

---

**[Caterpillar’s Biggest Bear Folds as AI Power Demand Soars](https://www.bloomberg.com/news/articles/2026-05-01/caterpillar-s-biggest-bear-folds-as-ai-power-demand-soars)**

Caterpillar Inc.’s biggest Wall Street bear has thrown in the towel after watching the stock more than double on the back of surging demand for the company’s power generation equipment.

Bloomberg.com • 48m ago

---

**[Classified Networks AI Agreements](https://www.war.gov/News/Releases/Release/Article/4475177/classified-networks-ai-agreements/)**

The War Department has entered into agreements with seven of the world's leading frontier artificial intelligence companies to deploy their advanced AI capabilities on the department's classified

U.S. Department of War (.gov) • 2h ago

---

**[Pentagon Makes Deals With A.I. Companies to Expand Classified Work](https://www.nytimes.com/2026/05/01/us/politics/pentagon-ai-companies-deals.html)**

The New York Times • 1h ago

---

**[Pentagon reaches agreements with leading AI companies](https://www.nbcnews.com/tech/tech-news/pentagon-reaches-agreements-leading-ai-companies-rcna343071)**

The Pentagon’s main AI platform GenAI.mil has been used by over 1.3 million Defense Department personnel, the agency noted in its release.

NBC News • 20m ago

---

**[In real-world test, an AI model did better than ER doctors at diagnosing patients](https://www.npr.org/2026/04/30/nx-s1-5804474/ai-doctors-openai-patient-care-diagnosis)**

Researchers evaluated how well an AI model could diagnose and make decisions about patient care.

NPR • 20h ago

---

**[AI Investor Coatue Joins Data Center Frenzy With New Venture to Buy Land](https://www.wsj.com/tech/ai/ai-investor-coatue-joins-data-center-frenzy-with-new-venture-to-buy-land-9f4c374f)**

Philippe Laffont’s firm has launched Next Frontier, whose facilities will be meant for AI companies including Anthropic.

WSJ • 51m ago

---

**[Where the goblins came from](https://openai.com/index/where-the-goblins-came-from/)**

How goblin outputs spread in AI models: timeline, root cause, and fixes behind personality-driven quirks in GPT-5 behavior.

OpenAI • 1d ago

---

---

## HackerNews: "ai"

**[The Zig project's rationale for their anti-AI contribution policy](https://news.ycombinator.com/item?id=47957294)**

Zig has one of the most stringent anti-LLM policies of any major open source project: No LLMs for issues. No LLMs for pull requests. No LLMs for comments on the …

⬆️ 657 • 💬 443 • 1d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)

---

**[Shai-Hulud Themed Malware Found in the PyTorch Lightning AI Training Library](https://news.ycombinator.com/item?id=47964617)**

The PyPI package lightning was compromised in versions 2.6.2 and 2.6.3 with Mini Shai-Hulud themed malicious code to execute credential-stealing malware on import.

⬆️ 427 • 💬 158 • 22h ago • [Semgrep](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/)

---

**[Google and Pentagon reportedly agree on deal for 'any lawful' use of AI](https://news.ycombinator.com/item?id=47936156)**

﻿The classified deal apparently doesn’t allow Google to veto how the government will use its AI models.

⬆️ 314 • 💬 279 • 2d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal)

---

**[Claude.ai unavailable and elevated errors on the API](https://news.ycombinator.com/item?id=47938097)**

Claude's Status Page - Claude.ai unavailable and elevated errors on the API.

⬆️ 297 • 💬 251 • 2d ago • [status.claude.com](https://status.claude.com/incidents/9l93x2ht4s5w)

---

**[Why AI companies want you to be afraid of them](https://news.ycombinator.com/item?id=47949750)**

They built it. They're scared of it. They're selling it anyway.

⬆️ 286 • 💬 219 • 1d ago • [bbc.com](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)

---

**[He asked AI to count carbs 27000 times. It couldn't give the same answer twice](https://news.ycombinator.com/item?id=47947490)**

Ask ChatGPT to estimate the carbs in your lunch. Now ask it again. And again. Five hundred times. You’d expect the same answer each time. It’s the same photo, the same model, the same question. But you won’t get the same answer. Not even close — and the differences are large enough to cause a

⬆️ 240 • 💬 305 • 2d ago • [Diabettech - Diabetes and Technology | Where Diabetes and Technology meet](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)

---

**[AI's economics don't make sense](https://news.ycombinator.com/item?id=47936867)**

If you liked this piece, please subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s finances,

⬆️ 236 • 💬 189 • 2d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/ais-economics-dont-make-sense/)

---

**[Mike: open-source legal AI](https://news.ycombinator.com/item?id=47956739)**

An open-source alternative to Harvey and Legora. Feature parity, zero cost, self-hostable — built for law firms to own and extend.

⬆️ 200 • 💬 99 • 1d ago • [mikeoss.com](https://mikeoss.com/)

---

**[AISLE Discovers 38 CVEs in OpenEMR Healthcare Software](https://news.ycombinator.com/item?id=47936347)**

38 zero-day security vulnerabilities, three critical, and the shift from disclosure to prevention in healthcare software

⬆️ 177 • 💬 113 • 2d ago • [AISLE](https://aisle.com/blog/aisle-discovers-38-critical-security-vulnerabilities-in-healthcare-software-used-by-100000-providers)

---

**["People who don't use AI will be left behind"](https://news.ycombinator.com/item?id=47953011)**

"People who don't use AI will be left behind", they say. 
I can't emphasize enough how much I hate it when I hear/read shit like that because I'm pretty sur...

⬆️ 168 • 💬 262 • 1d ago • [migraine brain](https://migrainebrain.bearblog.dev/people-who-dont-use-ai-will-be-left-behind/)

---

---

## YouTube Videos: "ai"

**[The AI Economy is about to change](https://www.youtube.com/watch?v=_Q-e_nczWqM)**

Don't let bad code get merged without reviewing (hopefully not by merge cop!). Checkout out Code Rabbit at ...

📺 The PrimeTime

👁️ 33K • 👍 4K • 💬 362 • ⏱️ 9:39 • 1h ago

---

**[Sundar Pichai Reveals What AI Will Do Next](https://www.youtube.com/watch?v=bxDObdH2YSc)**

Google CEO Sundar Pichai spoke with TIME about how artificial intelligence is reshaping decision-making, the rise of AI ...

📺 TIME

👁️ 71K • 👍 1K • 💬 89 • ⏱️ 6:44 • 21h ago

---

**[AI Shows America Without Democrats](https://www.youtube.com/watch?v=Jn-7ZuhoAEc)**

We asked Artificial Intelligence what America would look like without Democrats.

📺 The Babylon Bee

👁️ 105K • 👍 9K • 💬 986 • ⏱️ 1:09 • 1d ago

---

**[The Only 20 Ways to Make Money with AI in 2026](https://www.youtube.com/watch?v=K8Ros5RhJW4)**

Get your FREE Sell by Chat Playbook here: https://go.danmartell.com/4mWrJke Are you building an AI software company?

📺 Dan Martell

👁️ 108K • 👍 5K • 💬 221 • ⏱️ 26:44 • 1d ago

---

**[Deepseek is a problem](https://www.youtube.com/watch?v=epzzALZ8oYo)**

Check out Zapier MCP https://bit.ly/3QGTz87 Sign up for their Webinar https://bit.ly/3P80Dds Download The 25 OpenClaw Use ...

📺 Matthew Berman

👁️ 103K • 👍 5K • 💬 2K • ⏱️ 17:27 • 1d ago

---

**[AI Is REPLACING YOU and the MARKET LOVES IT](https://www.youtube.com/watch?v=hsjEckj9kO8)**

The AI revolution isn't coming; it's already here, and it's moving faster than anyone in Washington or on Wall Street wants to admit.

📺 Anthony Scaramucci

👁️ 29K • 👍 1K • 💬 214 • ⏱️ 27:44 • 1d ago

---

**[&quot;The Bankruptcy Of The United States&quot; - Musk WARNS Only AI &amp; Robots Can Save America](https://www.youtube.com/watch?v=oIHxMjQYSJc)**

Elon Musk warns the U.S. is “1000%” headed for bankruptcy without AI and robots to supercharge growth, but economists push ...

📺 Valuetainment

👁️ 180K • 👍 4K • 💬 950 • ⏱️ 17:12 • 1d ago

---

**[Trump posts AI image of himself with a gun, says Iran ‘better get smart soon’](https://www.youtube.com/watch?v=Wjsft-U5qLQ)**

The Heritage Foundation senior research fellow Brent Sadler says it may come down to a 'waiting game' as Iran continues to face ...

📺 Fox News

👁️ 62K • 👍 1K • 💬 1K • ⏱️ 5:08 • 1d ago

---

**[Elon Musk testifies he has &quot;extreme concerns&quot; about who controls AI in trial vs. Altman](https://www.youtube.com/watch?v=0xyL4l9Geu8)**

Elon Musk took the stand Tuesday in a trial against fellow billionaire Sam Altman that could change the future of AI. Musk accused ...

📺 CBS Mornings

👁️ 62K • 👍 325 • 💬 185 • ⏱️ 3:00 • 2d ago

---

**[9 FREE* AI Tools 🔥AI Videos ✅ Image to Video #ai #aivideo](https://www.youtube.com/watch?v=Yfyo6-1epSg)**

Want to make your videos sound more cinematic and professional? ✓ Epidemic Sound Link: ...

📺 Raj Photo Editing and Much More

👁️ 22K • 👍 1K • 💬 86 • ⏱️ 10:13 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 321,492 • ❤️ 3,343 • 4d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 92,567 • ❤️ 1,162 • 8d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 281,356 • ❤️ 899 • 4d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 7,944 • ❤️ 330 • 3d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 906,859 • ❤️ 1,048 • 7d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 649,331 • ❤️ 1,172 • 1d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 6,809 • ❤️ 188 • 1d ago

---

**[talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it)**

*talkie*

talkie-1930-13b-it is a 13B instruction-tuned language model trained on pre-1931 English text, excelling at generating responses in a vintage style for applications like historical chatbots or creative writing.

⬇️ 0 • ❤️ 178 • 8d ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 35,000 • ❤️ 176 • 2d ago

---

**[MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)**

*Xiaomi MiMo*

MiMo-V2.5 is a native omnimodal LLM supporting text, image, video, and audio with a 1M token context window. It excels in multimodal understanding, long-context reasoning, and agentic workflows, utilizing a hybrid attention architecture and efficient pre-training.

`310.8B`

⬇️ 21,407 • ❤️ 174 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 54 • 💬 2 • ⭐ 58,162 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 167 • 💬 10 • ⭐ 46,162 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 15 • 💬 2 • ⭐ 8,517 • 13d ago

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

▲ 19 • 💬 2 • ⭐ 5,449 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 81 • 💬 6 • ⭐ 19,479 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://huggingface.co/papers/2604.24764)**

*Weijie Wang, Xiaoxuan He, Youping Gu et al. (12 authors)*

🏢 Microsoft Research

World-R1 framework improves video generation by incorporating 3D constraints through reinforcement learning and specialized text datasets while maintaining visual quality and scalability.

▲ 113 • 💬 3 • ⭐ 280 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24764) • [💻 code](https://github.com/microsoft/World-R1) • [🔗 project](https://aka.ms/world-r1)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 76 • 💬 7 • ⭐ 1,745 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

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

▲ 64 • 💬 4 • ⭐ 450 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24763) • [💻 code](https://github.com/facebookresearch/tuna-2) • [🔗 project](https://tuna-ai.org/tuna-2/)

---

---

## GitHub Repositories: "ai"

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 51.7k • 🔱 2.8k • 14h ago

---

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 50.6k • 🔱 6.6k • 5h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 41.5k • 🔱 8.6k • 20h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 39.4k • 🔱 4.4k • 8m ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.3k • 🔱 2.5k • 4d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 9.1k • 🔱 575 • 3d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.6k • 🔱 1.1k • 2d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

`Python`

⭐ 5.1k • 🔱 454 • 2d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 4.9k • 🔱 339 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 4.8k • 🔱 357 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*
