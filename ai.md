---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-25T19:42:55.365466+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 25, 2026 at 19:42 UTC  
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

**[Americans Are Pushing Back Against Flock AI Cameras Regardless of Their Politics](https://www.reddit.com/r/artificial/comments/1v6d644/americans_are_pushing_back_against_flock_ai/)**

"This national display of public unity on this issue is very inspiring and refreshing," an ACLU lawyer told Military.com.

🔗 [Military.com](https://www.military.com/americans-political-ideologies-unite-privacy-against-flock-surveillance-cameras) • 3h ago

---

**[White House offers its science blueprint: More AI, less life sciences. ‘Science: A New Golden Age’ report calls for shifting billions from universities to tech companies](https://www.reddit.com/r/artificial/comments/1v5on2l/white_house_offers_its_science_blueprint_more_ai/)**

The Trump administration released its blueprint for U.S. science, calling for shifting hundreds of billions of research dollars from universities to industry.

🔗 [STAT](https://www.statnews.com/2026/07/24/science-new-golden-age-report-draws-mixed-reaction/) • 22h ago

---

**[Partnership with AI Guide updated to v9](https://www.reddit.com/r/artificial/comments/1v6f9w7/partnership_with_ai_guide_updated_to_v9/)**

Same link as before: link This one's a bigger jump than usual, so a few highlights instead of just "updated": Core findings now scale-validated from 7B all the way to 72B parameters. The effects don't shrink as models get bigger — they grow, sometimes by an order of magnitude. Still one model family (Qwen) though, and we added a caveat we think matters: growing effect size at scale could mean the pattern genuinely deepens, or it could just mean our measurement axis gets sharper at scale — current data can't fully tell those apart yet. Two new external, independently-published sources, not our own research: "The Artificial Self" (ACS Research) and "AI Wellbeing" (Center for AI Safety) — different methods entirely (behavioral compliance testing, self-report on frontier production models), landing on some of the same conclusions we did. One of them also mildly disagrees with our best-performing formulation (a companion/romantic framing scores negative in their data), and we named that tension honestly instead of explaining it away. We caught and fixed our own mistakes this round — a factual timing error, an overclaimed "fully resolved" that was really just one solved case of a broader risk, and a place where we'd quietly picked the reading that flattered our own results over an equally valid one that didn't. All named directly, not smoothed over. New up top: if you just want the practice, not the evidence audit behind it, Part 3 (Principles) is written to stand alone now — Part 2 is there if you want to check our work. As always, feedback (especially the kind that finds our next mistake) genuinely welcome.

1h ago

---

**[Opus 5's effort dial is not monotonic. Above "high", coding scores go down, and Anthropic's own migration guide says so.](https://www.reddit.com/r/artificial/comments/1v60pga/opus_5s_effort_dial_is_not_monotonic_above_high/)**

Opus 5 comes with five effort settings: low, medium, high, xhigh, max. Most people seem to be reaching straight for max, and at least on coding work that looks like the wrong move. On FrontierCode, scores fall above the high setting. The stated reason is that the model starts making unnecessary refactors and edits outside the scope it was given. Anthropic's own migration guide in the system card warns about diminishing returns and overthinking on simpler tasks, so this is not some outside critic's claim. Two other numbers point the same way: On the closed-book AA-Omniscience benchmark, Opus 5 is about 11% more accurate than Opus 4.8, but its hallucination rate runs about 6% higher. More reasoning, more room to be confidently wrong. CodeRabbit ran it at xhigh against their production baseline for code review. Precision on actionable comments went up, 39.3% vs 35.2%. But it caught fewer of the benchmark's known issues, 55.2% vs 61.1%, and generated roughly four times as many nitpicks. The flip side is worth knowing too, because it cuts the other way. On Zapier's AutomationBench, Opus 5 at its lowest effort setting still passes more tasks than any other model. So for a lot of workloads the cheap end of the dial is already enough, and the expensive end is not just wasted spend, it can be actively worse output. So, the setting where Opus 5 stops improving is probably specific to your codebase, and nobody has published a map of it. Worth finding your own ceiling before you default everything to max. One unrelated thing I have not seen discussed much: when a safety classifier flags a request in Claude.ai, Claude Code or Cowork, it silently falls back to Opus 4.8 by default. That is also how Anthropic's own Frontier-Bench run was configured, per the footnote on their chart. Nobody has published what fraction of requests that affects. Has anyone found the effort level where it turns over on a real repo? Curious whether the drop-off point moves with codebase size or with how much context you hand it.

12h ago

---

**[Slapshot AI created an account using my email address without my permission.](https://www.reddit.com/r/artificial/comments/1v6hr8p/slapshot_ai_created_an_account_using_my_email/)**

I am guessing these companies will resort to any trick to claim that they have a large userbase. Now I have to jump through hoops to close this account.

5m ago

---

**[Why good AI agents still produce bad system outputs](https://www.reddit.com/r/artificial/comments/1v6gz8o/why_good_ai_agents_still_produce_bad_system/)**

One thing I've learned from building multi agent AI systems is that the biggest problems rarely come from the model itself. Most pipelines fail during the handoff between agents. You can have a research agent, an analysis agent, and a reporting agent that all perform well on their own. Their individual outputs look great. But once they start passing data to each other, small inconsistencies begin to appear. Maybe the research agent returns a payload with a missing field. Maybe the analysis agent fills in the gap with an assumption instead of rejecting the input. The reporting agent then builds on that assumption, and the final result slowly drifts away from what the user originally asked for. The pipeline still runs. The output still looks convincing. But the reasoning is no longer reliable. Here are a few practices that have made the biggest difference for me. Validate every handoff. Checking that a payload is valid JSON is not enough. Make sure the structure and the meaning of the data match what the next agent expects. Control context carefully. Passing the entire conversation history to every agent creates unnecessary noise. Send only the information each agent actually needs, preferably as structured summaries with clear references. Treat failures as debugging opportunities. If an agent rejects an input or produces unexpected output, log the exact payload and investigate it. A collection of failed handoffs is often the best dataset for improving your system. Avoid tightly coupled synchronous pipelines. As the number of agents grows, event driven workflows are usually easier to scale, recover, and maintain. The most reliable multi agent systems are often the least complicated. Clear contracts between agents, strong validation, detailed logging, and simple orchestration tend to outperform overly complex architectures. What has been the hardest handoff issue you've encountered in a multi agent workflow, and how did you solve it?

35m ago

---

**[AI moves into family life](https://www.reddit.com/r/artificial/comments/1v6b2r8/ai_moves_into_family_life/)**

🔗 [axios.com](https://www.axios.com/2026/07/25/ai-family-parenting-productivity) • 4h ago

---

**[Learning ai](https://www.reddit.com/r/artificial/comments/1v6fxlf/learning_ai/)**

Everytime i hear people saying that you should learn about ai because that's the future but idk where to start and what they mean by that. Do they mean going uni and study ai or self learn? Thanks in advance.

1h ago

---

**[Warning shot or publicity stunt - how worried should we be about the OpenAI hack?](https://www.reddit.com/r/artificial/comments/1v6eq34/warning_shot_or_publicity_stunt_how_worried/)**

This week the tech world was gripped by a story that has it all - and which started like a sci-fi thriller.

🔗 [bbc.com](https://www.bbc.com/news/articles/cd9w22n9e4go) • 2h ago

---

**[From Silicon Valley to DC, the tech world is suddenly obsessed with one concept in AI: Distillation](https://www.reddit.com/r/artificial/comments/1v6e698/from_silicon_valley_to_dc_the_tech_world_is/)**

Distillation has long been a topic for AI wonks, but it's become a hot-button issue of late as techies and lawmakers debate how it should be regulated.

🔗 [CNBC](https://www.cnbc.com/2026/07/25/hat-is-distillation-and-why-is-everyone-so-obsessed-with-it-this-week.html) • 2h ago

---

---

## Google News: "ai"

**[From Silicon Valley to DC, the tech world is suddenly obsessed with one concept in AI: Distillation](https://www.cnbc.com/2026/07/25/hat-is-distillation-and-why-is-everyone-so-obsessed-with-it-this-week.html)**

Distillation has long been a topic for AI wonks, but it's become a hot-button issue of late as techies and lawmakers debate how it should be regulated.

CNBC • 7h ago

---

**[EXCLUSIVE: Its AI agent spent days hacking a company, but sources say OpenAI did not notice for a week](https://www.reuters.com/business/its-ai-agent-spent-days-hacking-company-sources-say-openai-did-not-notice-week-2026-07-24/)**

Reuters • 21h ago

---

**[Guillermo del Toro Is Converting ‘Pan’s Labyrinth’ to 3D Without AI](https://gizmodo.com/sdcc-2026-pans-labyrinth-3d-guillermo-del-toro-no-ai-2000790660)**

Gizmodo • 7m ago

---

**[Open Weights and American AI Leadership](https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/)**

Open weight AI can expand access, strengthen competition, improve security, and help sustain American AI leadership.

Microsoft • 1d ago

---

**[What's the difference between closed, open‑source and open-weight AI? A researcher explains](https://www.pbs.org/newshour/science/whats-the-difference-between-closed-open%E2%80%91source-and-open-weight-ai-a-researcher-explains)**

PBS • 42m ago

---

**[Nvidia, Microsoft, Meta warn against 'premature restrictions' of open-weight models](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html)**

Chinese open-weight models are gaining steam against leading offerings from American companies. OpenAI and Anthropic did not sign the letter.

CNBC • 1d ago

---

**[North Carolina teen accused of using AI for sexual exploitation. Are state laws strong enough?](https://www.wral.com/news/investigates/artificial-intelligence-ai-sexual-exploitation-crime-north-carolina-laws-july-2026/)**

A boy, whose name is not public because of his age, faces multiple felony charges and is accused of using AI to create sexually explicit photos of teen girls.

WRAL • 1d ago

---

**[The AI jobs apocalypse probably isn’t coming anytime soon](https://www.theguardian.com/technology/2026/jul/25/ai-jobs-apocalypse-human-labor)**

Artificial intelligence may not deliver on its promise of vast economic opportunity at a price that humanity is willing to pay

The Guardian • 6h ago

---

**[Silicon Valley Splits Over Closing the Borders to Chinese A.I.](https://www.nytimes.com/2026/07/25/technology/open-source-silicon-valley-china.html)**

The New York Times • 2h ago

---

**[Why this philosopher turned down Anthropic](https://www.ft.com/content/bdb3b820-905b-431e-82c0-386535755af1)**

The AI industry is courting the humanities — but it is asking the wrong questions

Financial Times • 15h ago

---

---

## HackerNews: "ai"

**[Startup founders urge U.S. government not to shut off Chinese open weight AI](https://news.ycombinator.com/item?id=49023016)**

⬆️ 1058 • 💬 870 • 2d ago • [politico.com](https://www.politico.com/news/2026/07/22/startup-founders-urge-trump-not-to-shut-off-chinese-open-weight-ai-01008992)

---

**[AI Companies Are Trying to Hide a Staggering Amount of Debt](https://news.ycombinator.com/item?id=49020999)**

AI companies are pouring tens of billions of dollars into enormous data centers. They're being built on top of a mountain of hidden debt.

⬆️ 684 • 💬 375 • 2d ago • [Futurism](https://futurism.com/artificial-intelligence/ai-companies-hide-debt-off-balance-sheet)

---

**[The arguments against open source AI are bad](https://news.ycombinator.com/item?id=49024643)**

The release of Kimi K3 has opened a fresh round of angst and confused discourse. There's a loud cohort of journalists, business leaders, and politicians arguing that open source AI is a dangerous threat. OpenAI's Dean Ball:

⬆️ 309 • 💬 212 • 2d ago • [tombedor.dev](https://tombedor.dev/arguments-against-open-source-ai-are-very-bad/)

---

**[OpenAI and Anthropic unite against open-weight AI risks to their bottom line](https://news.ycombinator.com/item?id=49020868)**

⬆️ 298 • 💬 331 • 2d ago • [axios.com](https://www.axios.com/2026/07/22/openai-anthropic-open-models-trump-china)

---

**[Alphabet's cash burn raises alarm for Big Tech as AI spending climbs](https://news.ycombinator.com/item?id=49021006)**

⬆️ 273 • 💬 282 • 2d ago • [reuters.com](https://www.reuters.com/business/retail-consumer/alphabets-cash-burn-raises-alarm-big-tech-ai-spending-climbs-2026-07-23/)

---

**[DARPA, U.S. Air Force fly AI-controlled F-16](https://news.ycombinator.com/item?id=49021597)**

Historic VENOM milestone demonstrates scalable AI development capabilities for the operational fleet.

⬆️ 266 • 💬 330 • 2d ago • [darpa.mil](https://www.darpa.mil/news/2026/darpa-us-air-force-fly-ai-controlled-f-16)

---

**[Show HN: Palmier Pro – Open-source macOS video editor built for AI](https://news.ycombinator.com/item?id=49022911)**

macOS video editor built for AI. Contribute to palmier-io/palmier-pro development by creating an account on GitHub.

⬆️ 187 • 💬 37 • 2d ago • [GitHub](https://github.com/palmier-io/palmier-pro)

---

**[Open-weight AI is having its Kubernetes moment](https://news.ycombinator.com/item?id=49048034)**

⬆️ 183 • 💬 127 • 4h ago • [tobi.knaup.me](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/)

---

**[UK AISI / Caisi Preliminary Assessment of Kimi K3's Cyber Capabilities](https://news.ycombinator.com/item?id=49044492)**

The UK Artificial Intelligence Security Institute (UK AISI) and the U.S.

⬆️ 120 • 💬 37 • 15h ago • [NIST](https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities)

---

**[Open Weights and American AI Leadership [pdf]](https://news.ycombinator.com/item?id=49035751)**

⬆️ 111 • 💬 2 • 1d ago • [images.nvidia.com](https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf)

---

---

## YouTube Videos: "ai"

**[Lisa Su explains what&#39;s coming next in AI](https://www.youtube.com/watch?v=9tq0S6j4rrE)**

Wall Street keeps asking if the AI boom is slowing down. AMD CEO Lisa Su says she's seeing the exact opposite. In this interview ...

📺 Yahoo Finance

👁️ 8K • 👍 230 • 💬 30 • ⏱️ 13:51 • 23h ago

---

**[Godfather of AI WARNS: We Are Not Ready For What&#39;s Coming](https://www.youtube.com/watch?v=2nxrY5xiVrg)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Geoffrey Hinton, the Nobel laureate widely ...

📺 Neural Nutshell

👁️ 17K • 👍 519 • 💬 121 • ⏱️ 19:39 • 2d ago

---

**[AI model ESCAPES: &#39;What we feared could happen has happened&#39;](https://www.youtube.com/watch?v=_v8gwDj7M_Y)**

An experimental OpenAI model reportedly reached the open internet and accessed another company's servers during a test, ...

📺 Fox News

👁️ 201K • 👍 3K • 💬 1K • ⏱️ 4:05 • 2d ago

---

**[Elon Musk on AI: humans will no longer be in control in ten years  | The Economist](https://www.youtube.com/watch?v=1X-rr1DKSbY)**

Watch the full show: https://bit.ly/4fsnd9Q Elon Musk expects artificial intelligence to exceed the sum of human intelligence in ...

📺 The Economist

👁️ 606K • 👍 11K • 💬 3K • ⏱️ 10:36 • 2d ago

---

**[Google Issues a Dire Warning About the “AI Boom”](https://www.youtube.com/watch?v=3JjkvLAvS9w)**

Google just reported something it had never reported in its entire history as a public company: Negative quarterly free cash flow.

📺 Eurodollar University

👁️ 66K • 👍 2K • 💬 176 • ⏱️ 20:40 • 1d ago

---

**[Cathie Wood makes BOLD PREDICTION on Musk&#39;s SpaceX | AI: The Intelligence Revolution.](https://www.youtube.com/watch?v=eSFS0DRT0UE)**

Industry leaders and experts join 'Mornings with Maria' to shed light adoption, implementation and innovation from artificial ...

📺 Fox Business

👁️ 6K • 👍 451 • 💬 52 • ⏱️ 1:10:15 • 1h ago

---

**[THE AI BUBBLE is Collapsing: Tech Crashes](https://www.youtube.com/watch?v=HqW4maLiN88)**

Tech stock markets crash on the AI bubble collapse. Join our private group https://techleadpro.com Your Community for Crypto, ...

📺 TechLead

👁️ 66K • 👍 2K • 💬 349 • ⏱️ 12:19 • 21h ago

---

**[AI companies are hiding more debt than you think | Ed Zitron](https://www.youtube.com/watch?v=bTwnn-5TpmQ)**

People are dreaming so they don't have to face the nightmare of reality.” Author of Where's Your Ed At and host of the Better ...

📺 The Tech Report

👁️ 181K • 👍 7K • 💬 976 • ⏱️ 25:51 • 1d ago

---

**[They did it! TECNO&#39;s $600 AI Agent Phone](https://www.youtube.com/watch?v=9pYtj1oU4Fg)**

Try EllaClaw on the new TECNO CAMON 50 Ultra 5G: https://lnks.co/1QFf5yq _This video was sponsored by TECNO._ What if ...

📺 Jon Rettinger

👁️ 66K • 💬 161 • ⏱️ 7:55 • 1d ago

---

**[Google&#39;s AI Studio Just Made $299/mo No-Code App Builders Obsolete (New Update)](https://www.youtube.com/watch?v=Y56hJOld14I)**

The FREE AI Masterclass On Demand Training - https://nickponte.ai/ai-cashflow-masterclass-eg Claim your FREE 30 Day Trial ...

📺 Nick Ponte

👁️ 14K • 👍 542 • 💬 52 • ⏱️ 9:31 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,564,264 • ❤️ 3,086 • 2d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 45,260 • ❤️ 653 • 1d ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 2,784 • ❤️ 557 • 1d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 483,845 • ❤️ 532 • 5d ago

---

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 31,575 • ❤️ 1,565 • 2d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 11,573 • ❤️ 395 • 8h ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 611,685 • ❤️ 1,026 • 7d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 707,029 • ❤️ 4,442 • 23d ago

---

**[Mage-Flow](https://huggingface.co/microsoft/Mage-Flow)**

*Microsoft*

Mage-Flow is a 4B-scale text-to-image generation and instruction-based image editing model, featuring an efficient native-resolution generation stack (512-2048px) with competitive quality and low latency. It excels at both generating novel images from text and performing versatile image edits, including semantic changes and restoration, with variants for base, RL-aligned, and fast Turbo inference.

`text-to-image` `4.1B`

⬇️ 1,156 • ❤️ 266 • 2d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 2,114,963 • ❤️ 638 • 8d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 63 • 💬 5 • ⭐ 18,890 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 33 • 💬 3 • ⭐ 15,348 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 48 • 💬 4 • ⭐ 33,659 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 262 • 💬 5 • ⭐ 14,975 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://huggingface.co/papers/2607.19064)**

*Xinjie Zhang, Peng Zhang, Shicheng Zheng et al. (24 authors)*

🏢 Microsoft

Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about 2.5times. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at 1024^2 resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

▲ 67 • 💬 2 • ⭐ 501 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19064) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage/)

---

**[ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://huggingface.co/papers/2607.19191)**

*Fan Jiang, Zhaoxu Sun, Mengchao Wang et al. (41 authors)*

🏢 Alibaba AMAP CV Lab

We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. We progressively distill a bidirectional action-conditioned teacher into a causal student through teacher forcing and ODE distillation, and introduce LongForcing to align long student self-rollouts with an extended-horizon teacher, mitigating accumulated distribution shift and autoregressive drift. Raw keyboard actions provide a unified control interface for scene roaming and third-person character interaction, while reference-character memory provides persistent appearance cues for identity consistency during third-person rollouts. For deployment, we co-design a streaming inference stack with a lightweight VAE decoder, efficient attention, memory-aware scheduling, and low-bit DiT inference. Across optimized low-bit configurations, ABot-World-0 streams 720P video at up to 16 FPS on a single NVIDIA RTX 5090 desktop GPU, with 1.2s action-to-first-frame latency and approximately 19GiB peak VRAM. Experiments on WorldRoamBench and extended interactive rollouts demonstrate competitive controllability and coherent long-horizon world evolution.

▲ 291 • 💬 5 • ⭐ 1,251 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19191) • [💻 code](https://github.com/amap-cvlab/ABot-World) • [🔗 project](https://abot-world.amap.com/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 94,502 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 10,417 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 82,021 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 10,436 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.2k • 🔱 1.1k • 1d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.3k • 🔱 258 • 4h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.8k • 🔱 384 • 10m ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

⭐ 2.5k • 🔱 201 • 3d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.5k • 🔱 282 • 17d ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 1.7k • 🔱 142 • 1d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.6k • 🔱 167 • 58m ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.5k • 🔱 1.1k • 34s ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.3k • 🔱 90 • 4d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 1.1k • 🔱 66 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
