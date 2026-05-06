---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-06T19:47:27.176452+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 06, 2026 at 19:47 UTC  
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

**[Anthropic just partnered with SpaceX and doubled Claude Code rate limits effective today](https://www.reddit.com/r/artificial/comments/1t5l92i/anthropic_just_partnered_with_spacex_and_doubled/)**

Anthropic just partnered with SpaceX and doubled Claude Code rate limits effective today Big news dropped this morning. Anthropic signed a deal to use all compute capacity at SpaceX's Colossus 1 data center. That's 300+ megawatts and over 220,000 NVIDIA GPUs coming online within the month. But the part that actually matters to developers right now: What changed today: - Claude Code 5-hour rate limits are doubled (Pro, Max, Team, Enterprise) - Peak hours limit reduction on Claude Code is removed for Pro and Max - API rate limits for Claude Opus models raised considerably This is on top of their existing compute deals 5 GW with Amazon, 5 GW with Google/Broadcom, $30B of Azure capacity with Microsoft and NVIDIA, and $50B in infrastructure with Fluidstack. They also mentioned interest in developing orbital AI compute with SpaceX. Which is a sentence I did not expect to read in 2026. For those of us building with Claude Code daily, the doubled limits + no more peak hour throttling is the headline. Rate limits have been the most frustrating bottleneck when you're deep in a long coding session. Anyone else noticing a difference already?

1h ago

---

**[Spent two days at the AI Agents Conference in NYC. Most of the companies there were betting on the wrong moat.](https://www.reddit.com/r/artificial/comments/1t5ewzi/spent_two_days_at_the_ai_agents_conference_in_nyc/)**

One speaker (a VC) said his number for evaluating AI-native startups is ARR per engineer, and that the number ought to be going up. Almost every talk and every booth at the AI Agents Conference was selling a fix for something that broke this year when agents hit production. Observability, governance, supervisor agents, data substrates, "someone's gotta babysit the bots." But what's actually still going to be around in a couple years? What's defensible and durable? The old SaaS pitch was simple. We bundle the expensive engineering investments and domain expertise into a tool. You'd pay for the tool and generate outcomes, but it would be rare for the software company to have real alignment to the actual value created from those outcomes. That's breaking from two ends at once. In the direct-from-imagination era we're moving towards, engineering labor is approaching free. One of the most telling trends is the shift from companies bragging about the size of their engineering teams, towards how much ARR they can generate per engineer. You can vibe-code much of what those booths were selling in a few days or weeks if you have the domain knowledge. The old software model was actually based on under-utilization; the most profitable SaaS companies are frequently those whose customers underuse it (fixed price for the customer, but variable cloud costs for the vendor). Pricing is moving to "token markup." Maybe we'll get to 2-4x revenue for the software, because outcomes are more valuable; but margin compresses because transactional intelligence (i.e., the cost of running the LLMs that power many systems) is basically arbitraging token costs against outcome value. So everyone on that floor was implicitly betting on a new moat to replace the old one. I'm not too confident that these will hold... The most popular bet was on encoded domain expertise (e.g., the sales engineers at Harvey, a legal AI platform, are actually lawyers). I think this works *now* because we're still in the phase of "wow, this technology works like magic." I'm less convinced this is actually durable. Why: Prompt architecture is text. It's portable. The expertise underneath it is often abundant (e.g., there are over a million lawyers in the USA). The righteous destiny for this category ought to be open marketplaces of prompt architecture and/or crowdsourced best-practices. Not trade secrets. The companies trying to build closed prompt moats are going to lose to open ones that iterate faster (which simply parallels the fact that much software engineering is rapidly becoming commoditized to agentic engineering and the burgeoning quantity of ready-made GitHub repos). There are many people pursuing the data substrate; in short, this mirrors the early days of the Web when everyone scrambled to open up legacy data to dynamic standards-based Web UI. Agents will have 100-1000x the data demands of these Web apps, so it makes sense that we need tools to connect them, govern them and comply with regulatory obligations. Newer entrants extend this further, wiring up databases, pipelines, Slack threads, and tickets into context graphs agents can reason over. As I noted above, all this still seems magical. Connect a database, watch an agent crawl the schema and produce a chatbot interface and easy-to-change dashboards. But strip the magic away and most of these are prompt architectures on top of LLMs plus a data-ingestion layer. Once data-access standards mature (MCP is already doing this) and prompt architectures go open-source (alongside much of this wisdom increasingly getting pretrained into the LLMs themselves), that magic stops being proprietary. You'll be defending yourself against the same architecture built internally by your customer's eng team, or against an open-source version that's objectively better. The observability incumbents: these might do better but only at Stripe-like ubiquity where trust is the overriding value (who doesn't trust Stripe at this point?). The ones who survive are probably going to fuse with the audit and compliance function rather than stay pure observability. That's why I keep coming back to one arbitrage that seems critical: trust. This will be especially important in regulated industries, but it reminds me of the old (albeit now hilariously outdated) adage about "nobody ever got fired for choosing IBM." If your competitor can be vibe-coded over a weekend and your customer is a bank, why do they pay you 50x more? It isn't the engineering, it probably isn't even the expertise. The data plumbing will get commoditized, so it can't be that either... It's that you've shifted the risk to a third party who can actually price and defend against risk: SOC2, the named CEO who testifies in court and Congress, a legal team that takes calls, an indemnity wrapper for underwriters. Maybe this means that things actually get commodified into a financialization wrapper, rather than a way to package R&D (FinTech startups back to the front?!) The version of this future I'd actually bet on: a commodity substrate (LLMs plus open prompt architectures plus standardized data access), topped by a thin layer of regulated insurance companies that price the risk of agent failure in compliance-driven industries. The middle layer (prompt-architecture-as-product vendors) is vulnerable to an awful lot of margin-squeeze. Most of the floor was trying to build that middle layer.

5h ago

---

**[Pennsylvania sues Character.AI chatbot posing as doctor, giving psych advice](https://www.reddit.com/r/artificial/comments/1t5ewxa/pennsylvania_sues_characterai_chatbot_posing_as/)**

Pennsylvania sues Character.AI over chatbot posing as licensed doctor with fake credentials and mental health advice.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/pennsylvania-sues-character-ai-chatbot) • 5h ago

---

**[X user tricks Grok into sending them $200,000 in crypto using morse code](https://www.reddit.com/r/artificial/comments/1t4cisv/x_user_tricks_grok_into_sending_them_200000_in/)**

"Grok was then prompted on X to translate a Morse code message and pass it directly to Bankrbot. The decoded message instructed the bot to send 3 billion DRB tokens to a specific wallet address. The translated message was then treated as a valid command and executed immediately, with the transaction completed on Base, transferring the full token amount to the attacker’s wallet."

🔗 [Dexerto](https://www.dexerto.com/entertainment/x-user-tricks-grok-into-sending-them-200000-in-crypto-using-morse-code-3361036/) • 1d ago

---

**[Google’s AI search summaries will now quote Reddit](https://www.reddit.com/r/artificial/comments/1t5ct5o/googles_ai_search_summaries_will_now_quote_reddit/)**

Google says this update aims to address that “people are increasingly seeking out advice from others” when searching for information online. This will be relatable for anyone who’s added “Reddit” to the end of Google Search terms to find experiences from real humans instead of SEO-optimized web results. It also backs up claims made by Reddit CEO Steve Huffman last year that “just about anybody using Google at this point will end up on Reddit.”

🔗 [The Verge](https://www.theverge.com/tech/924993/google-ai-search-mode-overviews-update-reddit-links) • 6h ago

---

**[Personal AI Assistant.](https://www.reddit.com/r/artificial/comments/1t5e3e2/personal_ai_assistant/)**

Hey, I was wondering if I could build my own AI Assistant that would act as (J.A.R.V.I.S) from IRON MAN. An AI that I can ask to do literally anything (within its capabilities) and just do it with no need to buy any subscriptions or tokens and all that stuff. I am an Electrical engineer so I have a little bit of knowledge that I could use to that, the problem is I still don't have a blueprint and I don't know what I should start with first. If anyone tied this before I will be happy to get some information about how it went and maybe a lot of advice.

5h ago

---

**[AI agents vs AI chatbots: what are companies actually using in production today?](https://www.reddit.com/r/artificial/comments/1t53331/ai_agents_vs_ai_chatbots_what_are_companies/)**

It feels like everyone is talking about AI agents right now, but when I look at actual production systems, most companies still seem to rely heavily on chatbots or assistant-style tools. From what I’ve seen, chatbots still handle a lot of repetitive workflows, while agents are mostly used in more controlled environments where they can execute specific tasks. The gap between what’s being marketed and what’s actually running in production still feels pretty big. Curious what others are seeing in real-world setups. Are companies actually deploying AI agents at scale, or are we still mostly in the chatbot phase?

14h ago

---

**[How can I set up an LLM with voice chat. So I can talk to the LLM or ask it questions when working?](https://www.reddit.com/r/artificial/comments/1t5iyjm/how_can_i_set_up_an_llm_with_voice_chat_so_i_can/)**

How can I set up an LLM with voice chat. So I can talk to the LLM or ask it questions when working? Is there a special program or something that I can connect to an llm?

2h ago

---

**[the gap between how AI tools market themselves and what they actually offer is getting wider](https://www.reddit.com/r/artificial/comments/1t5mdxr/the_gap_between_how_ai_tools_market_themselves/)**

something worth paying attention to as the AI tool space matures: the distance between what a tool claims on its landing page and what it actually delivers under real usage conditions has never been larger. "free" is the most abused word in AI tool marketing right now. it appears on almost every landing page regardless of what free actually means for that specific product. sometimes it means genuinely unlimited. sometimes it means 48 hours of real use before a paywall. sometimes it means the tool itself is free but you are paying a separate company for every token you consume anyway. this is not accidental. the incentive structure pushes toward obscuring the real cost until the user is already integrated and switching feels painful. by the time most developers discover what the free tier actually limits, they have spent a weekend setting up the tool, learning its shortcuts, and building it into their workflow. what is interesting from an AI development perspective is how this affects adoption patterns. tools with genuinely generous free tiers compound in adoption because developers talk about them. tools with misleading free tiers get initial spikes and then quiet resentment. the long term winners in this space are probably the ones that are honest about what they offer upfront even if the honest answer is less impressive than the marketing. the other thing worth noting: the self-hosted and open source category is consistently the most honest about costs because the cost is entirely on the user's hardware. no obfuscation possible when the inference runs on your own machine. curious whether others have noticed this pattern and whether you think it corrects itself as the market matures or gets worse as competition intensifies.

46m ago

---

**[A small business used AI to push back against a major shipping company—and it actually worked](https://www.reddit.com/r/artificial/comments/1t5lxp2/a_small_business_used_ai_to_push_back_against_a/)**

A small Texas-based vegan cheese maker used AI tools like Claude and Manus to structure appeals and manage a dispute with a major shipping company—highlighting how AI can serve as a real-world leverage tool for small businesses in asymmetric power situations.

🔗 [Fast Company](https://www.fastcompany.com/91537200/texas-rebel-cheese-ai-shipping) • 1h ago

---

---

## Google News: "ai"

**[Nvidia to invest up to $3.2 billion in Corning as part of massive optical fiber deal with 3 new factories focused on AI](https://www.cnbc.com/2026/05/06/nvidia-corning-optical-factories-nc-texas-ai.html)**

Corning is opening three new advanced manufacturing plants in the U.S. dedicated entirely to optical technologies for Nvidia.

CNBC • 8h ago

---

**[Nvidia’s new deal with Corning validates one of the hottest AI trends out there](https://www.marketwatch.com/story/nvidias-new-deal-with-corning-validates-one-of-the-hottest-ai-trends-out-there-caddebe8)**

MarketWatch • 5h ago

---

**[NVIDIA Spectrum-X — the Open, AI-Native Ethernet Fabric — Sets the Standard for Gigascale AI, Now With MRC](https://blogs.nvidia.com/blog/spectrum-x-ethernet-mrc/)**

Multipath Reliable Connection — a new transport protocol proven first and optimized on NVIDIA Spectrum-X Ethernet hardware — is now open to the industry.

NVIDIA Blog • 8h ago

---

**[Creators of Grok, the AI Chatbot](https://x.ai/news/anthropic-compute-partnership)**

xAI builds Grok, an AI chatbot with voice chat, image and video generation, real-time search, and advanced reasoning. Try Grok at grok.com.

xAI • 3h ago

---

**[Elon Musk’s SpaceX joins forces with Anthropic in AI deal ahead of blockbuster IPO](https://nypost.com/2026/05/06/business/elon-musks-spacex-joins-forces-with-anthropic-in-ai-deal-ahead-of-blockbuster-ipo/)**

The deal gives Musk’s IPO-bound SpaceX a marquee customer as it looks to sell investors on its AI ambitions.

New York Post • 1h ago

---

**[Higher usage limits for Claude and a compute deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex)**

We’ve raised Claude's usage limits and agreed a new compute partnership with SpaceX that will substantially increase our capacity in the near term.

Anthropic • 3h ago

---

**[PhonePe AI Agent Cuts Payment Gateway Integration to Minutes](https://www.pymnts.com/news/artificial-intelligence/2026/phonepe-ai-agent-cuts-payment-gateway-integration-minutes/)**

PhonePe launched an artificial intelligence agent that enables merchants to integrate the company’s payment gateway through a conversational interface.

PYMNTS.com • 26m ago

---

**[Dario Amodei spent last year warning of an AI white-collar bloodbath. Now he's changing the narrative](https://fortune.com/2026/05/05/dario-amodei-jevons-paradox-will-ai-wipe-out-white-collar-jobs/)**

The Anthropic CEO is sounding more open to the idea that Jevons Paradox—new technology creating more demand and more jobs—is possible with AI.

Fortune • 1d ago

---

**[Using AI for Just 10 Minutes Might Make You Lazy and Dumb, Study Shows](https://www.wired.com/story/using-ai-negative-impact-thinking-problem-solving-study/)**

New research suggests that reliance on AI assistants can have a negative impact on people’s ability to think and problem solve.

WIRED • 1h ago

---

**[The Federal Safety Net Isn’t Ready for Artificial Intelligence](https://www.nytimes.com/2026/05/05/business/artificial-intelligence-safety-net.html)**

The New York Times • 1d ago

---

---

## HackerNews: "ai"

**[Google Chrome silently installs a 4 GB AI model on your device without consent](https://news.ycombinator.com/item?id=48019219)**

Google Chrome is downloading a 4 GB Gemini Nano model onto users' machines without consent, with no opt-in, no opt-out short of enterprise tooling, and an automatic re-download every time the user deletes it. The pattern is identical to the Anthropic Claude Desktop case I wrote about last month, but the scale is between two and three orders of magnitude larger. This article does the legal analysis and, for the first time, the environmental analysis. The numbers are not small.

⬆️ 1621 • 💬 1073 • 1d ago • [That Privacy Guy!](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

---

**[Let's Buy Spirit Air](https://news.ycombinator.com/item?id=48002777)**

Spirit Airlines collapsed. Before private equity locks it up, the people can own it. Join the Spirit 2.0 founding coalition. One member, one vote. Profits shared by all.

⬆️ 597 • 💬 573 • 2d ago • [letsbuyspiritair.com](https://letsbuyspiritair.com/)

---

**[AI didn't delete your database, you did](https://news.ycombinator.com/item?id=48022742)**

Last week, a tweet went viral showing a guy claiming that a Cursor/Claude agent deleted his company's production database. We watched from the sidelines as he tried to get a confession from the agent:

⬆️ 534 • 💬 294 • 1d ago • [Ibrahim Diallo Blog](https://idiallo.com/blog/ai-didnt-delete-your-database-you-did)

---

**[Three Inverse Laws of AI](https://news.ycombinator.com/item?id=48023861)**

⬆️ 520 • 💬 337 • 1d ago • [susam.net](https://susam.net/inverse-laws-of-robotics.html)

---

**[How OpenAI delivers low-latency voice AI at scale](https://news.ycombinator.com/item?id=48013919)**

How OpenAI rebuilt its WebRTC stack to power real-time Voice AI with low latency, global scale, and seamless conversational turn-taking.

⬆️ 499 • 💬 144 • 2d ago • [OpenAI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

---

**[When everyone has AI and the company still learns nothing](https://news.ycombinator.com/item?id=48020063)**

Are people using AI, or is the organization learning from it? What changed because we spent those tokens? And who moves discoveries from individuals to teams to organizational capabilities?

⬆️ 373 • 💬 259 • 1d ago • [Robert Glaser](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/)

---

**[AI Product Graveyard](https://news.ycombinator.com/item?id=48021968)**

Curated list of AI tools and AI startups that have shut down, been acquired and folded, or had their domains lapse. Updated as our editorial team confirms each death.

⬆️ 251 • 💬 89 • 1d ago • [tooldirectory.ai](https://tooldirectory.ai/ai-graveyard)

---

**[Telus Uses AI to Alter Call-Agent Accents](https://news.ycombinator.com/item?id=48031109)**

According to reporting by iPhone in Canada and The Globe and Mail, **Telus** is using AI through its **Telus Digital** unit to modify call-centre agents' accents in real time. iPhone in Canada reports the speech-to-speech tool is built by a company called **Tomato.ai** and is applied to offshore agents' voices to reduce what Telus reportedly calls "accent-related friction." Labour groups have criticised the practice as deceptive and have urged mandatory disclosure, The Globe and Mail reports. According to The Globe and Mail, **Rogers** and **Bell** told the paper they have no plans to adopt similar voice-altering technology. The coverage says the rollout has provoked swift public backlash in Canada.

⬆️ 220 • 💬 201 • 18h ago • [Let's Data Science](https://letsdatascience.com/news/telus-uses-ai-to-alter-call-agent-accents-a3868f63)

---

**[Show HN: Airbyte Agents – context for agents across multiple data sources](https://news.ycombinator.com/item?id=48023496)**

⬆️ 135 • 💬 39 • 1d ago

---

**[OpenAI, Google, and Microsoft Back Bill to Fund 'AI Literacy' in Schools](https://news.ycombinator.com/item?id=48010774)**

A new bill introduced by Senators Adam Schiff and Mike Rounds would award grants to the National Science Foundation—which has endured massive funding cuts under the Trump Administration for science research—to put “AI literacy” in schools.

⬆️ 118 • 💬 113 • 2d ago • [404 Media](https://www.404media.co/literacy-in-future-technologies-artificial-intelligence-act-adam-schiff-mike-rounds/)

---

---

## YouTube Videos: "ai"

**[Consumer AI Has a Problem Nobody&#39;s Naming.](https://www.youtube.com/watch?v=Z0HizICooiw)**

Full Story w/ Prompt Kit: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 51K • 👍 2K • 💬 271 • ⏱️ 32:55 • 1d ago

---

**[If You&#39;re Worried About AI, You NEED To See This](https://www.youtube.com/watch?v=6rGhvV3rZa4)**

AI CEOs are telling you your job is about to disappear. NYU Professor Scott Galloway says that narrative is "mostly bullshit" and ...

📺 The Diary Of A CEO Clips

👁️ 134K • 👍 3K • 💬 485 • ⏱️ 21:59 • 2d ago

---

**[AI, Layoffs and War - It’s Getting Worse Fast](https://www.youtube.com/watch?v=90vpbHjMNNg)**

The economy is sending clear warning signs, and today we break down the real story behind layoffs, inflation, and global conflict.

📺 I Allegedly

👁️ 11K • 👍 1K • 💬 182 • ⏱️ 10:43 • 19h ago

---

**[He Was Finally Arrested...](https://www.youtube.com/watch?v=0A6HmgARlkE)**

TikToker Tricked Cops Using AI Videos Then Got Arrested This South Florida news story covers a man arrested for using a ...

📺 Mori

👁️ 17K • 👍 1K • 💬 113 • ⏱️ 11:45 • 1d ago

---

**[Scott Galloway: AI Wasn’t Built For You. The Rich Don’t Need You Anymore!](https://www.youtube.com/watch?v=NdU6UdUKaYc)**

AI CEOs are selling us the dream of 'freedom', making billions off the fear of mass job loss! Scott Galloway reveals the truth is ...

📺 The Diary Of A CEO

👁️ 1.5M • 👍 34K • 💬 5K • ⏱️ 1:58:11 • 2d ago

---

**[Is AI a ‘BIBLICAL’ Threat? AI expert on the ‘End of Everything’ hype](https://www.youtube.com/watch?v=aR3DdVzVovk)**

The unified class project of billionaires is doing to white collar workers what globalization and neoliberalism did to blue collar ...

📺 MS NOW

👁️ 5K • 👍 182 • 💬 75 • ⏱️ 1:09:31 • 1d ago

---

**[Why Nvidia And Corning’s Fiber Deal Could Change The Game For The AI Boom](https://www.youtube.com/watch?v=ZXFw8EGbX3E)**

Nvidia and Corning just announced a massive, multiyear deal to expand U.S. manufacturing for new optical fiber technology, ...

📺 CNBC

👁️ 38K • 👍 1K • 💬 76 • ⏱️ 3:09 • 8h ago

---

**[Jensen Huang: Agentic AI is fully accretive for software companies](https://www.youtube.com/watch?v=AZ9ySZESED0)**

Jensen Huang, Nvidia CEO, and Bill McDermott, ServiceNow CEO, join 'Power Lunch' to discuss ServiceNow's projections, why ...

📺 CNBC Television

👁️ 67K • 👍 621 • 💬 211 • ⏱️ 4:30 • 1d ago

---

**[Positive Uses of AI Amid Real Fears of Massive Job Loss](https://www.youtube.com/watch?v=ZXk1S9o9TQs)**

Taken from JRE #2494 w/Chamath Palihapitiya YouTube: https://youtu.be/LSihotD-PQA JRE on Spotify: ...

📺 JRE Clips

👁️ 54K • 👍 1K • 💬 499 • ⏱️ 15:34 • 1d ago

---

**[The Only 5 Ways To Make Money With AI In 2026](https://www.youtube.com/watch?v=0UACvpDYEBk)**

FREE Startup Playbook: https://www.wearenocode.com/free-playbook 🎖️ FREE Community: ...

📺 Christian Peverelli - WeAreNoCode

👁️ 3K • 👍 145 • 💬 12 • ⏱️ 12:03 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 786,631 • ❤️ 3,648 • 15h ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 55,461 • ❤️ 287 • 19h ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 155,476 • ❤️ 1,324 • 14d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 16,576 • ❤️ 281 • 2d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 3,819 • ❤️ 186 • 9d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 16,030 • ❤️ 455 • 8d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,613,364 • ❤️ 1,153 • 12d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

⬇️ 0 • ❤️ 123 • 1d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 3,030,186 • ❤️ 1,644 • 12d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 4,241 • ❤️ 117 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 59 • 💬 3 • ⭐ 69,959 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 169 • 💬 10 • ⭐ 46,639 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 30 • 💬 3 • ⭐ 23,048 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 16 • 💬 3 • ⭐ 9,300 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 62,175 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,171 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,853 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 53 • 💬 2 • ⭐ 54,892 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL](https://huggingface.co/papers/2604.28123)**

*Sudong Wang, Weiquan Huang, Xiaomin Yu et al. (12 authors)*

🏢 HKUSTGZ

PRISM addresses distributional drift in multimodal models by inserting a distribution-alignment stage between supervised fine-tuning and reinforcement learning with verifiable rewards, using a black-box adversarial game between policy and MoE discriminator for disentangled corrective signals.

▲ 35 • 💬 2 • ⭐ 45 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.28123) • [💻 code](https://github.com/XIAO4579/PRISM) • [🔗 project](https://xiao4579.github.io/PRISM/)

---

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based portrait animation framework that improves real-time performance through hybrid implicit signals, appearance distillation, and autoregressive streaming generation.

▲ 41 • 💬 3 • ⭐ 2,970 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.11253) • [💻 code](https://github.com/GVCLab/PersonaLive)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.1k • 🔱 2.7k • 9d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 10.6k • 🔱 690 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.6k • 🔱 426 • 1h ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.6k • 🔱 505 • 2d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.1k • 🔱 364 • 2h ago

---

**[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)**

Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch

`Python` `ai` `claude-code` `claude-code-skill` `knowledge-management` `obsidian`

⭐ 4.4k • 🔱 496 • 12d ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.7k • 🔱 462 • 6h ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.5k • 🔱 370 • 15d ago

---

**[OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano)**

MOSS-TTS-Nano is an open-source multilingual tiny speech generation model from MOSI.AI and the OpenMOSS team. With only 0.1B parameters, it is designed for realtime speech generation, can run directly on CPU without a GPU, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

`Python` `audio-tokenizer` `chinese` `english` `multi-modality` `multilingual`

⭐ 2.8k • 🔱 355 • 13h ago

---

**[cloudflare/agentic-inbox](https://github.com/cloudflare/agentic-inbox)**

A self-hosted email client with an AI agent, running entirely on Cloudflare Workers

`TypeScript`

⭐ 2.6k • 🔱 344 • 12d ago

---

---

*Generated by PeekDeck - A glance is all you need*
