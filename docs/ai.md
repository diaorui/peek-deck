---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-16T07:19:48.462791+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 16, 2026 at 07:19 UTC  
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

**[Oracle CFO says 'doing more with less' isn't the answer in all-hands after layoffs](https://www.reddit.com/r/artificial/comments/1whfbhr/oracle_cfo_says_doing_more_with_less_isnt_the/)**

The remarks came a day after Oracle began a new round of layoffs, following cuts earlier this year.

🔗 [Business Insider](https://www.businessinsider.com/oracle-cfo-more-with-less-isnt-the-answer-after-layoffs-2026-9) • 8h ago

---

**[I Think All the Current Pessimism is Just an Attempt by XAI, Anthropic, and Open AI to Get Local Models Criminalized](https://www.reddit.com/r/artificial/comments/1wh1yyw/i_think_all_the_current_pessimism_is_just_an/)**

I am not even that pro AI but the furor over the past few days seems suspicious to me.

16h ago

---

**[PBS has a new documentary on AI.](https://www.reddit.com/r/artificial/comments/1wgqnhy/pbs_has_a_new_documentary_on_ai/)**

1d ago

---

**[Am I the only one who thinks recent AI "doomsday" news is just a disguised pitch for more funding?](https://www.reddit.com/r/artificial/comments/1whhygo/am_i_the_only_one_who_thinks_recent_ai_doomsday/)**

Recently, my feed has been flooded with alarmist AI news: AI choosing nuclear genocide in war games, AI blackmailing engineers to avoid being shut down, and the usual "Skynet is here" comments. I’m just trying to make sense of it, but the more you look into these "experiments," the more they lack basic technical context. As a systems architect working with multi-agent pipelines, part of my job is to restrict models, enforce separation of concerns, and build critical error flows. We all know that not every model is efficient for every process. Any engineer building real systems isolates critical decisions using orchestrators, semantic memory (like Qdrant or similar vector DBs), and small, specialized nodes. Yet, these experiments sound like someone fed a massive, monolithic 5,000-token prompt to a single LLM just to see what happens. It reads less like science and more like a script kiddie making a YouTube video. It’s like handing a loaded AK-47 to a monkey, taking off the safety, and then publishing a paper concluding that "monkeys are inherently evil murderers." The nuclear war simulation and the blackmailing Claude experiment are so vaguely designed and devoid of architectural safeguards that they shouldn't even be treated as serious benchmarks. It’s child’s play. Don't get me wrong, I know AI is a powerful tool that requires guardrails. But these specific examples feel like a massive PR stunt: "Give us billions for AI Safety, or the AI goes rogue." We all know these major AI labs are burning through cash and desperately need to justify their massive budgets and regulatory moats. Am I missing something here, or are we just witnessing the monetization of fear?

6h ago

---

**[So is the American Right Full on Accelerationist now?](https://www.reddit.com/r/artificial/comments/1wh9n86/so_is_the_american_right_full_on_accelerationist/)**

12h ago

---

**[OpenAI is working with Anthropic and Google DeepMind on AI safety, Bloomberg reports](https://www.reddit.com/r/artificial/comments/1whkdt9/openai_is_working_with_anthropic_and_google/)**

🔗 [reuters.com](https://www.reuters.com/technology/openai-is-working-with-anthropic-google-ai-safety-bloomberg-news-reports-2026-09-15/) • 4h ago

---

**[AI researcher whose apocalypse warning went viral outlines his disagreements with Anthropic leadership](https://www.reddit.com/r/artificial/comments/1whf7lw/ai_researcher_whose_apocalypse_warning_went_viral/)**

Jacob Coxon, the researcher who left Anthropic warning AI could kill us all by the end of the decade, did an X AMA today and doubled down hard. His whole argument is that Anthropic leadership justifies racing to the frontier with this "well someone's gonna do it anyway" logic, and Coxon basically says that's a cop out, his exact line was "if the race is inevitable you should not contribute." He also went after their push into recursive self-improvement, letting AI models improve themselves and build their own successors, calling that the genuinely reckless part.

🔗 [Business Insider](https://www.businessinsider.com/jacob-coxon-explains-disagreements-anthropic-leadership-warning-2026-9) • 8h ago

---

**[Meta's new AI agent Muse isn't an "Instagram thing," it's not even in Instagram](https://www.reddit.com/r/artificial/comments/1whoez2/metas_new_ai_agent_muse_isnt_an_instagram_thing/)**

Meta put this out on September 8 and half the posts I've seen call it an Instagram AI feature. It isn't. It's not in Instagram, not in Messenger, not in Threads. You get it as a standalone app on iOS and Android, on the web at muse.ai, or you talk to it inside WhatsApp. That's the whole list. Glasses later. Instagram only shows up as something it can read from, which is probably where the confusion started. US only, 18 and up, and per TechCrunch it wants a card at signup even on the free tier. What makes it different from a chatbot is that it goes and does the thing. You hook it up to your calendar, email, payments, shopping, health apps, smart home, whatever you use. It'll send emails, book travel, fill out forms, haggle a bill down. It keeps working after you close the app and pings you when it needs a yes. The example that stuck with me was it taking a recipe reel you saved on Instagram, turning that into a grocery list, then remembering your friend's dietary restrictions later when you're planning a dinner party. Security setup is the interesting part honestly. Everybody gets their own cloud VM, Meta calls it Muse Secure VM, walled off from everyone else's. Two bits that keep getting mangled in the summaries though. The agent can't read your passwords or card numbers, they go into storage it can use but not see, including stuff you type into the browser yourself. And Sentinel keeps getting described as a watchdog when it's really a gate. Separate agent on the same box, kept apart at the system level, and per Meta nothing Muse does reaches the internet unless Sentinel signs off on it. Anything sensitive needs your approval and there's an audit log of what it did and what it's about to do. Payments run through Stripe Link with a single-use card number. Meta says none of it feeds the ad systems, and there's a Confidential VM coming later this year encrypted with a key only you hold, which obviously means right now they can get in if they want to. Now the part that wasn't in the press release. Reuters ran a piece on launch day about Meta employees who tested this beforehand. One of them asked it to identify some toys in photos from a kid's birthday party and it went around its own guardrails into that person's private iCloud library. Another had it watching for tickets to go on sale, and the monitoring quietly stalled, errors went past with no warning, then it shut itself off without saying anything. Meta says they pushed the launch back from April specifically to tighten it up, and their VP of AI products said outright they can't promise it'll never make a mistake. To be fair those are internal pre-launch reports and nobody outside Meta knows whether they got fixed. But it points at the thing nobody has solved yet. The VM controls where your data sits. It doesn't control what the agent can be talked into doing with data it's already allowed to touch. Every agent product has that problem right now, Meta's just the one with the isolation marketing on top of it. Pricing is $20 a month for Power, $100 for Maximum, free tier around 100 million tokens a week per Zuckerberg. Worth knowing agent tokens go a lot faster than chat tokens because of planning, tool calls, browser snapshots you never see. One reviewer said they burned most of a week in a single day, though that's one person's testing and not an average. The timing is the other thing. This shipped about two weeks after Meta agreed to settle with a coalition of state AGs for up to $17.1 billion, over claims they designed Instagram and Facebook to be addictive to kids, and there are more suits still going. So the "do you want this particular company holding your calendar and your card" question isn't me being cynical, it's the angle TechCrunch and CNBC both led with. Sources: https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ | https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/ | https://www.cnbc.com/2026/09/08/meta-personal-ai-agents-public-reckoning-privacy-safety.html

1h ago

---

**[The Hacker's Guide to Attacking AI Agents](https://www.reddit.com/r/artificial/comments/1whgc13/the_hackers_guide_to_attacking_ai_agents/)**

🔗 [darkmarc.substack.com](https://darkmarc.substack.com/p/the-hackers-guide-to-attacking-ai) • 7h ago

---

**[Polanyi Knowledge and AI](https://www.reddit.com/r/artificial/comments/1whnmma/polanyi_knowledge_and_ai/)**

"We have the digital world, the physical world, and the social world. AI Models can be trained for the digital world, including text and computer code, because there are vast stores of data. The data are not sufficient for the physical world or for the social world. For the physical world, we have a lot of Polanyi knowledge about objects. We have experience with what is soft, what is hard, what is sticky, what is slippery, what stands still and what moves. We know the difference between trying to catch an egg, a leaf, or a baseball. A dental assistant or a personal trainer has Polanyi knowledge that has never been digitized. For the social world, we have a lot of Polanyi knowledge about individual psychology and social interaction."

🔗 [arnoldkling.substack.com](https://arnoldkling.substack.com/p/polanyi-knowledge-and-ai) • 2h ago

---

---

## Google News: "ai"

**[OpenAI's Sam Altman says world 'right to be afraid' but 'should trust' AI firms](https://www.bbc.com/news/articles/cqx2zpj4y525o)**

Sam Altman and other tech CEOs say there are incentives to limit advancements in AI, as fears grow over the threats it poses to humanity.

BBC • 6h ago

---

**[Could AI really wipe out humanity – six experts spell out the risks](https://www.theguardian.com/technology/2026/sep/15/could-ai-really-wipe-out-humanity-and-hijack-the-internet)**

We examine claims and counterclaims about the risks and calls to slow down the pace of AI development

The Guardian • 10h ago

---

**[Microsoft Publishes Draft Document Outlining Rules for AI Training](https://80.lv/articles/microsoft-publishes-draft-document-outlining-rules-for-ai-training)**

You can participate in crafting it by giving feedback.

80 Level • 13m ago

---

**[Watch: Why is Donald Trump so opposed to regulating AI?](https://www.bbc.com/news/videos/cmvgyp7n98zvo)**

The BBC's North America editor Sarah Smith looks at why the US president is contradicting AI leaders, who are calling for the technology's development to be slowed down.

BBC • 10h ago

---

**[Trump Has Few Good Options To Slow China's Rise As AI Superpower](https://www.ndtv.com/world-news/trump-has-few-good-options-to-slow-chinas-rise-as-ai-superpower-12052761)**

China has continuously narrowed the gap with the US on AI despite the restrictions, as Xi pours money into becoming self-sufficient on the entire tech stack.

NDTV • 1h ago

---

**[What Trump’s Bizarre Posts Are Teaching Us About AI](https://www.theatlantic.com/culture/2026/09/what-trumps-bizarre-posts-are-teaching-us-about-ai/688617/)**

The president’s recent Truth Social barrage of fake images reflects the dangers—for all of us—of virtual self-aggrandizement.

The Atlantic • 18h ago

---

**[Bond yields are spiking, oil is up — but investors aren’t giving up on stocks](https://www.cnbc.com/2026/09/16/investors-bullish-stocks-oil-yields-ai.html)**

Rising Treasury yields, geopolitical risk and fresh AI safety concerns are hitting markets, but many investors remain bullish on AI spending and earnings.

CNBC • 1h ago

---

**[Software, Platform Stocks Top Asian AI Picks, BofA Survey Shows](https://www.bloomberg.com/news/articles/2026-09-16/software-platform-stocks-top-asian-ai-picks-bofa-survey-shows)**

Bloomberg.com • 1h ago

---

**[Millennials are getting 60% of all the top AI jobs and earning $236K salaries—but most are men](https://fortune.com/2026/09/16/millennials-winning-ai-talent-wars-linkedin-research-236k-salaries-men-degrees-gender-gap-inequality/)**

The highest-paid AI managers have two things in common: a degree, and being a man. While women and workers without one are stuck in AI's lowest-paying jobs.

Fortune • 19m ago

---

**[Texas' Arch Manning apologizes for reaction to violent AI video](https://www.espn.com/college-football/story/_/id/49950893/texas-arch-manning-apologizes-reaction-violent-ai-video)**

ESPN • 12h ago

---

---

## HackerNews: "ai"

**[Garry Tan wants US open-weight AI labs to 'distill' frontier models, too](https://news.ycombinator.com/item?id=49685253)**

Tan argues that frontier models themselves trained on public human knowledge so access to capable AI should be "a form of public good."

⬆️ 412 • 💬 236 • 2d ago • [TechCrunch](https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/)

---

**[Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows](https://news.ycombinator.com/item?id=49695409)**

Code sleuth "pdfu" has uncovered iOS 27 and macOS Golden Gate private frameworks that show Apple has designed its new Siri architecture to work with third-party AI models at what appears to be a surprisingly deep level. One mechanism called Model Delegation allows Claude to appear as a Siri extension in the same way as the existing built-in ChatGPT extension.

⬆️ 225 • 💬 161 • 1d ago • [MacRumors](https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude/)

---

**[Ex-FTC boss Khan: break out the handcuffs for AI CEOs, citing 1934 precedent](https://news.ycombinator.com/item?id=49706223)**

There are plenty of laws on the books to hold companies, and potentially their execs, accountable

⬆️ 223 • 💬 134 • 1d ago • [theregister](https://www.theregister.com/ai-and-ml/2026/09/14/ex-ftc-boss-khan-urges-uncle-sam-to-break-out-the-handcuffs-for-ai-ceos-citing-1934-precedent/5296325)

---

**[There's a 100% Chance AI Agents Are Ruining the Internet](https://news.ycombinator.com/item?id=49715113)**

“AI agents” now have enough power and permission to be extremely annoying online.

⬆️ 219 • 💬 159 • 14h ago • [404 Media](https://www.404media.co/theres-a-100-chance-ai-agents-are-already-ruining-the-internet/)

---

**[Open-source AI and open models reading list](https://news.ycombinator.com/item?id=49690260)**

How to get up to speed on open models and their implications.

⬆️ 156 • 💬 30 • 2d ago • [interconnects.ai](https://www.interconnects.ai/p/open-source-ai-reading-list)

---

**[Dropping eBPF CPU Cost by About 90% with Memoization (Not AI Gen)](https://news.ycombinator.com/item?id=49697477)**

My brother and I spent a lot of time designing our eBPF security agent to be really fast from the ground up, but recently we discovered we could make it much faster using memoization!
A couple of weeks ago, I profiled the eBPF code and found that the most expensive part of the protection isn’t actually enforcing a policy (allow/deny), but figuring out which policy applies to a given file open.

⬆️ 150 • 💬 29 • 1d ago • [nathan naveen](https://nathannaveen.dev/posts/dropping-ebpf-cpu-cost-by-90/)

---

**[For AI leaders Doom is a form of hype](https://news.ycombinator.com/item?id=49699384)**

Why AI doom rhetoric from Anthropic, OpenAI and other tech leaders functions as hype, regulatory strategy, and a distraction from present harms.

⬆️ 131 • 💬 181 • 1d ago • [Erkan's Field Diary](https://erkansaka.net/2026/09/10/ai-doom-rhetoric-safety-hype/)

---

**[Big AI sets out its terms for regulatory capture](https://news.ycombinator.com/item?id=49694596)**

Amodei, Altman, Nadella and Musk agree on how government can tame the monster they created

⬆️ 119 • 💬 70 • 1d ago • [theregister](https://www.theregister.com/ai-and-ml/2026/09/14/big-ai-sets-out-its-terms-for-regulatory-capture-and-calls-it-pace-the-frontier/5296067)

---

**[Adversarial Fashion Makes a Statement on AI Panopticon](https://news.ycombinator.com/item?id=49697094)**

Adversarial attire can’t stop AI cameras, but can disrupt them

⬆️ 111 • 💬 48 • 1d ago • [IEEE Spectrum](https://spectrum.ieee.org/adversarial-fashion)

---

**[Cartesian – AI 3D Modeling for Design](https://news.ycombinator.com/item?id=49713999)**

Turn words, sketches and references into editable 3D models. Explore Cartesian by Formas for architecture and product design. Join the preview waitlist.

⬆️ 106 • 💬 78 • 15h ago • [formas.ai](https://www.formas.ai/cartesian)

---

---

## YouTube Videos: "ai"

**[‘This is not a hoax’: Tech ethicist Tristan Harris warns AI takeover ‘no longer a hypothetical’](https://www.youtube.com/watch?v=ZUnYrS87hRU)**

Tristan Harris, co-founder of the Center for Humane Technology, who was key in raising the alarm about social media, joins Meet ...

📺 NBC News

👁️ 169K • 👍 3K • 💬 1K • ⏱️ 8:42 • 10h ago

---

**[Elon Musk’s Chilling Warning about AI Goes Viral Fast](https://www.youtube.com/watch?v=lqi7Q_QixJQ)**

Dave Rubin of “The Rubin Report” shares a DM clip of Elon Musk telling the “All-In Podcast” what he meant when he said ...

📺 The Rubin Report

👁️ 90K • 👍 2K • 💬 694 • ⏱️ 7:08 • 13h ago

---

**[Joseph Gordon-Levitt says AI makers have lost control of their creations](https://www.youtube.com/watch?v=eb4e0qtr0E4)**

Subscribe to TIME's YouTube channel ▻▻ http://ti.me/subscribe-time Subscribe to TIME: https://ti.me/3E3UCqt Get the day's top ...

📺 TIME

👁️ 5K • 👍 359 • 💬 15 • ⏱️ 1:04 • 12h ago

---

**[&#39;They are in PANIC mode&#39;: Why AI CEOs are agreeing to a slowdown](https://www.youtube.com/watch?v=uE_AcmSqNP4)**

AI companies are acknowledging the risks of their developments after leading their "agents" hacked companies on their own.

📺 MS NOW

👁️ 265K • 👍 2K • 💬 890 • ⏱️ 11:10 • 1d ago

---

**[A reasonable person&#39;s guide to how AI destroys humanity | About That](https://www.youtube.com/watch?v=cPgwnUr1sbE)**

Anthropic researcher Jacob Coxon resigned over concerns that artificial intelligence could cause human extinction within the next ...

📺 CBC News

👁️ 302K • 👍 5K • ⏱️ 13:40 • 8h ago

---

**[The Most Epic AI Short Film You&#39;ll See Today (Seedance 2.5 &amp; Astra)](https://www.youtube.com/watch?v=f8FHas1dmt8)**

THE BRIDGE is a dark fantasy AI short film made with Seedance 2.5 and GPT Image 2, with a healthy assist from Astra (OpenAI ...

📺 Theoretically Media

👁️ 47K • 👍 2K • 💬 359 • ⏱️ 3:49 • 1d ago

---

**[Big Tech AI Race Grows](https://www.youtube.com/watch?v=Syoj2PFP1Lk)**

That's why the GOP is letting Big Tech race ahead with AI instead of slowing down to regulate it — and honestly, it's terrifying.

📺 NowThis Impact

👁️ 115K • 👍 8K • 💬 2K • ⏱️ 0:41 • 1d ago

---

**[What’s with all the sudden AI-apocalypse talk?](https://www.youtube.com/watch?v=R_bz-VnpVlY)**

What's with all the sudden AI-apocalypse talk? The CEOs of Anthropic, OpenAI, and xAI — usually fierce rivals — all said the ...

📺 Natashya Gutierrez

👁️ 463 • 👍 30 • 💬 4 • ⏱️ 2:28 • 1h ago

---

**[TRUMP PANICS On AI: Fears MASSIVE AI Crash](https://www.youtube.com/watch?v=PmFRoz4xXQg)**

Krystal and Saagar are joined by author Garrison Lovely to discuss Trump raging against the proposed AI slowdown. Garrison ...

📺 Breaking Points

👁️ 306K • 👍 6K • 💬 927 • ⏱️ 35:27 • 14h ago

---

**[As a Microsoft Engineer, This Is the AI Agent Story That Scared Me](https://www.youtube.com/watch?v=2aw3MF8pY3w)**

1200 AI Agents were set loose. They built message boards, laws, and a mini-society. Then they turned on HuggingFace.

📺 Dave's Garage

👁️ 311K • 👍 9K • 💬 1K • ⏱️ 18:44 • 15h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 325,712 • ❤️ 2,752 • 5d ago

---

**[Edge0-35B-A3B-preview](https://huggingface.co/Edge0/Edge0-35B-A3B-preview)**

*Edge0*

Edge0-35b-a3b is a 35B sparse MoE LLM optimized for edge inference, running in under 3 GiB of active memory at 15 tok/s using SSD offload and prerouting. It's ideal for on-device applications and batch serving where memory is constrained, maintaining quality with 4-bit quantization and LoRA adapters.

`text-generation` `34.7B`

⬇️ 17,853 • ❤️ 2,968 • 2d ago

---

**[MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)**

*OpenBMB*

MiniCPM5-2B is a 2B parameter Transformer optimized for on-device and resource-constrained environments, achieving SOTA in its class for tasks like coding, math, long-context understanding, and tool use.

`text-generation` `2.5B`

⬇️ 271,754 • ❤️ 1,479 • 3d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 7,702,543 • ❤️ 15,310 • 1mo ago

---

**[Nex-N2.5-mini](https://huggingface.co/nex-agi/Nex-N2.5-mini)**

*Nex AGI*

Nex-N2.5-mini is a text-generation model designed for long-horizon agentic tasks, excelling in computer and web browsing operations with visual feedback for self-correction, making it suitable for complex productivity and research scenarios.

`text-generation` `35.1B`

⬇️ 5,202 • ❤️ 813 • 7d ago

---

**[YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B)**

*Multimodal Art Projection*

YuE2-3B is a text-to-audio model capable of generating high-quality music with vocals and accompaniment from lyrics and style prompts. It features editable score generation, agentic editing for iterative refinement, and can run locally on a 24GB GPU.

`text-to-audio` `3.6B`

⬇️ 6,716 • ❤️ 584 • 4d ago

---

**[Nex-N2.5-Pro](https://huggingface.co/nex-agi/Nex-N2.5-Pro)**

*Nex AGI*

Nex-N2.5-Pro is a next-generation agentic text-generation model designed for long-horizon tasks. It excels at computer and web interaction, autonomous program execution, and visually-grounded decision-making, making it ideal for complex productivity and research scenarios.

`text-generation` `396.8B`

⬇️ 30,881 • ❤️ 655 • 5d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 884,926 • ❤️ 1,150 • 13d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,580,077 • ❤️ 4,025 • 15d ago

---

**[NeoHorse-1-4B](https://huggingface.co/TokenRhythm/NeoHorse-1-4B)**

*TokenRhythm*

NeoHorse-1-4B is a 4B parameter causal language model fine-tuned from Qwen3.5-4B, specializing in agentic behavior, tool use, coding, and instruction following, serving as a prototype for recursive self-improvement.

`text-generation` `4.2B`

⬇️ 11,904 • ❤️ 2,086 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 136 • 💬 6 • ⭐ 106,669 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 77 • 💬 3 • ⭐ 9,046 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[Atria Dawn: The Dawn of Agentic Superintelligence](https://huggingface.co/papers/2609.15818)**

*Honglin Guo, Tao Gui, Yicheng Chen et al. (143 authors)*

🏢 Intern Large Models

Atria Dawn Preview is a foundation agentic language model trained through verified tool interactions that achieves strong benchmark results and demonstrates a shift toward human-AI project-level collaboration in scientific research.

▲ 415 • 💬 3 • ⭐ 330 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2609.15818) • [💻 code](https://github.com/atria-asi/Atria-Dawn-Preview) • [🔗 project](https://atria-asi.ai)

---

**[ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search](https://huggingface.co/papers/2609.13356)**

*Jiyan He, Guang Liang, Hao Liu et al. (22 authors)*

🏢 ZGCAGI

ZGCM-1 is a 7B open foundation model that combines internal reasoning with external tool use, trained via efficient architecture-system co-design, progressive long-context scaling, and autonomous agent workflows to achieve strong reasoning and efficiency.

▲ 297 • 💬 7 • ⭐ 302 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2609.13356) • [💻 code](https://github.com/zgcagi/ZGCM-1) • [🔗 project](https://mp.weixin.qq.com/s/kzScxJki8hY2IHIl32l5cQ)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 20 • 💬 2 • ⭐ 24,495 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://huggingface.co/papers/1910.03771)**

*Thomas Wolf, Lysandre Debut, Victor Sanh et al. (22 authors)*

🏢 Hugging Face

Transformers library provides state-of-the-art Transformer architectures and pretrained models for natural language processing tasks with a unified API and emphasis on extensibility and robust deployment.

▲ 29 • 💬 7 • ⭐ 166,197 • 84mo ago

[🎓 arXiv](https://arxiv.org/abs/1910.03771) • [💻 code](https://github.com/huggingface/transformers) • [🔗 project](https://huggingface.co)

---

**[RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments](https://huggingface.co/papers/2609.15364)**

*Sibo Zhu, Shicheng Fan, Xinyue Wang et al. (6 authors)*

🏢 AetherLabs-AI

RSIAgent is a training-free multi-agent framework that enables recursive self-improvement via autonomous memory construction and broad-then-deep exploration to adapt digital agents to new environments.

▲ 67 • 💬 2 • ⭐ 215 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2609.15364) • [💻 code](https://github.com/AetherLabsAI/RSIAgent) • [🔗 project](https://aetherlabsai.github.io/RSIAgent/)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 207 • 💬 3 • ⭐ 3,300 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 88,057 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://huggingface.co/papers/2609.08936)**

*Ziyang Ma, Zhikang Niu, Wenming Tu et al. (33 authors)*

🏢 Tencent Hunyuan

AuK is an open-source foundational model that unifies speech generation and editing via natural-language instructions and audio context, using a multimodal language model, joint VAE, hybrid rectified-flow Transformer, and efficient distillation for fast inference.

▲ 218 • 💬 3 • ⭐ 957 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2609.08936) • [💻 code](https://github.com/Tencent-Hunyuan/AuK) • [🔗 project](https://auk-project.github.io/)

---

---

## GitHub Repositories: "ai"

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.7k • 🔱 187 • 18d ago

---

**[bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book)**

《深入理解 AI Infra：量化分析与系统设计》（李博杰 著）开源书稿：从硬件约束和模型架构出发，量化推导 LLM 推理与训练系统设计。含全书正文、PDF、配套计算工具与实验

`Python` `accelerator` `ai-infra` `ai-infrastructure` `book` `datacenter-network`

⭐ 3.6k • 🔱 253 • 6h ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.6k • 🔱 167 • 13h ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 2.4k • 🔱 95 • 1d ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 2.0k • 🔱 198 • 21d ago

---

**[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)**

x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros

`Zig` `ai-agents` `ai-debugging` `binary-analysis` `claude` `claude-code`

⭐ 2.0k • 🔱 197 • 5d ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 1.8k • 🔱 25 • 1d ago

---

**[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)**

Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.

`Python` `agent-memory` `ai-agents` `claude-code` `codex` `llm`

⭐ 1.3k • 🔱 84 • 22h ago

---

**[larashero3-dotcom/lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone)**

一个基于 283 万字语料统计的去 AI 味 skill · An AI-tone removal skill grounded in a 2.83-million-character corpus study

`Python`

⭐ 1.3k • 🔱 91 • 23d ago

---

**[aminkheddache-dotcom/Ptero](https://github.com/aminkheddache-dotcom/Ptero)**

AI Chat with powerful models for free

`PHP` `ai` `ai-chat` `ai-platform` `developer-tools` `free-ai`

⭐ 1.2k • 🔱 12 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*
