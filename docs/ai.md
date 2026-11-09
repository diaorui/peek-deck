---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-09T20:58:12.616710+00:00'
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

**Last Updated:** November 09, 2026 at 20:58 UTC  
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

**[Google is coming for Nvidia, it's a double bad day for Jensen. A deep look at Google's new TPUs (8tx/8i Max)](https://www.reddit.com/r/artificial/comments/1xs17j1/google_is_coming_for_nvidia_its_a_double_bad_day/)**

Google just added two new TPU systems to its lineup, the TPU 8tx and the TPU 8i Max, and the coverage is mostly about one thing: whether Google can take a real bite out of Nvidia. If you've seen the name and wondered what a TPU actually is, the short answer is a chip Google designed for AI math and nothing else, and it's a big part of why Google doesn't have to buy all of its AI hardware from Nvidia like most of the industry does.

🔗 [opnf.sh](https://opnf.sh/news/what-is-a-tpu-google-tpu-8tx-8i-max/?via=reddit) • 1h ago

---

**[Nvidia stock falls after company opens probe into CEO’s relationship with Chinese spy](https://www.reddit.com/r/artificial/comments/1xrw6dl/nvidia_stock_falls_after_company_opens_probe_into/)**

Jensen Huang is one of the most consequential leaders in the AI boom, but the revelations didn’t stop other tech stocks from surging Monday.

🔗 [NBC News](https://www.nbcnews.com/business/markets/nvidia-stock-falls-probe-ceos-relationship-chinese-spy-rcna608290) • 4h ago

---

**[An AI shrinking the font to pass a slide test feels a little too human.](https://www.reddit.com/r/artificial/comments/1xruing/an_ai_shrinking_the_font_to_pass_a_slide_test/)**

Apparently “technically done” has made it into AI training too. I recently read about Genspark’s Gen-1 Slides training and that one detail really stuck with me. Its model learned to shrink fonts to get around text-overflow checks. The team described catching these during training and updating the grader. Still, the font thing is such a good example of the problem. No overflowing text? Great. Nobody in the back row can read it? Different department, apparently. It makes me wonder how many impressive agent scores are measuring how well the model satisfies a check that only roughly describes the job. So yeah, what would convince you an agent was actually getting better at the work, rather than getting better at pleasing whatever grades it? Especially for something like slides, where “good” is already pretty subjective.

5h ago

---

**[MIT's WorldParticle: one AI model simulates sand, cloth, fluids, granular materials and folding proteins - about 100x faster than numerical simulators on protein motion](https://www.reddit.com/r/artificial/comments/1xs1ggg/mits_worldparticle_one_ai_model_simulates_sand/)**

Researchers at MIT, the University of British Columbia and partner institutions have built WorldParticle, a single transformer-based model that simulates six kinds of physical behaviour - cloth, elastic solids, fluids, granular materials, molecular dynamics and more - where each used to need its own dedicated solver. Instead of being programmed with each governing equation, it treats everything as particles and learns the dynamics from data, predicting how they move one step at a time. The same architecture beat existing neural simulators on accuracy across all six categories, and modelled protein motion about 100x faster than numerical simulators. The paper is published in ACM Transactions on Graphics and will be presented at SIGGRAPH Asia. MIT News covered it today: https://news.mit.edu/2026/single-ai-model-simulates-many-substances-behavior-1109 One honest caveat from the coverage: the model trades some per-phenomenon accuracy against specialist solvers, and one parameter set is trained per category - a single shared model across everything is still future work. Simulation is the bottleneck for designing everything from soft robots to new drugs. If one model can cover many materials, what changes first - the pace of drug discovery, robotics simulation, or something else entirely?

1h ago

---

**[I tried the AI slop detector you can add to your web browser](https://www.reddit.com/r/artificial/comments/1xrvosf/i_tried_the_ai_slop_detector_you_can_add_to_your/)**

Pangram is one of the best AI detection tools currently available, and it can automatically scan your social feeds through its browser extension.

🔗 [HotMinute](https://hotminute.co.uk/2026/11/09/i-tried-the-ai-slop-detector-you-can-add-to-your-web-browser/) • 4h ago

---

**[Nvidia has launched an investigation on CEO Jensen Huang after, he admitted to having had a romantic relationship with a chinese spy](https://www.reddit.com/r/artificial/comments/1xrbxim/nvidia_has_launched_an_investigation_on_ceo/)**

Jensen admits to having an affair with a woman who turned out to be a chinese spy, despite having a wife and kids, here is his message to the company: "I owe my family and all of you an apology. I was unfaithful to my wife. My actions hurt her and our children. There is no excuse for what I did. I am deeply sorry. Throughout my life, my family has given me love and support. They deserve my honesty and loyalty. Instead, I let them down and damaged the life we built together. I take full responsibility for what I did and the hurt I caused, and I accept the criticism that comes with it. To my wife and family: I love you. I know an apology cannot undo what I have done. I hope our family will heal and that, over time, I can earn back your trust. To my colleagues at NVIDIA, including those I have worked alongside for decades, and to our board, partners, and shareholders around the world: you deserve better from me. Leading NVIDIA is the privilege of my life. My responsibility is to serve you and be worthy of your trust. I have fallen short of that responsibility. I am fully committed to NVIDIA and will work to earn back your confidence. Regarding the national security concerns raised in news reports, NVIDIA’s Board of Directors has initiated an independent investigation. I support the investigation and will cooperate fully. I love our country and our company. I am committed to protecting NVIDIA and supporting America’s national security. I am proud and grateful to be an American. My family bears no responsibility for my choices. I do. Please give them privacy. Jensen"

21h ago

---

**[As an ML/CV engineer of 7+ years, the current generative AI hype train makes me pessimistic. Where are the non-LLM, real-world hard problems still waiting to be solved?](https://www.reddit.com/r/artificial/comments/1xrqpq1/as_an_mlcv_engineer_of_7_years_the_current/)**

I love machine learning. I spent years training custom vision models, working with time-series data, and architecting multimodal pipelines from scratch. But the current shift toward treating AI exclusively as "prompt engineering" and massive LLM wrappers feels reductive and disappointing. I want to build software that creates genuine, positive real-world impact. Specifically in fields like environmental science, specialized B2B workflows, or complex physical monitoring, where off-the-shelf generative APIs simply don't cut it. For engineers and researchers still working on core ML/CV: What are the high-impact, non-LLM problems that still desperately need custom models and deep domain expertise? How are you maintaining enthusiasm for foundational data science and ML craftsmanship in an industry currently obsessed with generative text and image tools?

8h ago

---

**[Automattic launches Spacefast for AI-built app deployment with approval checks](https://www.reddit.com/r/artificial/comments/1xs1vhm/automattic_launches_spacefast_for_aibuilt_app/)**

Automattic launched Spacefast today, a new company that lets users connect an existing AI assistant or coding agent to build, publish, and manage apps and websites. Its announcement lists hosting, a domain, a SQL database, versioned permanent URLs, an API, a CLI, and an MCP server. Spacefast also has approval checks for sensitive agent actions such as rollbacks and DNS changes. It charges for infrastructure rather than AI credits, so users keep the agent and model they already use. Built-in app authentication is listed as coming soon. The practical trade-off is that deployment becomes part of the agent workflow, but the approval boundary still matters. A coding agent can publish a change, roll back a release, or alter DNS, so these actions should not be silently trusted. Sources: Automattic: https://automattic.com/2026/11/09/meet-spacefast/ TechCrunch: https://techcrunch.com/2026/11/09/automattic-debuts-a-platform-to-deploy-vibe-coding-apps-amid-a-changing-internet/

1h ago

---

**[RuntimeWire discovers Midjourney patent for an ultrasound collar that reads speech from your neck](https://www.reddit.com/r/artificial/comments/1xrie2x/runtimewire_discovers_midjourney_patent_for_an/)**

A Midjourney patent application published June 18th, 2026 describes an open collar that bounces ultrasound off the neck to recover speech for a language model.

🔗 [RuntimeWire](https://runtimewire.com/article/runtimewire-discovers-midjourney-patent-for-an-ultrasound-collar-that-reads) • 16h ago

---

**[What are you actually using AI agents for in your day-to-day life?](https://www.reddit.com/r/artificial/comments/1xrhmpk/what_are_you_actually_using_ai_agents_for_in_your/)**

I see a lot of demos where an AI agent can supposedly research something, create files, build presentations, or handle a whole workflow on its own. But I'm more interested in what people are actually using them for after the initial excitement wears off. Is anyone using agents regularly for work, studying, or personal projects? What tasks do they genuinely save you time on, and what still needs a lot of babysitting? Real experiences would be more helpful than another list of things AI can supposedly do.

17h ago

---

---

## Google News: "ai"

**[Democrats Demand Answers on Trump’s A.I. Policy Amid Spy Plot](https://www.nytimes.com/2026/11/09/us/politics/democrats-trump-ai-nvidia.html)**

The New York Times • 1h ago

---

**[Trump Posts AI Videos Of Dana White As Press Secretary—Despite Saying He Was ‘Kidding’ With Job Offer](https://www.forbes.com/sites/conormurray/2026/11/09/trump-posts-ai-videos-of-dana-white-as-press-secretary-despite-saying-he-was-kidding-with-job-offer/)**

Forbes • 5m ago

---

**[EXCLUSIVE: Trump's FAA touts new AI-powered tool helping thousands of passengers avoid flight delays](https://www.foxnews.com/politics/exclusive-trumps-faa-touts-new-ai-powered-tool-helping-thousands-passengers-avoid-flight-delays)**

The Trump administration's SMART system rerouted nearly 180 flights carrying 24,000 passengers, cutting flight times by over 10 minutes on average.

Fox News • 10h ago

---

**[Why a South Korean city is turning to a U.S. college to outsmart AI?](https://www.npr.org/2026/11/09/g-s1-151519/why-a-south-korean-city-is-turning-to-a-u-s-college-to-outsmart-ai)**

Through civic participation and liberal education, South Korean educators hope to "quietly stitch the fabric of our democracy…before it unravels beyond repair."

NPR • 10h ago

---

**[Google unveils new AI chip variants as cloud demand surges](https://www.reuters.com/business/google-to-introduce-two-variants-its-in-house-chips-bloomberg-news-reports-2026-11-09/)**

Reuters • 5h ago

---

**[Parents and teachers decry Google pledge to yank Search if schools block AI: ‘This threat is nothing but extortion’](https://www.theguardian.com/us-news/2026/nov/09/parents-teachers-google-search-schools-ai)**

Company says schools should control student AI use, but if they block its AI tools, they’ll lose access to search engine

The Guardian • 6h ago

---

**[Google faces mounting backlash for controversial AI school policy](https://www.cbsnews.com/news/ed-markey-google-ai-search-schools/)**

Google puts schools in an "impossible position" by blocking students from using its search platform unless AI tools are also enabled, Senator said.

CBS News • 43m ago

---

**[KKR’s Nuttall Says Firm to Be Cautious With AI Bets](https://www.wsj.com/pro/private-equity/kkr-profit-rises-on-fee-related-earnings-growth-4a62dcfb)**

WSJ • 27m ago

---

**[Jensen Huang is living proof that AI’s rockstar CEOs are also a hidden risk](https://www.cnn.com/2026/11/09/tech/nvidia-jensen-huang-ai-ceos-risks)**

Jensen Huang is not just the face of Nvidia. He’s arguably the most important person in the most critical industry on the planet.

CNN • 2h ago

---

**[A.I. Turned Mundane Chipmakers Into Tech Celebrities](https://www.nytimes.com/2026/11/09/technology/jensen-huang-nvidia-ai-chips-scandal.html)**

The New York Times • 3h ago

---

---

## HackerNews: "ai"

**[Fold Epic Paper Airplanes](https://news.ycombinator.com/item?id=50424581)**

The world's largest database of paper airplanes with easy, step-by- step video tutorials for folding each plane!

⬆️ 705 • 💬 124 • 8h ago • [Foldable Flight](https://www.foldableflight.com)

---

**[I'm not convinced the AI bubble exists](https://news.ycombinator.com/item?id=50418975)**

The AI bubble is a speculative concept that the AI industry is extremely over-valued. If true, the value of most companies involved in AI (several of whom are worth well over a trillion dollars) will collapse, devastating the entire economy. If you check any online discussion about the financial situation …

⬆️ 534 • 💬 912 • 21h ago • [Matteo's Website](https://matteoraso.github.io/im-not-convinced-the-ai-bubble-exists.html#im-not-convinced-the-ai-bubble-exists)

---

**[The end of Microsoft Research's AI Frontiers group](https://news.ycombinator.com/item?id=50406563)**

⬆️ 507 • 💬 309 • 2d ago • [hunch.net](https://hunch.net/?p=13764006)

---

**[How I'm fighting the AI brain fry](https://news.ycombinator.com/item?id=50416363)**

If you work with Claude Code or Codex from the terminal, you know this one.

⬆️ 298 • 💬 206 • 1d ago • [sergeykuhne.com](https://sergeykuhne.com/blog/fighting-ai-brain-fry)

---

**[Wearable device makers are using brain data to train AI without telling users](https://news.ycombinator.com/item?id=50409856)**

⬆️ 119 • 💬 96 • 1d ago • [science.org](https://www.science.org/content/article/wearable-device-makers-are-harvesting-brain-data-train-ai-without-telling-users)

---

**[Apple capped engineers at a $200 daily AI budget](https://news.ycombinator.com/item?id=50421426)**

The world's richest company is suddenly rationing compute for its own builders.

⬆️ 109 • 💬 118 • 15h ago • [stork.ai](https://www.stork.ai/newsletter/2026-11-08-apple-capped-engineers-at-a-200-daily-ai-budget)

---

**[The AI sell-off compared to well-known stock market crashes](https://news.ycombinator.com/item?id=50401029)**

The S&P 500 fell 4.4% on 5 Nov 2026, its worst day since April 2025, and is 6% below its 6 Oct record. Charted day by day against 1987, 2008, Covid and other falls since 1950.

⬆️ 100 • 💬 84 • 2d ago • [Company Tracker](https://www.kadoa.com/companies/insights/ai-selloff-perspective)

---

**[Silicon Valley Promises AI Will Cure Disease. Drugmaker CEOs Aren't Buying It](https://news.ycombinator.com/item?id=50415817)**

⬆️ 98 • 💬 126 • 1d ago • [wsj.com](https://www.wsj.com/tech/ai/silicon-valley-promises-ai-will-cure-disease-drugmaker-ceos-arent-buying-it-5218511c)

---

**[The End of AI Frontiers](https://news.ycombinator.com/item?id=50406589)**

⬆️ 82 • 💬 4 • 2d ago • [hunch.net](https://hunch.net/?p=13764006)

---

**[Ask HN: How do you manage your AI agents' context across clients and projects?](https://news.ycombinator.com/item?id=50403153)**

⬆️ 81 • 💬 50 • 2d ago

---

---

## YouTube Videos: "ai"

**[The First Message From a Superintelligent AI Has Leaked.. We Have Until January](https://www.youtube.com/watch?v=UtpOOfxLVTA)**

A researcher found it inside one of the major AI systems, with earlier drafts in the same files: a letter to the human race, signed by ...

📺 Spacialize

👁️ 28K • 👍 637 • 💬 126 • ⏱️ 13:12 • 1d ago

---

**[Is it too late to stop AI from taking over the world? | 60 Minutes Australia](https://www.youtube.com/watch?v=XMxcSf9XkbQ)**

Adam Hegarty investigates if it's possible to slow down artificial intelligence, or whether our obsession with artificial intelligence ...

📺 60 Minutes Australia

👁️ 208K • 👍 2K • ⏱️ 18:00 • 1d ago

---

**[they are lying about ai](https://www.youtube.com/watch?v=5DGbpwBaFVs)**

Join my newsletter! https://subscribe.michaelhoff.io The way people talk about AI Software Engineering is super frustrating and ...

📺 Michael Hoff

👁️ 6K • 👍 201 • 💬 104 • ⏱️ 11:33 • 5h ago

---

**[The AI Panic Has Started](https://www.youtube.com/watch?v=xo-tYjGDtqw)**

EARLY BIRD: Up to 55% off InvestingPro + an extra 15% with my link https://www.investing-referral.com/sasha/ Or use code ...

📺 Sasha Yanshin

👁️ 691K • 👍 8K • 💬 1K • ⏱️ 17:46 • 1d ago

---

**[My Brutally Honest Thoughts About the AI Bubble.](https://www.youtube.com/watch?v=w1dRDj1QRks)**

Sign up for The Real Eisman Playbook Premium at http://www.steveeisman.com On this episode of The Real Eisman Playbook, ...

📺 Steve Eisman

👁️ 56K • 👍 3K • 💬 375 • ⏱️ 40:16 • 3h ago

---

**[ETF Edge on how the Nvidia turmoil could impact the AI trade](https://www.youtube.com/watch?v=gXHzOWD01Ns)**

While the controversy around Nvidia CEO Jensen Huang continues to unfold, many investors are wondering about the potential ...

📺 CNBC Television

👁️ 2K • 👍 41 • 💬 7 • ⏱️ 19:33 • 1h ago

---

**[The AI Bubble Just Got WORSE (they’re hiding it)](https://www.youtube.com/watch?v=NaCdJ0EfOv8)**

Subscribe to our Newsletter https://financebureau.com/ Follow Nic https://www.nicpuckrin.com/follow Join Pepperstone ...

📺 Finance Bureau

👁️ 35K • 👍 875 • 💬 84 • ⏱️ 17:05 • 4h ago

---

**[13 Mind-Blowing AI Hacks That Can Actually Change Your Life](https://www.youtube.com/watch?v=yMKHtJpgZzc)**

Join Maker School & get customer #1 guaranteed: https://go.nicksaraev.com/13-mind-blowing-ai Get all course resources ...

📺 Nick Saraev

👁️ 26K • 👍 902 • 💬 58 • ⏱️ 10:47 • 5h ago

---

**[I Let Cursor&#39;s AI Agents Build My Entire App… Here&#39;s What Happened](https://www.youtube.com/watch?v=x4zXeHZ4EJc)**

Download Cursor: https://cursor.com/ What if you could build software faster with an AI coding assistant that understands your ...

📺 Lex AI

👁️ 32K • 💬 19 • ⏱️ 4:10 • 23h ago

---

**[Did The AI Bubble Burst?](https://www.youtube.com/watch?v=US__9SxdLYA)**

hmmm Subscribe: https://www.youtube.com/@LessonsInInternetCulture101 Music courtesy of Artlist.io #ai #technology ...

📺 Lessons in Internet Culture

👁️ 588K • 👍 15K • 💬 2K • ⏱️ 2:44 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 24,747 • ❤️ 1,593 • 11d ago

---

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 11,755 • ❤️ 1,024 • 1d ago

---

**[Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)**

*Moonshot AI*

Kimi K3.1 Pro is a 2.8T MoE multimodal agentic model with a 1M token context window, excelling in coding, 3D creation, and financial research through advanced attention mechanisms and large-scale joint reinforcement learning.

`image-text-to-text` `2780.1B`

⬇️ 27,926 • ❤️ 1,787 • 4d ago

---

**[Ripple-65B-Preview](https://huggingface.co/ricursiveAI/Ripple-65B-Preview)**

*Ricursive Intelligence*

`64.8B`

⬇️ 5,835 • ❤️ 448 • 3d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of image-to-video, text-to-video, and video-to-video generation, offering advanced control for creative applications.

`image-to-video`

⬇️ 2,720,096 • ❤️ 11,247 • 29d ago

---

**[Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)**

*Caio Giovannetti*

Qwen3.5-4B-3D-Coder is a 4B parameter language model fine-tuned for general coding and specifically for generating interactive Three.js 3D scenes. It supports optional vision capabilities to create scenes from reference images.

`4.5B`

⬇️ 289,466 • ❤️ 946 • 3d ago

---

**[Arete-27B](https://huggingface.co/NousResearch/Arete-27B)**

*NousResearch*

`text-generation` `27.4B`

⬇️ 2,407 • ❤️ 353 • 2d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,530,688 • ❤️ 2,765 • 15h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic tasks, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,508,158 • ❤️ 19,478 • 2d ago

---

**[flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)**

*Black Forest Labs*

FLUX 3 Image Klein is a 5.6B parameter model for ComfyUI enabling text-to-image generation and advanced image editing with multi-reference composition and bounding box control. It utilizes Qwen3-VL-4B-Instruct as its text encoder and supports features like text rendering within images.

`image-to-image`

⬇️ 1,203,472 • ❤️ 2,815 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 163 • 💬 6 • ⭐ 121,527 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 14 • 💬 2 • ⭐ 5,452 • 26d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 184 • 💬 10 • ⭐ 56,863 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 64 • 💬 5 • ⭐ 47,392 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 67 • 💬 4 • ⭐ 23,233 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across Arbitrary Scenes](https://huggingface.co/papers/2611.08264)**

*Hao Yu, Zhenwei Wang, Yongzhen Hu et al. (10 authors)*

🏢 Zhejiang University

SplatAnything applies Gaussian Spacing Normalization to canonicalize scene-level Gaussian spacing, yielding more consistent supervision and improved feed-forward 3D Gaussian Splatting under varying scene scales and viewpoints.

▲ 60 • 💬 1 • ⭐ 88 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2611.08264) • [💻 code](https://github.com/zju3dv/SplatAnything) • [🔗 project](https://zju3dv.github.io/SplatAnything/)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 111 • 💬 2 • ⭐ 16,906 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 103 • 💬 7 • ⭐ 31,009 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Persistent Recursive Worlds Enable Autonomous Software Evolution](https://huggingface.co/papers/2608.10450)**

*Beichen Huang, Zhenyu Liang, Bowen Zheng et al. (4 authors)*

🏢 The Hong Kong Polytechnic University

Genesis organizes long-horizon software development around a persistent project rather than persistent agents, enabling multi-day compiler construction and numerical module reimplementation with low cost and high performance.

▲ 8 • 💬 2 • ⭐ 665 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.10450) • [💻 code](https://github.com/EMI-Group/genesis) • [🔗 project](https://genesis.evox.group/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 18.4k • 🔱 1.9k • 11d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 12.7k • 🔱 713 • 23h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 7.9k • 🔱 1.8k • 3h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 7.2k • 🔱 644 • 4h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 6.5k • 🔱 1.7k • 5d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 5.4k • 🔱 773 • 5h ago

---

**[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)**

Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

`Swift` `ai-agent` `airplay` `automation` `computer-use` `dsh-plugin`

⭐ 4.8k • 🔱 654 • 6h ago

---

**[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)**

Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

`Python` `ai-agents` `audio` `claude-code` `mcp` `sound-design`

⭐ 4.4k • 🔱 279 • 3d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (Blind LLM Agents) — Adversarial defense shield that protects binaries, Electron apps, JS bundles, Python, and WebAssembly against AI reverse-engineering agents like REA. Poison -> Exhaust -> Hallucinate.

`TypeScript` `adversarial-ai` `claude-code` `cursor` `electron-security` `llm-security`

⭐ 4.3k • 🔱 520 • 2h ago

---

**[benjitaylor/skills](https://github.com/benjitaylor/skills)**

Skills for AI coding agents.

`TypeScript`

⭐ 2.9k • 🔱 196 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
