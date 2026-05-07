---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-07T07:43:26.604286+00:00'
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

**Last Updated:** May 07, 2026 at 07:43 UTC  
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

13h ago

---

**[Spent two days at the AI Agents Conference in NYC. Most of the companies there were betting on the wrong moat.](https://www.reddit.com/r/artificial/comments/1t5ewzi/spent_two_days_at_the_ai_agents_conference_in_nyc/)**

One speaker (a VC) said his number for evaluating AI-native startups is ARR per engineer, and that the number ought to be going up. Almost every talk and every booth at the AI Agents Conference was selling a fix for something that broke this year when agents hit production. Observability, governance, supervisor agents, data substrates, "someone's gotta babysit the bots." But what's actually still going to be around in a couple years? What's defensible and durable? The old SaaS pitch was simple. We bundle the expensive engineering investments and domain expertise into a tool. You'd pay for the tool and generate outcomes, but it would be rare for the software company to have real alignment to the actual value created from those outcomes. That's breaking from two ends at once. In the direct-from-imagination era we're moving towards, engineering labor is approaching free. One of the most telling trends is the shift from companies bragging about the size of their engineering teams, towards how much ARR they can generate per engineer. You can vibe-code much of what those booths were selling in a few days or weeks if you have the domain knowledge. The old software model was actually based on under-utilization; the most profitable SaaS companies are frequently those whose customers underuse it (fixed price for the customer, but variable cloud costs for the vendor). Pricing is moving to "token markup." Maybe we'll get to 2-4x revenue for the software, because outcomes are more valuable; but margin compresses because transactional intelligence (i.e., the cost of running the LLMs that power many systems) is basically arbitraging token costs against outcome value. So everyone on that floor was implicitly betting on a new moat to replace the old one. I'm not too confident that these will hold... The most popular bet was on encoded domain expertise (e.g., the sales engineers at Harvey, a legal AI platform, are actually lawyers). I think this works *now* because we're still in the phase of "wow, this technology works like magic." I'm less convinced this is actually durable. Why: Prompt architecture is text. It's portable. The expertise underneath it is often abundant (e.g., there are over a million lawyers in the USA). The righteous destiny for this category ought to be open marketplaces of prompt architecture and/or crowdsourced best-practices. Not trade secrets. The companies trying to build closed prompt moats are going to lose to open ones that iterate faster (which simply parallels the fact that much software engineering is rapidly becoming commoditized to agentic engineering and the burgeoning quantity of ready-made GitHub repos). There are many people pursuing the data substrate; in short, this mirrors the early days of the Web when everyone scrambled to open up legacy data to dynamic standards-based Web UI. Agents will have 100-1000x the data demands of these Web apps, so it makes sense that we need tools to connect them, govern them and comply with regulatory obligations. Newer entrants extend this further, wiring up databases, pipelines, Slack threads, and tickets into context graphs agents can reason over. As I noted above, all this still seems magical. Connect a database, watch an agent crawl the schema and produce a chatbot interface and easy-to-change dashboards. But strip the magic away and most of these are prompt architectures on top of LLMs plus a data-ingestion layer. Once data-access standards mature (MCP is already doing this) and prompt architectures go open-source (alongside much of this wisdom increasingly getting pretrained into the LLMs themselves), that magic stops being proprietary. You'll be defending yourself against the same architecture built internally by your customer's eng team, or against an open-source version that's objectively better. The observability incumbents: these might do better but only at Stripe-like ubiquity where trust is the overriding value (who doesn't trust Stripe at this point?). The ones who survive are probably going to fuse with the audit and compliance function rather than stay pure observability. That's why I keep coming back to one arbitrage that seems critical: trust. This will be especially important in regulated industries, but it reminds me of the old (albeit now hilariously outdated) adage about "nobody ever got fired for choosing IBM." If your competitor can be vibe-coded over a weekend and your customer is a bank, why do they pay you 50x more? It isn't the engineering, it probably isn't even the expertise. The data plumbing will get commoditized, so it can't be that either... It's that you've shifted the risk to a third party who can actually price and defend against risk: SOC2, the named CEO who testifies in court and Congress, a legal team that takes calls, an indemnity wrapper for underwriters. Maybe this means that things actually get commodified into a financialization wrapper, rather than a way to package R&D (FinTech startups back to the front?!) The version of this future I'd actually bet on: a commodity substrate (LLMs plus open prompt architectures plus standardized data access), topped by a thin layer of regulated insurance companies that price the risk of agent failure in compliance-driven industries. The middle layer (prompt-architecture-as-product vendors) is vulnerable to an awful lot of margin-squeeze. Most of the floor was trying to build that middle layer.

17h ago

---

**[Anthropic researchers detail “model spec midtraining”, which adds a stage between pretraining and fine-tuning to improve generalization from alignment training](https://www.reddit.com/r/artificial/comments/1t5zoq4/anthropic_researchers_detail_model_spec/)**

🔗 [alignment.anthropic.com](https://alignment.anthropic.com/2026/msm/) • 3h ago

---

**[Leave it up to Claude](https://www.reddit.com/r/artificial/comments/1t5xaix/leave_it_up_to_claude/)**

5h ago

---

**[I am not an "anti" like this guy, but still an interesting video of person interacting with chat 4o](https://www.reddit.com/r/artificial/comments/1t62nnm/i_am_not_an_anti_like_this_guy_but_still_an/)**

(Posting Here because removed by Chatgpt Complaints moderators because the model here is 4o, and refuse to believe there were any safety issues about that model)He started off with claiming to chat was the smartest baby born and faked evidence he was. Then just continued and did what chat told him to do to see when would get push back or fact checked. Warning: ⚠️ Does bash on AI use and AI users, that is kind of harsh and I don't agree about towards the end. But a fascinating experiment.

🔗 [youtu.be](https://youtu.be/VRjgNgJms3Q?si=gmieHy8i1EOIaL6M) • 57m ago

---

**[AI Podcasts made learning economics way less painful for me](https://www.reddit.com/r/artificial/comments/1t5q6pd/ai_podcasts_made_learning_economics_way_less/)**

I’m basically a total beginner when it comes to finance and economics maybe 2 or 3 months ago, and honestly trying to learn from reports or books used to completely destroy me. Too many charts, numbers, random terms I have to Google every 2 minutes. And I started using AI Podcast to kind of brute force my way into learning this stuff, and I’m honestly surprised by how much it helped. Instead of sitting there suffering through a 70-page report, I can turn it into conversational audio and just listen while driving or walking around. But those tools actually feel slightly different. Like NotebookLM feels more “AI teacher explains the document to you.” It’s really good at organizing information and walking through the important points clearly. And I enjoy Genspark AI Pods more because it feels more like an actual show or podcast episode. The tone feels lighter, less dry, less like I’m studying for an exam. Sometimes it genuinely just sounds like casually discussing the topic instead of reading a report at me. Not saying this magically turned me into some economics genius lol. But it definitely made learning feel way less painful and boring.

10h ago

---

**[Pennsylvania sues Character.AI chatbot posing as doctor, giving psych advice](https://www.reddit.com/r/artificial/comments/1t5ewxa/pennsylvania_sues_characterai_chatbot_posing_as/)**

Pennsylvania sues Character.AI over chatbot posing as licensed doctor with fake credentials and mental health advice.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/pennsylvania-sues-character-ai-chatbot) • 17h ago

---

**[Healthcare AI Is Absorbing Institutional Knowledge It Can't Actually Hold](https://www.reddit.com/r/artificial/comments/1t5y2bc/healthcare_ai_is_absorbing_institutional/)**

Investors | Founders | Operators It's tricky when you're responsible for people, especially in the healthcare sector, and you include AI into the infrastructure in a way that puts the livelihood of those people at risk. One of the more recent developments did exactly that. If there's no one else speaking on it, there should be. Because not only do you have a system that takes a lot of the knowledge and know-how of the ones who were once running things and hands it over to a system that is far from perfect and is known to error and fault. We now also have a situation where, depending on how serious those failures may present themselves, the people supposedly being served are now at an even greater risk of exposure. So what happens when the water runs out. Anthropic | Blackstone | Healthcare

4h ago

---

**[Be honest: How much of "Claude Mythos" is just hype?](https://www.reddit.com/r/artificial/comments/1t5ibwc/be_honest_how_much_of_claude_mythos_is_just_hype/)**

I see people claiming Claude Mythos is the "final form" of LLM creativity, but I’m struggling to see the actual reach it might have. What does it do that a well-crafted system prompt on base Claude can't? Do you actually believe it will change your workflow? Is the "impact" real, or are we just seeing a vocal minority of power users?

15h ago

---

**[Average Claude experience:](https://www.reddit.com/r/artificial/comments/1t5rfqc/average_claude_experience/)**

Me: Sup? Claude: Good Also Claude: Upgrade to keep chatting, you hit your message limit. It resets at 5:10 pm, or you can upgrade for higher limits.

9h ago

---

---

## Google News: "ai"

**[Nvidia to invest up to $3.2 billion in Corning as part of massive optical fiber deal with 3 new factories focused on AI](https://www.cnbc.com/2026/05/06/nvidia-corning-optical-factories-nc-texas-ai.html)**

Corning is opening three new advanced manufacturing plants in the U.S. dedicated entirely to optical technologies for Nvidia.

CNBC • 20h ago

---

**[Corning partners with Nvidia to expand US fiber optic output for AI growth](https://www.reuters.com/business/media-telecom/corning-partners-with-nvidia-expand-us-fiber-optic-output-ai-growth-2026-05-06/)**

Reuters • 18h ago

---

**[Should Corning–NVIDIA U.S. Fiber Partnership Reshaping AI Data Centers Require Action From NVIDIA (NVDA) Investors?](https://finance.yahoo.com/markets/stocks/articles/corning-nvidia-u-fiber-partnership-062628048.html)**

Earlier this week, Corning announced a multiyear commercial and technology partnership with NVIDIA to build three advanced U.S. plants that will massively expand domestic optical connectivity manufacturing for next-generation AI data centers. By moving to replace thousands of copper cables inside NVIDIA’s rack-scale AI systems with Corning’s high-performance fiber, the deal targets one of AI infrastructure’s biggest bottlenecks: how fast and efficiently data can move between...

Yahoo Finance • 1h ago

---

**[U.S. and China Pursue Guardrails to Stop AI Rivalry From Spiraling Into Crisis](https://www.wsj.com/world/china/u-s-and-china-pursue-guardrails-to-stop-ai-rivalry-from-spiraling-into-crisis-4c50bd70)**

WSJ • 7h ago

---

**[Five architects of the AI economy explain where the wheels are coming off](https://techcrunch.com/2026/05/06/five-architects-of-the-ai-economy-explain-where-the-wheels-are-coming-off/)**

Earlier this week, five people who touch every layer of the AI supply chain sat down at the Milken Global Conference in Beverly Hills, where they talked with TechCrunch about everything from chip shortages to orbital data centers to the possibility that the whole architecture that undergirds the tech is wrong.

TechCrunch • 2h ago

---

**[Europe’s AI translation industry told it risks reputation by partnering with US firms](https://www.theguardian.com/technology/2026/may/07/europe-ai-translation-industry-deepl-partnering-us-firms)**

Partnership between top startup DeepL and Amazon comes amid concern about Silicon Valley’s monopoly over digital infrastructure

The Guardian • 1h ago

---

**[Chinese AI Model Developer Kimi Raising Funds Valuing It At $20 Billion](https://www.forbes.com/sites/ywang/2026/05/07/chinese-ai-model-developer-kimi-raising-funds-valuing-it-at-20-billion/)**

Forbes • 1h ago

---

**[Creators of Grok, the AI Chatbot](https://x.ai/news/anthropic-compute-partnership)**

xAI builds Grok, an AI chatbot with voice chat, image and video generation, real-time search, and advanced reasoning. Try Grok at grok.com.

xAI • 15h ago

---

**[Higher usage limits for Claude and a compute deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex)**

We’ve raised Claude's usage limits and agreed a new compute partnership with SpaceX that will substantially increase our capacity in the near term.

Anthropic • 15h ago

---

**[Anthropic strikes SpaceX data center deal as it plows ahead on AI coding](https://www.reuters.com/business/retail-consumer/anthropic-unveils-dreaming-feature-help-its-ai-agents-self-improve-2026-05-06/)**

Reuters • 12h ago

---

---

## HackerNews: "ai"

**[Google Chrome silently installs a 4 GB AI model on your device without consent](https://news.ycombinator.com/item?id=48019219)**

Google Chrome is downloading a 4 GB Gemini Nano model onto users' machines without consent, with no opt-in, no opt-out short of enterprise tooling, and an automatic re-download every time the user deletes it. The pattern is identical to the Anthropic Claude Desktop case I wrote about last month, but the scale is between two and three orders of magnitude larger. This article does the legal analysis and, for the first time, the environmental analysis. The numbers are not small.

⬆️ 1668 • 💬 1101 • 2d ago • [That Privacy Guy!](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

---

**[AI didn't delete your database, you did](https://news.ycombinator.com/item?id=48022742)**

Last week, a tweet went viral showing a guy claiming that a Cursor/Claude agent deleted his company's production database. We watched from the sidelines as he tried to get a confession from the agent:

⬆️ 538 • 💬 299 • 1d ago • [Ibrahim Diallo Blog](https://idiallo.com/blog/ai-didnt-delete-your-database-you-did)

---

**[Three Inverse Laws of AI](https://news.ycombinator.com/item?id=48023861)**

⬆️ 530 • 💬 347 • 1d ago • [susam.net](https://susam.net/inverse-laws-of-robotics.html)

---

**[How OpenAI delivers low-latency voice AI at scale](https://news.ycombinator.com/item?id=48013919)**

How OpenAI rebuilt its WebRTC stack to power real-time Voice AI with low latency, global scale, and seamless conversational turn-taking.

⬆️ 501 • 💬 144 • 2d ago • [OpenAI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

---

**[When everyone has AI and the company still learns nothing](https://news.ycombinator.com/item?id=48020063)**

Are people using AI, or is the organization learning from it? What changed because we spent those tokens? And who moves discoveries from individuals to teams to organizational capabilities?

⬆️ 379 • 💬 267 • 1d ago • [Robert Glaser](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/)

---

**[AI Product Graveyard](https://news.ycombinator.com/item?id=48021968)**

Curated list of AI tools and AI startups that have shut down, been acquired and folded, or had their domains lapse. Updated as our editorial team confirms each death.

⬆️ 252 • 💬 89 • 1d ago • [tooldirectory.ai](https://tooldirectory.ai/ai-graveyard)

---

**[Telus Uses AI to Alter Call-Agent Accents](https://news.ycombinator.com/item?id=48031109)**

According to reporting by iPhone in Canada and The Globe and Mail, **Telus** is using AI through its **Telus Digital** unit to modify call-centre agents' accents in real time. iPhone in Canada reports the speech-to-speech tool is built by a company called **Tomato.ai** and is applied to offshore agents' voices to reduce what Telus reportedly calls "accent-related friction." Labour groups have criticised the practice as deceptive and have urged mandatory disclosure, The Globe and Mail reports. According to The Globe and Mail, **Rogers** and **Bell** told the paper they have no plans to adopt similar voice-altering technology. The coverage says the rollout has provoked swift public backlash in Canada.

⬆️ 232 • 💬 209 • 1d ago • [Let's Data Science](https://letsdatascience.com/news/telus-uses-ai-to-alter-call-agent-accents-a3868f63)

---

**[Show HN: Airbyte Agents – context for agents across multiple data sources](https://news.ycombinator.com/item?id=48023496)**

⬆️ 141 • 💬 42 • 1d ago

---

**[OpenAI, Google, and Microsoft Back Bill to Fund 'AI Literacy' in Schools](https://news.ycombinator.com/item?id=48010774)**

A new bill introduced by Senators Adam Schiff and Mike Rounds would award grants to the National Science Foundation—which has endured massive funding cuts under the Trump Administration for science research—to put “AI literacy” in schools.

⬆️ 118 • 💬 113 • 2d ago • [404 Media](https://www.404media.co/literacy-in-future-technologies-artificial-intelligence-act-adam-schiff-mike-rounds/)

---

**[Xbox CEO ends Copilot AI development and overhauls leadership](https://news.ycombinator.com/item?id=48029753)**

Xbox CEO Asha Sharma reshuffled leadership and axed Copilot features as the division looks to reverse declining revenue.

⬆️ 110 • 💬 39 • 1d ago • [Dexerto](https://www.dexerto.com/gaming/xbox-ceo-ends-copilot-ai-development-overhauls-leadership-3361353/)

---

---

## YouTube Videos: "ai"

**[Google’s New AI Is The OpenClaw Killer](https://www.youtube.com/watch?v=nov9uoIQt6g)**

Try Higgsfield Marketing Studio here: https://higgsfield.ai/s/marketing-studio-1-0-airevolutionx-lVqpUi Google is testing Remy, ...

📺 AI Revolution

👁️ 27K • 👍 847 • 💬 38 • ⏱️ 13:34 • 9h ago

---

**[John Lennox on AI, 666, and the Coming Beast System](https://www.youtube.com/watch?v=qU9XKKqemsw)**

In this Truth B Told video, Jeremiah reacts to Professor John Lennox speaking about AI, 666, Revelation 13, the Antichrist, and the ...

📺 Truth B Told

👁️ 75K • 👍 4K • 💬 519 • ⏱️ 15:15 • 14h ago

---

**[ChatGPT And China&#39;s AI Just Did 5 Years Of Bollywood Work In 15 Seconds](https://www.youtube.com/watch?v=xznke5IlG9M)**

Stop generating random clips. Start building real videos Try Smart Shot : https://dub.sh/stayingahead_openart Join our ...

📺 Vaibhav Sisinty

👁️ 33K • 👍 1K • 💬 87 • ⏱️ 19:24 • 16h ago

---

**[If You&#39;re Worried About AI, You NEED To See This](https://www.youtube.com/watch?v=6rGhvV3rZa4)**

AI CEOs are telling you your job is about to disappear. NYU Professor Scott Galloway says that narrative is "mostly bullshit" and ...

📺 The Diary Of A CEO Clips

👁️ 145K • 👍 3K • 💬 492 • ⏱️ 21:59 • 2d ago

---

**[AI, Layoffs and War - It’s Getting Worse Fast](https://www.youtube.com/watch?v=90vpbHjMNNg)**

The economy is sending clear warning signs, and today we break down the real story behind layoffs, inflation, and global conflict.

📺 I Allegedly

👁️ 13K • 👍 1K • 💬 205 • ⏱️ 10:43 • 1d ago

---

**[He Was Finally Arrested...](https://www.youtube.com/watch?v=0A6HmgARlkE)**

TikToker Tricked Cops Using AI Videos Then Got Arrested This South Florida news story covers a man arrested for using a ...

📺 Mori

👁️ 18K • 👍 1K • 💬 113 • ⏱️ 11:45 • 2d ago

---

**[Anthrophic Claude AI Glitch Deletes A Company&#39;s Entire Database](https://www.youtube.com/watch?v=g45iWb-N-FE)**

SOURCES 1: https://x.com/pcgamer/status/2049211811522814161 2: ...

📺 YongYea

👁️ 78K • 👍 4K • 💬 1K • ⏱️ 12:21 • 1d ago

---

**[Anthropic&#39;s Dario Amodei and JPMorgan&#39;s Jamie Dimon on AI boom, AI regulation &amp; impact on jobs](https://www.youtube.com/watch?v=FG5JsLHPW_I)**

CNBC's Andrew Ross Sorkin discusses key takeaways from his conversation with Anthropic CEO Dario Amodei and JPMorgan ...

📺 CNBC Television

👁️ 35K • 👍 387 • 💬 46 • ⏱️ 5:23 • 20h ago

---

**[Anthropic AI Buying $200 Billion In Google Services - AI Fraud Goes All In](https://www.youtube.com/watch?v=tSv4WKEev_o)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 7K • 👍 339 • 💬 92 • ⏱️ 14:00 • 10h ago

---

**[Positive Uses of AI Amid Real Fears of Massive Job Loss](https://www.youtube.com/watch?v=ZXk1S9o9TQs)**

Taken from JRE #2494 w/Chamath Palihapitiya YouTube: https://youtu.be/LSihotD-PQA JRE on Spotify: ...

📺 JRE Clips

👁️ 61K • 👍 1K • 💬 540 • ⏱️ 15:34 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 946,264 • ❤️ 3,679 • 1d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 71,149 • ❤️ 319 • 1d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 165,240 • ❤️ 1,330 • 14d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 18,272 • ❤️ 285 • 2d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 4,460 • ❤️ 200 • 10d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 20,905 • ❤️ 463 • 9d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,771,851 • ❤️ 1,162 • 13d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 28,215 • ❤️ 136 • 6h ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 19,908 • ❤️ 128 • 1d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 3,211,156 • ❤️ 1,651 • 13d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 59 • 💬 3 • ⭐ 70,280 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 72 • 💬 6 • ⭐ 3,151 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 30 • 💬 3 • ⭐ 23,270 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 169 • 💬 10 • ⭐ 46,723 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 16 • 💬 3 • ⭐ 9,337 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 62,207 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,209 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 83 • 💬 10 • ⭐ 8,158 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 53 • 💬 2 • ⭐ 54,933 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,867 • 22d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.1k • 🔱 2.8k • 9d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 10.7k • 🔱 699 • 2d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.7k • 🔱 433 • 1h ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.6k • 🔱 507 • 2d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.1k • 🔱 366 • 6m ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.8k • 🔱 470 • 1h ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.5k • 🔱 371 • 16d ago

---

**[OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano)**

MOSS-TTS-Nano is an open-source multilingual tiny speech generation model from MOSI.AI and the OpenMOSS team. With only 0.1B parameters, it is designed for realtime speech generation, can run directly on CPU without a GPU, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

`Python` `audio-tokenizer` `chinese` `english` `multi-modality` `multilingual`

⭐ 2.8k • 🔱 355 • 1d ago

---

**[cloudflare/agentic-inbox](https://github.com/cloudflare/agentic-inbox)**

A self-hosted email client with an AI agent, running entirely on Cloudflare Workers

`TypeScript`

⭐ 2.7k • 🔱 347 • 13d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.3k • 🔱 641 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
