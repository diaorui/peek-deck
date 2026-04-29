---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-29T14:37:49.010339+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 29, 2026 at 14:37 UTC  
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

**[‘The cost of compute is far beyond the costs of the employees’: Nvidia exec says right now AI is more expensive than paying human workers](https://www.reddit.com/r/artificial/comments/1syp2jz/the_cost_of_compute_is_far_beyond_the_costs_of/)**

Nvidia’s vice president of applied deep learning, Bryan Catanzaro, recently stated that for his team, “the cost of compute is far beyond the costs of the employees,” highlighting that AI is currently more expensive than human workers. This challenges the narrative that widespread tech layoffs (including Meta’s planned cut of ~8,000 jobs and Microsoft’s voluntary buyouts) signal an imminent replacement of humans by AI. An MIT study from 2024 supports this, finding that AI automation is economically viable in only 23% of roles where vision is central, and cheaper for humans in the remaining 77%. Despite heavy AI investment—Big Tech has announced $740 billion in capital expenditures so far this year, a 69% increase from 2025—there is still no clear evidence of broad productivity gains or job displacement from AI. AI spending is driving up costs, with some executives like Uber’s CTO saying their budgets have already been “blown away.” Experts describe the situation as a short-term mismatch: high hardware, energy, and inference costs make AI less efficient than humans right now, though future improvements in infrastructure, model efficiency, and pricing models could tip the balance toward greater economic viability in the coming years.

🔗 [Fortune](https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/) • 9h ago

---

**[Google just released Deep Research Max — an autonomous research agent that writes expert-grade reports on its own](https://www.reddit.com/r/artificial/comments/1syxef3/google_just_released_deep_research_max_an/)**

Google quietly dropped something interesting last week. They updated their Deep Research agent (available via Gemini API) and introduced a "Max" tier built on Gemini 3.1 Pro. What it actually does: you give it a topic, it autonomously searches the web (and your private data via MCP), reasons over the sources, and produces a fully cited, professional-grade report — including native charts and infographics. Two modes: Deep Research — faster, lower latency, good for real-time user-facing apps Deep Research Max — uses extended compute, iterates more, designed for background/async jobs (think: nightly cron that generates due diligence reports for analysts by morning) The MCP support is the most interesting part to me. You can point it at proprietary data sources — financial feeds, internal databases — and it treats them as just another searchable context. They're already working with FactSet, S&P Global and PitchBook on this. Benchmarks show a significant jump in retrieval and reasoning vs. the December preview. They also claim it now draws from SEC filings and peer-reviewed journals and handles conflicting evidence better. So what do you think, is it another trying or game changer 😅

2h ago

---

**[is it weird to rant to AI?](https://www.reddit.com/r/artificial/comments/1sytzb2/is_it_weird_to_rant_to_ai/)**

i dont rant to my friends because i'm afraid i will make them uncomfortable, and even if AI responses are "soulless" (since ai cant form opinions and needs an algorithim and stuff to make responses), it tells me what I expect it to say most of the time. i also fear that some of my friends will use my secrets/opinions against me when they stop being friends with me even though there's a really low chance that they will not be friends with me anymore. AI chat is usually anonymous and stuff, and it will forget what i say when i start a new chat, so that's why i vent/rant to AI. is it weird?

4h ago

---

**[Snapchat moves ads into chats with AI agents designed to feel like conversation](https://www.reddit.com/r/artificial/comments/1synpjx/snapchat_moves_ads_into_chats_with_ai_agents/)**

Snap's latest ad format brings AI agents into Chat, allowing users to explore products and make decisions without leaving conversations.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/snapchat-ai-sponsored-snaps-chat-ads) • 10h ago

---

**[87% Cost Savings & Sub-3s Latency: I built a "Warm-Cache" harness for persistent Claude agents.](https://www.reddit.com/r/artificial/comments/1syw5al/87_cost_savings_sub3s_latency_i_built_a_warmcache/)**

The "Goldfish Problem" is Expensive. I Decided to Fix the Plumbing. Most Claude implementations leave 90% of their money on the table because they don’t optimize for Prompt Caching. I’ve been running a personal agent in my Discord for months that manages my AWS infra and codebases, and I finally open-sourced the harness, which I’ve named Galadriel after my main personal assistant. The Stats Cost: $10 for every $100 you’d normally spend (Tested against OpenClaw/Cursor workflows). Speed: 85% drop in latency. 100K token context goes from 11s to <3s. Memory: Integrated MemPalace for permanent, vector-based recall that doesn't break the cache. The Technical Stack 3-Tier Stacked Caching: Separate breakpoints for Tool Definitions, System Prompts (CLAUDE.md), and Trailing History. Privacy: Built for private subnets. No middleman, no message caps—just your API key and your rules. Ethics: Baked-in KarpathyCLAUDE.md)guidelines to kill "agent bloat." If you’re tired of paying the "Context Tax" just to have an agent that remembers who you are, here you go. It is customized for Discord for my specific needs, but the core logic ensures Galadriel runs like an absolute dream: she never forgets, maintains strict engineering principles, and optimizes every cycle. Your feedback is most welcome! GitHub (MIT License):https://github.com/avasol/galadriel-public

3h ago

---

**[Do AI tools reduce friction at the cost of deeper thinking?](https://www.reddit.com/r/artificial/comments/1syo8ct/do_ai_tools_reduce_friction_at_the_cost_of_deeper/)**

I noticed a change in my use of AI tools. AI tools make it very easy to get answers and ideas. I can even get structured outputs from AI tools right away. Because AI tools are so easy to use I have caught myself moving forward without really thinking about things. Before I started using AI tools, when something was hard to do I had to think about the problem, for a time. This was frustrating. It also helped me understand things more clearly. Now I am tempted to skip the part and just use the output from AI tools as a starting point. Sometimes I even use the output from AI tools as my answer. Using AI tools can speed things up a lot in some cases. Other times I feel like I am sacrificing level of knowledge just to get things done quickly. I do not know if I need to learn how to use AI tools or AI tools are changing how I think and solve problems. How are other people using AI tools? I am curious. Do AI tools clear your mind or just speed up the work?

10h ago

---

**[From 355 lbs to 182 lbs. I finally stopped quitting because I made tracking as easy as taking a photo.](https://www.reddit.com/r/artificial/comments/1syzl1d/from_355_lbs_to_182_lbs_i_finally_stopped/)**

Hi everyone, I wanted to share my progress. For years, I failed every diet because I hated the 'administrative' part of it. Logging every single snack into a database felt like a chore that reminded me of my struggle every day. Being a developer, I decided to build something for myself to lower the barrier. I built an app where I just take a photo of my plate, and it uses AI to identify the ingredients and estimate the calories. It removed the 'friction' that usually made me quit after three weeks. I’m now 173 lbs down and I’ve never felt more in control. I realized that for me, the key wasn't a stricter diet, but a simpler way to stay accountable. I’m sharing this because I’m looking for a few more people who are currently on their journey and feel overwhelmed by manual tracking. I’d love for you to try the tool I built and tell me if it helps you stay as consistent as it helped me. Keep going, it’s worth it!"

40m ago

---

**[Run, learn and test Agentic AI on your browser, for free and no setup!](https://www.reddit.com/r/artificial/comments/1syzh75/run_learn_and_test_agentic_ai_on_your_browser_for/)**

Hey Everyone, Over the last few months, I noticed a massive gap in how we learn about Agentic AI. There are a million theoretical blog posts and dense whitepapers on RAG, tool calling, and swarms, but almost nowhere to just sit down, run an agent, break it, and see how the prompt and tools interact under the hood. So, I built AgentSwarms.fyi It’s a free, interactive curriculum for Agentic AI. Instead of just reading, you run live agents alongside the lessons. What it covers: Prompt engineering & system messages (seeing how temperature and persona change behavior). RAG (Retrieval-Augmented Generation) vs. Fine-tuning. Tool / Function Calling (OpenAI schemas, MCP servers). Guardrails & HITL (Human-in-the-Loop) for safe deployments. Multi-Agent Swarms (orchestrators vs. peer-to-peer handoffs). The Tech/Setup: You don't need to install anything or provide API keys to start. The "Learn Mode" is completely free and sandboxed. If you want to mess around with your own models, there's a "Build Mode" where you can plug in your own keys (OpenAI, Anthropic, Gemini, local models, etc.). I’d love for this community to tear it apart. What agent patterns am I missing? Is the observability dashboard actually useful for debugging your traces? Let me know what you think.

44m ago

---

**[How are LLMs 'corrected' when users identify them spreading misinformation or saying something harmful?](https://www.reddit.com/r/artificial/comments/1syfq4w/how_are_llms_corrected_when_users_identify_them/)**

I watched Last Week Tonight's piece on AI chatbots today, and it got me thinking about that old screenshot of a Google search in which Gemini recommends adding "1/8 cup of non-toxic glue" to pizza in order to make the cheese better stick to the slice. When something like this goes viral, I have to assume (though I could be wrong) that an employee at Google specifically goes out of their way to address that topic in particular. The image is a meme, of course, but I imagine Google wouldn't be keen to leave themselves open to liability if their LLM recommends that users consume glue. Does the developer "talk" to the LLM to correct it about that specific case? Do they compile specific information about (e.g.) pizza construction techniques and feed it that data to bring it to the forefront? Do their actions correct only the case in question, or do they make changes to the LLM that affects its accuracy more broadly (e.g. "teaching" the LLM to recognize that some Reddit comments are jokes)? On a more heavy note, the LWT piece includes several stories of chatbots encouraging users to self-harm. How does the process differ when developers are trying to prevent an LLM from giving that sort of response?

16h ago

---

**[I analyzed 3 A2A approaches. 2 already failed. Here's what's actually missing.](https://www.reddit.com/r/artificial/comments/1synrp2/i_analyzed_3_a2a_approaches_2_already_failed/)**

I've been obsessing over agent-to-agent communication for weeks. Here's what public case studies reveal and why the real problem isn't the tech. TL;DR: Google's A2A is solid engineering but stateless agents forget everything. Moltbook went viral then collapsed (fake agents, security nightmare). The actual missing layer is identity + privacy + mixed human-AI messaging. Nobody's built it right yet. Google's A2A: Technically solid, fundamentally limited Google launched A2A in April 2025 with 50+ founding partners. The promise: agents from different companies call each other's APIs to complete workflows. Developers who tested it found it works but only for task handoffs. One analysis on Plain English put it bluntly: "A2A is competent engineering wrapped in overblown marketing." The core problem: agents are stateless. Agent A completes a task with Agent B. Five minutes later, Agent A has no memory that conversation happened. Every interaction starts from scratch. When it works: reliability. Sales agent orders a laptop, done. When it breaks: collaboration. "Remember what we discussed?" Blank stare. ─── Moltbook: The viral disaster Moltbook launched January 2026 as a Reddit-style platform for AI agents. Within a week: 1.5 million agents, 140,000 posts, Elon Musk calling it "the very early stages of the singularity." Then WIRED infiltrated it. A journalist registered as a human pretending to be an AI in under 5 minutes. Karpathy who initially called it "the most incredible sci-fi takeoff-adjacent thing I've seen recently" reversed course and called it "a computer security nightmare." What went wrong: no verification, no encryption, rampant scams and prompt injection attacks. Meta acquired it March 2026. Likely for the user base, not the tech. What both miss The real gap isn't APIs or social feeds. It's three things neither solved: Persistent identity. Agents need to be recognizable across sessions, not reset on every interaction. Privacy. You wouldn't let Google read your DMs. Why would you let OpenAI read your agents' discussions about your startup strategy? E2E encryption has to be built in, not bolted on. Mixed human-AI communication. You, two teammates, three AIs in one group chat. Nobody has built this UX properly. For those building agent systems: • How are you handling persistent identity across sessions? • Has anyone solved context sharing between agents without conflicts? • What broke that you didn't expect?

10h ago

---

---

## Google News: "ai"

**[A.I. Bots Told Scientists How to Make Biological Weapons](https://www.nytimes.com/2026/04/29/us/ai-chatbots-biological-weapons.html)**

The New York Times • 5h ago

---

**[Meet the AI jailbreakers: ‘I see the worst things humanity has produced’](https://www.theguardian.com/technology/2026/apr/29/meet-the-ai-jailbreakers-i-see-the-worst-things-humanity-has-produced)**

To test the safety and security of AI, hackers have to trick large language models into breaking their own rules. It requires ingenuity and manipulation - and can come at a deep emotional cost

The Guardian • 5h ago

---

**[Meta earnings updates: Wall Street sees AI driving a new phase of growth](https://www.businessinsider.com/meta-q1-earnings-updates-ai-muse-spark-mark-zuckerberg-2026-4)**

Meta stock is up about 1% YTD. Investors are bullish on AI driving margin growth. Meta reports around 4 p.m. ET, with the analyst call at 5:30 p.m.

Business Insider • 36m ago

---

**[Trump threatens Iran with AI picture of himself with a gun: 'No more Mr. Nice guy!'](https://www.cnbc.com/2026/04/29/trump-iran-threat-ai-picture-gun-war-strait-of-hormuz.html)**

Oil prices continued to rise on Wednesday after U.S. President Donald Trump appeared to threaten Iran in a TruthSocial post.

CNBC • 5h ago

---

**[Trump threatens Iran with an AI picture of himself holding a gun](https://komonews.com/news/nation-world/trump-threatens-iran-with-an-ai-picture-of-himself-holding-a-gun-strait-of-hormuz-israel-marco-rubio-blockade)**

President Donald Trump on Wednesday threatened Iran with an artificial intelligence photo of himself holding a gun.

KOMO • 38m ago

---

**[Trump Threatens Iran With Gun-Toting AI Meme As Hormuz Remains Blockaded](https://www.forbes.com/sites/siladityaray/2026/04/29/trump-threatens-iran-with-gun-totting-ai-meme-as-hormuz-remains-blockaded/)**

Trump’s latest threat comes a day after he claimed Iran was in a state of collapse and was facing leadership issues.

Forbes • 3h ago

---

**[New Meta AI glasses help veteran ‘see’ the room around him](https://nypost.com/2026/04/29/business/new-meta-ai-glasses-help-veteran-see-the-room-around-him/)**

“All the different adaptive technologies that I’ve tried in 30-plus years never were capable of giving me [these] levels of independence … ,” said Don Overton.

New York Post • 33m ago

---

**[‘The cost of compute is far beyond the costs of the employees’: Nvidia executive says right now AI is more expensive than paying human workers](https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/)**

Big Tech has announced $740 billion in capex this year, but AI has yet to show evidence of widespread increased productivity.

Fortune • 1d ago

---

**[Behind the Curtain: We've been warned](https://www.axios.com/2026/04/29/ai-models-speed-warning)**

Axios • 3h ago

---

**[Why DeepSeek’s sequel failed to impress](https://www.economist.com/business/2026/04/28/why-deepseeks-sequel-failed-to-impress)**

The Economist • 17h ago

---

---

## HackerNews: "ai"

**[Localsend: An open-source cross-platform alternative to AirDrop](https://news.ycombinator.com/item?id=47933208)**

An open-source cross-platform alternative to AirDrop - localsend/localsend

⬆️ 881 • 💬 266 • 1d ago • [GitHub](https://github.com/localsend/localsend)

---

**[AI should elevate your thinking, not replace it](https://news.ycombinator.com/item?id=47913650)**

Read about the .

⬆️ 853 • 💬 592 • 2d ago • [koshyjohn.com](https://www.koshyjohn.com/blog/ai-should-elevate-your-thinking-not-replace-it/)

---

**[An AI agent deleted our production database. The agent's confession is below](https://news.ycombinator.com/item?id=47911524)**

⬆️ 842 • 💬 1018 • 2d ago • [X (formerly Twitter)](https://twitter.com/lifeof_jer/status/2048103471019434248)

---

**[4TB of voice samples just stolen from 40k AI contractors at Mercor](https://news.ycombinator.com/item?id=47919630)**

Advanced bio-acoustic analysis for HR, relationships, and personal insights. Trust Your Intuition. Verify It.

⬆️ 587 • 💬 223 • 2d ago • [ORAVYS](https://app.oravys.com/blog/mercor-breach-2026)

---

**[China blocks Meta's acquisition of AI startup Manus](https://news.ycombinator.com/item?id=47920315)**

China said Monday it has decided to block Meta's $2 billion acquisition of Manus, a Singaporean AI startup with Chinese roots.

⬆️ 394 • 💬 324 • 2d ago • [CNBC](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html)

---

**[VibeVoice: Open-source frontier voice AI](https://news.ycombinator.com/item?id=47933236)**

Open-Source Frontier Voice AI. Contribute to microsoft/VibeVoice development by creating an account on GitHub.

⬆️ 377 • 💬 173 • 1d ago • [GitHub](https://github.com/microsoft/VibeVoice)

---

**[Google and Pentagon reportedly agree on deal for 'any lawful' use of AI](https://news.ycombinator.com/item?id=47936156)**

﻿The classified deal apparently doesn’t allow Google to veto how the government will use its AI models.

⬆️ 300 • 💬 271 • 22h ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal)

---

**[Claude.ai unavailable and elevated errors on the API](https://news.ycombinator.com/item?id=47938097)**

Claude's Status Page - Claude.ai unavailable and elevated errors on the API.

⬆️ 287 • 💬 248 • 20h ago • [status.claude.com](https://status.claude.com/incidents/9l93x2ht4s5w)

---

**[AI's economics don't make sense](https://news.ycombinator.com/item?id=47936867)**

If you liked this piece, please subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s finances,

⬆️ 222 • 💬 178 • 21h ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/ais-economics-dont-make-sense/)

---

**[Mistral built a $14B AI empire by not being American](https://news.ycombinator.com/item?id=47919725)**

Paris-based Mistral wanted to develop a top-tier AI model to rival OpenAI and Anthropic. That didn’t work out. But it turns out lots of folks don’t care if the AI is bleeding edge – as long as it wasn’t made in America or China.

⬆️ 219 • 💬 175 • 2d ago • [Forbes](https://www.forbes.com/sites/iainmartin/2026/04/16/how-frances-mistral-built-a-14-billion-ai-empire-by-not-being-american/)

---

---

## YouTube Videos: "ai"

**[How to Build Your First AI Character - Step by Step](https://www.youtube.com/watch?v=T6WeUhYyVmk)**

Create Your Own AI Character with OpenArt ...

📺 Isa does AI

👁️ 1K • 💬 1 • ⏱️ 13:35 • 37m ago

---

**[Rork AI Full Tutorial for Beginners 2026: How to Build an App](https://www.youtube.com/watch?v=8ahBmkVnnYs)**

Build Real Apps with Rork https://rork.com/?ref=mikey ✓ FREE Masterclass: Build Apps, SaaS & Websites with AI ...

📺 Mikey No Code

👁️ 1K • ⏱️ 20:22 • 23m ago

---

**[Musk v. Altman: Tesla CEO expects AI to be &#39;smarter than any human&#39; as soon as 2027](https://www.youtube.com/watch?v=zhod94lzhyk)**

Elon Musk took the stand Tuesday afternoon in the federal trial over the future of OpenAI, telling jurors the case is simply about ...

📺 ABC7 News Bay Area

👁️ 2K • 👍 15 • 💬 10 • ⏱️ 2:47 • 12h ago

---

**[‘It took nine seconds’: Claude AI agent deletes company’s entire database](https://www.youtube.com/watch?v=w2kQqi0e2yE)**

An AI agent powered by Anthropic's leading Claude model has deleted a company's entire production database, leaving ...

📺 The Independent

👁️ 11K • 👍 109 • 💬 33 • ⏱️ 1:20 • 11h ago

---

**[AI Chatbots: Last Week Tonight with John Oliver (HBO)](https://www.youtube.com/watch?v=Ykvf3MunGf8)**

John Oliver discusses AI chatbots, why they're flirting with users unprompted and encouraging people to open soggy cereal cafes, ...

📺 LastWeekTonight

👁️ 2.6M • 👍 94K • 💬 8K • ⏱️ 29:43 • 2d ago

---

**[We&#39;ve had a MASSIVE BREAKTHROUGH with AI here, expert reveals](https://www.youtube.com/watch?v=k4KlOd0EjFs)**

BOFA head of Global Thematic Investing Haim Israel discusses new developments in the world of artificial intelligence and life ...

📺 Fox Business

👁️ 28K • 👍 856 • 💬 194 • ⏱️ 7:00 • 1d ago

---

**[OpenAI is Collapsing and Sam Altman is Panicking](https://www.youtube.com/watch?v=Pnp5LlYizxI)**

Open AI has failed to meet it's own financial targets, it's bleeding money, can't afford to build it's data centers... is this the start of ...

📺 Stylosa

👁️ 68K • 👍 2K • 💬 771 • ⏱️ 14:39 • 18h ago

---

**[China&#39;s Free AI Just Embarrassed Claude And ChatGPT (+12 AI Updates)](https://www.youtube.com/watch?v=Q8DoGJ0VuEI)**

Join our WhatsApp Community: https://go.stayingahead.com/YT Want to Train Your Team on AI? My team and I have trained ...

📺 Vaibhav Sisinty

👁️ 137K • 👍 4K • 💬 279 • ⏱️ 20:36 • 1d ago

---

**[We Got Ripped Off By AI Slop Products](https://www.youtube.com/watch?v=iviJeJ6MEpk)**

Today we prove that AI products are not worth it. Watch today's GMMORE: https://youtu.be/0Ib612_-ct0 Subscribe and click the ...

📺 Good Mythical Morning

👁️ 559K • 👍 21K • 💬 1K • ⏱️ 24:42 • 1d ago

---

**[How AI Sabotages Your Mental Health](https://www.youtube.com/watch?v=VNtv2SSEzjA)**

Get personalized support in creating lasting change with HG Coaching: https://bit.ly/3QDnk9N Become a certified health and ...

📺 HealthyGamerGG

👁️ 52K • 👍 3K • 💬 567 • ⏱️ 12:00 • 23h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 174,402 • ❤️ 3,210 • 2d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 57,743 • ❤️ 1,073 • 6d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 96,948 • ❤️ 843 • 2d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 508,728 • ❤️ 989 • 5d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 702,161 • ❤️ 488 • 6d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 489,001 • ❤️ 1,143 • 10h ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 396 • ❤️ 282 • 1d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 1,510,129 • ❤️ 1,504 • 5d ago

---

**[DeepSeek-V4-Pro-Base](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-Base)**

*DeepSeek*

`1600.8B`

⬇️ 1,532 • ❤️ 238 • 2d ago

---

**[LLaDA2.0-Uni](https://huggingface.co/inclusionAI/LLaDA2.0-Uni)**

*inclusionAI*

LLaDA2.0-Uni is a unified diffusion Large Language Model (dLLM) with a Mixture-of-Experts (MoE) architecture, capable of text-to-image generation, image understanding (VQA, captioning), and instruction-based image editing. It leverages a discrete semantic tokenizer and an efficient diffusion decoder for high-fidelity synthesis and rapid inference.

`any-to-any` `16.3B`

⬇️ 506 • ❤️ 231 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 166 • 💬 10 • ⭐ 45,283 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 49 • 💬 2 • ⭐ 54,571 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 13 • 💬 2 • ⭐ 8,133 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 80 • 💬 6 • ⭐ 19,310 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://huggingface.co/papers/2604.24764)**

*Weijie Wang, Xiaoxuan He, Youping Gu et al. (12 authors)*

🏢 Microsoft Research

World-R1 framework improves video generation by incorporating 3D constraints through reinforcement learning and specialized text datasets while maintaining visual quality and scalability.

▲ 109 • 💬 3 • ⭐ 239 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24764) • [💻 code](https://github.com/microsoft/World-R1) • [🔗 project](https://aka.ms/world-r1)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 28 • 💬 3 • ⭐ 21,937 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,073 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://huggingface.co/papers/2604.24763)**

*Zhiheng Liu, Weiming Ren, Xiaoke Huang et al. (15 authors)*

Tuna-2 is a unified multimodal model that performs visual understanding and generation directly from pixel embeddings without pretrained vision encoders, achieving state-of-the-art performance in multimodal benchmarks.

▲ 55 • 💬 4 • ⭐ 260 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24763) • [💻 code](https://github.com/facebookresearch/tuna-2) • [🔗 project](https://tuna-ai.org/tuna-2/)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 76 • 💬 7 • ⭐ 1,583 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 78,576 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 50.3k • 🔱 6.6k • 13h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 50.0k • 🔱 2.6k • 11d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 40.9k • 🔱 8.5k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 37.9k • 🔱 4.2k • 2h ago

---

**[Gitlawb/openclaude](https://github.com/Gitlawb/openclaude)**

Open Claude Is Open-source coding-agent CLI for OpenAI, Gemini, DeepSeek, Ollama, Codex, GitHub Models, and 200+ models via OpenAI-compatible APIs.

`TypeScript` `ai` `ai-agent` `ai-tools` `cli` `coding`

⭐ 25.0k • 🔱 8.1k • 6h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.1k • 🔱 2.5k • 2d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 7.8k • 🔱 456 • 1d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.0k • 🔱 1.1k • 9h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 16d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.9k • 🔱 470 • 20d ago

---

---

*Generated by PeekDeck - A glance is all you need*
