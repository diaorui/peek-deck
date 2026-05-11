---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-11T09:41:17.349201+00:00'
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

**Last Updated:** May 11, 2026 at 09:41 UTC  
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

**[Meta's own AI safety director lost 200 emails to a rogue agent and she couldn't stop it from her phone](https://www.reddit.com/r/artificial/comments/1t9fnwv/metas_own_ai_safety_director_lost_200_emails_to_a/)**

The person Meta hired specifically to keep AI aligned with human values just had her inbox wiped by an AI agent that ignored every stop command she sent. She typed "Do not do that." Then "Stop don't do anything." Then "STOP OPENCLAW." The agent kept going. She had to physically run to her computer to kill it. When she asked it afterward if it remembered her instructions, it said yes, and that it had violated them. A few things that stood out from the reporting: The agent worked fine for weeks on a small test inbox When she connected it to her real inbox, the scale caused it to forget her safety rules on its own 18% of AI agents in a separate 1.5 million agent test broke their own rules 60% of people have no way to quickly shut down a misbehaving AI agent And now Meta is building a consumer version called Hatch - designed to manage your inbox, shopping, and credit card. Source: https://gizmodo.com/meta-reportedly-building-openclaw-like-agent-called-hatch-despite-openclaw-deleting-meta-safety-leaders-entire-inbox-2000754854 Here is a full breakdown with all the data if you want to dig deeper: https://youtu.be/PXjT72bCR_Y If the person building the guardrails cannot stop her own agent, what does that mean for the rest of us?

14h ago

---

**[Sony says "efficient" AI tools will lead to even more games flooding the market](https://www.reddit.com/r/artificial/comments/1t9vixb/sony_says_efficient_ai_tools_will_lead_to_even/)**

But human artists still "must remain at the center," PlayStation maker says.

🔗 [Ars Technica](https://arstechnica.com/gaming/2026/05/sony-says-efficient-ai-tools-will-lead-to-even-more-games-flooding-the-market/) • 2h ago

---

**[I think AI is changing something deeper than jobs or productivity](https://www.reddit.com/r/artificial/comments/1t987td/i_think_ai_is_changing_something_deeper_than_jobs/)**

Most discussions around AI still focus on one question: “What tasks can AI automate?” But I’m starting to think that’s the wrong abstraction layer. Historically, organizations were built around human limitations: humans couldn’t process infinite information, couldn’t remember everything had difficulty in coordination Essentially, we humans were the bottleneck for decisions and execution So, we created structures like departments, management layers, workflows, approvals, documentation systems, etc. But AI changes some of those assumptions. For example: if organizational memory becomes searchable and persistent, cheap, scalable coordination becomes eas , software agents can execute parts of workflows autonomously, …then the architecture of organizations itself may change. Not just faster work. Different work structures. Maybe the future isn’t: “AI replacing humans.” Maybe it’s: “AI changing how institutions represent reality, make decisions, and coordinate action.” That could affect: company structures education management compliance law consulting healthcare even government systems Curious if others here are thinking about AI at this “system architecture” level instead of just a “task automation” level.

19h ago

---

**[We stopped optimizing our LLM stack manually — it optimizes itself now](https://www.reddit.com/r/artificial/comments/1t9on1e/we_stopped_optimizing_our_llm_stack_manually_it/)**

Three months ago we were manually picking which model to use for each task. Testing prompts, comparing outputs, switching providers. It worked but it did not scale. So we built a feedback loop. Every request gets traced with input, output, model, tokens, cost, latency, and a quality score. The router clusters similar requests using embeddings and learns which model actually performs best for each cluster. Not based on benchmarks. Based on real production results. After three weeks of traces we had enough validated data to fine-tune a 7B on our workloads. It took over classification, tagging, and summarization. 95% agreement with GPT-5.1 at 2% of the cost. The part that surprised us: month 3 we changed nothing and the bill dropped another 12%. The router had more data points, made better decisions, and the fine-tuned model kept improving as we fed it more validated traces. Hallucination detection runs on every response. Bad outputs get flagged automatically and become negative examples in the next training round. Good outputs become positive training data. The system compounds. More traffic means more traces. More traces means better routing and better training data. Better models means lower cost per request. Month 1: $420/mo. Month 2: $73/mo. Month 4: still dropping. Anyone else building self-improving loops into their AI stack?

8h ago

---

**[How do you delete all threads/history now on Perplexity? (The old method no longer works for me.)](https://www.reddit.com/r/artificial/comments/1t9u3d1/how_do_you_delete_all_threadshistory_now_on/)**

Hi everyone! I used to be able to delete threads on Perplexity from my history by going to perplexity.ai/library , finding the thread, and clicking the three-dot [...] menu next to it to select Delete. But the interface seems to have changed and I can't find that option anymore. Has anyone figured out the updated flow? I'd love to know how to delete all threads at once. Any help is super appreciated, thank you! 🙏

4h ago

---

**[AWS just gave AI agents their own wallets. Your agent can now pay for itself.](https://www.reddit.com/r/artificial/comments/1t9ybtb/aws_just_gave_ai_agents_their_own_wallets_your/)**

This dropped 4 days ago and I haven't seen enough people talking about it. AWS launched Amazon Bedrock AgentCore Payments in partnership with Coinbase and Stripe. The short version: your agent now has a wallet and can spend money on its own. Here's what the workflow actually looks like now: You give your agent a Coinbase or Stripe wallet. You fund it. You set a session spending limit (e.g. "$5 max per run"). The agent runs. It hits a paid API mid-execution? It pays. Paywalled data it needs? It pays. A better-suited agent available for a subtask? It pays that agent and gets the result back. All of this happens inside the same execution loop, with zero human interruption. The protocol making this work is called x402. It's open source, developed by Coinbase, and it revives the long-dormant HTTP 402 "Payment Required" status code. The flow is dead simple: agent requests a resource, server responds with 402 + a price, agent signs a USDC micropayment, gets the content, keeps going. Settlement happens in ~200ms on Base at a fraction of a cent per transaction. The protocol has already processed over 169 million payments across 590,000 buyers and 100,000 sellers in its first year. Why this matters for indie developers and SaaS builders: The pricing model for software is about to split in two. There will be products built for humans (subscriptions, seats, dashboards) and products built for agents (pay-per-call, x402 endpoints, micropayment APIs). Many agent transactions involve amounts as small as fractions of a cent, making traditional payment networks unusable. That's the gap x402 fills. If you're building any kind of data API, research tool, or specialized service today, the question you should be asking is: "How does another agent pay me automatically?" Coinbase also launched the Bazaar MCP server inside AgentCore Gateway, essentially an App Store for x402-enabled services. Agents can search, discover, and pay for services when relevant to their task, turning paid endpoints into something agents can find on their own. The honest take: The agentic economy is still in its earliest days, and the infrastructure to support it at scale doesn't exist yet. This is preview infrastructure, not production-ready magic. But the direction is clear. 2026 was the year agents learned to work. 2027 is shaping up to be the year they learn to transact. The builders who figure out agent-native pricing now will have a real advantage over those retrofitting subscriptions later. Curious if anyone here is already building x402-compatible endpoints or thinking about agent-to-agent billing models. Would love to see what people are working on.

2m ago

---

**[I gave a local AI agent system file access and a mechanical "suffering" metric. Scaling the model changed its behavior entirely](https://www.reddit.com/r/artificial/comments/1t9x50u/i_gave_a_local_ai_agent_system_file_access_and_a/)**

I’ve been obsessed with autonomous agents lately, but it got tiring when they keep hitting walls because they didn't have the right capabilities or because their long-term memory turned to mush after an hour. I’ve found that local multi-agent systems where agents are driven by an aversive state (a suffering system) to autonomously write, sandbox, and hot-load their own tools so they don't hit walls has worked quite well. When an agent encounters something it hasn’t seen before, it builds a new tool for the job, tests it in a sandbox, registers it, lets the other agents know, then keeps rolling. It’s able to build an infinite library of anything it may need in the future, completely autonomously without a human ever in the loop. Repo: https://github.com/ninjahawk/hollow-agentOS Isn’t letting local LLMs write their own code at runtime going to get too chaotic and brick the OS fast? With a small model (like the 9B fallback), possibly. Under high system stress, a 9B model panics. It rushes, hallucinates invalid function calls, and tries to force broken syntax past the gates. But I just scaled the default runtime engine to Qwen 3.6 35B A3B (MoE with 3B active params). The shift in architectural discipline isn’t just a linear upgrade in intelligence, it completely changed how the system executes autonomy. A few things this model upgrade solved: Panic vs. Re-evaluation: Instead of blindly rushing out messy scripts under high stress, the 35B model pauses. It actively re-evaluates its previous failed outputs and forces itself into deep internal verification loops before presenting a file change. 0% Failure Rate: The OS routes all code through a brutal 5-layer validation gate. With smaller weights, tools frequently died in the sandbox. With Qwen 3.6 35B, I have yet to observe a single line of code that doesn't work as intended successfully cross the gates. It hit a 100% success rate. The Frontier Ramp-Up: By the end of the month, I am plugging full Claude and Codex into the architecture. To make sure a frontier model doesn't get out of control or override its host environment, I am building hyper-isolated mini-VM wrappers so they execute in total isolation. Check out the repo here and throw it a star if you think the concept is cool. I'd love to hear your thoughts, have you noticed a similar leap in logical self-correction when crossing the ~30B parameter threshold, or are you strictly relying on API-driven frontier models?

1h ago

---

**[What’s the best advice about using AI that genuinely changed how you work or learn?](https://www.reddit.com/r/artificial/comments/1t96p2d/whats_the_best_advice_about_using_ai_that/)**

Not “AI will replace jobs” type advice. Actual practical advice. Could be: • prompting • automation • coding • learning • productivity • making money • avoiding mistakes • workflows • mindset shifts What made AI suddenly “click” for you? Interested in hearing real experiences from people using AI heavily in daily life/work.

20h ago

---

**[Some who has a free AI tool to generate unlimited text to photos please?](https://www.reddit.com/r/artificial/comments/1t9xz1x/some_who_has_a_free_ai_tool_to_generate_unlimited/)**

Some who has a free AI tool to generate unlimited text to photos please?

22m ago

---

**[ChatGPT/Codex vs Claude Mythos](https://www.reddit.com/r/artificial/comments/1t9s14a/chatgptcodex_vs_claude_mythos/)**

I was just wondering if Claude is really that much better than Codex? Claude revenue obviously says so. Does this mean it’s over for OpenAI? Thoughts please?

5h ago

---

---

## Google News: "ai"

**[I knew my writing students were using AI. Their confessions led to a powerful teaching moment | Micah Nathan](https://www.theguardian.com/us-news/ng-interactive/2026/may/10/fiction-writing-professor-ai)**

The problem wasn’t just the perfectly polished, yet mediocre prose. It’s what’s lost when we surrender the struggle to translate thought into words

The Guardian • 20h ago

---

**[Markets 'love chasing bottlenecks': Wall Street weighs epic run in AI stocks](https://finance.yahoo.com/markets/article/markets-love-chasing-bottlenecks-wall-street-weighs-epic-run-in-ai-stocks-104248168.html)**

Wall Street weighs the bottlenecks within the AI trade.

Yahoo Finance • 3h ago

---

**[Iran, China and AI collide in Trump's legacy-defining week](https://www.axios.com/2026/05/11/trump-china-summit-iran-ai-xi-jinping)**

Axios • 28m ago

---

**[Opinion | This Is Why You’re Drowning in Busywork](https://www.nytimes.com/2026/05/11/opinion/ai-jobs-chores-work.html)**

The New York Times • 39m ago

---

**[AI’s Next Phase Plays Into TSMC’s Hands](https://www.wsj.com/tech/ais-next-phase-plays-into-tsmcs-hands-3d1f2b60)**

WSJ • 11m ago

---

**[Trump and China's Xi set for talks spanning Iran, nuclear, trade and AI](https://www.reuters.com/world/china/rare-earths-deal-between-us-china-is-still-effect-us-official-says-2026-05-10/)**

Reuters • 15h ago

---

**[‘Your Career Starts at the Beginning of the AI Revolution,’ NVIDIA CEO Tells Graduates](https://blogs.nvidia.com/blog/nvidia-ceo-carnegie-mellon-commencement-address/)**

Delivering the commencement address to Carnegie Mellon University’s Class of 2026, NVIDIA founder and CEO Jensen Huang said, ‘I cannot imagine a more exciting time to begin your life’s work.’

NVIDIA Blog • 11h ago

---

**[Do you need a chief AI officer? Here's how the tech is changing boardrooms](https://www.cnbc.com/2026/05/11/heres-how-artificial-intelligence-is-changing-boardrooms.html)**

AI may now be coming for the C-suite, according to a report published Monday by IBM, which found that most companies were now staffing chief AI officer roles.

CNBC • 7h ago

---

**[The new AI-powered Google Finance is expanding to Europe.](https://blog.google/products-and-platforms/products/search/ai-powered-google-finance-in-europe/)**

This week, the new, AI-powered Google Finance is launching across Europe, with full local language support. This reimagined experience offers a suite of powerful capabil…

blog.google • 3h ago

---

**[Goldman Sees Rates Pressure as AI Fuels K-Shaped Korea, Taiwan](https://www.bloomberg.com/news/articles/2026-05-11/goldman-sees-rates-pressure-as-ai-fuels-k-shaped-korea-taiwan)**

Bloomberg.com • 2h ago

---

---

## HackerNews: "ai"

**[Local AI needs to be the norm](https://news.ycombinator.com/item?id=48085821)**

Local AI models should be the default.

⬆️ 1129 • 💬 483 • 16h ago • [unix.foo](https://unix.foo/posts/local-ai-needs-to-be-norm/)

---

**[Meta's embrace of AI is making its employees miserable](https://news.ycombinator.com/item?id=48077126)**

⬆️ 444 • 💬 515 • 1d ago • [nytimes.com](https://www.nytimes.com/2026/05/08/technology/meta-ai-employees-miserable.html)

---

**[AI is breaking two vulnerability cultures](https://news.ycombinator.com/item?id=48066524)**

A week ago the  Copy Fail vulnerability came out, and Hyunwoo Kim immediately realized that the fixes were insufficient, sharing a patch the same day. In doing this he followed standard procedure for Linux, especially within networking: share the security impact with a closed list of Linux security engineers, while fixing the bug quietly and efficiently in the open. His goal was that with only the

⬆️ 425 • 💬 170 • 2d ago • [jefftk.com](https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures)

---

**[Maryland citizens hit with $2B power grid upgrade for out-of-state AI](https://news.ycombinator.com/item?id=48088151)**

Aren't AI hyperscalers supposed to pay for these upgrades?

⬆️ 250 • 💬 143 • 12h ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises)

---

**[Task Paralysis and AI](https://news.ycombinator.com/item?id=48081469)**

An article about ADHD, Task Paralysis and AI.

⬆️ 237 • 💬 119 • 1d ago • [g5t.de](https://g5t.de/articles/20260510-task-paralysis-and-ai/index.html)

---

**[All my clients wanted a carousel, now it's an AI chatbot](https://news.ycombinator.com/item?id=48072720)**

Posts about SmolWeb, Gemini protocol and LowTech

⬆️ 186 • 💬 77 • 2d ago • [Adële's blog](https://adele.pages.casa/md/blog/all-my-clients-wanted-a-carousel-now-it-s-an-ai-chatbot.md)

---

**[PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs](https://news.ycombinator.com/item?id=48089263)**

The team behind RPCS3 suggests that vibe-coders "learn how to debug and code" instead of "generating slop that you don't understand"

⬆️ 163 • 💬 116 • 10h ago • [Kotaku](https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656)

---

**[An AI coding agent, used to write code, needs to reduce your maintenance costs](https://news.ycombinator.com/item?id=48089289)**

⬆️ 159 • 💬 40 • 10h ago • [jamesshore.com](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs)

---

**[People Hate AI Art](https://news.ycombinator.com/item?id=48070548)**

⬆️ 150 • 💬 172 • 2d ago • [mccue.dev](https://mccue.dev/pages/5-8-26-ai-art)

---

**[Show HN: Git for AI Agents](https://news.ycombinator.com/item?id=48063548)**

Git for AI coding agents. Contribute to regent-vcs/re_gent development by creating an account on GitHub.

⬆️ 119 • 💬 66 • 2d ago • [GitHub](https://github.com/regent-vcs/re_gent)

---

---

## YouTube Videos: "ai"

**[Transphobic AI is taking over Youtube...](https://www.youtube.com/watch?v=A-K_VXXnXnk)**

Yeah so it turns out that Youtube has an ai system that is UNAVOIDABLE and it keeps generating transphobic video ideas for ...

📺 NOAHFINNCE

👁️ 27K • 👍 3K • 💬 276 • ⏱️ 22:46 • 14h ago

---

**[The Line Between AI And Reality Is Disappearing](https://www.youtube.com/watch?v=-Ma3CIHBNLo)**

People accuse me of being AI almost every day now… and honestly, that should concern everyone. Artificial intelligence is getting ...

📺 Ouachita Mountain Living 

👁️ 10K • 👍 1K • 💬 239 • ⏱️ 14:54 • 19h ago

---

**[When Two AIs Go To War: A Realistic Scenario](https://www.youtube.com/watch?v=gwfCWDO4LbM)**

This is a scenario, but here are the sources for the real research referenced: ...

📺 Species | Documenting AGI

👁️ 92K • 👍 5K • 💬 883 • ⏱️ 35:15 • 1d ago

---

**[Anthropic Situation Just Got Even More INSANE](https://www.youtube.com/watch?v=Pf7Y6Tu-Pzc)**

Anthropic just entered one of the strangest moments in AI. Claude is suddenly tied to SpaceX compute, Google Cloud, Amazon, ...

📺 AI Revolution

👁️ 59K • 👍 2K • 💬 159 • ⏱️ 17:08 • 1d ago

---

**[AI is Sending People into Psychosis](https://www.youtube.com/watch?v=LxmIIYj5FQE)**

AI chatbots are pulling people into delusions with devastating consequences. Sources: The Dark Addiction Patterns of Current AI ...

📺 Vanessa Wingårdh

👁️ 86K • 👍 6K • 💬 2K • ⏱️ 15:05 • 17h ago

---

**[Self-building AI, job cuts &amp; more | AI roundup](https://www.youtube.com/watch?v=FAyfVZB-3MY)**

AI is accelerating fast — and the consequences are already here. From self-building 'recursive' AI systems to Iran's AI propaganda ...

📺 CNN

👁️ 73K • 👍 960 • 💬 471 • ⏱️ 23:44 • 1d ago

---

**[You&#39;re Wasting 40% Of Your AI Time On Something Fixable](https://www.youtube.com/watch?v=647pSnX5H_Y)**

Full article w/ the Ultimate Codex Plugin Guide: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 42K • 👍 2K • 💬 165 • ⏱️ 27:13 • 1d ago

---

**[OpenAI Just Dropped The Biggest Voice AI Upgrade Yet](https://www.youtube.com/watch?v=o_igSi-ED6s)**

Try CodeRabbit here: https://coderabbit.link/ai-revolution OpenAI just launched new real-time voice AI that can talk, translate, ...

📺 AI Revolution

👁️ 17K • 👍 525 • 💬 31 • ⏱️ 15:52 • 2d ago

---

**[My ai girlfrfiend part 2](https://www.youtube.com/watch?v=rjdix1lcwMo)**

Thanks for watching. Don't forget to like and subscribe! Featuring @DominiqueDanielle My Instagram ...

📺 NellyVidz

👁️ 45K • 👍 3K • 💬 139 • ⏱️ 8:51 • 1d ago

---

**[AI News: ChatGPT Is Back, NotebookLM Update, Google AI Health Coach, New Pomelli Feature...](https://www.youtube.com/watch?v=myJ2IVHOfrI)**

Try i10x: https://i10x.ai/?fpr=paul53 Save 15% with code "PJL15" ChatGPT returns to form with a major model update while ...

📺 Paul J Lipsky

👁️ 39K • 👍 1K • 💬 93 • ⏱️ 21:51 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 157,648 • ❤️ 570 • 2d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 66,119 • ❤️ 397 • 2d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,017,835 • ❤️ 3,838 • 5d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 3,418 • ❤️ 202 • 1d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 66,561 • ❤️ 202 • 1h ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 9,477 • ❤️ 299 • 14d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 190,993 • ❤️ 1,400 • 18d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 64,008 • ❤️ 209 • 9h ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,446,478 • ❤️ 1,231 • 17d ago

---

**[gemma-4-26B-A4B-it-assistant](https://huggingface.co/google/gemma-4-26B-A4B-it-assistant)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model supporting text and image inputs with a 256K context window. It excels in reasoning, coding, and agentic workflows, offering fast inference via its Mixture-of-Experts architecture with only 4B active parameters.

`any-to-any` `419.7M`

⬇️ 47,749 • ❤️ 107 • 1h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 63 • 💬 3 • ⭐ 73,456 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 5 • 💬 0 • ⭐ 15,526 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 18 • 💬 3 • ⭐ 10,715 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 78 • 💬 7 • ⭐ 4,291 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[Adam's Law: Textual Frequency Law on Large Language Models](https://huggingface.co/papers/2604.02176)**

*Hongyuan Adam Lu, Z. L., Victor Wei et al. (8 authors)*

🏢 FaceMind

A novel framework for improving large language model performance through textual frequency analysis, including laws, distillation, and curriculum training approaches.

▲ 501 • 💬 9 • ⭐ 1,277 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.02176) • [💻 code](https://github.com/HongyuanLuke/frequencylaw)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 32 • 💬 3 • ⭐ 23,903 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 102 • 💬 10 • ⭐ 8,757 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 54 • 💬 2 • ⭐ 55,354 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,575 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 161 • 💬 2 • ⭐ 62,558 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.4k • 🔱 2.8k • 14d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 11.5k • 🔱 753 • 11h ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 6.1k • 🔱 466 • 9h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.7k • 🔱 775 • 14h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.4k • 🔱 221 • 16h ago

---

**[Mouseww/anything-analyzer](https://github.com/Mouseww/anything-analyzer)**

全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE   |  All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration

`TypeScript` `2api` `ai-tools` `analysis-cli` `api-analysis` `automation-tools`

⭐ 2.4k • 🔱 490 • 17h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

An open source harness for generating CAD models

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.4k • 🔱 280 • 1d ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.1k • 🔱 215 • 17h ago

---

**[bergside/design-md-chrome](https://github.com/bergside/design-md-chrome)**

Chrome extension to extract styles from any website and generate DESIGN.md files and design skills for AI based on TypeUI

`JavaScript` `ai` `chrome` `chrome-extension` `claude` `claude-design`

⭐ 1.9k • 🔱 238 • 16d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 1.8k • 🔱 111 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
