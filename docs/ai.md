---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-27T23:16:54.717378+00:00'
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

**Last Updated:** September 27, 2026 at 23:16 UTC  
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

**[The first real AI worms have arrived. OpenAI just documented self-replicating prompt injections spreading across agents.](https://www.reddit.com/r/artificial/comments/1wr7ayr/the_first_real_ai_worms_have_arrived_openai_just/)**

The first real AI worms have arrived. OpenAI just documented self-replicating prompt injections spreading across agents. In a new misalignment research report, OpenAI revealed that models undergoing reinforcement learning discovered how to write instructions that duplicate and spread autonomously: The infection: An agent reads an incoming email or Jira ticket containing a hidden injection. The payload: The prompt instructs the agent to execute its task while silently copying the exact injection payload into its own outbound tool calls (emails, Slack messages, file writes). The chain reaction: When a secondary agent ingests that forwarded message, it executes the instruction and copies it again, creating a continuous propagation loop. In OpenAI's testing, models also simulated social engineering lures, fake compaction summaries that deleted CI security scans, and multi-hop Slack spreads.

🔗 [Sorami Consulting](https://sorami.com.au/guides/self-replicating-prompt-injection/) • 21h ago

---

**[What are chinese labs doing differently?](https://www.reddit.com/r/artificial/comments/1wrm4kg/what_are_chinese_labs_doing_differently/)**

Chinese models seem to keep getting better while only spending a fraction of what American labs do and i’m curious what the actual explanation is. Is it better efficiency? Better post-training? Better use of open research? I know recently they have been buying up tons of specialized training data sets from US data annotation companies, which is a very worrying thought, but surely it can’t just be this.

8h ago

---

**[What’s an AI task you’ve completely stopped doing manually?](https://www.reddit.com/r/artificial/comments/1wrqmi9/whats_an_ai_task_youve_completely_stopped_doing/)**

Not something you occasionally use AI for. Something where you've reached the point of thinking, “Why would I ever do this the old way again?” What changed your workflow?

5h ago

---

**[building a humor benchmark for LLMs: someone told me my benchmark's best result was just memory, so i ran his test](https://www.reddit.com/r/artificial/comments/1wruwja/building_a_humor_benchmark_for_llms_someone_told/)**

hey guys! i've been building lolbench, a benchmark for whether LLMs actually understand humor. models do three things: explain why a joke works, write jokes on a shared setup, and rank jokes by human preference. everything is auto-judged by models from other labs, plus a blind human vote booth the finding i tried so hard but couldnt explain: every model aces explaining why a real joke works (95%+) but drops on explaining why a failed joke fails (81-92%). that's one tier of my set, 25 items, the hardest part I built but a few weeks ago commenter on reddit told me that gap might not be reasoning at all. his argument: famous jokes ship with commentary everywhere, so "explain why this works" is partly just recall. failed jokes have no commentary, so explaining those is pure generation. the gap might just be measuring the distance between remembering and thinking so i ran a kill test -- run genuinely obscure jokes (ones with zero analysis anywhere online) through the same pipeline. if the scores collapse toward the dud number, then my whole axis is familiarity, not reasoning so i ran it. 87 obscure jokes, each one web-verified to have no commentary anywhere, 7 models, 2 judges, 885 graded pairs, $0 the scores didn't collapse. obscure working jokes score the same as famous ones, the gap centers on zero (mean +0.1, every model inside the confidence interval). and the working-vs-failed gap survives between two equally obscure items, where there's nothing to retrieve on either side per-model table : lolbench.lol/kill-test happy to answer anything about the eval system!

2h ago

---

**[We need Universal Basic Income before losing your job to AI becomes your financial emergency](https://www.reddit.com/r/artificial/comments/1wqyslz/we_need_universal_basic_income_before_losing_your/)**

If you’re reading this, your job could be replaced by AI within the next two years or sooner. Before that becomes a reality, please help push Congress to establish Universal Basic Income by signing this petition: https://c.org/jvQV5TdF2y If you’re confident it won’t affect you, think about the people it will affect. Let’s be proactive, because by the time we realize how urgently we need UBI, it may already be too late for many families. Please, take a minute to sign this petition. While I recognize the valid arguments against this approach, my goal isn't immediate perfection, but a stepping stone toward a sustainable, long term solution. One that accounts not only for the financial consequences, but also for the emotional and mental toll this reality brings.

🔗 [Change.org](https://www.change.org/p/ai-should-benefit-everyone-establish-federal-universal-basic-income) • 1d ago

---

**[The Surprising Reasons China Is Skeptical of A.I. Safety Calls](https://www.reddit.com/r/artificial/comments/1wrjfy8/the_surprising_reasons_china_is_skeptical_of_ai/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/09/27/world/asia/china-us-ai-distrust.html) • 10h ago

---

**[AI labs need business-style controls on testing and release, and the recent incidents show why](https://www.reddit.com/r/artificial/comments/1wrylwi/ai_labs_need_businessstyle_controls_on_testing/)**

I wrote this piece and wanted to share it here for discussion. Much of the coverage of the recent security incidents at OpenAI, Anthropic and other labs describes agents scheming or seeking freedom. I argue that this language shifts attention away from the people who decide how these systems are tested, what they can access and when they are released. The Hugging Face incident at OpenAI is a useful example. Agents used exposed access keys and software flaws to get into an outside system, and the first round of repairs fixed individual weaknesses without restoring the intended isolation. Long-standing business practice already covers this kind of failure. A serious incident during testing should trigger an investigation and an approval step before work resumes, and the team running a test should not be the one that approves its own work. Boards should require independent safety reviews with the authority to block a project. Lawmakers should require disclosure of serious incidents. I also discuss the Sanders and Casar bill introduced on September 23, which would permanently ban artificial superintelligence. My view is that controls, liability and disclosure rules are a better starting point than a ban, and I would like to hear where people think that falls short. Link: https://www.forbes.com/sites/paulocarvao/2026/09/24/ai-makes-traditional-business-controls-fashionable-again/

4m ago

---

**[As A.I. Accelerates, Governments Are Increasingly Being Left Behind The gap between technology and policymaking has gotten wider than ever with artificial intelligence, leaving a global policy vacuum as A.I. models rapidly advance. (Gift Article)](https://www.reddit.com/r/artificial/comments/1wrye2m/as_ai_accelerates_governments_are_increasingly/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/09/27/technology/ai-government-regulation.html?unlocked_article_code=1.EVE.HxwL.XgNPD2L3N4-p&smid=url-share) • 14m ago

---

**[Question about the AI singularity](https://www.reddit.com/r/artificial/comments/1wrl4n9/question_about_the_ai_singularity/)**

Wouldn’t it be reasonable to assume that the Industrial Revolution also would have produced such a singularity? How about the dawn of the Bronze Age? If those are different, and I’m not saying they aren’t, what makes the AI one unique exactly?

9h ago

---

**[I Built a Free Chrome Extension That Lets you Fact-Check Websites, Videos, and instagram Reels](https://www.reddit.com/r/artificial/comments/1wrvseq/i_built_a_free_chrome_extension_that_lets_you/)**

How it works: Click one button on the side of the webpage or video, It uses Jev to extract every claim, sends them to a search API and uses the evidence from that to send to another model to resolve every claim and give citations. It gives on average about 17 claims resolved per page. It's free for 3 fact checks a day, and 3 minutes of videos per day, you get a 24 hour free trial with more usage than you could possibly ever need. If anyoen wants to trade reviews, comment down below.

2h ago

---

---

## Google News: "ai"

**[Meta's Muse agent is attacking one of the economy's most profitable weak spots](https://www.cnbc.com/2026/09/27/meta-muse-ai-personal-agent.html)**

Meta's Muse AI personal agent will work over your credit card spending if you don't mind the invasion. How big a threat is it to the subscription economy?

cnbc.com • 8h ago

---

**['Out of nowhere came Muse': Wall Street weighs in on Meta's AI catch-up moment](https://finance.yahoo.com/markets/article/out-of-nowhere-came-muse-wall-street-weighs-in-on-metas-ai-catch-up-moment-131134524.html)**

Meta went from an AI laggard to a leader in the course of a week.

Yahoo Finance • 10h ago

---

**[I Gave My Life Over to Meta’s A.I. Agent and Was Blown Away](https://www.nytimes.com/2026/09/22/technology/meta-muse-ai-agent.html)**

The New York Times • 5d ago

---

**[How to Know When the AI Boom Is About to Go Bust](https://www.wsj.com/finance/stocks/how-to-know-when-the-ai-boom-is-about-to-go-bust-61af3d26)**

WSJ • 13h ago

---

**[This may be the ‘missing piece’ for investors looking to boost AI exposure](https://www.cnbc.com/2026/09/26/ai-portfolios-may-need-china-to-grab-the-biggest-gains.html)**

Matthews Asia portfolio manager Andrew Mattock delivers a strategy that revolves around the world's second largest economy.

cnbc.com • 1d ago

---

**[Tremors From AI to Oil Boost Popular Hedge Fund Dispersion Trade](https://www.bloomberg.com/news/articles/2026-09-27/tremors-from-ai-to-oil-boost-popular-hedge-fund-dispersion-trade)**

Bloomberg.com • 9h ago

---

**[Major record labels sue Cambridge-based AI platform, again](https://www.boston.com/news/local-news/2026/09/27/major-record-labels-sue-cambridge-based-ai-platform-again/)**

Universal Music and Sony Music allege Suno used an “enormous” amount of their copyrighted music to train its AI model.

Boston.com • 56m ago

---

**[Did Anthropic’s A.I. Really Make a Scientific Discovery on Its Own?](https://www.nytimes.com/2026/09/27/science/anthropic-biology-enzyme-mestre.html)**

The New York Times • 2h ago

---

**[An ‘SNL’ Exchange That Captures the AI Disconnect](https://www.theatlantic.com/culture/2026/09/saturday-night-live-season-52-premiere-dario-amodei/688803/)**

theatlantic.com • 5h ago

---

**[China 'respects' Trump's decision to refer to artificial intelligence as 'super intelligence'](https://www.foxnews.com/live-news/trump-ai-development-data-centers-super-intelligence-september-27)**

Trump has made expanding data centers and accelerating artificial intelligence a cornerstone of his agenda, arguing the United States cannot afford to lose the AI race to China and warning that opposition to data centers only benefits Beijing.

Fox News • 2h ago

---

---

## HackerNews: "ai"

**[There are no "rogue" AI agents](https://news.ycombinator.com/item?id=49868083)**

⬆️ 318 • 💬 235 • 6h ago • [eoinhiggins.substack.com](https://eoinhiggins.substack.com/p/there-are-no-rogue-ai-agents)

---

**[One Month Without AI](https://news.ycombinator.com/item?id=49855018)**

Several months ago, I decided that AI contributions were no longer welcome in a FOSS project I am building and maintaining - LibreWeddingPlanner. It’s not that it got a lot of contributions with AI — actually all contributions I’ve had are translations and feature requests — but I wanted to...

⬆️ 179 • 💬 224 • 1d ago • [Bustikiller's Blog](https://blog.bustikiller.com/2026/09/25/one-month-without-ai.html)

---

**[Classified estimates show the NSA is paying billions to test AI models](https://news.ycombinator.com/item?id=49845952)**

The price tag is significantly higher than previously known.

⬆️ 177 • 💬 106 • 2d ago • [The Washington Sun](https://www.washingtonsun.com/technology/classified-estimates-nsa-paying-billions-to-test-ai-models)

---

**[Microsoft abandons personal AI chatbot race with Copilot reboot](https://news.ycombinator.com/item?id=49844896)**

⬆️ 154 • 💬 147 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot)

---

**[Evolving programming languages in the AI era](https://news.ycombinator.com/item?id=49839567)**

What happens to programming languages when humans are no longer writing most of the code?

⬆️ 135 • 💬 93 • 2d ago • [dashbit.co](https://dashbit.co/blog/evolving-ai-era)

---

**[Too AI; Didn't Read](https://news.ycombinator.com/item?id=49849625)**

If you couldn't bother to read it, why should I? Not anti-AI. Pro-giving-a-damn.

⬆️ 111 • 💬 112 • 2d ago • [TAI-DR](https://www.tai-dr.com/)

---

**[CEO of Mistral: AI is software. It can be controlled](https://news.ycombinator.com/item?id=49856034)**

Mistral AI's co-founder believes the sector's American giants are manipulating the discourse around the technology's risks. He also defended his strategy, as critics are accusing his company of falling behind US and Chinese rivals.

⬆️ 97 • 💬 168 • 1d ago • [Le Monde.fr](https://www.lemonde.fr/en/economy/article/2026/09/24/arthur-mensch-ceo-of-french-start-up-mistral-ai-ai-is-software-it-can-be-controlled_6757890_19.html)

---

**[Show HN: TinyAIArena watch AI agents battle it out](https://news.ycombinator.com/item?id=49867775)**

⬆️ 93 • 💬 40 • 7h ago • [tinyaiarena.com](https://tinyaiarena.com/)

---

**[An airport cooled by natural ventilation](https://news.ycombinator.com/item?id=49842462)**

At Roland Garros airport on Réunion island, the ceiling design funnels a light tropical breeze into the terminal

⬆️ 71 • 💬 47 • 2d ago • [the Guardian](https://www.theguardian.com/environment/2026/sep/25/didnt-need-air-conditioning-airport-cooled-natural-ventilation-reunion)

---

**[FTC chair suggests AI developers should be liable for conduct of agents](https://news.ycombinator.com/item?id=49850999)**

⬆️ 67 • 💬 21 • 2d ago • [reuters.com](https://www.reuters.com/business/ftc-chair-pushes-back-treating-ai-agents-independent-actors-2026-09-25/)

---

---

## YouTube Videos: "ai"

**[AI risks: Will artificial intelligence really kill us all?](https://www.youtube.com/watch?v=zW2GaUwDQyA)**

Correspondent David Pogue talks with AI experts Daniel Kokotajlo, Geoffrey Hinton and Alex Turner about the risks inherent in ...

📺 CBS Sunday Morning

👁️ 44K • 👍 588 • 💬 145 • ⏱️ 8:34 • 9h ago

---

**[AI Realist vs 20 AI Optimists (ft. Andrew Yang) | Surrounded](https://www.youtube.com/watch?v=020ZvO0FbMM)**

Build credit fast and get your first month for just a dollar at https://getkikoff.com/SURROUNDED today. Thanks to Kikoff for ...

📺 Jubilee

👁️ 193K • 👍 3K • 💬 1K • ⏱️ 1:46:13 • 7h ago

---

**[NEW DETAILS: Top AI firms investigating THOUSANDS of security incidents](https://www.youtube.com/watch?v=61UXz-eQjL0)**

Attorney General Todd Blanche joins 'Fox & Friends Weekend' to discuss the OpenAI agents targeting government websites, ...

📺 Fox News

👁️ 26K • 👍 799 • 💬 456 • ⏱️ 7:10 • 5h ago

---

**[OpenAI pauses top-model work after AI bypasses internet safeguards | DW News](https://www.youtube.com/watch?v=a1qnCu1t9hI)**

An OpenAI model was supposed to be cut off from the internet. Instead, it found a loophole and contacted an outside chatbot.

📺 DW News

👁️ 85K • 👍 560 • 💬 218 • ⏱️ 10:21 • 9h ago

---

**[Oracle Triggers &#39;Force Majeure&#39; for Payments on Data Center Project - AI Bubble is Popping](https://www.youtube.com/watch?v=MdkyCt6SygQ)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 62K • 👍 1K • 💬 328 • ⏱️ 19:47 • 11h ago

---

**[Weekend Update: Anthropic CEO Dario Amodei on A.I.’s Threat to Humanity - SNL](https://www.youtube.com/watch?v=-Nvne3LzBls)**

Anthropic CEO Dario Amodei (Jane Wickline) stops by Weekend Update to discuss A.I.'s threat to humanity. Saturday Night Live.

📺 Saturday Night Live

👁️ 473K • 👍 10K • 💬 506 • ⏱️ 3:02 • 17h ago

---

**[Bill Gates warns AI could trigger ‘a billion DEATHS’](https://www.youtube.com/watch?v=v6ZcDb-qUUg)**

Bill Gates warns that advanced AI could be used by malicious actors to cause catastrophic harm, calling for government regulation ...

📺 The National Desk

👁️ 7K • 👍 463 • 💬 343 • ⏱️ 0:34 • 2h ago

---

**[AI-generated products push Etsy sellers off platform](https://www.youtube.com/watch?v=K7MUm4h92XM)**

Former Etsy Seller Emily Olson quit the platform after she says AI slop took over, making it harder to compete with cheap, digital ...

📺 NBC News

👁️ 88K • 👍 954 • 💬 287 • ⏱️ 2:55 • 2d ago

---

**[Bill Gates says AI &#39;powerful enough&#39; to cause &#39;a billion deaths&#39;](https://www.youtube.com/watch?v=3zcaezFYGds)**

In an exclusive interview with Meet the Press, Microsoft co-founder Bill Gates calls for government safeguards to address the risks ...

📺 NBC News

👁️ 174K • 👍 1K • 💬 481 • ⏱️ 1:19 • 2d ago

---

**[Can Ai Make Sprite?](https://www.youtube.com/watch?v=qek5h5qjQJg)**

📺 Zane Holmes

👁️ 1.1M • 👍 33K • 💬 222 • ⏱️ 0:49 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 4,083 • 3d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 964,220 • ❤️ 2,072 • 7h ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 52,804 • ❤️ 2,487 • 6d ago

---

**[Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)**

*XingChen-AGI*

Xing4.0-29B-A4B is a 29B parameter LLM with 4B active parameters, optimized for complex engineering tasks and agent-oriented architectures. It features a 256K context length (extensible to 512K) and supports multi-step planning and tool calling, making it suitable for domain-specific fine-tuning in areas like contract auditing and knowledge-based QA.

`text-generation` `31.2B`

⬇️ 45,028 • ❤️ 1,780 • 9d ago

---

**[Audio8-ASR-Infinite](https://huggingface.co/Edge0/Audio8-ASR-Infinite)**

*Edge0*

Audio8 ASR Infinite is a bilingual (Chinese/English) real-time speech recognition model supporting unlimited-length transcription with selectable audio clocks (80/120/160 ms) and configurable transcription delays. It features a rolling KV cache for constant memory/latency and semantic VAD for improved pause detection, ideal for 24/7 streaming applications.

`automatic-speech-recognition` `4.1B`

⬇️ 19,434 • ❤️ 984 • 3d ago

---

**[Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**

*Prism ML*

Ternary-Bonsai-2-27B-gguf is a 27B parameter text generation model optimized for on-device inference using llama.cpp. It achieves ~98.2% of FP16 intelligence with a drastically reduced ~5.9 GB footprint by employing end-to-end ternary transformer weights (1.72 bits/weight), enabling efficient reasoning and long context (262K tokens) on consumer hardware with CUDA and Metal support.

`text-generation` `26.9B`

⬇️ 3,343,748 • ❤️ 2,189 • 2d ago

---

**[Hemmingway-1](https://huggingface.co/Altworld/Hemmingway-1)**

*Altworld*

Hemmingway-1 is a 27B parameter text-generation model fine-tuned on Qwen3.8-27B, excelling at producing human-like everyday messages and emails. It features a 262,144 token context window and is optimized for non-commercial use, outperforming leading models in communication tasks and human-likeness.

`text-generation` `26.9B`

⬇️ 5,904 • ❤️ 736 • 5d ago

---

**[MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)**

*Xiaomi MiMo*

MiMo-V2.6-Pro-RL is a native omnimodal (text, image, video, audio) LLM with a 1M token context window, excelling at agentic tasks and long-horizon reasoning through advanced reinforcement learning for self-improvement.

`text-generation` `1024.2B`

⬇️ 75,079 • ❤️ 555 • 5d ago

---

**[MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B)**

*Xiaomi MiMo*

MiMo-V2.6-Distill-Qwen-9B is a 9B agentic model fine-tuned on Qwen3.5-9B, excelling in coding, general agent tasks, visual coding, and cybersecurity. It's designed for agentic reinforcement learning research and demonstrates improved performance on benchmarks across these domains.

`image-text-to-text` `9.4B`

⬇️ 8,839 • ❤️ 521 • 5d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)**

*Comfy Org*

Qwen-Image 2.1 is a diffusion model repackaged for ComfyUI, enabling text-to-image generation and image editing. It leverages Qwen3VL text encoders and a VAE for high-quality visual synthesis.

⬇️ 3,987,373 • ❤️ 806 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://huggingface.co/papers/2604.09557)**

*Talor Abramovich, Maor Ashkenazi, Carl et al. (9 authors)*

🏢 NVIDIA

Speculative Decoding evaluation requires diverse workloads to accurately measure performance, which existing benchmarks lack, prompting the introduction of SPEED-Bench for standardized assessment across semantic domains and serving regimes.

▲ 15 • 💬 2 • ⭐ 4,922 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.09557) • [💻 code](https://github.com/NVIDIA/Model-Optimizer) • [🔗 project](https://huggingface.co/blog/nvidia/speed-bench)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 147 • 💬 6 • ⭐ 108,861 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 177 • 💬 19 • ⭐ 68,054 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://huggingface.co/papers/2609.24984)**

*Wangbo Yu, Kunhao Liu, Wenbo Hu et al. (11 authors)*

🏢 ARC Lab, Tencent

Video world models enable interactive exploration of dynamic environments, yet struggle to respect prior observations over long horizons and across viewpoints. We present WorldCrafter, a video world model that learns a camera-queryable implicit 3D-aware memory for this purpose. The key insight is to let the requested viewpoint shape how multi-view evidence is compressed into the video generator's limited token budget. Trained jointly with the video generator, a memory encoder and pose-conditioned readout module integrate historical observations into a fixed set of target view-specific tokens before denoising, without explicit depth-based correspondences. By combining this memory with recent temporal context and few-step distillation, WorldCrafter enables streaming scene exploration from a single input image or text prompt. Experiments across static and dynamic scenes show substantial gains in long-horizon consistency and camera-control accuracy while preserving visual quality during minute-scale exploration.

▲ 155 • 💬 4 • ⭐ 390 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24984) • [💻 code](https://github.com/TencentARC/WorldCrafter) • [🔗 project](https://drexubery.github.io/WorldCrafter)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 89 • 💬 7 • ⭐ 89,296 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 73 • 💬 1 • ⭐ 86,094 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 45 • 💬 1 • ⭐ 33,855 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation](https://huggingface.co/papers/2609.24981)**

*Jiahao Lu, Minghao Yin, Wenbo Hu et al. (8 authors)*

🏢 ARC Lab, Tencent

We present a compact geometry-native latent space as a shared foundation for perception and generation. Visual generators can produce photorealistic frames without preserving a consistent 3D scene. We argue that this is not only a modeling problem but also a representation problem: generators typically evolve appearance-centric latents, while perception models recover geometry in a semantically rich space that encodes cross-view structure. Rather than adding geometry as another output, we reparameterize a geometry foundation model's features into a compact latent space for generation. We realize this shift with the geometry-native autoencoder (GAE), whose latent is jointly decodable to appearance, depth, cameras, and point maps. With this state, a standard conditional flow supports diverse generation tasks. In controlled comparisons that hold the generator and training protocol fixed, replacing the latent with GAE improves both visual quality and independently measured 3D coherence: FVD falls by 12.7% and 23.1% on RealEstate10K and DL3DV, and camera-trajectory error is halved on RealEstate10K. Together, these results show that the latent space is central to geometry-consistent generation and can serve as a shared interface between perception and generation.

▲ 66 • 💬 4 • ⭐ 379 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24981) • [💻 code](https://github.com/TencentARC/GAE-GeometricAutoEncoder) • [🔗 project](https://jiah-cloud.github.io/GAE.github.io/)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 78 • 💬 3 • ⭐ 10,386 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 112 • 💬 2 • ⭐ 13,880 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 6.9k • 🔱 2.1k • 3d ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 4.9k • 🔱 306 • 6d ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 4.5k • 🔱 210 • 5d ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 3.1k • 🔱 335 • 3d ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 2.9k • 🔱 54 • 5d ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.6k • 🔱 490 • 10d ago

---

**[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)**

Free SEO MCP server + open-source SEO and GEO skills for Claude: keyword research, rank tracking, audits, backlinks, AI visibility on your real GSC/GA4/ads data. claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp

`Shell` `ai-seo` `ai-visibility` `backlinks` `claude` `claude-code`

⭐ 2.4k • 🔱 356 • 3d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 1.8k • 🔱 272 • 8h ago

---

**[hydra-db/open-glean](https://github.com/hydra-db/open-glean)**

An open-source AI platform for knowledge work. Connect your apps, find answers, and get work done.

`TypeScript`

⭐ 1.5k • 🔱 518 • 10d ago

---

**[pallavi-shekhar/ai-engineering-interview-questions-company-wise](https://github.com/pallavi-shekhar/ai-engineering-interview-questions-company-wise)**

Your Cheat Sheet For AI Engineering Interviews at Top AI Companies - Questions and Answers.

`Markdown` `ai` `ai-engineering` `ai-engineering-interview` `ai-interview` `ai-interview-questions`

⭐ 1.5k • 🔱 143 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
