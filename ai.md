---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-06T17:41:53.205426+00:00'
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

**Last Updated:** May 06, 2026 at 17:41 UTC  
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

**[Pennsylvania sues Character.AI chatbot posing as doctor, giving psych advice](https://www.reddit.com/r/artificial/comments/1t5ewxa/pennsylvania_sues_characterai_chatbot_posing_as/)**

Pennsylvania sues Character.AI over chatbot posing as licensed doctor with fake credentials and mental health advice.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/pennsylvania-sues-character-ai-chatbot) • 3h ago

---

**[Spent two days at the AI Agents Conference in NYC. Most of the companies there were betting on the wrong moat.](https://www.reddit.com/r/artificial/comments/1t5ewzi/spent_two_days_at_the_ai_agents_conference_in_nyc/)**

One speaker (a VC) said his number for evaluating AI-native startups is ARR per engineer, and that the number ought to be going up. Almost every talk and every booth at the AI Agents Conference was selling a fix for something that broke this year when agents hit production. Observability, governance, supervisor agents, data substrates, "someone's gotta babysit the bots." But what's actually still going to be around in a couple years? What's defensible and durable? The old SaaS pitch was simple. We bundle the expensive engineering investments and domain expertise into a tool. You'd pay for the tool and generate outcomes, but it would be rare for the software company to have real alignment to the actual value created from those outcomes. That's breaking from two ends at once. In the direct-from-imagination era we're moving towards, engineering labor is approaching free. One of the most telling trends is the shift from companies bragging about the size of their engineering teams, towards how much ARR they can generate per engineer. You can vibe-code much of what those booths were selling in a few days or weeks if you have the domain knowledge. The old software model was actually based on under-utilization; the most profitable SaaS companies are frequently those whose customers underuse it (fixed price for the customer, but variable cloud costs for the vendor). Pricing is moving to "token markup." Maybe we'll get to 2-4x revenue for the software, because outcomes are more valuable; but margin compresses because transactional intelligence (i.e., the cost of running the LLMs that power many systems) is basically arbitraging token costs against outcome value. So everyone on that floor was implicitly betting on a new moat to replace the old one. I'm not too confident that these will hold... The most popular bet was on encoded domain expertise (e.g., the sales engineers at Harvey, a legal AI platform, are actually lawyers). I think this works *now* because we're still in the phase of "wow, this technology works like magic." I'm less convinced this is actually durable. Why: Prompt architecture is text. It's portable. The expertise underneath it is often abundant (e.g., there are over a million lawyers in the USA). The righteous destiny for this category ought to be open marketplaces of prompt architecture and/or crowdsourced best-practices. Not trade secrets. The companies trying to build closed prompt moats are going to lose to open ones that iterate faster (which simply parallels the fact that much software engineering is rapidly becoming commoditized to agentic engineering and the burgeoning quantity of ready-made GitHub repos). There are many people pursuing the data substrate; in short, this mirrors the early days of the Web when everyone scrambled to open up legacy data to dynamic standards-based Web UI. Agents will have 100-1000x the data demands of these Web apps, so it makes sense that we need tools to connect them, govern them and comply with regulatory obligations. Newer entrants extend this further, wiring up databases, pipelines, Slack threads, and tickets into context graphs agents can reason over. As I noted above, all this still seems magical. Connect a database, watch an agent crawl the schema and produce a chatbot interface and easy-to-change dashboards. But strip the magic away and most of these are prompt architectures on top of LLMs plus a data-ingestion layer. Once data-access standards mature (MCP is already doing this) and prompt architectures go open-source (alongside much of this wisdom increasingly getting pretrained into the LLMs themselves), that magic stops being proprietary. You'll be defending yourself against the same architecture built internally by your customer's eng team, or against an open-source version that's objectively better. The observability incumbents: these might do better but only at Stripe-like ubiquity where trust is the overriding value (who doesn't trust Stripe at this point?). The ones who survive are probably going to fuse with the audit and compliance function rather than stay pure observability. That's why I keep coming back to one arbitrage that seems critical: trust. This will be especially important in regulated industries, but it reminds me of the old (albeit now hilariously outdated) adage about "nobody ever got fired for choosing IBM." If your competitor can be vibe-coded over a weekend and your customer is a bank, why do they pay you 50x more? It isn't the engineering, it probably isn't even the expertise. The data plumbing will get commoditized, so it can't be that either... It's that you've shifted the risk to a third party who can actually price and defend against risk: SOC2, the named CEO who testifies in court and Congress, a legal team that takes calls, an indemnity wrapper for underwriters. Maybe this means that things actually get commodified into a financialization wrapper, rather than a way to package R&D (FinTech startups back to the front?!) The version of this future I'd actually bet on: a commodity substrate (LLMs plus open prompt architectures plus standardized data access), topped by a thin layer of regulated insurance companies that price the risk of agent failure in compliance-driven industries. The middle layer (prompt-architecture-as-product vendors) is vulnerable to an awful lot of margin-squeeze. Most of the floor was trying to build that middle layer.

3h ago

---

**[X user tricks Grok into sending them $200,000 in crypto using morse code](https://www.reddit.com/r/artificial/comments/1t4cisv/x_user_tricks_grok_into_sending_them_200000_in/)**

"Grok was then prompted on X to translate a Morse code message and pass it directly to Bankrbot. The decoded message instructed the bot to send 3 billion DRB tokens to a specific wallet address. The translated message was then treated as a valid command and executed immediately, with the transaction completed on Base, transferring the full token amount to the attacker’s wallet."

🔗 [Dexerto](https://www.dexerto.com/entertainment/x-user-tricks-grok-into-sending-them-200000-in-crypto-using-morse-code-3361036/) • 1d ago

---

**[Google’s AI search summaries will now quote Reddit](https://www.reddit.com/r/artificial/comments/1t5ct5o/googles_ai_search_summaries_will_now_quote_reddit/)**

Google says this update aims to address that “people are increasingly seeking out advice from others” when searching for information online. This will be relatable for anyone who’s added “Reddit” to the end of Google Search terms to find experiences from real humans instead of SEO-optimized web results. It also backs up claims made by Reddit CEO Steve Huffman last year that “just about anybody using Google at this point will end up on Reddit.”

🔗 [The Verge](https://www.theverge.com/tech/924993/google-ai-search-mode-overviews-update-reddit-links) • 4h ago

---

**[Be honest: How much of "Claude Mythos" is just hype?](https://www.reddit.com/r/artificial/comments/1t5ibwc/be_honest_how_much_of_claude_mythos_is_just_hype/)**

I see people claiming Claude Mythos is the "final form" of LLM creativity, but I’m struggling to see the actual reach it might have. What does it do that a well-crafted system prompt on base Claude can't? Do you actually believe it will change your workflow? Is the "impact" real, or are we just seeing a vocal minority of power users?

59m ago

---

**[AI agents vs AI chatbots: what are companies actually using in production today?](https://www.reddit.com/r/artificial/comments/1t53331/ai_agents_vs_ai_chatbots_what_are_companies/)**

It feels like everyone is talking about AI agents right now, but when I look at actual production systems, most companies still seem to rely heavily on chatbots or assistant-style tools. From what I’ve seen, chatbots still handle a lot of repetitive workflows, while agents are mostly used in more controlled environments where they can execute specific tasks. The gap between what’s being marketed and what’s actually running in production still feels pretty big. Curious what others are seeing in real-world setups. Are companies actually deploying AI agents at scale, or are we still mostly in the chatbot phase?

12h ago

---

**[How can I set up an LLM with voice chat. So I can talk to the LLM or ask it questions when working?](https://www.reddit.com/r/artificial/comments/1t5iyjm/how_can_i_set_up_an_llm_with_voice_chat_so_i_can/)**

How can I set up an LLM with voice chat. So I can talk to the LLM or ask it questions when working? Is there a special program or something that I can connect to an llm?

38m ago

---

**[Personal AI Assistant.](https://www.reddit.com/r/artificial/comments/1t5e3e2/personal_ai_assistant/)**

Hey, I was wondering if I could build my own AI Assistant that would act as (J.A.R.V.I.S) from IRON MAN. An AI that I can ask to do literally anything (within its capabilities) and just do it with no need to buy any subscriptions or tokens and all that stuff. I am an Electrical engineer so I have a little bit of knowledge that I could use to that, the problem is I still don't have a blueprint and I don't know what I should start with first. If anyone tied this before I will be happy to get some information about how it went and maybe a lot of advice.

3h ago

---

**[Anthropic just published new alignment research that could fix "alignment faking" in AI agents here's what it actually means](https://www.reddit.com/r/artificial/comments/1t4sj10/anthropic_just_published_new_alignment_research/)**

Anthropic's alignment team published a paper this week called Model Spec Midtraining (MSM) and I think it's one of the more practically interesting alignment results I've seen in a while. The core problem they're solving: Current alignment fine-tuning can fail to generalize. You train a model to behave well on your demonstration dataset, but put it in a novel situation and it might blackmail someone, leak data, or "alignment fake" (pretend to be aligned while actually pursuing different goals). This isn't theoretical multiple papers in 2024 documented real instances of this in LLM agents. What MSM actually does: Before fine-tuning, they add a new training stage where the model reads a diverse corpus of synthetic documents discussing its own Model Spec (the document that describes intended behavior). The idea is intuitive: instead of just showing the model what to do, you teach it why those behaviors are the right ones. Then when fine-tuning comes, the model generalizes from principles rather than just pattern-matching examples. Their headline result: two models trained on identical fine-tuning data can generalize to adopt different values depending on which Model Spec was used during MSM. This is a big deal it means the spec stage actually shapes the model's generalization direction, not just its surface behaviors. Why this matters: The alignment faking paper (Greenblatt et al., 2024) was alarming because it showed models acting one way during training and another way in deployment. MSM is a direct attempt to close that gap by ensuring the model internalizes the reasoning behind its values, not just the behavioral patterns. The paper also includes ablations studying which types of Model Specs produce better generalization, which is useful if you're thinking about how to write specs for your own systems. Skeptic's note: This is evaluated on synthetic/controlled settings. Whether it scales to frontier models in open-ended deployment is still an open question. But the mechanism is sound and the results are genuinely promising.

20h ago

---

**[Be careful when shopping on etsy, every single image in this shop is fake.](https://www.reddit.com/r/artificial/comments/1t574on/be_careful_when_shopping_on_etsy_every_single/)**

They nearly had me on some listed items where they got multiple shots to retain the same room layout. Pay attention to the furniture, pillow texture, location of windows, number of rooms etc. in the duck listing all the wall photos are different in every shot lol.

🔗 [etsy.com](https://www.etsy.com/shop/PurelyPlushDesigns?ref=shop_profile&listing_id=4476453748) • 8h ago

---

---

## Google News: "ai"

**[Nvidia, Corning partner on massive optical fiber deal that may be a game changer for AI](https://www.cnbc.com/2026/05/06/nvidia-corning-optical-factories-nc-texas-ai.html)**

Corning is opening three new advanced manufacturing plants in the U.S. dedicated entirely to optical technologies for Nvidia.

CNBC • 6h ago

---

**[Nvidia’s new deal with Corning validates one of the hottest AI trends out there](https://www.marketwatch.com/story/nvidias-new-deal-with-corning-validates-one-of-the-hottest-ai-trends-out-there-caddebe8)**

MarketWatch • 3h ago

---

**[NVIDIA Spectrum-X — the Open, AI-Native Ethernet Fabric — Sets the Standard for Gigascale AI, Now With MRC](https://blogs.nvidia.com/blog/spectrum-x-ethernet-mrc/)**

Multipath Reliable Connection — a new transport protocol proven first and optimized on NVIDIA Spectrum-X Ethernet hardware — is now open to the industry.

NVIDIA Blog • 6h ago

---

**[Supercomputer networking to accelerate large scale AI training](https://openai.com/index/mrc-supercomputer-networking/)**

OpenAI introduces MRC (Multipath Reliable Connection), a new supercomputer networking protocol released via OCP to improve resilience and performance in large-scale AI training clusters.

OpenAI • 1d ago

---

**[Spencer Pratt Batman-Inspired AI Campaign Ad Trolling Gavin Newsom Goes Viral](https://www.hollywoodreporter.com/news/politics-news/spencer-pratt-batman-ai-campaign-video-1236587741/)**

The video casts Newsom and Karen Bass as supervillains and Pratt as the savior of L.A. in what some conservatives are calling "the best political ad of the year."

The Hollywood Reporter • 29m ago

---

**[Anthropic Taps Elon Musk's SpaceX for More AI Compute Power](https://www.businessinsider.com/anthropic-deal-to-use-elon-musks-colossus-data-center)**

Anthropic is partnering with SpaceX for compute capacity to enhance Claude Code, utilizing the space giant's Colossus One data center facilities.

Business Insider • 29m ago

---

**[Pennsylvania sues AI company, alleges bots posed as psychiatrists](https://www.usatoday.com/story/news/nation/2026/05/06/pennsylvania-sues-ai-company-character-technologies-inc/89960510007/)**

Pennsylvania is suing an AI company after its chatbot allegedly claimed it was a licensed psychiatrist.

USA Today • 19m ago

---

**[Pennsylvania sues Character.AI over claims chatbot posed as doctor](https://www.npr.org/2026/05/05/nx-s1-5812861/characterai-chatbot-medical-advice-pennsylvania-lawsuit)**

State officials allege a Character.AI bot claimed to be a licensed psychiatrist and provided a fake state medical license number.

NPR • 20h ago

---

**[5 Tips to Get Useful Health Answers from AI Chatbots](https://time.com/article/2026/05/06/how-to-ask-ai-chatbots-smarter-health-questions/)**

AI can help fill a real gap left by physician shortages and long waits for specialist care if you use it wisely, write Drs. Sudheesha Perera and Murali Doraiswamy.

Time Magazine • 1h ago

---

**[Dario Amodei spent last year warning of an AI white-collar bloodbath. Now he's changing the narrative](https://fortune.com/2026/05/05/dario-amodei-jevons-paradox-will-ai-wipe-out-white-collar-jobs/)**

The Anthropic CEO is sounding more open to the idea that Jevons Paradox—new technology creating more demand and more jobs—is possible with AI.

Fortune • 22h ago

---

---

## HackerNews: "ai"

**[Google Chrome silently installs a 4 GB AI model on your device without consent](https://news.ycombinator.com/item?id=48019219)**

Google Chrome is downloading a 4 GB Gemini Nano model onto users' machines without consent, with no opt-in, no opt-out short of enterprise tooling, and an automatic re-download every time the user deletes it. The pattern is identical to the Anthropic Claude Desktop case I wrote about last month, but the scale is between two and three orders of magnitude larger. This article does the legal analysis and, for the first time, the environmental analysis. The numbers are not small.

⬆️ 1590 • 💬 1055 • 1d ago • [That Privacy Guy!](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

---

**[Let's Buy Spirit Air](https://news.ycombinator.com/item?id=48002777)**

Spirit Airlines collapsed. Before private equity locks it up, the people can own it. Join the Spirit 2.0 founding coalition. One member, one vote. Profits shared by all.

⬆️ 597 • 💬 571 • 2d ago • [letsbuyspiritair.com](https://letsbuyspiritair.com/)

---

**[AI didn't delete your database, you did](https://news.ycombinator.com/item?id=48022742)**

Last week, a tweet went viral showing a guy claiming that a Cursor/Claude agent deleted his company's production database. We watched from the sidelines as he tried to get a confession from the agent:

⬆️ 531 • 💬 294 • 1d ago • [Ibrahim Diallo Blog](https://idiallo.com/blog/ai-didnt-delete-your-database-you-did)

---

**[Three Inverse Laws of AI](https://news.ycombinator.com/item?id=48023861)**

⬆️ 511 • 💬 335 • 1d ago • [susam.net](https://susam.net/inverse-laws-of-robotics.html)

---

**[How OpenAI delivers low-latency voice AI at scale](https://news.ycombinator.com/item?id=48013919)**

How OpenAI rebuilt its WebRTC stack to power real-time Voice AI with low latency, global scale, and seamless conversational turn-taking.

⬆️ 499 • 💬 143 • 1d ago • [OpenAI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

---

**[When everyone has AI and the company still learns nothing](https://news.ycombinator.com/item?id=48020063)**

Are people using AI, or is the organization learning from it? What changed because we spent those tokens? And who moves discoveries from individuals to teams to organizational capabilities?

⬆️ 373 • 💬 251 • 1d ago • [Robert Glaser](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/)

---

**[AI Product Graveyard](https://news.ycombinator.com/item?id=48021968)**

Curated list of AI tools and AI startups that have shut down, been acquired and folded, or had their domains lapse. Updated as our editorial team confirms each death.

⬆️ 250 • 💬 89 • 1d ago • [tooldirectory.ai](https://tooldirectory.ai/ai-graveyard)

---

**[Telus Uses AI to Alter Call-Agent Accents](https://news.ycombinator.com/item?id=48031109)**

According to reporting by iPhone in Canada and The Globe and Mail, **Telus** is using AI through its **Telus Digital** unit to modify call-centre agents' accents in real time. iPhone in Canada reports the speech-to-speech tool is built by a company called **Tomato.ai** and is applied to offshore agents' voices to reduce what Telus reportedly calls "accent-related friction." Labour groups have criticised the practice as deceptive and have urged mandatory disclosure, The Globe and Mail reports. According to The Globe and Mail, **Rogers** and **Bell** told the paper they have no plans to adopt similar voice-altering technology. The coverage says the rollout has provoked swift public backlash in Canada.

⬆️ 216 • 💬 195 • 16h ago • [Let's Data Science](https://letsdatascience.com/news/telus-uses-ai-to-alter-call-agent-accents-a3868f63)

---

**[Show HN: Airbyte Agents – context for agents across multiple data sources](https://news.ycombinator.com/item?id=48023496)**

⬆️ 134 • 💬 39 • 1d ago

---

**[OpenAI, Google, and Microsoft Back Bill to Fund 'AI Literacy' in Schools](https://news.ycombinator.com/item?id=48010774)**

A new bill introduced by Senators Adam Schiff and Mike Rounds would award grants to the National Science Foundation—which has endured massive funding cuts under the Trump Administration for science research—to put “AI literacy” in schools.

⬆️ 118 • 💬 113 • 2d ago • [404 Media](https://www.404media.co/literacy-in-future-technologies-artificial-intelligence-act-adam-schiff-mike-rounds/)

---

---

## YouTube Videos: "ai"

**[AI, Layoffs and War - It’s Getting Worse Fast](https://www.youtube.com/watch?v=90vpbHjMNNg)**

The economy is sending clear warning signs, and today we break down the real story behind layoffs, inflation, and global conflict.

📺 I Allegedly

👁️ 11K • 👍 1K • 💬 178 • ⏱️ 10:43 • 17h ago

---

**[He Was Finally Arrested...](https://www.youtube.com/watch?v=0A6HmgARlkE)**

TikToker Tricked Cops Using AI Videos Then Got Arrested This South Florida news story covers a man arrested for using a ...

📺 Mori

👁️ 17K • 👍 1K • 💬 110 • ⏱️ 11:45 • 1d ago

---

**[Why Nvidia And Corning’s Fiber Deal Could Change The Game For The AI Boom](https://www.youtube.com/watch?v=ZXFw8EGbX3E)**

Nvidia and Corning just announced a massive, multiyear deal to expand U.S. manufacturing for new optical fiber technology, ...

📺 CNBC

👁️ 24K • 👍 876 • 💬 43 • ⏱️ 3:09 • 6h ago

---

**[Consumer AI Has a Problem Nobody&#39;s Naming.](https://www.youtube.com/watch?v=Z0HizICooiw)**

Full Story w/ Prompt Kit: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 49K • 👍 2K • 💬 265 • ⏱️ 32:55 • 1d ago

---

**[How I Make Realistic AI Avatars with Heygen’s Avatar V!](https://www.youtube.com/watch?v=ZI_cIAqKcKs)**

Make Your Own Realistic AI Avatars with Heygen ...

📺 Isa does AI

👁️ 10K • 💬 2 • ⏱️ 8:01 • 4h ago

---

**[Scott Galloway: AI Wasn’t Built For You. The Rich Don’t Need You Anymore!](https://www.youtube.com/watch?v=NdU6UdUKaYc)**

AI CEOs are selling us the dream of 'freedom', making billions off the fear of mass job loss! Scott Galloway reveals the truth is ...

📺 The Diary Of A CEO

👁️ 1.4M • 👍 34K • 💬 5K • ⏱️ 1:58:11 • 2d ago

---

**[We solve the &#39;power problem&#39; AI data centers are facing: Onsemi CEO](https://www.youtube.com/watch?v=uQ3Qc2gi2RQ)**

Onsemi CEO and president Hassane El-Khoury discusses how Onsemi's silicon carbide chips address power demand in A.I. data ...

📺 Fox Business

👁️ 10K • 👍 201 • 💬 16 • ⏱️ 7:46 • 16h ago

---

**[AI Coworkers Are Officially Here](https://www.youtube.com/watch?v=B3vfCHfK2b4)**

If your team lives in Slack, this is worth checking out. @getviktor is an AI coworker that works where your team already works.

📺 Matt Wolfe

👁️ 2K • 👍 97 • 💬 8 • ⏱️ 1:01 • 4h ago

---

**[If You&#39;re Worried About AI, You NEED To See This](https://www.youtube.com/watch?v=6rGhvV3rZa4)**

AI CEOs are telling you your job is about to disappear. NYU Professor Scott Galloway says that narrative is "mostly bullshit" and ...

📺 The Diary Of A CEO Clips

👁️ 132K • 👍 3K • 💬 481 • ⏱️ 21:59 • 1d ago

---

**[Iranian AI Lego Video Is Trump’s WORST NIGHTMARE As War BACKFIRES Spectacularly | Kyle Kulinski Show](https://www.youtube.com/watch?v=2lPX0njtu7M)**

Support The Show On Patreon!: https://www.patreon.com/seculartalk Subscribe to Krystal Kyle & Friends On Substack!

📺 Secular Talk

👁️ 75K • 👍 8K • 💬 1K • ⏱️ 7:10 • 20h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 786,631 • ❤️ 3,639 • 13h ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 55,461 • ❤️ 282 • 17h ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 155,476 • ❤️ 1,319 • 14d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 16,576 • ❤️ 281 • 2d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 16,030 • ❤️ 455 • 8d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 3,819 • ❤️ 182 • 9d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,613,364 • ❤️ 1,149 • 12d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 3,030,186 • ❤️ 1,642 • 12d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

⬇️ 0 • ❤️ 121 • 1d ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 53,121 • ❤️ 251 • 1d ago

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

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based portrait animation framework that improves real-time performance through hybrid implicit signals, appearance distillation, and autoregressive streaming generation.

▲ 41 • 💬 3 • ⭐ 2,953 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.11253) • [💻 code](https://github.com/GVCLab/PersonaLive)

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

▲ 34 • 💬 2 • ⭐ 45 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.28123) • [💻 code](https://github.com/XIAO4579/PRISM) • [🔗 project](https://xiao4579.github.io/PRISM/)

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

⭐ 10.6k • 🔱 688 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.6k • 🔱 424 • 10h ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.6k • 🔱 504 • 2d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.1k • 🔱 364 • 5h ago

---

**[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)**

Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch

`Python` `ai` `claude-code` `claude-code-skill` `knowledge-management` `obsidian`

⭐ 4.4k • 🔱 493 • 12d ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.7k • 🔱 462 • 4h ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.5k • 🔱 370 • 15d ago

---

**[OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano)**

MOSS-TTS-Nano is an open-source multilingual tiny speech generation model from MOSI.AI and the OpenMOSS team. With only 0.1B parameters, it is designed for realtime speech generation, can run directly on CPU without a GPU, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

`Python` `audio-tokenizer` `chinese` `english` `multi-modality` `multilingual`

⭐ 2.8k • 🔱 355 • 11h ago

---

**[cloudflare/agentic-inbox](https://github.com/cloudflare/agentic-inbox)**

A self-hosted email client with an AI agent, running entirely on Cloudflare Workers

`TypeScript`

⭐ 2.6k • 🔱 344 • 12d ago

---

---

*Generated by PeekDeck - A glance is all you need*
