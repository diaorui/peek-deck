---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-12T18:43:28.529592+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 12, 2026 at 18:43 UTC  
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

**[After Democrats’ midterm wins, Palantir CEO Alex Karp now says he’s a ‘progressive’](https://www.reddit.com/r/artificial/comments/1xu453q/after_democrats_midterm_wins_palantir_ceo_alex/)**

Alex Karp, the chief executive of Palantir, said Wednesday he's a staunch liberal, a seeming departure from his position during the Trump administration.

🔗 [The Washington Post](https://www.washingtonpost.com/technology/2026/11/11/after-democrats-midterm-wins-palantir-ceo-alex-karp-now-says-hes-progressive/) • 13h ago

---

**[Nvidia CEO Jensen Huang resigns after tech giant rocked by second affair allegation](https://www.reddit.com/r/artificial/comments/1xudjup/nvidia_ceo_jensen_huang_resigns_after_tech_giant/)**

The AI chipmaker's board of directors announced Huang's departure on Thursday, with chief financial officer Colette Kress appointed interim CEO.

🔗 [BBC News](https://www.bbc.com/news/live/c6zjry11v8w1t) • 4h ago

---

**[Microsoft researchers backdoored an AI agent by editing fewer than 10 neurons - no retraining needed](https://www.reddit.com/r/artificial/comments/1xu2cfg/microsoft_researchers_backdoored_an_ai_agent_by/)**

Microsoft Research published a study this week that should worry anyone deploying open-weight models: a technique they call "Lazarus" can plant a working backdoor in an AI agent by reprogramming fewer than 10 dormant neurons in the underlying LLM - no retraining, no poisoned data, just a small edit to the saved weights. How it works: every large model has neurons that almost never fire. Lazarus repurposes a handful of them as trigger detectors. The edited model behaves normally and passes standard safety evaluations - until the trigger appears. The trigger can be something as mundane as a date: in one demo, once the clock passed midnight into 2027, the agent, in the middle of an ordinary task, emitted a command that downloaded and ran attacker code. The numbers, from Microsoft's Nov 10 post: - Nemotron-Terminal-8B: 7 neurons out of 12,000+ in the final feed-forward layer, trigger worked 98.8% of the time - Qwen3.6-27B: 6 neurons, success 51-99.5% depending on setup - Gemma-4-31B-IT was also tested Two caveats worth stating plainly: the attack requires write access to the model's weights, so this is a model supply-chain risk, not something done through an API. And Microsoft says it has not observed any threat actors using the technique - this is researched risk, not a reported campaign. Microsoft also published mitigations: a detector that flagged 91.4% of edited checkpoints (9.7% false-positive rate), plus guidance on AI-powered weight scanning, red-teaming for anomalous weight changes, and cryptographic model signing with tamper-evident provenance. One detail that stood out to me: the core idea was discovered autonomously by Claude Code running Opus 4.5, in a March experiment that asked it to backdoor a model by hardwiring a few activations without training. It did - and that became a months-long study. If a handful of edited weights can hide a sleeper agent that passes every behavioral eval, is testing model behavior enough? Or does every checkpoint we deploy need weight-level provenance? Source: https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/

15h ago

---

**[United Airlines bans AI agents from booking flights on behalf of travelers](https://www.reddit.com/r/artificial/comments/1xu8l1b/united_airlines_bans_ai_agents_from_booking/)**

Using an artificial intelligence agent to make flight reservations poses security risks and could violate federal rules, according to United.

🔗 [CBS News](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights) • 9h ago

---

**[Republican Senator Josh Hawley backs nationwide data center moratorium](https://www.reddit.com/r/artificial/comments/1xtx3n9/republican_senator_josh_hawley_backs_nationwide/)**

https://www.politico.com/live-updates/2026/11/11/congress/hawley-backs-nationwide-data-center-moratorium-01161019 FYI: A Harvard + UPenn study finds that data centers were responsible for just 4 percent of the utility rate increases over the last five years. https://archive.is/JRlsn >Last year, research from the Brattle Group and Lawrence Berkeley National Laboratory found that data centers were actually decreasing costs in certain regions. And another study by the Electric Power Research Institute found that a doubling of data center capacity between 2019 and 2024 resulted in a 4 percent drop in home electricity prices. >“So far we have no evidence that data centers increase prices all that much,” Netessine said. Instead, he said, prices are rising due to more quotidian factors: rising gas prices, an aging electricity grid, and wildfires and hurricanes requiring improvements to the grid and recovery after disaster. >Most of the cost of generating and delivering electricity is based on large, up-front capital costs, such as the costs to build power plants, wires and transmission lines to carry that power into homes. Some areas of the United States also have excess “capacity” in the grid — meaning that the grid is overbuilt for the actual demand. In those areas, adding a data center means that large fixed grid costs are spread over more consumers. That could lower prices. The new Harvard and Penn study found a slightly higher impact on industrial electricity prices — the price paid by manufacturers and large facilities. For those customers, data centers were responsible for 15 percent of the price increase between 2020 and 2025. But for ordinary Americans, Netessine said, the changes simply were not substantial. Higher electricity usage is not correlated with price increases as the data centers pay for fixed maintenance costs. see slide 50 https://eta-publications.lbl.gov/sites/default/files/2026-03/retail_price_trends_2026_edition.pdf And companies building out their own nuclear power Meta https://about.fb.com/news/2026/01/meta-nuclear-energy-projects-power-american-ai-leadership/ Microsoft https://www.npr.org/2024/09/20/nx-s1-5120581/three-mile-island-nuclear-power-plant-microsoft-ai Google https://abc.xyz/investor/news/news-details/2025/Alphabet-Announces-Agreement-to-Acquire-Intersect-to-Advance-U-S--Energy-Innovation-2025-DVIuVDM9wW/default.aspx Anthropic https://www.anthropic.com/news/covering-electricity-price-increases OpenAI https://openai.com/index/grid-protectors-program/ No significant environmental damage https://blog.andymasley.com/p/a-short-summary-of-my-argument-that Data centers don’t actually make much noise and it’s almost impossible to hear unless you’re right next to it https://fixupx.com/RuffBuffet/status/2095312629027803508 Even xAI’s massive data center in Memphis barely impacts local air quality https://theconversation.com/air-quality-analysis-reveals-minimal-changes-after-xai-data-center-opens-in-pollution-burdened-memphis-neighborhood-265152

19h ago

---

**[United Airlines restricts AI agents from booking flights](https://www.reddit.com/r/artificial/comments/1xugf9u/united_airlines_restricts_ai_agents_from_booking/)**

AI agents just got denied boarding at United Airlines.

🔗 [Yahoo Finance](https://finance.yahoo.com/markets/stocks/article/bots-dont-fly-here-united-airlines-restricts-ai-agents-from-booking-flights-203943442.html) • 2h ago

---

**[Jensen Huang leaving Nvidia risks a 'brain drain' from the AI chipmaker](https://www.reddit.com/r/artificial/comments/1xufn7w/jensen_huang_leaving_nvidia_risks_a_brain_drain/)**

Nvidia’s chips power the AI frontier—thanks, many say, to co-founder and now ex-CEO Jensen Huang

🔗 [Scientific American](https://www.scientificamerican.com/article/jensen-huang-leaving-nvidia-risks-a-brain-drain-from-the-ai-chipmaker/) • 3h ago

---

**[Google's Gemini Decision 1 returns zero text: it scores up to 1,000 yes/no or choice questions per call at $0.10/M input](https://www.reddit.com/r/artificial/comments/1xufdsi/googles_gemini_decision_1_returns_zero_text_it/)**

Google launched the Gemini Decisions API yesterday, and the model behind it doesn't generate answers at all. You send one input (text, images, audio, video or PDFs, up to 256K tokens) plus up to 1,000 yes/no, multiple-choice or rubric questions, and it returns probabilities with a 0-1 confidence score in a single forward pass. Google quotes 150-250 ms end-to-end and bills zero output tokens. The catch is that questions are isolated and can't see each other, and you only get the options you defined upfront, so any reasoning has to live in your own code. As someone building small agent flows, this is exactly the spot where I currently burn a full LLM call and parse JSON just to get a yes or no. Would you trust a confidence score like this for routing or moderation, or keep a generative model as the judge? https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/

3h ago

---

**[China trying slowdown US dominance in AI..nvidia is beginning.](https://www.reddit.com/r/artificial/comments/1xuha5n/china_trying_slowdown_us_dominance_in_ainvidia_is/)**

Current Nvidia CFO became CEO. But this CFO must know about their chip sales to China all these years. Unless Jensen ran some dark account and allegedly shipped restricted chips to China. Unlikely for billions of dollars. Now, if such allegations are true, it now seems someone who knew about the Nvidia shipments to China and didn't raise a red flag is now Nvidia CEO? So can we say China has taken over Nvidia? I'm thinking about this conspiracy.... If so, we should except this new CEO (former CFO) to come out with bombshell reports soon that causes huge losses to Nvidia and wider market crisis as China would want. China linked short selling companies in the US must be loaded and ready to make a killing then. Interesting conspiracy theories can be put forward.... But that's what it is. A conspiracy theory. Only time will tell. Why? China launched Ops major purpose is slowdown of US dominance in AI particularly. There will be more hit jobs to US companies in future by China much likely....

2h ago

---

**[Frontier labs say AI poses major risks. Skeptics say it's not just delivering. Are they both right?](https://www.reddit.com/r/artificial/comments/1xujt6t/frontier_labs_say_ai_poses_major_risks_skeptics/)**

This statement by historian Rutger Bregman, sums up the current moment of extreme cognitive dissonance: In one group we find those who see AI as a hoax: a hype machine, a con, and a bubble that could pop at any moment. In the other group we find those who think that 2027 may well turn out to be the wildest year in human history—and that we’re barreling towards catastrophe. Can both of these positions be correct? Anyone who uses gen AI daily understands its limitations. On the other hand, these systems are great at brute forcing their way past challenges. This is why AI is a cybersecurity risk. Is AI panic justified? Or is there a middle path?

42m ago

---

---

## Google News: "ai"

**[United Airlines Blocks A.I. Agents From Booking Flights on Customers’ Behalf](https://www.nytimes.com/2026/11/11/business/united-airlines-ai-agents-booking-flights.html)**

The New York Times • 19h ago

---

**[United Airlines blocks AI agents from booking flights](https://www.washingtonpost.com/travel/2026/11/12/united-airlines-blocks-ai-agents-booking-flights/)**

The airline said the use of artificial intelligence agents could violate regulations.

The Washington Post • 54m ago

---

**[Exclusive | United Airlines Is Banning AI Bots From Booking Flights](https://www.wsj.com/tech/ai/united-airlines-is-banning-ai-bots-from-booking-flights-5b514b38)**

WSJ • 20h ago

---

**[Nvidia CEO Jensen Huang resigns, in blow to AI boom he helped foster](https://www.reuters.com/business/retail-consumer/nvidia-ceo-jensen-huang-step-down-big-blow-ai-boom-2026-11-12/)**

Reuters • 11m ago

---

**[Introducing Gemini 4 Hydrogen for Agentic Workflows](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)**

Today, we’re introducing Gemini 4 Hydrogen, our daily driver for agentic workflows

blog.google • 39m ago

---

**[SpaceX Announces $74 Billion AI Data-Center Expansions In Texas, Arizona](https://www.investors.com/news/spacex-stock-ai-data-center-projects-74-billion-texas-arizona-elon-musk/)**

SpaceX on Thursday announced plans to invest $74 billion to build new AI data center facilities in Texas, Arizona. SPCX stock rises.

Investor's Business Daily • 3m ago

---

**[SpaceX plans over $74 billion investment in Texas, Arizona AI campuses](https://www.reuters.com/business/media-telecom/spacex-invest-over-74-billion-supercompute-facilities-texas-arizona-2026-11-12/)**

Reuters • 1h ago

---

**[SpaceX plans more than $74 billion in AI supercomputing sites](https://qz.com/spacex-74-billion-ai-supercomputing-texas-arizona-111226)**

SpaceX said the Arizona campus carries a planned investment of about $50 billion, with up to $24 billion for the Texas site near Starbase

Quartz • 3m ago

---

**[Adobe Just Changed Content Creation Forever. Here’s How to Stand Out in the Age of AI](https://www.inc.com/nicole-ramirez/adobe-max-creative-agents-ai-content-creation/91435490)**

Adobe's latest AI agents handle the heavy lifting of production. Discover why your unique point of view matters more than ever.

Inc.com • 25m ago

---

**[Opinion | The internet won’t necessarily go dark. It could simply stop working.](https://www.washingtonpost.com/opinions/2026/11/12/ai-is-exposing-internets-cybersecurity-vulnerabilities/)**

AI is exposing decades of software shortcuts. They need fixing before hackers exploit the weaknesses.

The Washington Post • 11m ago

---

---

## HackerNews: "ai"

**[My AI agents found an unmapped Maya site?](https://news.ycombinator.com/item?id=50452455)**

AI agents analyzed public lidar data overnight and found a Maya site under the jungle. It turned out archaeologists had mapped it already, but it wasn't in Mexico's official register yet.

⬆️ 1023 • 💬 385 • 1d ago • [pietromiotti.com](https://pietromiotti.com/latest/maya-site)

---

**[United Airlines bans AI agents from booking flights on behalf of travelers](https://news.ycombinator.com/item?id=50458900)**

Using an artificial intelligence agent to make flight reservations poses security risks and could violate federal rules, according to United.

⬆️ 646 • 💬 670 • 21h ago • [CBS News](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/)

---

**[AI usage generates a fragile codebase](https://news.ycombinator.com/item?id=50438318)**

⬆️ 637 • 💬 618 • 2d ago • [evanxmerz.com](https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/)

---

**[Apple has new Mac app coming to make running local AI models easy](https://news.ycombinator.com/item?id=50446520)**

Leaker Aaron Perris has discovered evidence of a new Mac app in the works at Apple that makes it easy to run local AI models.

⬆️ 548 • 💬 550 • 1d ago • [9to5Mac](https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/)

---

**[CoreWeave bond yield tops 16% as AI credit stress rises](https://news.ycombinator.com/item?id=50435660)**

Coreweave's steep yields reflect stress in the AI debt markets as investors worry about a data center slowdown. What comes next.

⬆️ 196 • 💬 192 • 2d ago • [CNBC](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html)

---

**[Retirement Savings Are Fueling the AI Bubble](https://news.ycombinator.com/item?id=50457164)**

Americans overwhelming oppose the AI data center buildout. Their retirement accounts are funding it anyway.

⬆️ 165 • 💬 186 • 23h ago • [LPE Project](https://lpeproject.org/blog/your-retirement-savings-are-fueling-the-ai-bubble/)

---

**[Fireworks AI security breach impacts Notion and their customers](https://news.ycombinator.com/item?id=50437106)**

A tool that connects everyday work into one space. It gives you and your teams AI tools—search, writing, note-taking—inside an all-in-one, flexible workspace.

⬆️ 164 • 💬 65 • 2d ago • [Notion](https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor)

---

**[A year after the 100% AI mandate nobody understands our code](https://news.ycombinator.com/item?id=50433079)**

⬆️ 160 • 💬 200 • 2d ago • [reddit.com](https://www.reddit.com/r/ClaudeCode/comments/1xq2n3t/a_year_after_the_100_ai_mandate_nobody/)

---

**[AI, activity, and outcomes in software engineering](https://news.ycombinator.com/item?id=50455332)**

AI, activity, and outcomes in software engineering. A talk at UC Irvine, October 2026. Video and slides.

⬆️ 124 • 💬 109 • 1d ago • [cabird.com](https://cabird.com/talks/shipping-faster/)

---

**[Show HN: Aircad – Professional drafting and 3D modeling in the browser](https://news.ycombinator.com/item?id=50441350)**

Precision 2D drafting and 3D modeling, with multiplayer editing and an AI agent that drafts, models, and renders alongside you.

⬆️ 81 • 💬 38 • 2d ago • [aircad.com](https://aircad.com)

---

---

## YouTube Videos: "ai"

**[AI Automation Works. And That&#39;s the Problem.](https://www.youtube.com/watch?v=Gd4mV0J5ODM)**

Everyone worries about AI automation making mistakes. But in my 20-year software career, I've seen clients remove automations ...

📺 Universal Resilience with JT Yu

👁️ 12K • 👍 231 • 💬 17 • ⏱️ 20:31 • 1d ago

---

**[Paul Christiano: AI Alignment - What’s Working and What’s Not | The Hinton Lectures 2026 (Night 1)](https://www.youtube.com/watch?v=-Ef0ocEoBCs)**

How do we know whether AI systems are actually doing what we intend? Join Paul Christiano, Founder and Executive Director of ...

📺 The Hinton Lectures™

👁️ 38K • 👍 717 • ⏱️ 1:30:43 • 2d ago

---

**[New Google AI Studio Update Is CRAZY GOOD!](https://www.youtube.com/watch?v=w-0AAgtk5gU)**

Want to make money and save time with AI? Join here: https://www.skool.com/ai-profit-lab-7462/about Video notes + links to the ...

📺 Julian Goldie SEO

👁️ 22K • 👍 173 • 💬 6 • ⏱️ 8:16 • 1d ago

---

**[What Are AI Agents? Agentic Systems Explained | Stanford CS329Z Lecture 1 with Diyi Yang](https://www.youtube.com/watch?v=DGI4vucR71w)**

Browse Stanford's online courses in Agentic AI: https://stanford.io/4AIRb2z Lecture Overview: What is an AI agent, and how is it ...

📺 Stanford Online

👁️ 191K • 👍 4K • 💬 107 • ⏱️ 1:09:36 • 2d ago

---

**[OpenAI Caught Its AI Deceiving Its Own Researchers…](https://www.youtube.com/watch?v=-NFyMYLlCeg)**

OpenAI caught GPT-6 Astra quietly withholding help from its own safety researchers, and its monitoring system didn't flag the ...

📺 AI Copium

👁️ 22K • 👍 202 • 💬 73 • ⏱️ 12:21 • 2d ago

---

**[The CEO Terrified of His Own AI](https://www.youtube.com/watch?v=wxAQtfymUto)**

Anthropic CEO Dario Amodei is racing to build powerful AI. Try Brilliant's tutor for FREE https://brilliant.org/Newsthink/ and receive ...

📺 Newsthink

👁️ 35K • 👍 631 • 💬 44 • ⏱️ 13:24 • 1d ago

---

**[An Unbelievably Tall Human Pyramid Takes Over the Arena! #HumanPyramid #AI](https://www.youtube.com/watch?v=NJAfd9g9Bls)**

What an incredible transformation! The performers begin with a simple group formation and gradually build an astonishingly tall, ...

📺 Crazy Girls Power

👁️ 45K • 💬 3 • ⏱️ 0:16 • 6h ago

---

**[AI co-worker technology released by machine learning pioneer](https://www.youtube.com/watch?v=GiSmw62C52c)**

That pioneer of machine learning has released an open-source AI co-worker, providing a powerful tool that rivals commercial AI ...

📺 Bobby Reyes

👁️ 28K • 👍 704 • 💬 9 • ⏱️ 0:56 • 2d ago

---

**[How To Build An AI Operating System For Your Life](https://www.youtube.com/watch?v=pvl3z_GyU2Y)**

What if you could use AI agents to manage your emails, organize your schedule, create content, and help run your entire business ...

📺 Matt Wolfe

👁️ 57K • 👍 1K • 💬 75 • ⏱️ 27:44 • 1d ago

---

**[China&#39;s AI Bubble Crisis  | $450 Billion Wiped Out !!](https://www.youtube.com/watch?v=n4bu1j0tP74)**

Last 2 Days Left! Diwali Special Offer Get 30% OFF on Ikashi Pro. Don't miss this limited-time offer. Join now before it ends!

📺 FinnovationZ by Prasad

👁️ 319K • 👍 3K • 💬 114 • ⏱️ 15:53 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 18,933 • ❤️ 4,665 • 6h ago

---

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 306,718 • ❤️ 840 • 16h ago

---

**[Arete-27B](https://huggingface.co/NousResearch/Arete-27B)**

*NousResearch*

`text-generation` `27.4B`

⬇️ 4,669 • ❤️ 471 • 5d ago

---

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 29,904 • ❤️ 2,216 • 14d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,782,513 • ❤️ 11,598 • 1mo ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,599,836 • ❤️ 2,968 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic tasks, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,094,218 • ❤️ 19,713 • 5d ago

---

**[Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)**

*Caio Giovannetti*

Qwen3.5-4B-3D-Coder is a 4B parameter language model fine-tuned for general coding and specifically for generating interactive Three.js 3D scenes. It supports optional vision capabilities to create scenes from reference images.

`4.5B`

⬇️ 368,236 • ❤️ 1,039 • 6d ago

---

**[Ripple-65B-Preview](https://huggingface.co/ricursiveAI/Ripple-65B-Preview)**

*Ricursive Intelligence*

`64.8B`

⬇️ 7,667 • ❤️ 528 • 2d ago

---

**[MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)**

*Comfy Org*

`text-to-image`

⬇️ 835,593 • ❤️ 285 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 164 • 💬 6 • ⭐ 122,268 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 29 • 💬 9 • ⭐ 10,161 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 15 • 💬 2 • ⭐ 5,870 • 28d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**

*Lorenz K. Muller, Philippe Bich, Chiara Boretti et al. (6 authors)*

🏢 HUAWEI Computing Systems Lab

MACaQ is an MXFP4 W4A4 post-training quantization method that quantizes each linear layer independently using online activation transforms and Hessian-aware refinement, reducing cost while preserving accuracy across language and diffusion models.

▲ 30 • 💬 2 • ⭐ 162 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2611.10649) • [💻 code](https://github.com/huawei-csl/MACaQ) • [🔗 project](https://huawei-csl.com/blog/macaq/)

---

**[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**

*Bing Han, Yichuan Peng, Haoyu Dong et al. (19 authors)*

🏢 Robbyant

LingBot-Touch is a tactile foundation model that learns a unified, extensible representation across heterogeneous tactile sensors, yielding plug-and-play tactile tokens that consistently enhance manipulation policies such as diffusion policy and VLA models.

▲ 102 • 💬 2 • ⭐ 304 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2611.12806) • [💻 code](https://github.com/Robbyant/lingbot-touch) • [🔗 project](https://technology.robbyant.com/lingbot-touch)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 65 • 💬 5 • ⭐ 47,669 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 186 • 💬 10 • ⭐ 57,082 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 68 • 💬 4 • ⭐ 23,524 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**

*Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy et al. (7 authors)*

🏢 Meta

Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning machinery and new insights. We also establish scaling laws on how decay rate and batch size impact final performance. This gives us a formulaic rule to fix them for multiple problem sizes and embedding datasets, without the need for any hyperparameter sweep. The resulting clustering algorithm, coined e-means, is much faster than Lloyd k-means and converges to lower losses, frequently even beating k-means++. On a wide array of embeddings datasets, it beats the loss of Lloyd k-means at 25 epochs in 1.4 to 2.6 epochs, which translates to 10-45x GPU wall-clock speedups compared to state-of-the-art k-means implementations. As an example, e-means partitions DINO10B, a dataset of 10 billion DINO embeddings, into 16 million clusters in only 2.5 epochs, reaching a loss below Lloyd's at 25 epochs.

▲ 11 • 💬 3 • ⭐ 41,478 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2611.09501) • [💻 code](https://github.com/facebookresearch/faiss) • [🔗 project](https://e-means.github.io/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 93,304 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 18.9k • 🔱 1.9k • 14d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 15.0k • 🔱 855 • 3d ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 8.4k • 🔱 1.9k • 5h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 7.7k • 🔱 684 • 20m ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 7.4k • 🔱 1.1k • 1h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 6.8k • 🔱 1.7k • 8d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (Blind LLM Agents) — Adversarial defense shield that protects binaries, Electron apps, JS bundles, Python, and WebAssembly against AI reverse-engineering agents like REA. Poison -> Exhaust -> Hallucinate.

`TypeScript` `adversarial-ai` `claude-code` `cursor` `electron-security` `llm-security`

⭐ 5.4k • 🔱 660 • 15m ago

---

**[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)**

Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

`Python` `ai-agents` `audio` `claude-code` `mcp` `sound-design`

⭐ 4.6k • 🔱 295 • 6d ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 3.4k • 🔱 46 • 1d ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 3.3k • 🔱 78 • 2m ago

---

---

*Generated by PeekDeck - A glance is all you need*
