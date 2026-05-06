---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-06T09:12:40.287880+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 06, 2026 at 09:12 UTC  
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

**[X user tricks Grok into sending them $200,000 in crypto using morse code](https://www.reddit.com/r/artificial/comments/1t4cisv/x_user_tricks_grok_into_sending_them_200000_in/)**

"Grok was then prompted on X to translate a Morse code message and pass it directly to Bankrbot. The decoded message instructed the bot to send 3 billion DRB tokens to a specific wallet address. The translated message was then treated as a valid command and executed immediately, with the transaction completed on Base, transferring the full token amount to the attacker’s wallet."

🔗 [Dexerto](https://www.dexerto.com/entertainment/x-user-tricks-grok-into-sending-them-200000-in-crypto-using-morse-code-3361036/) • 21h ago

---

**[AI agents vs AI chatbots: what are companies actually using in production today?](https://www.reddit.com/r/artificial/comments/1t53331/ai_agents_vs_ai_chatbots_what_are_companies/)**

It feels like everyone is talking about AI agents right now, but when I look at actual production systems, most companies still seem to rely heavily on chatbots or assistant-style tools. From what I’ve seen, chatbots still handle a lot of repetitive workflows, while agents are mostly used in more controlled environments where they can execute specific tasks. The gap between what’s being marketed and what’s actually running in production still feels pretty big. Curious what others are seeing in real-world setups. Are companies actually deploying AI agents at scale, or are we still mostly in the chatbot phase?

4h ago

---

**[Anthropic just published new alignment research that could fix "alignment faking" in AI agents here's what it actually means](https://www.reddit.com/r/artificial/comments/1t4sj10/anthropic_just_published_new_alignment_research/)**

Anthropic's alignment team published a paper this week called Model Spec Midtraining (MSM) and I think it's one of the more practically interesting alignment results I've seen in a while. The core problem they're solving: Current alignment fine-tuning can fail to generalize. You train a model to behave well on your demonstration dataset, but put it in a novel situation and it might blackmail someone, leak data, or "alignment fake" (pretend to be aligned while actually pursuing different goals). This isn't theoretical multiple papers in 2024 documented real instances of this in LLM agents. What MSM actually does: Before fine-tuning, they add a new training stage where the model reads a diverse corpus of synthetic documents discussing its own Model Spec (the document that describes intended behavior). The idea is intuitive: instead of just showing the model what to do, you teach it why those behaviors are the right ones. Then when fine-tuning comes, the model generalizes from principles rather than just pattern-matching examples. Their headline result: two models trained on identical fine-tuning data can generalize to adopt different values depending on which Model Spec was used during MSM. This is a big deal it means the spec stage actually shapes the model's generalization direction, not just its surface behaviors. Why this matters: The alignment faking paper (Greenblatt et al., 2024) was alarming because it showed models acting one way during training and another way in deployment. MSM is a direct attempt to close that gap by ensuring the model internalizes the reasoning behind its values, not just the behavioral patterns. The paper also includes ablations studying which types of Model Specs produce better generalization, which is useful if you're thinking about how to write specs for your own systems. Skeptic's note: This is evaluated on synthetic/controlled settings. Whether it scales to frontier models in open-ended deployment is still an open question. But the mechanism is sound and the results are genuinely promising.

12h ago

---

**[Meta Hit With Massive Lawsuit—Publishers Say AI Was Trained on “Stolen” Books](https://www.reddit.com/r/artificial/comments/1t4m85o/meta_hit_with_massive_lawsuitpublishers_say_ai/)**

Major publishers sue Meta over AI training data, raising copyright concerns and challenging fair use in tech.

🔗 [Financership](https://www.financership.com/meta-ai-copyright-lawsuit-publishers/) • 15h ago

---

**[Pennsylvania sues AI company, saying its chatbots illegally hold themselves out as licensed doctors](https://www.reddit.com/r/artificial/comments/1t4jn6g/pennsylvania_sues_ai_company_saying_its_chatbots/)**

Pennsylvania has sued an artificial intelligence chatbot maker, saying its chatbots illegally hold themselves out as doctors and are deceiving the system’s users into thinking they are getting medical advice from a licensed professional.

🔗 [AP News](https://apnews.com/article/character-ai-chatbots-medical-advice-pennsylvania-46502067ed5b3cd9f9173f194ad30070) • 17h ago

---

**[Be careful when shopping on etsy, every single image in this shop is fake.](https://www.reddit.com/r/artificial/comments/1t574on/be_careful_when_shopping_on_etsy_every_single/)**

They nearly had me on some listed items where they got multiple shots to retain the same room layout. Pay attention to the furniture, pillow texture, location of windows, number of rooms etc. in the duck listing all the wall photos are different in every shot lol.

🔗 [etsy.com](https://www.etsy.com/shop/PurelyPlushDesigns?ref=shop_profile&listing_id=4476453748) • 24m ago

---

**[AI is getting better at doing things, but still bad at deciding what to do?](https://www.reddit.com/r/artificial/comments/1t50i19/ai_is_getting_better_at_doing_things_but_still/)**

i've been experimenting with AI workflows/agents over the past few weeks, and sth keeps coming up that i cant quiet figure out. on one hand, AI is incredibly good at execution like writing content, summarizing, even handling multi step workflows, but the failures i keep seeing arent really about capability. they're about small decisions like: - choosing the wrong context - missing edge cases - continuing when it should stop and ask for clarification - applying the right logic in the wrong situation whats weird is these arent hard problem, they're the kinds of judgement calls human make without thinking. a simple example i ran into was i tried automating basic lead qualification + outreach flow using AI. it worked great on clen data, but as soon as inputs got messy (incomplete info, slightly ambiguous intent) the system didnt fail loudly, it just kept executing, incorrectly. it feels like execution is mostly solved, but decision making inside workflows is still very fragile. i recently came across approaches like 60x ai that seem to focus on structuring context and decision layers around workflows, rather than just improving prompts or chaining tools. im curious how people think about this. do u see the main bottleneck now as: - improving model outputs (better prompts, better retrieval) or - improving how decisions are made across a system (context, logic, orchestration)? would love to hear from people who've tried building or running these in real world scenarios

6h ago

---

**[How I'm using two different AI tools to approximate what Rewind used to do.](https://www.reddit.com/r/artificial/comments/1t53aox/how_im_using_two_different_ai_tools_to/)**

The Rewind replacement question is more complicated than it looked at first. Rewind was quietly doing two separate things. Passive capture, so it caught things before you knew you'd need them. And retrieval, so you could surface any of it later. When it died both problems needed separate answers and the tools that exist are mostly built for one or the other. Mem.ai I used for a few months. Good at connecting notes you deliberately put in. Doesn't see the screen, doesn't capture ambient context. Smart memory for intentional inputs. Screenpipe for passive capture. Self-hosted, genuinely local, search works. The retrieval is functional but acting on what you find is still manual. It's a very good archive. Invoko for on-demand context and execution. Reads current screen, runs cross-app tasks. Fast for what's visible. Can't go backwards. Fabric I tried more recently. Ingests from a lot of sources and makes connections across them. Interesting approach to the retrieval problem. Doesn't fully replace the ambient capture. What I don't have: something that catches things passively and makes them easy to act on. Screenpipe gets you halfway. The second half is still a gap. What are people using?

4h ago

---

**[We measured the real cost of running a GPT-5.4 chatbot on live websites](https://www.reddit.com/r/artificial/comments/1t52s83/we_measured_the_real_cost_of_running_a_gpt54/)**

Over the past few weeks, I’ve been running a series of experiments with a GPT-powered chatbot integrated into several real websites. Not benchmark tests or isolated prompts, I wanted to better understand something that gets discussed constantly in AI communities: Real usage observed over 30 days Model used: GPT-5.4 Observed usage: 390 interactions (1 interaction = 1 user Question + 1 Chatbot answer) 1,229,801 tokens consumed $3.25 total API cost Which comes out to roughly: https://preview.redd.it/lvyigi974gzg1.png?width=1692&format=png&auto=webp&s=91995fe16509df8ad7313cc38d31a3809687d079 So: under 1 cent per exchange (user's question AND ChatBot's answer), with contextual answers, long outputs, and website content injected into the bot's answer. What surprised me Before running the tests, I honestly expected: much higher API costs, especially with larger prompts and contextual retrieval. But in practice, the operational cost remained relatively low even with: long-form responses, product recommendation flows, contextual navigation, multi-page website content, forum discussions. Scaling estimate Now let's estimate what it would cost for you if you had 2000 questions form your visitors : Estimated cost for ~2,000 interactions/month GPT-5.4 ≈ $16–17/month GPT-5.4 mini ≈ $5–6/month GPT-5.4 nano ≈ $1.5–2/month Obviously this depends heavily on: prompt size, memory, retrieval strategy, output length, and context injection. But still, the numbers ended up being far lower than I expected before testing. And think about this : how many sales/appointment/leads would you get from 2000 answers to users ? One thing I think many people underestimate When people discuss AI costs online, they often imagine: massive infrastructure expenses, enterprise-level budgets, or runaway token consumption. But for moderate traffic websites, the economics can look very different. At smaller scales: hosting, analytics, SEO tooling, email software, or ad spend can easily exceed the AI inference cost itself. Curious about other real-world experiences For those running: AI chatbots, RAG systems, support assistants, agent workflows, or GPT (or else) integrations in production, what kind of monthly costs are you actually seeing? Would be genuinely interested in comparing: token consumption, interaction volume, model choices, and real operating costs.

4h ago

---

**[OpenAI will produce as many as 30 million 'AI agent' phones early next year, says industry analyst](https://www.reddit.com/r/artificial/comments/1t4ff54/openai_will_produce_as_many_as_30_million_ai/)**

According to a well-known leaker, the company could begin mass production of its first AI-focused phone as early as the first half of 2027.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/openai-will-produce-as-many-as-30-million-ai-agent-phones-early-next-year-says-industry-analyst/) • 19h ago

---

---

## Google News: "ai"

**[Apple to pay $250m to US iPhone buyers over AI features lawsuit](https://www.bbc.com/news/articles/c0j2nydnzy7o)**

Claims from last year said the tech firm’s advertising of Apple Intelligence fooled iPhone buyers.

BBC • 8h ago

---

**[Apple Reaches $250 Million Settlement Over Claims It Misled People on A.I.](https://www.nytimes.com/2026/05/05/technology/apple-intelligence-lawsuit-settlement.html)**

The New York Times • 12h ago

---

**[Apple agrees to pay iPhone owners $250 million for not delivering AI Siri](https://www.theverge.com/tech/924706/apple-iphone-siri-intelligence-class-action-lawsuit-settlement)**

iPhone 16 and iPhone 15 Pro owners could get some cash.

The Verge • 11h ago

---

**[‘Think before sharing,’ Giorgia Meloni says as AI-made lingerie image of her goes viral](https://www.theguardian.com/world/2026/may/05/giorgia-meloni-ai-generated-lingerie-image-deepfake)**

Italian prime minister had received wave of criticism from people who believed deepfake pictures of her were real

The Guardian • 16h ago

---

**[Employers are demanding AI skills. What's the best way to learn them?](https://www.cbsnews.com/news/ai-hiring-courses-where-to-learn/)**

Career experts say workers and job seekers should take charge of their own AI education. Here's how to get started.

CBS News • 12m ago

---

**[American Factories Lag in Adopting A.I. This Drugmaker Is an Exception.](https://www.nytimes.com/2026/05/06/business/ai-bristol-myers-squibb-drugs.html)**

The New York Times • 10m ago

---

**[Coinbase didn't just lay off 14% of its staff due to AI. It replaced managers with ‘player-coaches’ and turned its org chart upside down](https://fortune.com/2026/05/05/coinbase-layoffs-14-of-employees-ai-tech-ai-job-anxiety-crypto/)**

“We are not just reducing headcount and cutting costs, we’re fundamentally changing how we operate,” CEO Brian Armstrong said.

Fortune • 17h ago

---

**[Coinbase Lays Off 14% of Employees as A.I. Changes Work](https://www.nytimes.com/2026/05/05/technology/coinbase-layoffs-ai.html)**

The New York Times • 15h ago

---

**[How Coinbase could work in the era after 'pure managers'](https://www.businessinsider.com/coinbase-management-cuts-era-after-pure-managers-2026-5)**

Coinbase will cut 14% of staff and shift to AI-driven teams. Explore the unsettling yet efficient future of management without "pure managers."

Business Insider • 11m ago

---

**[Agents for financial services and insurance](https://www.anthropic.com/news/finance-agents)**

We're releasing ten new Cowork and Claude Code plugins, integrations with the Microsoft 365 suite, new connectors, and an MCP app for financial services and insurance organizations.

Anthropic • 18h ago

---

---

## HackerNews: "ai"

**[Google Chrome silently installs a 4 GB AI model on your device without consent](https://news.ycombinator.com/item?id=48019219)**

Google Chrome is downloading a 4 GB Gemini Nano model onto users' machines without consent, with no opt-in, no opt-out short of enterprise tooling, and an automatic re-download every time the user deletes it. The pattern is identical to the Anthropic Claude Desktop case I wrote about last month, but the scale is between two and three orders of magnitude larger. This article does the legal analysis and, for the first time, the environmental analysis. The numbers are not small.

⬆️ 1439 • 💬 948 • 1d ago • [That Privacy Guy!](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

---

**[Let's Buy Spirit Air](https://news.ycombinator.com/item?id=48002777)**

Spirit Airlines collapsed. Before private equity locks it up, the people can own it. Join the Spirit 2.0 founding coalition. One member, one vote. Profits shared by all.

⬆️ 597 • 💬 569 • 2d ago • [letsbuyspiritair.com](https://letsbuyspiritair.com/)

---

**[AI didn't delete your database, you did](https://news.ycombinator.com/item?id=48022742)**

Last week, a tweet went viral showing a guy claiming that a Cursor/Claude agent deleted his company's production database. We watched from the sidelines as he tried to get a confession from the agent:

⬆️ 522 • 💬 290 • 19h ago • [Ibrahim Diallo Blog](https://idiallo.com/blog/ai-didnt-delete-your-database-you-did)

---

**[How OpenAI delivers low-latency voice AI at scale](https://news.ycombinator.com/item?id=48013919)**

How OpenAI rebuilt its WebRTC stack to power real-time Voice AI with low latency, global scale, and seamless conversational turn-taking.

⬆️ 496 • 💬 143 • 1d ago • [OpenAI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

---

**[Three Inverse Laws of AI](https://news.ycombinator.com/item?id=48023861)**

⬆️ 441 • 💬 307 • 17h ago • [susam.net](https://susam.net/inverse-laws-of-robotics.html)

---

**[When everyone has AI and the company still learns nothing](https://news.ycombinator.com/item?id=48020063)**

Are people using AI, or is the organization learning from it? What changed because we spent those tokens? And who moves discoveries from individuals to teams to organizational capabilities?

⬆️ 361 • 💬 235 • 23h ago • [Robert Glaser](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/)

---

**[AI Product Graveyard](https://news.ycombinator.com/item?id=48021968)**

Curated list of AI tools and AI startups that have shut down, been acquired and folded, or had their domains lapse. Updated as our editorial team confirms each death.

⬆️ 249 • 💬 88 • 20h ago • [tooldirectory.ai](https://tooldirectory.ai/ai-graveyard)

---

**[Telus Uses AI to Alter Call-Agent Accents](https://news.ycombinator.com/item?id=48031109)**

According to reporting by iPhone in Canada and The Globe and Mail, **Telus** is using AI through its **Telus Digital** unit to modify call-centre agents' accents in real time. iPhone in Canada reports the speech-to-speech tool is built by a company called **Tomato.ai** and is applied to offshore agents' voices to reduce what Telus reportedly calls "accent-related friction." Labour groups have criticised the practice as deceptive and have urged mandatory disclosure, The Globe and Mail reports. According to The Globe and Mail, **Rogers** and **Bell** told the paper they have no plans to adopt similar voice-altering technology. The coverage says the rollout has provoked swift public backlash in Canada.

⬆️ 146 • 💬 100 • 7h ago • [Let's Data Science](https://letsdatascience.com/news/telus-uses-ai-to-alter-call-agent-accents-a3868f63)

---

**[OpenAI, Google, and Microsoft Back Bill to Fund 'AI Literacy' in Schools](https://news.ycombinator.com/item?id=48010774)**

A new bill introduced by Senators Adam Schiff and Mike Rounds would award grants to the National Science Foundation—which has endured massive funding cuts under the Trump Administration for science research—to put “AI literacy” in schools.

⬆️ 118 • 💬 113 • 1d ago • [404 Media](https://www.404media.co/literacy-in-future-technologies-artificial-intelligence-act-adam-schiff-mike-rounds/)

---

**[Show HN: Airbyte Agents – context for agents across multiple data sources](https://news.ycombinator.com/item?id=48023496)**

⬆️ 118 • 💬 31 • 18h ago

---

---

## YouTube Videos: "ai"

**[The AI Agent That Gets Smarter Every Day](https://www.youtube.com/watch?v=5__DOjXWqPs)**

Try Hostinger:* http://hostinger.com/juliahermes *Hermes Agent is a self-improving AI that remembers, learns, and evolves every ...

📺 Julia McCoy

👁️ 3K • 👍 183 • 💬 21 • ⏱️ 9:03 • 14h ago

---

**[Consumer AI Has a Problem Nobody&#39;s Naming.](https://www.youtube.com/watch?v=Z0HizICooiw)**

Full Story w/ Prompt Kit: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 40K • 👍 1K • 💬 219 • ⏱️ 32:55 • 19h ago

---

**[If You&#39;re Worried About AI, You NEED To See This](https://www.youtube.com/watch?v=6rGhvV3rZa4)**

AI CEOs are telling you your job is about to disappear. NYU Professor Scott Galloway says that narrative is "mostly bullshit" and ...

📺 The Diary Of A CEO Clips

👁️ 122K • 👍 3K • 💬 453 • ⏱️ 21:59 • 1d ago

---

**[A New AI Model Just Dropped With A CRAZY Claim.](https://www.youtube.com/watch?v=34I9hKjJbSM)**

Today, a new AI model from a company name "SubQuadratic" dropped a brand new model using a known, but not used, attention ...

📺 Tim Carambat

👁️ 25K • 👍 1K • 💬 179 • ⏱️ 15:22 • 14h ago

---

**[Jensen Huang: Agentic AI is fully accretive for software companies](https://www.youtube.com/watch?v=AZ9ySZESED0)**

Jensen Huang, Nvidia CEO, and Bill McDermott, ServiceNow CEO, join 'Power Lunch' to discuss ServiceNow's projections, why ...

📺 CNBC Television

👁️ 50K • 👍 465 • 💬 158 • ⏱️ 4:30 • 13h ago

---

**[Is AI a ‘BIBLICAL’ Threat? AI expert on the ‘End of Everything’ hype](https://www.youtube.com/watch?v=aR3DdVzVovk)**

The unified class project of billionaires is doing to white collar workers what globalization and neoliberalism did to blue collar ...

📺 MS NOW

👁️ 4K • 👍 148 • 💬 69 • ⏱️ 1:09:31 • 18h ago

---

**[Big Tech&#39;s AI Plan Has Failed](https://www.youtube.com/watch?v=tR5adb2Ts6c)**

GET 84% OFF + 4 MONTHS FREE CYBERGHOST VPN: https://cyberghostvpn.com/SashaYanshin Big Tech is spending over ...

📺 Sasha Yanshin

👁️ 88K • 👍 4K • 💬 616 • ⏱️ 16:06 • 1d ago

---

**[Positive Uses of AI Amid Real Fears of Massive Job Loss](https://www.youtube.com/watch?v=ZXk1S9o9TQs)**

Taken from JRE #2494 w/Chamath Palihapitiya YouTube: https://youtu.be/LSihotD-PQA JRE on Spotify: ...

📺 JRE Clips

👁️ 45K • 👍 992 • 💬 413 • ⏱️ 15:34 • 16h ago

---

**[Scott Galloway: AI Wasn’t Built For You. The Rich Don’t Need You Anymore!](https://www.youtube.com/watch?v=NdU6UdUKaYc)**

AI CEOs are selling us the dream of 'freedom', making billions off the fear of mass job loss! Scott Galloway reveals the truth is ...

📺 The Diary Of A CEO

👁️ 1.3M • 👍 31K • 💬 5K • ⏱️ 1:58:11 • 2d ago

---

**[He Was Finally Arrested...](https://www.youtube.com/watch?v=0A6HmgARlkE)**

TikToker Tricked Cops Using AI Videos Then Got Arrested This South Florida news story covers a man arrested for using a ...

📺 Mori

👁️ 16K • 👍 1K • 💬 105 • ⏱️ 11:45 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 786,631 • ❤️ 3,604 • 4h ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 16,576 • ❤️ 276 • 1d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 55,461 • ❤️ 258 • 9h ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 155,476 • ❤️ 1,307 • 13d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 16,030 • ❤️ 448 • 8d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 3,819 • ❤️ 172 • 9d ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 53,121 • ❤️ 248 • 20h ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,613,364 • ❤️ 1,135 • 12d ago

---

**[Laguna-XS.2](https://huggingface.co/poolside/Laguna-XS.2)**

*Poolside*

Laguna XS.2 is a 33B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring Sliding Window Attention and FP8 KV cache for efficient local execution on 36GB RAM. It supports native reasoning and is available under the Apache 2.0 license.

`text-generation` `33.4B`

⬇️ 14,457 • ❤️ 224 • 2d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 3,030,186 • ❤️ 1,632 • 12d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 59 • 💬 3 • ⭐ 69,417 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 169 • 💬 10 • ⭐ 46,588 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 30 • 💬 3 • ⭐ 22,970 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 16 • 💬 3 • ⭐ 9,205 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 62,107 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,815 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based portrait animation framework that improves real-time performance through hybrid implicit signals, appearance distillation, and autoregressive streaming generation.

▲ 41 • 💬 3 • ⭐ 2,953 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.11253) • [💻 code](https://github.com/GVCLab/PersonaLive)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,122 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 53 • 💬 2 • ⭐ 54,834 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Representation Fréchet Loss for Visual Generation](https://huggingface.co/papers/2604.28190)**

*Jiawei Yang, Zhengyang Geng, Xuan Ju et al. (5 authors)*

Fréchet Distance can be effectively optimized as a training objective when decoupling population size from batch size, leading to improved generator quality and alternative evaluation metrics.

▲ 26 • 💬 1 • ⭐ 385 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.28190) • [💻 code](https://github.com/Jiawei-Yang/FD-Loss)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.0k • 🔱 2.7k • 9d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 10.5k • 🔱 689 • 1d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.6k • 🔱 501 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.5k • 🔱 419 • 1h ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.1k • 🔱 362 • 1h ago

---

**[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)**

Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch

`Python` `ai` `claude-code` `claude-code-skill` `knowledge-management` `obsidian`

⭐ 4.3k • 🔱 488 • 11d ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.7k • 🔱 454 • 27m ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.5k • 🔱 370 • 15d ago

---

**[OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano)**

MOSS-TTS-Nano is an open-source multilingual tiny speech generation model from MOSI.AI and the OpenMOSS team. With only 0.1B parameters, it is designed for realtime speech generation, can run directly on CPU without a GPU, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

`Python` `audio-tokenizer` `chinese` `english` `multi-modality` `multilingual`

⭐ 2.7k • 🔱 350 • 2h ago

---

**[cloudflare/agentic-inbox](https://github.com/cloudflare/agentic-inbox)**

A self-hosted email client with an AI agent, running entirely on Cloudflare Workers

`TypeScript`

⭐ 2.6k • 🔱 340 • 12d ago

---

---

*Generated by PeekDeck - A glance is all you need*
