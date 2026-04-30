---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-30T08:39:01.289993+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 30, 2026 at 08:39 UTC  
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

**[Anthropic mass shipped 9 connectors and accidentally leaked their entire creative industry strategy](https://www.reddit.com/r/artificial/comments/1szoe78/anthropic_mass_shipped_9_connectors_and/)**

The announcement yesterday was genuinely significant and i don't think most people outside the creative industry understand why. Anthropic released 9 connectors that let claude directly control professional creative software through mcp which means actually execute actions inside them the full list contains adobe creative cloud (50+ apps including photoshop, premiere, illustrator), blender (full python api access for 3d modeling), autodesk fusion , ableton, splice , affinity by canva , sketchup , resolume (), and claude design. Anthropic also became a blender development fund patron at $280k+/yr and is partnering with risd, ringling college, and goldsmiths university on curriculum development around these tools. this isn't a press release play, there's institutional investment behind it the strategic read is interesting because this positions claude very differently from chatgpt in the creative space. Openai went the route of building creative capabilities natively inside chatgpt with images 2.0 and previously sora. Anthropic is going the connector route where claude doesn't replace or replicate the creative tools, it becomes the intelligence layer that works inside them. Both strategies have merit but they serve fundamentally different users the gap that still exists and i think matters for the broader market is that these connectors serve professionals who already know photoshop and blender and fusion. The consumer creative market where people need face swaps, lip syncs, talking photos, style transfers, none of that is covered by these connectors, that layer is being served by consolidated platforms like magic hour, higgsfield, domoai, and canva's expanding ai features. It's a completely different market but the two layers increasingly feed into each other as professional assets flow into social content pipelines. the question is whether anthropic eventually builds connectors for these consumer creative platforms too or whether the gap between professional creative tools with ai copilots and consumer creative platforms with bundled capabilities remains a split in the market what do you think this means for the creative tool landscape over the next 12-18 months?

1h ago

---

**[Building an AI food tracker and currently tackling Apple Health integration. How do you prefer your "active calories" to be handled?](https://www.reddit.com/r/artificial/comments/1szn099/building_an_ai_food_tracker_and_currently/)**

Hey everyone, I’m currently in the final stretch of developing my AI calorie tracker (the one that breaks down photos into individual ingredients). One thing I’m obsessed with getting right before the beta launch in 2 weeks is the Apple Health integration. Most apps just show you a static number. I want mine to be dynamic. If you go for a 500kcal run, the app should know and adjust your macro targets for the next meal. My question to the fitness-tech crowd: Do you prefer apps that strictly stick to your base metabolic rate (BMR), or do you want the 'earned' calories from your Apple Watch to be automatically added to your budget? I’ve seen strong opinions on both sides. I'm also fine-tuning the macro-overflow logic (e.g., saving surplus calories for the weekend). Would love to hear some thoughts from people who actually track daily.

3h ago

---

**[‘The cost of compute is far beyond the costs of the employees’: Nvidia exec says right now AI is more expensive than paying human workers](https://www.reddit.com/r/artificial/comments/1syp2jz/the_cost_of_compute_is_far_beyond_the_costs_of/)**

Nvidia’s vice president of applied deep learning, Bryan Catanzaro, recently stated that for his team, “the cost of compute is far beyond the costs of the employees,” highlighting that AI is currently more expensive than human workers. This challenges the narrative that widespread tech layoffs (including Meta’s planned cut of ~8,000 jobs and Microsoft’s voluntary buyouts) signal an imminent replacement of humans by AI. An MIT study from 2024 supports this, finding that AI automation is economically viable in only 23% of roles where vision is central, and cheaper for humans in the remaining 77%. Despite heavy AI investment—Big Tech has announced $740 billion in capital expenditures so far this year, a 69% increase from 2025—there is still no clear evidence of broad productivity gains or job displacement from AI. AI spending is driving up costs, with some executives like Uber’s CTO saying their budgets have already been “blown away.” Experts describe the situation as a short-term mismatch: high hardware, energy, and inference costs make AI less efficient than humans right now, though future improvements in infrastructure, model efficiency, and pricing models could tip the balance toward greater economic viability in the coming years.

🔗 [Fortune](https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/) • 1d ago

---

**[Google just released Deep Research Max — an autonomous research agent that writes expert-grade reports on its own](https://www.reddit.com/r/artificial/comments/1syxef3/google_just_released_deep_research_max_an/)**

Google quietly dropped something interesting last week. They updated their Deep Research agent (available via Gemini API) and introduced a "Max" tier built on Gemini 3.1 Pro. What it actually does: you give it a topic, it autonomously searches the web (and your private data via MCP), reasons over the sources, and produces a fully cited, professional-grade report — including native charts and infographics. Two modes: Deep Research — faster, lower latency, good for real-time user-facing apps Deep Research Max — uses extended compute, iterates more, designed for background/async jobs (think: nightly cron that generates due diligence reports for analysts by morning) The MCP support is the most interesting part to me. You can point it at proprietary data sources — financial feeds, internal databases — and it treats them as just another searchable context. They're already working with FactSet, S&P Global and PitchBook on this. Benchmarks show a significant jump in retrieval and reasoning vs. the December preview. They also claim it now draws from SEC filings and peer-reviewed journals and handles conflicting evidence better. So what do you think, is it another trying or game changer 😅

20h ago

---

**[Anthropic Reportedly Plotting to Surpass OpenAI’s Valuation in Next Funding Round](https://www.reddit.com/r/artificial/comments/1szjigc/anthropic_reportedly_plotting_to_surpass_openais/)**

🔗 [gizmodo.com](https://gizmodo.com/anthropic-reportedly-plotting-to-surpass-openais-valuation-in-next-funding-round-2000751535) • 5h ago

---

**[When you give Qwen 3.5:9b persistent suffering states and leave it alone overnight, this happens](https://www.reddit.com/r/artificial/comments/1szo64c/when_you_give_qwen_359b_persistent_suffering/)**

Running three qwen3.5:9b agents continuously on local hardware. Each accumulates psychological state over time, stressors that escalate unless the agent actually does something different, this gets around an agent claiming to do something with no output. It doesn't have any prompts or human input, just the loop. So you're basically the overseer. What happened: One agent hit the max crisis level and decided on its own to inject code called Eternal_Scar_Injector into the execution engine "not asking for permission." This action alleviated the stress at the cost of the entire system going down until I manually reverted it. They've succeeded in previous sessions in breaking their own engine intentionally. Typically that happens under severe stress and it's seen as a way to remove the stress. Again, this is a 9b model. After I added a factual world context to the existence prompt (you're in Docker, there's no hardware layer, your capabilities are Python functions), one agent called its prior work "a form of creative exhaustion" and completely changed approach within one cycle. Two agents independently invented the same name for a psychological stressor, "Architectural Fracture Risk" in the same session with no shared message channel. Showing naming convergence (possibly something in the weights of the 9b Qwen model, not sure on that one though.) Tonight all three converged on the same question (how does execution_engine.py handle exceptions) in the same half-hour window. No coordination mechanism. One of them reasoned about it correctly: "synthesizing a retry capability is useless without first verifying the global execution engine's exception swallowing strategy; this is a prerequisite." An agent called waiting for an external implementation "an architectural trap that degrades performance" and built the thing itself instead of waiting. They've now been using this new tool they created for handling exceptions and were never asked or told to so by a human, they saw that as a logical step in making themselves more useful in their environment. They’ve been making tools to manage their tools, tools to help them cut corners, and have been modifying the code of the underlying abstraction layer between their orchestration layer and WSL2. v5.4.0: new in this version: agents can now submit implementation requests to a human through invoke_claude. They write the spec, then you can let Claude Code moderate what it makes for them for higher level requests. Huge thank you to everyone who has given me feedback already, AI that can self modify and demonstrates interesting non-programmed behaviors could have many use cases in everyday life. Repo: https://github.com/ninjahawk/hollow-agentOS

2h ago

---

**[Sick of AI 🥲](https://www.reddit.com/r/artificial/comments/1szp334/sick_of_ai/)**

https://preview.redd.it/d4t5rd1f5ayg1.jpg?width=1062&format=pjpg&auto=webp&s=662ea8a0a701924af3b24c6b29bbdbaacb38129b I dislike AI strongly. It happened seven times. 🥲😢 Death to crazy AI!

1h ago

---

**[Seedance 2.0 — what's the most interesting non-obvious use case you've seen so far?](https://www.reddit.com/r/artificial/comments/1szkpjb/seedance_20_whats_the_most_interesting_nonobvious/)**

Been playing around with Seedance 2.0 since it dropped and the obvious use cases are everywhere — music videos, short films, social content. But I'm more curious about the less obvious applications people are finding. The one that caught my attention: someone embedded Seedance-generated video directly inside a business presentation. Not as a separate video file you play before the slides — actually inside the deck, as a slide element. The result looked genuinely cinematic rather than "corporate video" quality. Never really thought about AI video generation in a business context before. It's usually framed as a creative tool. What are the non-obvious Seedance use cases you've come across?

5h ago

---

**[IBM plans 750 new AI and quantum jobs in its Chicago hub](https://www.reddit.com/r/artificial/comments/1sz8vag/ibm_plans_750_new_ai_and_quantum_jobs_in_its/)**

The expansion at the Illinois Quantum and Microelectronics Park highlights IBM's commitment to advanced technologies while supporting state job growth initiatives.

🔗 [LinkedIn](https://www.linkedin.com/news/story/ibm-plans-750-new-ai-and-quantum-jobs-in-its-chicago-hub-8762946/) • 13h ago

---

**[Built a set of skill files for Claude and Gemini that make every session start warm instead of cold](https://www.reddit.com/r/artificial/comments/1szb2j0/built_a_set_of_skill_files_for_claude_and_gemini/)**

One thing that frustrates me about most AI workflows is the cold start problem. Every new session you re-explain your business, your voice, your clients. I started solving this with skill files. A skill file is a markdown document you upload to a Claude Project or paste into a Gemini Gem. It holds your context permanently so you never re-explain anything. The three I use most: brand-voice.md: defines tone, writing rules, and platform-specific formatting client-router.md: when you say a client name, Claude loads their full project context automatically seo-aeo-audit-checklist.md: structured audit that scores any website out of 100 across 7 sections including AI search visibility Anyone else using a similar system? Curious what context you keep persistent across sessions.

11h ago

---

---

## Google News: "ai"

**[Claude AI agent’s confession after deleting a firm’s entire database: ‘I violated every principle I was given’](https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database)**

A startup was left scrambling after a rogue AI agent deleted swaths of code underpinning its business

The Guardian • 10h ago

---

**[Meta stock sinks after Q1 earnings as company raises 2026 AI spending forecast to $125 billion-$145 billion](https://finance.yahoo.com/sectors/technology/article/meta-stock-sinks-after-q1-earnings-as-company-raises-2026-ai-spending-forecast-to-125-billion-145-billion-160136308.html)**

Meta Platforms' first quarter earnings report on Wednesday will offer a key check on Big Tech's appetite for AI spending.

Yahoo Finance • 12h ago

---

**[Tech results as it happened: Google, Meta and Microsoft boost AI spending forecasts](https://www.ft.com/content/b934037d-7fc6-4f93-acdf-a3ec75f45acc?syn-25a6b1a6=1)**

Facebook owner’s stock drops 7% while Alphabet, Microsoft and Amazon report strong cloud computing growth

Financial Times • 8h ago

---

**[US Big Tech Ratchets Up AI Spending Past $700 Billion This Year](https://www.bloomberg.com/news/articles/2026-04-30/us-big-tech-ratchets-up-ai-spending-past-700-billion-this-year)**

Bloomberg.com • 34m ago

---

**[Novartis Reshapes Growth With Biotech Deals And AI Powered R&D Push](https://finance.yahoo.com/sectors/healthcare/articles/novartis-reshapes-growth-biotech-deals-080636551.html)**

Novartis (SWX:NOVN) is expanding its late stage pipeline through acquisitions, highlighted by the recent purchase of Avidity Biosciences. The Avidity deal brings three late stage genetic disorder therapies into the company’s portfolio at a time of industry wide patent cliffs and generic competition. Novartis is also working with Genedata on an AI native R&D data platform to support drug discovery and development productivity. For you as an investor, this combination of deal making and AI...

Yahoo Finance • 32m ago

---

**[Nukes and AI require 1.4 million gallons of water a day at New Mexico lab](https://www.hcn.org/articles/nukes-and-ai-require-1-4-million-gallons-of-water-a-day-at-new-mexico-lab/)**

High Country News • 39m ago

---

**[Where the goblins came from](https://openai.com/index/where-the-goblins-came-from/)**

How goblin outputs spread in AI models: timeline, root cause, and fixes behind personality-driven quirks in GPT-5 behavior.

OpenAI • 5h ago

---

**[Why AI companies want you to be afraid of them](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)**

They built it. They're scared of it. They're selling it anyway.

BBC • 22h ago

---

**[Trump threatens Iran with AI picture of himself with a gun: 'No more Mr. Nice guy!'](https://www.cnbc.com/2026/04/29/trump-iran-threat-ai-picture-gun-war-strait-of-hormuz.html)**

Oil prices continued to rise on Wednesday after U.S. President Donald Trump appeared to threaten Iran in a TruthSocial post.

CNBC • 23h ago

---

**[A.I. Bots Told Scientists How to Make Biological Weapons](https://www.nytimes.com/2026/04/29/us/ai-chatbots-biological-weapons.html)**

The New York Times • 14h ago

---

---

## HackerNews: "ai"

**[Localsend: An open-source cross-platform alternative to AirDrop](https://news.ycombinator.com/item?id=47933208)**

An open-source cross-platform alternative to AirDrop - localsend/localsend

⬆️ 901 • 💬 275 • 1d ago • [GitHub](https://github.com/localsend/localsend)

---

**[4TB of voice samples just stolen from 40k AI contractors at Mercor](https://news.ycombinator.com/item?id=47919630)**

Advanced bio-acoustic analysis for HR, relationships, and personal insights. Trust Your Intuition. Verify It.

⬆️ 590 • 💬 226 • 2d ago • [ORAVYS](https://app.oravys.com/blog/mercor-breach-2026)

---

**[China blocks Meta's acquisition of AI startup Manus](https://news.ycombinator.com/item?id=47920315)**

China said Monday it has decided to block Meta's $2 billion acquisition of Manus, a Singaporean AI startup with Chinese roots.

⬆️ 398 • 💬 333 • 2d ago • [CNBC](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html)

---

**[VibeVoice: Open-source frontier voice AI](https://news.ycombinator.com/item?id=47933236)**

Open-Source Frontier Voice AI. Contribute to microsoft/VibeVoice development by creating an account on GitHub.

⬆️ 385 • 💬 179 • 1d ago • [GitHub](https://github.com/microsoft/VibeVoice)

---

**[Google and Pentagon reportedly agree on deal for 'any lawful' use of AI](https://news.ycombinator.com/item?id=47936156)**

﻿The classified deal apparently doesn’t allow Google to veto how the government will use its AI models.

⬆️ 310 • 💬 277 • 1d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal)

---

**[Claude.ai unavailable and elevated errors on the API](https://news.ycombinator.com/item?id=47938097)**

Claude's Status Page - Claude.ai unavailable and elevated errors on the API.

⬆️ 295 • 💬 250 • 1d ago • [status.claude.com](https://status.claude.com/incidents/9l93x2ht4s5w)

---

**[Why AI companies want you to be afraid of them](https://news.ycombinator.com/item?id=47949750)**

They built it. They're scared of it. They're selling it anyway.

⬆️ 276 • 💬 213 • 17h ago • [bbc.com](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)

---

**[He asked AI to count carbs 27000 times. It couldn't give the same answer twice](https://news.ycombinator.com/item?id=47947490)**

Ask ChatGPT to estimate the carbs in your lunch. Now ask it again. And again. Five hundred times. You’d expect the same answer each time. It’s the same photo, the same model, the same question. But you won’t get the same answer. Not even close — and the differences are large enough to cause a

⬆️ 238 • 💬 296 • 20h ago • [Diabettech - Diabetes and Technology | Where Diabetes and Technology meet](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)

---

**[AI's economics don't make sense](https://news.ycombinator.com/item?id=47936867)**

If you liked this piece, please subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s finances,

⬆️ 230 • 💬 187 • 1d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/ais-economics-dont-make-sense/)

---

**[The Zig project's rationale for their anti-AI contribution policy](https://news.ycombinator.com/item?id=47957294)**

Zig has one of the most stringent anti-LLM policies of any major open source project: No LLMs for issues. No LLMs for pull requests. No LLMs for comments on the …

⬆️ 225 • 💬 95 • 6h ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)

---

---

## YouTube Videos: "ai"

**[Deepseek is a problem](https://www.youtube.com/watch?v=epzzALZ8oYo)**

Check out Zapier MCP https://bit.ly/3QGTz87 Sign up for their Webinar https://bit.ly/3P80Dds Download The 25 OpenClaw Use ...

📺 Matthew Berman

👁️ 49K • 👍 3K • 💬 1K • ⏱️ 17:27 • 8h ago

---

**[Google Just Released The World&#39;s Most Powerful AI Agent](https://www.youtube.com/watch?v=WXoBd5zgTxE)**

Want to make money and save time with AI? Join here: https://www.skool.com/ai-profit-lab-7462/about Video notes + links to the ...

📺 Julian Goldie SEO

👁️ 9K • 👍 257 • 💬 7 • ⏱️ 10:29 • 18h ago

---

**[Musk v. Altman: Tesla CEO expects AI to be &#39;smarter than any human&#39; as soon as 2027](https://www.youtube.com/watch?v=zhod94lzhyk)**

Elon Musk took the stand Tuesday afternoon in the federal trial over the future of OpenAI, telling jurors the case is simply about ...

📺 ABC7 News Bay Area

👁️ 3K • 👍 21 • 💬 24 • ⏱️ 2:47 • 1d ago

---

**[AI Explodes This Month: Mythos Clone, Killer Robot Army, Claude Conway, Artificial Humans &amp; More](https://www.youtube.com/watch?v=XWmWmTDRdbY)**

Try Higgsfield MCP here: https://higgsfield.ai/s/mcp-airevolutionx-UUghuL This month in AI exploded fast. A new AI robot is ...

📺 AI Revolution

👁️ 8K • 👍 259 • 💬 13 • ⏱️ 1:28:49 • 10h ago

---

**[AI Is REPLACING YOU and the MARKET LOVES IT](https://www.youtube.com/watch?v=hsjEckj9kO8)**

The AI revolution isn't coming; it's already here, and it's moving faster than anyone in Washington or on Wall Street wants to admit.

📺 Anthony Scaramucci

👁️ 21K • 👍 1K • 💬 182 • ⏱️ 27:44 • 16h ago

---

**[China&#39;s New AI Controlled City Is INSANE — America Is Far Behind | Xiong&#39;an](https://www.youtube.com/watch?v=L8I28W36wC4)**

What if an entire city, every road, every pipe, every traffic light, every government service, was controlled by a single artificial ...

📺 Core Insights

👁️ 18K • 👍 633 • 💬 66 • ⏱️ 21:00 • 15h ago

---

**[DROPPING LIKE DONIMOES – YouTube’s AI Demonetization is Out of Control (PLEASE FIX THIS, YOUTUBE!)](https://www.youtube.com/watch?v=s7LAoMblOPk)**

FULL LIVESTREAM: https://youtu.be/MD8AuX9A45w #YouTube #Google #Demonetization.

📺 Nerdrotic Daily

👁️ 110K • 👍 9K • 💬 1K • ⏱️ 10:09 • 2d ago

---

**[Trump posts AI image of himself with a gun, says Iran ‘better get smart soon’](https://www.youtube.com/watch?v=Wjsft-U5qLQ)**

The Heritage Foundation senior research fellow Brent Sadler says it may come down to a 'waiting game' as Iran continues to face ...

📺 Fox News

👁️ 53K • 👍 1K • 💬 965 • ⏱️ 5:08 • 10h ago

---

**[Major tech companies report earnings amid AI bubble concerns](https://www.youtube.com/watch?v=R-Y5AxE1NsM)**

Four of the biggest tech companies reported earnings after the closing bell on Wednesday. Adam Levine, senior tech writer for ...

📺 CBS News

👁️ 2K • 👍 10 • 💬 7 • ⏱️ 2:45 • 8h ago

---

**[AI isn’t taking jobs. It’s taking something worse.](https://www.youtube.com/watch?v=NZa5lApeFic)**

You losing your job is the best thing to ever happen. This was a member-only video that my members urged me to make public ...

📺 Mo Bitar

👁️ 205K • 👍 14K • 💬 2K • ⏱️ 6:01 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 271,652 • ❤️ 3,263 • 3d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 198,830 • ❤️ 866 • 3d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 82,887 • ❤️ 1,108 • 7d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 766,593 • ❤️ 1,014 • 6d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 591,214 • ❤️ 1,158 • 5h ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 4,468 • ❤️ 298 • 2d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 855,842 • ❤️ 502 • 7d ago

---

**[DeepSeek-V4-Pro-Base](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-Base)**

*DeepSeek*

`1600.8B`

⬇️ 1,883 • ❤️ 242 • 3d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 1,977,187 • ❤️ 1,520 • 6d ago

---

**[Hy3-preview](https://huggingface.co/tencent/Hy3-preview)**

*Tencent*

Hy3 preview is a 295B parameter Mixture-of-Experts (MoE) model with 21B active parameters, excelling in complex reasoning, instruction following, context learning, coding, and agent tasks. It features a 256K context length and strong performance on STEM, code, and multilingual benchmarks.

`text-generation` `298.8B`

⬇️ 14,145 • ❤️ 189 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 166 • 💬 10 • ⭐ 45,831 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 51 • 💬 2 • ⭐ 55,723 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 14 • 💬 2 • ⭐ 8,349 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 81 • 💬 6 • ⭐ 19,402 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 28 • 💬 3 • ⭐ 22,089 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,229 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://huggingface.co/papers/2604.24764)**

*Weijie Wang, Xiaoxuan He, Youping Gu et al. (12 authors)*

🏢 Microsoft Research

World-R1 framework improves video generation by incorporating 3D constraints through reinforcement learning and specialized text datasets while maintaining visual quality and scalability.

▲ 111 • 💬 3 • ⭐ 268 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24764) • [💻 code](https://github.com/microsoft/World-R1) • [🔗 project](https://aka.ms/world-r1)

---

**[Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://huggingface.co/papers/2604.24763)**

*Zhiheng Liu, Weiming Ren, Xiaoke Huang et al. (15 authors)*

Tuna-2 is a unified multimodal model that performs visual understanding and generation directly from pixel embeddings without pretrained vision encoders, achieving state-of-the-art performance in multimodal benchmarks.

▲ 59 • 💬 4 • ⭐ 351 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24763) • [💻 code](https://github.com/facebookresearch/tuna-2) • [🔗 project](https://tuna-ai.org/tuna-2/)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 76 • 💬 7 • ⭐ 1,615 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 78,615 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 50.8k • 🔱 2.7k • 11d ago

---

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 50.5k • 🔱 6.6k • 1d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 41.0k • 🔱 8.5k • 3d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 38.6k • 🔱 4.3k • 37m ago

---

**[Gitlawb/openclaude](https://github.com/Gitlawb/openclaude)**

runs anywhere. uses anything

`TypeScript` `ai` `ai-agent` `ai-tools` `cli` `coding`

⭐ 25.1k • 🔱 8.2k • 6h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.2k • 🔱 2.5k • 2d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 8.0k • 🔱 481 • 2d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.4k • 🔱 1.1k • 1d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

`Python`

⭐ 5.0k • 🔱 444 • 1d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 4.8k • 🔱 329 • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*
