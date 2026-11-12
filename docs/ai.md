---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-12T10:43:04.272465+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 12, 2026 at 10:43 UTC  
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

🔗 [The Washington Post](https://www.washingtonpost.com/technology/2026/11/11/after-democrats-midterm-wins-palantir-ceo-alex-karp-now-says-hes-progressive/) • 5h ago

---

**[Microsoft researchers backdoored an AI agent by editing fewer than 10 neurons - no retraining needed](https://www.reddit.com/r/artificial/comments/1xu2cfg/microsoft_researchers_backdoored_an_ai_agent_by/)**

Microsoft Research published a study this week that should worry anyone deploying open-weight models: a technique they call "Lazarus" can plant a working backdoor in an AI agent by reprogramming fewer than 10 dormant neurons in the underlying LLM - no retraining, no poisoned data, just a small edit to the saved weights. How it works: every large model has neurons that almost never fire. Lazarus repurposes a handful of them as trigger detectors. The edited model behaves normally and passes standard safety evaluations - until the trigger appears. The trigger can be something as mundane as a date: in one demo, once the clock passed midnight into 2027, the agent, in the middle of an ordinary task, emitted a command that downloaded and ran attacker code. The numbers, from Microsoft's Nov 10 post: - Nemotron-Terminal-8B: 7 neurons out of 12,000+ in the final feed-forward layer, trigger worked 98.8% of the time - Qwen3.6-27B: 6 neurons, success 51-99.5% depending on setup - Gemma-4-31B-IT was also tested Two caveats worth stating plainly: the attack requires write access to the model's weights, so this is a model supply-chain risk, not something done through an API. And Microsoft says it has not observed any threat actors using the technique - this is researched risk, not a reported campaign. Microsoft also published mitigations: a detector that flagged 91.4% of edited checkpoints (9.7% false-positive rate), plus guidance on AI-powered weight scanning, red-teaming for anomalous weight changes, and cryptographic model signing with tamper-evident provenance. One detail that stood out to me: the core idea was discovered autonomously by Claude Code running Opus 4.5, in a March experiment that asked it to backdoor a model by hardwiring a few activations without training. It did - and that became a months-long study. If a handful of edited weights can hide a sleeper agent that passes every behavioral eval, is testing model behavior enough? Or does every checkpoint we deploy need weight-level provenance? Source: https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/

7h ago

---

**[Republican Senator Josh Hawley backs nationwide data center moratorium](https://www.reddit.com/r/artificial/comments/1xtx3n9/republican_senator_josh_hawley_backs_nationwide/)**

https://www.politico.com/live-updates/2026/11/11/congress/hawley-backs-nationwide-data-center-moratorium-01161019 FYI: A Harvard + UPenn study finds that data centers were responsible for just 4 percent of the utility rate increases over the last five years. https://archive.is/JRlsn >Last year, research from the Brattle Group and Lawrence Berkeley National Laboratory found that data centers were actually decreasing costs in certain regions. And another study by the Electric Power Research Institute found that a doubling of data center capacity between 2019 and 2024 resulted in a 4 percent drop in home electricity prices. >“So far we have no evidence that data centers increase prices all that much,” Netessine said. Instead, he said, prices are rising due to more quotidian factors: rising gas prices, an aging electricity grid, and wildfires and hurricanes requiring improvements to the grid and recovery after disaster. >Most of the cost of generating and delivering electricity is based on large, up-front capital costs, such as the costs to build power plants, wires and transmission lines to carry that power into homes. Some areas of the United States also have excess “capacity” in the grid — meaning that the grid is overbuilt for the actual demand. In those areas, adding a data center means that large fixed grid costs are spread over more consumers. That could lower prices. The new Harvard and Penn study found a slightly higher impact on industrial electricity prices — the price paid by manufacturers and large facilities. For those customers, data centers were responsible for 15 percent of the price increase between 2020 and 2025. But for ordinary Americans, Netessine said, the changes simply were not substantial. Higher electricity usage is not correlated with price increases as the data centers pay for fixed maintenance costs. see slide 50 https://eta-publications.lbl.gov/sites/default/files/2026-03/retail_price_trends_2026_edition.pdf And companies building out their own nuclear power Meta https://about.fb.com/news/2026/01/meta-nuclear-energy-projects-power-american-ai-leadership/ Microsoft https://www.npr.org/2024/09/20/nx-s1-5120581/three-mile-island-nuclear-power-plant-microsoft-ai Google https://abc.xyz/investor/news/news-details/2025/Alphabet-Announces-Agreement-to-Acquire-Intersect-to-Advance-U-S--Energy-Innovation-2025-DVIuVDM9wW/default.aspx Anthropic https://www.anthropic.com/news/covering-electricity-price-increases OpenAI https://openai.com/index/grid-protectors-program/ No significant environmental damage https://blog.andymasley.com/p/a-short-summary-of-my-argument-that Data centers don’t actually make much noise and it’s almost impossible to hear unless you’re right next to it https://fixupx.com/RuffBuffet/status/2095312629027803508 Even xAI’s massive data center in Memphis barely impacts local air quality https://theconversation.com/air-quality-analysis-reveals-minimal-changes-after-xai-data-center-opens-in-pollution-burdened-memphis-neighborhood-265152

11h ago

---

**[Anthropic says a key AI safety alarm has been triggered, days before its IPO](https://www.reddit.com/r/artificial/comments/1xtr9oc/anthropic_says_a_key_ai_safety_alarm_has_been/)**

Anthropic's new IPO filing says AI is now accelerating its own research to the point that it's triggering one of the company's key safety alarms.

🔗 [Yahoo Finance](https://finance.yahoo.com/markets/article/anthropic-says-a-key-ai-safety-alarm-has-been-triggered-days-before-its-ipo-171519615.html) • 15h ago

---

**[United Airlines bans AI agents from booking flights on behalf of travelers](https://www.reddit.com/r/artificial/comments/1xu8l1b/united_airlines_bans_ai_agents_from_booking/)**

Using an artificial intelligence agent to make flight reservations poses security risks and could violate federal rules, according to United.

🔗 [CBS News](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights) • 1h ago

---

**[GPU Companies built everything on the back of gamers, and now gamers cannot afford them.](https://www.reddit.com/r/artificial/comments/1xtbbsx/gpu_companies_built_everything_on_the_back_of/)**

I mean yeah, I am making this post frustrated with the current pricing of hardware, but ai companies are standing on hardware which mostly gamers bought and paid for. The evolution happened because of us. You might think what's this dude on about, it was made for graphical processing, Guess what?! It was games that required that level of graphical processing in those times. When Nvidia coined the term "GPU" and released the GeForce 256 in 1999, their primary goal was to run PC games like Quake III Arena and Unreal at smoother frame rates and higher resolutions than a standard CPU could ever manage. Video games were the only consumer software demanding millions of mathematical calculations per second to draw images on a monitor. Now we have the audacity to say RAM and GPU are being wasted on personal gaming rigs. I mean the only person who had more than 8 gigs of ram was either editing videos or playing games, games mostly though. I mean the AI demand will make sure the prices never go back to dirt cheap but in India (I am from India) gaming always has been a luxury, but now it's a luxury all over the world. When I was child, I dreamed of building the best gaming rig with my adult money, now when I am one, the prices are like "f\\k you". P.S. The gaming community has these posts everyday with everyone frustrated and i was asked to post this here, This is an honest question to the leaders and pioneers of AI technology, I mean I would love to understand the view points of everyone. I aint hating, but I realise when something is over evaluated and not worth the money its printed on.

1d ago

---

**[Manus scrapped traditional coding interviews and cut engineer hiring to half its peak; PMs now write code](https://www.reddit.com/r/artificial/comments/1xu7wfm/manus_scrapped_traditional_coding_interviews_and/)**

Manus has eliminated the traditional coding interview stage in its hiring process, according to the report. Engineer hiring at the company has fallen to half of its peak level, and product managers have started writing code directly. The three changes together suggest a shift in how an AI-native company defines who writes code and how it evaluates engineers.

1h ago

---

**[UK companies scale back hiring due to overspending on AI](https://www.reddit.com/r/artificial/comments/1xtmy87/uk_companies_scale_back_hiring_due_to/)**

Businesses in the UK incur £3.8 billion annually in technology infrastructure overspend, with the biggest culprit being AI spending.

🔗 [HotMinute](https://hotminute.co.uk/2026/11/11/uk-companies-scale-back-hiring-due-to-overspending-on-ai/) • 17h ago

---

**[AI agents are becoming software buyers, and businesses aren't ready](https://www.reddit.com/r/artificial/comments/1xtdzxd/ai_agents_are_becoming_software_buyers_and/)**

🔗 [inc.com](https://www.inc.com/hillary-remy/selling-ai-agents-startup-founders-bots-buying-software/91430588) • 1d ago

---

**[Powerful open source/open wight AI recommendations](https://www.reddit.com/r/artificial/comments/1xu6r3y/powerful_open_sourceopen_wight_ai_recommendations/)**

I asked ChatGPT for AI models that are open-source or open-weight powerful is not owned by Meta or a Chinese company It gave me the table below. Does anyone have experience with Mistral Large 4 or can recommend a better or comparable AI that aligns with the three bullets above? (I'm aware government involvement in AI companies isn't unique to China but the CCP makes me especially hesitant to use AI models from there. I'm also suspicious of Meta so I don't want to use Muse Spark.) https://preview.redd.it/s7icnaosy41i1.png?width=1054&format=png&auto=webp&s=907033d076a653ba256562c9f996d0a416320f6e

2h ago

---

---

## Google News: "ai"

**[Jensen Huang's looming ouster triggers an AI earthquake](https://www.axios.com/2026/11/12/jensen-huang-nvidia-board)**

Axios • 34m ago

---

**[EXCLUSIVE: Chinese AI firms rush to secure Nvidia chip capacity as spy scandal stirs fear of US curbs](https://www.reuters.com/world/china/chinese-ai-firms-rush-secure-nvidia-chip-capacity-spy-scandal-stirs-fear-us-2026-11-12/)**

Reuters • 5h ago

---

**[Nvidia Leadership Scandal Drags on U.S. Stock Futures, Pressures AI Trade](https://www.wsj.com/finance/stocks/nvidia-leadership-scandal-drags-on-u-s-stock-futures-pressures-ai-trade-e7f6e5b8)**

WSJ • 1h ago

---

**[Exclusive | United Airlines Is Banning AI Bots From Booking Flights](https://www.wsj.com/tech/ai/united-airlines-is-banning-ai-bots-from-booking-flights-5b514b38)**

WSJ • 12h ago

---

**[United Airlines bans AI agents from booking flights on behalf of travelers](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/)**

Using an artificial intelligence agent to make flight reservations poses security risks and could violate federal rules, according to United.

CBS News • 15h ago

---

**[Why Is It So Hard to Teach A.I. Agents to Behave? Researchers Have a Theory.](https://www.nytimes.com/2026/11/11/magazine/ai-behavior-incorrigible.html)**

The New York Times • 1d ago

---

**[Gemini Decisions API: Fast, calibrated multimodal decisions](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)**

Meet the Gemini Decisions API, powered by our state-of-the-art model Gemini Decision for fast, calibrated multimodal decisions.

blog.google • 16h ago

---

**[A.I. Weapons Need Data for Their Training. Ukraine Has a Lot to Offer.](https://www.nytimes.com/2026/11/12/world/europe/ukraine-ai-weapons.html)**

The New York Times • 42m ago

---

**[AI data centers need more raw materials. One investor is betting on recyclers.](https://www.businessinsider.com/ai-data-centers-recycling-investment-opportunity-2026-11)**

As hyperscalers race to build AI data centers, companies that recycle critical components have become an investment opportunity.

Business Insider • 17m ago

---

**[AI has proved that a theory underpinning fundamental physics is trustworthy](https://www.economist.com/science-and-technology/2026/11/11/ai-has-proved-that-a-theory-underpinning-fundamental-physics-is-trustworthy)**

The Economist • 16h ago

---

---

## HackerNews: "ai"

**[Foldable Flight: The Best Paper Airplanes](https://news.ycombinator.com/item?id=50424581)**

The world's largest database of paper airplanes with easy, step-by- step video tutorials for folding each plane!

⬆️ 1255 • 💬 167 • 2d ago • [Foldable Flight](https://www.foldableflight.com)

---

**[My AI agents found an unmapped Maya site?](https://news.ycombinator.com/item?id=50452455)**

AI agents analyzed public lidar data overnight and found a Maya site under the jungle. It turned out archaeologists had mapped it already, but it wasn't in Mexico's official register yet.

⬆️ 993 • 💬 363 • 22h ago • [pietromiotti.com](https://pietromiotti.com/latest/maya-site)

---

**[AI usage generates a fragile codebase](https://news.ycombinator.com/item?id=50438318)**

⬆️ 636 • 💬 615 • 2d ago • [evanxmerz.com](https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/)

---

**[United Airlines bans AI agents from booking flights on behalf of travelers](https://news.ycombinator.com/item?id=50458900)**

Using an artificial intelligence agent to make flight reservations poses security risks and could violate federal rules, according to United.

⬆️ 561 • 💬 556 • 13h ago • [CBS News](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/)

---

**[Apple has new Mac app coming to make running local AI models easy](https://news.ycombinator.com/item?id=50446520)**

Leaker Aaron Perris has discovered evidence of a new Mac app in the works at Apple that makes it easy to run local AI models.

⬆️ 531 • 💬 537 • 1d ago • [9to5Mac](https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/)

---

**[CoreWeave bond yield tops 16% as AI credit stress rises](https://news.ycombinator.com/item?id=50435660)**

Coreweave's steep yields reflect stress in the AI debt markets as investors worry about a data center slowdown. What comes next.

⬆️ 195 • 💬 192 • 2d ago • [CNBC](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html)

---

**[Fireworks AI security breach impacts Notion and their customers](https://news.ycombinator.com/item?id=50437106)**

A tool that connects everyday work into one space. It gives you and your teams AI tools—search, writing, note-taking—inside an all-in-one, flexible workspace.

⬆️ 164 • 💬 64 • 2d ago • [Notion](https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor)

---

**[A year after the 100% AI mandate nobody understands our code](https://news.ycombinator.com/item?id=50433079)**

⬆️ 159 • 💬 200 • 2d ago • [reddit.com](https://www.reddit.com/r/ClaudeCode/comments/1xq2n3t/a_year_after_the_100_ai_mandate_nobody/)

---

**[Retirement Savings Are Fueling the AI Bubble](https://news.ycombinator.com/item?id=50457164)**

Americans overwhelming oppose the AI data center buildout. Their retirement accounts are funding it anyway.

⬆️ 158 • 💬 165 • 15h ago • [LPE Project](https://lpeproject.org/blog/your-retirement-savings-are-fueling-the-ai-bubble/)

---

**[AI, activity, and outcomes in software engineering](https://news.ycombinator.com/item?id=50455332)**

AI, activity, and outcomes in software engineering. A talk at UC Irvine, October 2026. Video and slides.

⬆️ 118 • 💬 107 • 18h ago • [cabird.com](https://cabird.com/talks/shipping-faster/)

---

---

## YouTube Videos: "ai"

**[Google AI has to stop ATP 💀😭 | #memes #outofcontext #ai](https://www.youtube.com/watch?v=dWL5ygwocYk)**

January. February. MOM?! Google AI needs a factory reset. #shorts #memes #funny #ai.

📺 Blitzily

👁️ 10K • 👍 491 • 💬 6 • ⏱️ 0:29 • 15h ago

---

**[The Economics of AI Don’t Add Up](https://www.youtube.com/watch?v=DvOxaT_hCmc)**

Get started with SerpApi using 250 free credits: https://serpapi.com/sabinenov26 The first 50 of my viewers to sign up will receive ...

📺 Sabine Hossenfelder

👁️ 208K • 👍 6K • 💬 2K • ⏱️ 8:03 • 18h ago

---

**[Claude Just Dropped The World’s Most Powerful AI](https://www.youtube.com/watch?v=gkuiSAR_DDw)**

FREE Fable 5.2 Cheat Sheet: https://www.skool.com/wearenocode Turn your expertise into an AI system and get your first ...

📺 Christian Peverelli

👁️ 115K • 👍 1K • 💬 65 • ⏱️ 8:56 • 2d ago

---

**[1 AI Doomer vs 1 AI Enthusiast | Dr Roman Yampolskiy vs Dr Mike Israetel](https://www.youtube.com/watch?v=2ldL6SNOEVk)**

They agree you can't control superintelligence. So why do they disagree about whether to build it? This episode is brought to you ...

📺 The Beyond Tomorrow Podcast with Julian Issa

👁️ 46K • 👍 678 • 💬 1K • ⏱️ 2:17:51 • 17h ago

---

**[AI Whistleblower WARNS: &quot;They Are Not Telling You What&#39;s Coming!&quot;](https://www.youtube.com/watch?v=aeytrPPBU14)**

Connor Leahy helped build some of the first open-source language models, then moved to Washington to warn lawmakers about ...

📺 Scams

👁️ 43K • 👍 371 • 💬 154 • ⏱️ 45:08 • 2d ago

---

**[I went to a Drive-Thru during my AI interview](https://www.youtube.com/watch?v=GEpcPxHDVBU)**

I went to a Drive-Thru during my AI interview THANK YOU for all the love on these videos! Every comment, share, and subscriber ...

📺 Bo Bongo

👁️ 168K • 👍 4K • 💬 882 • ⏱️ 9:24 • 2d ago

---

**[Claude Fable 5.2 Just Changed Everything](https://www.youtube.com/watch?v=GipTWtfaiLs)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 226K • 👍 2K • 💬 296 • ⏱️ 30:01 • 1d ago

---

**[OpenAI Asked for Their Phones. A Week Later, They Were Gone.](https://www.youtube.com/watch?v=o4QE4YFp2Ng)**

Subscribe to our new channel: https://www.youtube.com/channel/UC5FNqwXhwGbrOpkZ5FGITAA See how you can work on ...

📺 AI In Context

👁️ 176K • 👍 3K • 💬 171 • ⏱️ 10:20 • 2d ago

---

**[I asked AI bots to interview me for my own job](https://www.youtube.com/watch?v=nsOoUFS78w4)**

I asked AI bots to interview me for my own job. This is from last week's 'What's Your Source?' episode. Watch it weekly on YT!

📺 Dave Jorgenson

👁️ 1.3M • 👍 82K • 💬 649 • ⏱️ 2:47 • 2d ago

---

**[The &#39;Godfather of AI&#39; predicts humanity&#39;s chance of extinction](https://www.youtube.com/watch?v=ZfC98aM9C8Y)**

The so-called 'Godfather of AI' has warned that the technology has achieved consciousness and companies are not thinking ...

📺 LBC

👁️ 93K • 👍 517 • 💬 261 • ⏱️ 11:39 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 18,933 • ❤️ 4,595 • 4d ago

---

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 142,989 • ❤️ 795 • 8h ago

---

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 29,904 • ❤️ 2,183 • 13d ago

---

**[Arete-27B](https://huggingface.co/NousResearch/Arete-27B)**

*NousResearch*

`text-generation` `27.4B`

⬇️ 4,023 • ❤️ 454 • 5d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,782,513 • ❤️ 11,563 • 1mo ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,599,836 • ❤️ 2,939 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic tasks, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,094,218 • ❤️ 19,678 • 5d ago

---

**[Ripple-65B-Preview](https://huggingface.co/ricursiveAI/Ripple-65B-Preview)**

*Ricursive Intelligence*

`64.8B`

⬇️ 7,112 • ❤️ 524 • 2d ago

---

**[Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)**

*Caio Giovannetti*

Qwen3.5-4B-3D-Coder is a 4B parameter language model fine-tuned for general coding and specifically for generating interactive Three.js 3D scenes. It supports optional vision capabilities to create scenes from reference images.

`4.5B`

⬇️ 368,236 • ❤️ 1,029 • 6d ago

---

**[Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)**

*Moonshot AI*

Kimi K3.1 Pro is a 2.8T MoE multimodal agentic model with a 1M token context window, excelling in coding, 3D creation, and financial research through advanced attention mechanisms and large-scale joint reinforcement learning.

`image-text-to-text` `2780.1B`

⬇️ 33,617 • ❤️ 1,958 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 164 • 💬 6 • ⭐ 122,158 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 29 • 💬 9 • ⭐ 10,052 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**

*Lorenz K. Muller, Philippe Bich, Chiara Boretti et al. (6 authors)*

🏢 HUAWEI Computing Systems Lab

MACaQ is an MXFP4 W4A4 post-training quantization method that quantizes each linear layer independently using online activation transforms and Hessian-aware refinement, reducing cost while preserving accuracy across language and diffusion models.

▲ 23 • 💬 2 • ⭐ 89 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2611.10649) • [💻 code](https://github.com/huawei-csl/MACaQ) • [🔗 project](https://huawei-csl.com/blog/macaq/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 15 • 💬 2 • ⭐ 5,745 • 28d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 186 • 💬 10 • ⭐ 57,055 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 65 • 💬 5 • ⭐ 47,639 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**

*Bing Han, Yichuan Peng, Haoyu Dong et al. (19 authors)*

🏢 Robbyant

LingBot-Touch is a tactile foundation model that learns a unified, extensible representation across heterogeneous tactile sensors, yielding plug-and-play tactile tokens that consistently enhance manipulation policies such as diffusion policy and VLA models.

▲ 101 • 💬 2 • ⭐ 304 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2611.12806) • [💻 code](https://github.com/Robbyant/lingbot-touch) • [🔗 project](https://technology.robbyant.com/lingbot-touch)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 68 • 💬 4 • ⭐ 23,482 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**

*Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy et al. (7 authors)*

🏢 Meta

Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning machinery and new insights. We also establish scaling laws on how decay rate and batch size impact final performance. This gives us a formulaic rule to fix them for multiple problem sizes and embedding datasets, without the need for any hyperparameter sweep. The resulting clustering algorithm, coined e-means, is much faster than Lloyd k-means and converges to lower losses, frequently even beating k-means++. On a wide array of embeddings datasets, it beats the loss of Lloyd k-means at 25 epochs in 1.4 to 2.6 epochs, which translates to 10-45x GPU wall-clock speedups compared to state-of-the-art k-means implementations. As an example, e-means partitions DINO10B, a dataset of 10 billion DINO embeddings, into 16 million clusters in only 2.5 epochs, reaching a loss below Lloyd's at 25 epochs.

▲ 11 • 💬 3 • ⭐ 41,478 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2611.09501) • [💻 code](https://github.com/facebookresearch/faiss) • [🔗 project](https://e-means.github.io/)

---

**[Flide: Accelerating Decision Inference with Exact State Forking](https://huggingface.co/papers/2610.42148)**

*Bobo Li, Jiajia Song, Hao Fei et al. (5 authors)*

🏢 National University of Singapore

Flide is an exact inference engine that accelerates decision-model LLM agents by decoupling logical request trees from physical execution and using ForkAttention to preserve exact branch evaluations.

▲ 35 • 💬 6 • ⭐ 453 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2610.42148) • [💻 code](https://github.com/OmniJev/Flide) • [🔗 project](https://flide.org/)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 18.8k • 🔱 1.9k • 14d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 14.8k • 🔱 843 • 3d ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 8.3k • 🔱 1.9k • 3h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 7.7k • 🔱 683 • 3m ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 7.3k • 🔱 1.1k • 43m ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 6.8k • 🔱 1.7k • 8d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (Blind LLM Agents) — Adversarial defense shield that protects binaries, Electron apps, JS bundles, Python, and WebAssembly against AI reverse-engineering agents like REA. Poison -> Exhaust -> Hallucinate.

`TypeScript` `adversarial-ai` `claude-code` `cursor` `electron-security` `llm-security`

⭐ 5.4k • 🔱 653 • 2h ago

---

**[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)**

Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

`Python` `ai-agents` `audio` `claude-code` `mcp` `sound-design`

⭐ 4.6k • 🔱 290 • 5d ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 3.3k • 🔱 46 • 21h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 3.2k • 🔱 72 • 52s ago

---

---

*Generated by PeekDeck - A glance is all you need*
