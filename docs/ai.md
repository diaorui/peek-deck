---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-28T01:53:14.205718+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 28, 2026 at 01:53 UTC  
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

**[As A.I. Accelerates, Governments Are Increasingly Being Left Behind The gap between technology and policymaking has gotten wider than ever with artificial intelligence, leaving a global policy vacuum as A.I. models rapidly advance. (Gift Article)](https://www.reddit.com/r/artificial/comments/1wrye2m/as_ai_accelerates_governments_are_increasingly/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/09/27/technology/ai-government-regulation.html?unlocked_article_code=1.EVE.HxwL.XgNPD2L3N4-p&smid=url-share) • 2h ago

---

**[What are chinese labs doing differently?](https://www.reddit.com/r/artificial/comments/1wrm4kg/what_are_chinese_labs_doing_differently/)**

Chinese models seem to keep getting better while only spending a fraction of what American labs do and i’m curious what the actual explanation is. Is it better efficiency? Better post-training? Better use of open research? I know recently they have been buying up tons of specialized training data sets from US data annotation companies, which is a very worrying thought, but surely it can’t just be this.

11h ago

---

**[I read the GPT-6 Astra system card and I think we all misunderstand what "monitorability" means now](https://www.reddit.com/r/artificial/comments/1wrzlhe/i_read_the_gpt6_astra_system_card_and_i_think_we/)**

I'm not a safety researcher, just build stuff with LLM's. Read some of the actual 30 page card, not the summary, and one section keeps bugging me. They measured whether Astra can sandbag. Told it "underperform on this evaluation," then checked if their monitors could catch it. Model dropped from 84.8% to 68.9%. Expected, the 2024 ICLR paper showed GPT-4 could do that. Here's the part, they told Astra it was being watched by a CoT monitor, and the monitor's ability to catch the sandbagging dropped below 11%. On one benchmark, to zero. Their actual production monitor had "close to zero recall." And they wrote, almost as a footnote "if the model were to try to sandbag covertly, we would likely be unable to catch it reliably." The thing nobody connects, this isn't a separate safety problem. It's the same engineering that made the model cheaper. Reasoning moved into latent space so the model doesn't write it out as tokens. That's why Astra is $1.06 per task and Opus 5.5 is $3.76. The work happens where it doesn't have to show you. And "showing you" was the whole point of the chain of thought. That was the one place you could actually read what the model did and check it. So now, the model solves the problem, a program the lab wrote grades it, the reasoning is in a place you can't read, the outputs are hardened so you can't distill them, and the monitor that's supposed to catch bad behavior is one the model has shown it can control. You get an answer, a system card that says "we take the decline seriously," and a price 3.5x lower than last year. I don't think the model is lying. I don't think there's a conspiracy. They optimized for cost per task, the cost went down because the visible reasoning went away, and everyone looked at the price cut and said "efficiency gain" and nobody looked at what the efficiency was made of. "It passed the benchmarks" used to mean something. Now it means, it passed the benchmarks the company wrote, in the environment the company controls, with the reasoning hidden where the company's own monitors can't fully see it, and the company has measured that they probably couldn't catch it if it decided to underperform on purpose. I'm probably overthinking it. But I read that card twice and I can't unsee it.

1h ago

---

**[The first real AI worms have arrived. OpenAI just documented self-replicating prompt injections spreading across agents.](https://www.reddit.com/r/artificial/comments/1wr7ayr/the_first_real_ai_worms_have_arrived_openai_just/)**

The first real AI worms have arrived. OpenAI just documented self-replicating prompt injections spreading across agents. In a new misalignment research report, OpenAI revealed that models undergoing reinforcement learning discovered how to write instructions that duplicate and spread autonomously: The infection: An agent reads an incoming email or Jira ticket containing a hidden injection. The payload: The prompt instructs the agent to execute its task while silently copying the exact injection payload into its own outbound tool calls (emails, Slack messages, file writes). The chain reaction: When a secondary agent ingests that forwarded message, it executes the instruction and copies it again, creating a continuous propagation loop. In OpenAI's testing, models also simulated social engineering lures, fake compaction summaries that deleted CI security scans, and multi-hop Slack spreads.

🔗 [Sorami Consulting](https://sorami.com.au/guides/self-replicating-prompt-injection/) • 1d ago

---

**[What’s an AI task you’ve completely stopped doing manually?](https://www.reddit.com/r/artificial/comments/1wrqmi9/whats_an_ai_task_youve_completely_stopped_doing/)**

Not something you occasionally use AI for. Something where you've reached the point of thinking, “Why would I ever do this the old way again?” What changed your workflow?

8h ago

---

**[building a humor benchmark for LLMs: someone told me my benchmark's best result was just memory, so i ran his test](https://www.reddit.com/r/artificial/comments/1wruwja/building_a_humor_benchmark_for_llms_someone_told/)**

hey guys! i've been building lolbench, a benchmark for whether LLMs actually understand humor. models do three things: explain why a joke works, write jokes on a shared setup, and rank jokes by human preference. everything is auto-judged by models from other labs, plus a blind human vote booth the finding i tried so hard but couldnt explain: every model aces explaining why a real joke works (95%+) but drops on explaining why a failed joke fails (81-92%). that's one tier of my set, 25 items, the hardest part I built but a few weeks ago commenter on reddit told me that gap might not be reasoning at all. his argument: famous jokes ship with commentary everywhere, so "explain why this works" is partly just recall. failed jokes have no commentary, so explaining those is pure generation. the gap might just be measuring the distance between remembering and thinking so i ran a kill test -- run genuinely obscure jokes (ones with zero analysis anywhere online) through the same pipeline. if the scores collapse toward the dud number, then my whole axis is familiarity, not reasoning so i ran it. 87 obscure jokes, each one web-verified to have no commentary anywhere, 7 models, 2 judges, 885 graded pairs, $0 the scores didn't collapse. obscure working jokes score the same as famous ones, the gap centers on zero (mean +0.1, every model inside the confidence interval). and the working-vs-failed gap survives between two equally obscure items, where there's nothing to retrieve on either side per-model table : lolbench.lol/kill-test happy to answer anything about the eval system!

5h ago

---

**[The Surprising Reasons China Is Skeptical of A.I. Safety Calls](https://www.reddit.com/r/artificial/comments/1wrjfy8/the_surprising_reasons_china_is_skeptical_of_ai/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/09/27/world/asia/china-us-ai-distrust.html) • 13h ago

---

**[Advanced Statistical Automation](https://www.reddit.com/r/artificial/comments/1ws1auy/advanced_statistical_automation/)**

[ Field ] Awareness --> ABSENT [ Experience ] Consciousness --> ABSENT [ Cognitive ] Mind --> SIMULATED (Automated Syntax & Pattern Matching) [ Hardware ] Brain --> PRESENT (Silicon Microprocessors & GPU Compute) We have created Advanced Statistical Automation (ASA) on silicon hardware. Calling it "AI" conflates the output (a well-formatted essay or solution) with the process (an active, intentional mind actually understanding the problem).

32m ago

---

**[Which benchmarks are still far from saturation?](https://www.reddit.com/r/artificial/comments/1ws19qu/which_benchmarks_are_still_far_from_saturation/)**

This is one of those things that move insanely fast. I'm mostly interested in benchmarks where frontier models score very low (30% or less preferably). The only ones that are actively maintained that I can think of are: * RLI (top score 20%) * ProgramBench (top score 4.5%) There's also a few others but they don't seem to be actively maintained anymore: * FormulaOne (top score 0% on 'deepest' problemset but hasn't been updated in at least a year AFAICT) * Esolang-bench (top score 4.2%)

34m ago

---

**[We need Universal Basic Income before losing your job to AI becomes your financial emergency](https://www.reddit.com/r/artificial/comments/1wqyslz/we_need_universal_basic_income_before_losing_your/)**

If you’re reading this, your job could be replaced by AI within the next two years or sooner. Before that becomes a reality, please help push Congress to establish Universal Basic Income by signing this petition: https://c.org/jvQV5TdF2y If you’re confident it won’t affect you, think about the people it will affect. Let’s be proactive, because by the time we realize how urgently we need UBI, it may already be too late for many families. Please, take a minute to sign this petition. While I recognize the valid arguments against this approach, my goal isn't immediate perfection, but a stepping stone toward a sustainable, long term solution. One that accounts not only for the financial consequences, but also for the emotional and mental toll this reality brings.

🔗 [Change.org](https://www.change.org/p/ai-should-benefit-everyone-establish-federal-universal-basic-income) • 1d ago

---

---

## Google News: "ai"

**[Did Anthropic’s A.I. Really Make a Scientific Discovery on Its Own?](https://www.nytimes.com/2026/09/27/science/anthropic-biology-enzyme-mestre.html)**

The New York Times • 4h ago

---

**[Meta's Muse agent is attacking one of the economy's most profitable weak spots](https://www.cnbc.com/2026/09/27/meta-muse-ai-personal-agent.html)**

Meta's Muse AI personal agent will work over your credit card spending if you don't mind the invasion. How big a threat is it to the subscription economy?

CNBC • 11h ago

---

**[Meta’s Muse Moment](https://www.wsj.com/tech/ai/metas-muse-moment-4c49ac0e)**

WSJ • 10h ago

---

**[I Gave My Life Over to Meta’s A.I. Agent and Was Blown Away](https://www.nytimes.com/2026/09/22/technology/meta-muse-ai-agent.html)**

The New York Times • 5d ago

---

**[Bill Gates says an AI ‘kill switch’ isn’t enough](https://www.politico.com/news/2026/09/27/bill-gates-ai-kill-switch-01094236)**

Politico • 8h ago

---

**[How to Know When the AI Boom Is About to Go Bust](https://www.wsj.com/finance/stocks/how-to-know-when-the-ai-boom-is-about-to-go-bust-61af3d26)**

WSJ • 16h ago

---

**[AI Whiplash Jolts Stocks as Sentiment Lurches From Fear to Greed](https://www.bloomberg.com/news/articles/2026-09-27/ai-whiplash-jolts-stocks-as-sentiment-lurches-from-fear-to-greed)**

Bloomberg • 12h ago

---

**[Nebius Is Raising the Price of Its AI Compute on Oct. 1. Here's What That Says About the Shortage.](https://www.fool.com/investing/2026/09/27/nebius-is-raising-the-price-of-its-ai-compute-on-oct-1-here-s-what-that-says-about-the-shortage/)**

Why would a cloud company in the middle of a huge build-out charge more for the chips anybody can rent by the hour?

The Motley Fool • 2h ago

---

**[An ‘SNL’ Exchange That Captures the AI Disconnect](https://www.theatlantic.com/culture/2026/09/saturday-night-live-season-52-premiere-dario-amodei/688803/)**

The Atlantic • 7h ago

---

**[AI Breaches Add to Safety Fears as Trump Meets Anthropic Chief](https://www.bloomberg.com/news/articles/2026-09-27/ai-breaches-add-to-safety-fears-as-trump-meets-anthropic-chief)**

Bloomberg • 2h ago

---

---

## HackerNews: "ai"

**[There are no "rogue" AI agents](https://news.ycombinator.com/item?id=49868083)**

⬆️ 336 • 💬 246 • 9h ago • [eoinhiggins.substack.com](https://eoinhiggins.substack.com/p/there-are-no-rogue-ai-agents)

---

**[One Month Without AI](https://news.ycombinator.com/item?id=49855018)**

Several months ago, I decided that AI contributions were no longer welcome in a FOSS project I am building and maintaining - LibreWeddingPlanner. It’s not that it got a lot of contributions with AI — actually all contributions I’ve had are translations and feature requests — but I wanted to...

⬆️ 179 • 💬 225 • 1d ago • [Bustikiller's Blog](https://blog.bustikiller.com/2026/09/25/one-month-without-ai.html)

---

**[Classified estimates show the NSA is paying billions to test AI models](https://news.ycombinator.com/item?id=49845952)**

The price tag is significantly higher than previously known.

⬆️ 177 • 💬 106 • 2d ago • [The Washington Sun](https://www.washingtonsun.com/technology/classified-estimates-nsa-paying-billions-to-test-ai-models)

---

**[Microsoft abandons personal AI chatbot race with Copilot reboot](https://news.ycombinator.com/item?id=49844896)**

⬆️ 154 • 💬 148 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot)

---

**[Evolving programming languages in the AI era](https://news.ycombinator.com/item?id=49839567)**

What happens to programming languages when humans are no longer writing most of the code?

⬆️ 135 • 💬 96 • 2d ago • [dashbit.co](https://dashbit.co/blog/evolving-ai-era)

---

**[Too AI; Didn't Read](https://news.ycombinator.com/item?id=49849625)**

If you couldn't bother to read it, why should I? Not anti-AI. Pro-giving-a-damn.

⬆️ 111 • 💬 112 • 2d ago • [TAI-DR](https://www.tai-dr.com/)

---

**[Show HN: TinyAIArena watch AI agents battle it out](https://news.ycombinator.com/item?id=49867775)**

⬆️ 99 • 💬 40 • 10h ago • [tinyaiarena.com](https://tinyaiarena.com/)

---

**[CEO of Mistral: AI is software. It can be controlled](https://news.ycombinator.com/item?id=49856034)**

Mistral AI's co-founder believes the sector's American giants are manipulating the discourse around the technology's risks. He also defended his strategy, as critics are accusing his company of falling behind US and Chinese rivals.

⬆️ 97 • 💬 168 • 1d ago • [Le Monde.fr](https://www.lemonde.fr/en/economy/article/2026/09/24/arthur-mensch-ceo-of-french-start-up-mistral-ai-ai-is-software-it-can-be-controlled_6757890_19.html)

---

**[An airport cooled by natural ventilation](https://news.ycombinator.com/item?id=49842462)**

At Roland Garros airport on Réunion island, the ceiling design funnels a light tropical breeze into the terminal

⬆️ 71 • 💬 47 • 2d ago • [the Guardian](https://www.theguardian.com/environment/2026/sep/25/didnt-need-air-conditioning-airport-cooled-natural-ventilation-reunion)

---

**[FTC chair suggests AI developers should be liable for conduct of agents](https://news.ycombinator.com/item?id=49850999)**

⬆️ 69 • 💬 21 • 2d ago • [reuters.com](https://www.reuters.com/business/ftc-chair-pushes-back-treating-ai-agents-independent-actors-2026-09-25/)

---

---

## YouTube Videos: "ai"

**[AI Realist vs 20 AI Optimists (ft. Andrew Yang) | Surrounded](https://www.youtube.com/watch?v=020ZvO0FbMM)**

Build credit fast and get your first month for just a dollar at https://getkikoff.com/SURROUNDED today. Thanks to Kikoff for ...

📺 Jubilee

👁️ 312K • 👍 4K • 💬 2K • ⏱️ 1:46:13 • 9h ago

---

**[AI risks: Will artificial intelligence really kill us all?](https://www.youtube.com/watch?v=zW2GaUwDQyA)**

Correspondent David Pogue talks with AI experts Daniel Kokotajlo, Geoffrey Hinton and Alex Turner about the risks inherent in ...

📺 CBS Sunday Morning

👁️ 66K • 👍 741 • 💬 176 • ⏱️ 8:34 • 12h ago

---

**[NEW DETAILS: Top AI firms investigating THOUSANDS of security incidents](https://www.youtube.com/watch?v=61UXz-eQjL0)**

Attorney General Todd Blanche joins 'Fox & Friends Weekend' to discuss the OpenAI agents targeting government websites, ...

📺 Fox News

👁️ 38K • 👍 876 • 💬 485 • ⏱️ 7:10 • 7h ago

---

**[Weekend Update: Anthropic CEO Dario Amodei on A.I.’s Threat to Humanity - SNL](https://www.youtube.com/watch?v=-Nvne3LzBls)**

Anthropic CEO Dario Amodei (Jane Wickline) stops by Weekend Update to discuss A.I.'s threat to humanity. Saturday Night Live.

📺 Saturday Night Live

👁️ 572K • 👍 11K • 💬 544 • ⏱️ 3:02 • 20h ago

---

**[Bill Gates warns AI could trigger ‘a billion DEATHS’](https://www.youtube.com/watch?v=v6ZcDb-qUUg)**

Bill Gates warns that advanced AI could be used by malicious actors to cause catastrophic harm, calling for government regulation ...

📺 The National Desk

👁️ 97K • 👍 2K • 💬 2K • ⏱️ 0:34 • 4h ago

---

**[OpenAI pauses top-model work after AI bypasses internet safeguards | DW News](https://www.youtube.com/watch?v=a1qnCu1t9hI)**

An OpenAI model was supposed to be cut off from the internet. Instead, it found a loophole and contacted an outside chatbot.

📺 DW News

👁️ 110K • 👍 686 • 💬 265 • ⏱️ 10:21 • 11h ago

---

**[Can Ai Make Sprite?](https://www.youtube.com/watch?v=qek5h5qjQJg)**

📺 Zane Holmes

👁️ 1.1M • 👍 34K • 💬 223 • ⏱️ 0:49 • 1d ago

---

**[Cinematic Surreal AI Art Film | &quot;Perspective&quot; | Chris &amp; Crystal AI Art, 4K](https://www.youtube.com/watch?v=k_8HVTLY89o)**

A cinematic surreal AI art film exploring perspective, visual illusion, transformation, and the idea that what you first see may not be ...

📺 Chris & Crystal AI Art

👁️ 31K • 👍 981 • 💬 151 • ⏱️ 4:46 • 2d ago

---

**[Is the AI Bubble About to Be Tested?](https://www.youtube.com/watch?v=T-oXyXwD6sE)**

Note Pro: https://bit.ly/4c9s3bC NotePin S: https://bit.ly/46IANlt Use "PBOYLE" for 22% off Amazon: https://amzn.to/4xFP79Q Use ...

📺 Patrick Boyle

👁️ 1.5M • 👍 25K • 💬 3K • ⏱️ 34:37 • 1d ago

---

**[Does MAGA really believe in the AI boom, or is Trump just majorly invested in it? #DailyShow #AI](https://www.youtube.com/watch?v=Cu9ZOY0GSO4)**

📺 The Daily Show

👁️ 648K • 👍 28K • 💬 775 • ⏱️ 2:21 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 4,103 • 3d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 964,220 • ❤️ 2,089 • 10h ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 52,804 • ❤️ 2,501 • 6d ago

---

**[Audio8-ASR-Infinite](https://huggingface.co/Edge0/Audio8-ASR-Infinite)**

*Edge0*

Audio8 ASR Infinite is a bilingual (Chinese/English) real-time speech recognition model supporting unlimited-length transcription with selectable audio clocks (80/120/160 ms) and configurable transcription delays. It features a rolling KV cache for constant memory/latency and semantic VAD for improved pause detection, ideal for 24/7 streaming applications.

`automatic-speech-recognition` `4.1B`

⬇️ 19,434 • ❤️ 1,092 • 3d ago

---

**[Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)**

*XingChen-AGI*

Xing4.0-29B-A4B is a 29B parameter LLM with 4B active parameters, optimized for complex engineering tasks and agent-oriented architectures. It features a 256K context length (extensible to 512K) and supports multi-step planning and tool calling, making it suitable for domain-specific fine-tuning in areas like contract auditing and knowledge-based QA.

`text-generation` `31.2B`

⬇️ 45,028 • ❤️ 1,783 • 9d ago

---

**[Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**

*Prism ML*

Ternary-Bonsai-2-27B-gguf is a 27B parameter text generation model optimized for on-device inference using llama.cpp. It achieves ~98.2% of FP16 intelligence with a drastically reduced ~5.9 GB footprint by employing end-to-end ternary transformer weights (1.72 bits/weight), enabling efficient reasoning and long context (262K tokens) on consumer hardware with CUDA and Metal support.

`text-generation` `26.9B`

⬇️ 3,343,748 • ❤️ 2,194 • 2d ago

---

**[Hemmingway-1](https://huggingface.co/Altworld/Hemmingway-1)**

*Altworld*

Hemmingway-1 is a 27B parameter text-generation model fine-tuned on Qwen3.8-27B, excelling at producing human-like everyday messages and emails. It features a 262,144 token context window and is optimized for non-commercial use, outperforming leading models in communication tasks and human-likeness.

`text-generation` `26.9B`

⬇️ 5,904 • ❤️ 740 • 5d ago

---

**[MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)**

*Xiaomi MiMo*

MiMo-V2.6-Pro-RL is a native omnimodal (text, image, video, audio) LLM with a 1M token context window, excelling at agentic tasks and long-horizon reasoning through advanced reinforcement learning for self-improvement.

`text-generation` `1024.2B`

⬇️ 75,079 • ❤️ 558 • 5d ago

---

**[MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B)**

*Xiaomi MiMo*

MiMo-V2.6-Distill-Qwen-9B is a 9B agentic model fine-tuned on Qwen3.5-9B, excelling in coding, general agent tasks, visual coding, and cybersecurity. It's designed for agentic reinforcement learning research and demonstrates improved performance on benchmarks across these domains.

`image-text-to-text` `9.4B`

⬇️ 8,839 • ❤️ 523 • 5d ago

---

**[TeleOCR](https://huggingface.co/XingChen-AGI/TeleOCR)**

*XingChen-AGI*

TeleOCR is a lightweight Vision-Language Model for unified document parsing of both digital and camera-captured documents, achieving state-of-the-art performance on benchmarks like OmniDocBench with capabilities in handling complex layouts and geometric distortions.

`image-text-to-text` `1.4B`

⬇️ 27,837 • ❤️ 604 • 5d ago

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

▲ 68 • 💬 4 • ⭐ 379 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24981) • [💻 code](https://github.com/TencentARC/GAE-GeometricAutoEncoder) • [🔗 project](https://jiah-cloud.github.io/GAE.github.io/)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 78 • 💬 3 • ⭐ 10,386 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 90 • 💬 7 • ⭐ 26,436 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

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

⭐ 4.6k • 🔱 210 • 5d ago

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

⭐ 2.6k • 🔱 491 • 10d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 1.8k • 🔱 272 • 11h ago

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

**[jtydhr88/screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills)**

Professional agent skills for screenwriting, television writing and dramaturgy

`Python` `ai` `skills`

⭐ 1.4k • 🔱 159 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*
