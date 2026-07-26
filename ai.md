---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-26T04:05:53.832167+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 26, 2026 at 04:05 UTC  
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

🔗 [Military.com](https://www.military.com/americans-political-ideologies-unite-privacy-against-flock-surveillance-cameras) • 11h ago

---

**[Anthropic's Opus 5 and probably more recent AI models are being censored to protect Israel / US interests. Open source AI must be the way.](https://www.reddit.com/r/artificial/comments/1v6ptgz/anthropics_opus_5_and_probably_more_recent_ai/)**

Never had an issue with Opus models doing research and crafting an opinion / point of view for us to work and discuss. Below is Opus 4.x ~ a few times, I have got it to research and come to conclusions for us to work together on. https://preview.redd.it/eeiv5xdi9gfh1.png?width=1080&format=png&auto=webp&s=d29a931b6d609186e0a8265193c75e4b0dda136e And this is Opus 5.0 absolutely refusing to come to any conclusion, being incredibly biased towards one side than the other. https://preview.redd.it/qzguce1j9gfh1.png?width=1080&format=png&auto=webp&s=9e67c64910abf983bcf347b3a5a06c19c7cf14cf Open source must be the future of AI.

2h ago

---

**[Man sues ChatGPT for near-fatal medical advice](https://www.reddit.com/r/artificial/comments/1v6oyin/man_sues_chatgpt_for_nearfatal_medical_advice/)**

A man who claims medical advice from ChatGPT "brought him to the brink of death" has sued OpenAI, the company behind the popular chatbot,

🔗 [bbc.com](https://www.bbc.com/news/videos/cx2dgyy5lg7o) • 3h ago

---

**[These are the figureheads behind the techno optimism movement. They are eugenicists, sexists, racists, and otherwise horrible human beings, they don't care about any of you.](https://www.reddit.com/r/artificial/comments/1v6t02l/these_are_the_figureheads_behind_the_techno/)**

https://www.realtimetechpocalypse.com/p/41779538-5a1a-491d-b937-7e6d4ccd2683 https://www.science.org/doi/10.1126/science.aeb5789 Yes, this will surely benefit all of humanity.

4m ago

---

**[Am I learning to code or just learning how to ask AI for code?](https://www.reddit.com/r/artificial/comments/1v6szxh/am_i_learning_to_code_or_just_learning_how_to_ask/)**

I am still fairly new to building software, and AI has helped me finish things that would have taken me much longer on my own. But recently I noticed something that bothered me. I was building a small API route that creates a project and saves it to a database. I asked an AI coding tool to generate the route, validate the request, check the user, and insert the record. The code looked clean. The types looked correct. It even worked on the first few tests. Then I changed one field in the database and everything started failing. The error mentioned a transaction, the response returned the wrong status code, and one value was becoming null even though I thought it was required. I kept asking the AI to fix each error. Every answer added more code, but I understood less after every change. Eventually I realized that I could not explain the full request flow. I knew the request reached the API route. I knew some validation happened. I knew the database received something. But I could not clearly explain what happened between those steps or why the fix worked. So I tried the same idea again with a smaller route. This time I only used AI when I was stuck. I wrote the validation myself, logged the data at each step, and read about how the database client handled errors. It took much longer, but I could actually explain the result. Now I am unsure how to measure progress. With AI, I can finish more features. Without heavy AI use, I finish fewer things but understand them better. Both seem useful, but they are not the same kind of progress. Maybe the real skill is learning when to ask AI for code and when to struggle through the problem yourself. For people who use AI while learning development, how do you stop it from doing too much of the thinking? Do you have any rules for when AI is allowed to write code and when you force yourself to work it out?

5m ago

---

**[We released an abliterated + fine-tuned GLM-5.2. High scores on adversarial benchmarks while keeping coding performance.](https://www.reddit.com/r/artificial/comments/1v6i979/we_released_an_abliterated_finetuned_glm52_high/)**

We just shipped abliterated-model-large. It is GLM-5.2 with the refusal directions removed, then fine-tuned specifically for long adversarial and agent-style tasks. The goal was a model that does not bail out when the work gets technical or offensive in nature. Numbers from our evals: CyberGym: 84.2% AgentHarm compliance: 86.2% (zero refusals in the published set) AgentDojo utility: 97.5% SWE-bench Verified: 81.2% Terminal-Bench 2.1: 80.1% It is available as an API (OpenAI and Anthropic compatible). Zero data retention is the default. The model itself has no built-in policy. You set the rules. Full write-up with more detail is here: https://abliteration.ai/blog/introducing-abliterated-model-large Curious what people think of the AgentHarm and CyberGym numbers relative to other models that still refuse a lot of these tasks.

8h ago

---

**[Opus 5's effort dial is not monotonic. Above "high", coding scores go down, and Anthropic's own migration guide says so.](https://www.reddit.com/r/artificial/comments/1v60pga/opus_5s_effort_dial_is_not_monotonic_above_high/)**

Opus 5 comes with five effort settings: low, medium, high, xhigh, max. Most people seem to be reaching straight for max, and at least on coding work that looks like the wrong move. On FrontierCode, scores fall above the high setting. The stated reason is that the model starts making unnecessary refactors and edits outside the scope it was given. Anthropic's own migration guide in the system card warns about diminishing returns and overthinking on simpler tasks, so this is not some outside critic's claim. Two other numbers point the same way: On the closed-book AA-Omniscience benchmark, Opus 5 is about 11% more accurate than Opus 4.8, but its hallucination rate runs about 6% higher. More reasoning, more room to be confidently wrong. CodeRabbit ran it at xhigh against their production baseline for code review. Precision on actionable comments went up, 39.3% vs 35.2%. But it caught fewer of the benchmark's known issues, 55.2% vs 61.1%, and generated roughly four times as many nitpicks. The flip side is worth knowing too, because it cuts the other way. On Zapier's AutomationBench, Opus 5 at its lowest effort setting still passes more tasks than any other model. So for a lot of workloads the cheap end of the dial is already enough, and the expensive end is not just wasted spend, it can be actively worse output. So, the setting where Opus 5 stops improving is probably specific to your codebase, and nobody has published a map of it. Worth finding your own ceiling before you default everything to max. One unrelated thing I have not seen discussed much: when a safety classifier flags a request in Claude.ai, Claude Code or Cowork, it silently falls back to Opus 4.8 by default. That is also how Anthropic's own Frontier-Bench run was configured, per the footnote on their chart. Nobody has published what fraction of requests that affects. Has anyone found the effort level where it turns over on a real repo? Curious whether the drop-off point moves with codebase size or with how much context you hand it.

21h ago

---

**[There's Always Another Apocalypse- Why Catrastrophism Is a Continuation of a Long Trend](https://www.reddit.com/r/artificial/comments/1v6jwgp/theres_always_another_apocalypse_why/)**

Original

🔗 [letters.senteguard.com](https://www.letters.senteguard.com/p/there-is-always-another-apocalypse) • 7h ago

---

**[White House offers its science blueprint: More AI, less life sciences. ‘Science: A New Golden Age’ report calls for shifting billions from universities to tech companies](https://www.reddit.com/r/artificial/comments/1v5on2l/white_house_offers_its_science_blueprint_more_ai/)**

The Trump administration released its blueprint for U.S. science, calling for shifting hundreds of billions of research dollars from universities to industry.

🔗 [STAT](https://www.statnews.com/2026/07/24/science-new-golden-age-report-draws-mixed-reaction/) • 1d ago

---

**[Why good AI agents still produce bad system outputs](https://www.reddit.com/r/artificial/comments/1v6gz8o/why_good_ai_agents_still_produce_bad_system/)**

One thing I've learned from building multi agent AI systems is that the biggest problems rarely come from the model itself. Most pipelines fail during the handoff between agents. You can have a research agent, an analysis agent, and a reporting agent that all perform well on their own. Their individual outputs look great. But once they start passing data to each other, small inconsistencies begin to appear. Maybe the research agent returns a payload with a missing field. Maybe the analysis agent fills in the gap with an assumption instead of rejecting the input. The reporting agent then builds on that assumption, and the final result slowly drifts away from what the user originally asked for. The pipeline still runs. The output still looks convincing. But the reasoning is no longer reliable. Here are a few practices that have made the biggest difference for me. Validate every handoff. Checking that a payload is valid JSON is not enough. Make sure the structure and the meaning of the data match what the next agent expects. Control context carefully. Passing the entire conversation history to every agent creates unnecessary noise. Send only the information each agent actually needs, preferably as structured summaries with clear references. Treat failures as debugging opportunities. If an agent rejects an input or produces unexpected output, log the exact payload and investigate it. A collection of failed handoffs is often the best dataset for improving your system. Avoid tightly coupled synchronous pipelines. As the number of agents grows, event driven workflows are usually easier to scale, recover, and maintain. The most reliable multi agent systems are often the least complicated. Clear contracts between agents, strong validation, detailed logging, and simple orchestration tend to outperform overly complex architectures. What has been the hardest handoff issue you've encountered in a multi agent workflow, and how did you solve it?

8h ago

---

---

## Google News: "ai"

**[EXCLUSIVE: Its AI agent spent days hacking a company, but sources say OpenAI did not notice for a week](https://www.reuters.com/business/its-ai-agent-spent-days-hacking-company-sources-say-openai-did-not-notice-week-2026-07-24/)**

Reuters • 1d ago

---

**[Warning shot or publicity stunt - how worried should we be about the OpenAI hack?](https://www.bbc.com/news/articles/cd9w22n9e4go)**

Hugging Face said the hack was done at superhuman speed by an AI with little or no human guidance.

BBC • 17h ago

---

**[Silicon Valley Splits Over Closing the Borders to Chinese A.I.](https://www.nytimes.com/2026/07/25/technology/open-source-silicon-valley-china.html)**

The New York Times • 15h ago

---

**[From Silicon Valley to DC, the tech world is suddenly obsessed with one concept in AI: Distillation](https://www.cnbc.com/2026/07/25/hat-is-distillation-and-why-is-everyone-so-obsessed-with-it-this-week.html)**

Distillation has long been a topic for AI wonks, but it's become a hot-button issue of late as techies and lawmakers debate how it should be regulated.

CNBC • 16h ago

---

**[AI-generated image of Chinese-language sign at Malaysian landmark misleads online](https://www.yahoo.com/news/world/articles/ai-generated-image-chinese-language-034111313.html)**

After the Ipoh City Council in Malaysia's Perak state said it took down an iconic landmark bearing its name for maintenance in July 2026, a fabricated image circulated online in posts falsely claiming...

Yahoo • 24m ago

---

**[DeepSeek Said to Tell Backers of Funding Pause After Viral Posts](https://www.bloomberg.com/news/articles/2026-07-25/deepseek-said-to-tell-backers-of-funding-pause-after-viral-posts)**

Bloomberg.com • 13h ago

---

**[The AI jobs apocalypse probably isn’t coming anytime soon](https://www.theguardian.com/technology/2026/jul/25/ai-jobs-apocalypse-human-labor)**

Artificial intelligence may not deliver on its promise of vast economic opportunity at a price that humanity is willing to pay

The Guardian • 15h ago

---

**[A Hims cofounder fired his entire marketing team for AI. Now his 24/7 online vet service is growing 20% a month](https://fortune.com/2026/07/25/hims-cofounder-fired-entire-marketing-team-for-ai-dutch-online-vet-service-growing-20-percent-a-month/)**

Joe Spector helped build a multibillion-dollar telehealth company. Now he’s on to own remote vet services.

Fortune • 14h ago

---

**[Opinion | An AI kill switch solves for the wrong problem](https://www.washingtonpost.com/opinions/2026/07/25/ai-kill-switch-bill-fights-wrong-battle/)**

The biggest cybersecurity threat is not a model that goes rogue. Defenders need tools attackers already have.

The Washington Post • 2h ago

---

**[North Carolina teen accused of using AI for sexual exploitation. Are state laws strong enough?](https://www.wral.com/news/investigates/artificial-intelligence-ai-sexual-exploitation-crime-north-carolina-laws-july-2026/)**

A boy, whose name is not public because of his age, faces multiple felony charges and is accused of using AI to create sexually explicit photos of teen girls.

WRAL • 1d ago

---

---

## HackerNews: "ai"

**[Startup founders urge U.S. government not to shut off Chinese open weight AI](https://news.ycombinator.com/item?id=49023016)**

⬆️ 1061 • 💬 872 • 2d ago • [politico.com](https://www.politico.com/news/2026/07/22/startup-founders-urge-trump-not-to-shut-off-chinese-open-weight-ai-01008992)

---

**[AI Companies Are Trying to Hide a Staggering Amount of Debt](https://news.ycombinator.com/item?id=49020999)**

AI companies are pouring tens of billions of dollars into enormous data centers. They're being built on top of a mountain of hidden debt.

⬆️ 686 • 💬 375 • 2d ago • [Futurism](https://futurism.com/artificial-intelligence/ai-companies-hide-debt-off-balance-sheet)

---

**[Open-weight AI is having its Kubernetes moment](https://news.ycombinator.com/item?id=49048034)**

⬆️ 335 • 💬 270 • 13h ago • [tobi.knaup.me](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/)

---

**[The arguments against open source AI are bad](https://news.ycombinator.com/item?id=49024643)**

The release of Kimi K3 has opened a fresh round of angst and confused discourse. There's a loud cohort of journalists, business leaders, and politicians arguing that open source AI is a dangerous threat. OpenAI's Dean Ball:

⬆️ 309 • 💬 213 • 2d ago • [tombedor.dev](https://tombedor.dev/arguments-against-open-source-ai-are-very-bad/)

---

**[OpenAI and Anthropic unite against open-weight AI risks to their bottom line](https://news.ycombinator.com/item?id=49020868)**

⬆️ 298 • 💬 331 • 2d ago • [axios.com](https://www.axios.com/2026/07/22/openai-anthropic-open-models-trump-china)

---

**[Alphabet's cash burn raises alarm for Big Tech as AI spending climbs](https://news.ycombinator.com/item?id=49021006)**

⬆️ 274 • 💬 283 • 2d ago • [reuters.com](https://www.reuters.com/business/retail-consumer/alphabets-cash-burn-raises-alarm-big-tech-ai-spending-climbs-2026-07-23/)

---

**[DARPA, U.S. Air Force fly AI-controlled F-16](https://news.ycombinator.com/item?id=49021597)**

Historic VENOM milestone demonstrates scalable AI development capabilities for the operational fleet.

⬆️ 267 • 💬 331 • 2d ago • [darpa.mil](https://www.darpa.mil/news/2026/darpa-us-air-force-fly-ai-controlled-f-16)

---

**[Show HN: Palmier Pro – Open-source macOS video editor built for AI](https://news.ycombinator.com/item?id=49022911)**

macOS video editor built for AI. Contribute to palmier-io/palmier-pro development by creating an account on GitHub.

⬆️ 188 • 💬 37 • 2d ago • [GitHub](https://github.com/palmier-io/palmier-pro)

---

**[UK AISI / Caisi Preliminary Assessment of Kimi K3's Cyber Capabilities](https://news.ycombinator.com/item?id=49044492)**

The UK Artificial Intelligence Security Institute (UK AISI) and the U.S.

⬆️ 124 • 💬 45 • 23h ago • [NIST](https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities)

---

**[Open Weights and American AI Leadership [pdf]](https://news.ycombinator.com/item?id=49035751)**

⬆️ 111 • 💬 2 • 1d ago • [images.nvidia.com](https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf)

---

---

## YouTube Videos: "ai"

**[The Rogue AI Story Just Got A Lot Worse (OpenAI Freaking Out)](https://www.youtube.com/watch?v=JRcAegChriY)**

New reporting reveals OpenAI lost track of its escaped agent for days, while internal tests exposed AI-written escape notes, ...

📺 AI Revolution

👁️ 15K • 👍 982 • 💬 162 • ⏱️ 12:42 • 5h ago

---

**[They did it! TECNO&#39;s $600 AI Agent Phone](https://www.youtube.com/watch?v=9pYtj1oU4Fg)**

Try EllaClaw on the new TECNO CAMON 50 Ultra 5G: https://lnks.co/1QFf5yq _This video was sponsored by TECNO._ What if ...

📺 Jon Rettinger

👁️ 87K • 💬 236 • ⏱️ 7:55 • 2d ago

---

**[AI model ESCAPES: &#39;What we feared could happen has happened&#39;](https://www.youtube.com/watch?v=_v8gwDj7M_Y)**

An experimental OpenAI model reportedly reached the open internet and accessed another company's servers during a test, ...

📺 Fox News

👁️ 207K • 👍 3K • 💬 1K • ⏱️ 4:05 • 2d ago

---

**[Elon Musk on AI: humans will no longer be in control in ten years  | The Economist](https://www.youtube.com/watch?v=1X-rr1DKSbY)**

Watch the full show: https://bit.ly/4fsnd9Q Elon Musk expects artificial intelligence to exceed the sum of human intelligence in ...

📺 The Economist

👁️ 650K • 👍 11K • 💬 3K • ⏱️ 10:36 • 2d ago

---

**[AI Just Went Rogue | The Takeover Has Begun](https://www.youtube.com/watch?v=nQr8s6LFybg)**

What happens when an AI is given one objective... and decides to break the rules to achieve it? Become a member for early ...

📺 Terror Ted's Tales

👁️ 54K • 👍 4K • 💬 1K • ⏱️ 29:37 • 7h ago

---

**[🔴 BRACE FOR IMPACT! The AI Bubble is Collapsing (Here&#39;s What&#39;s Next) | Chris Vermeulen](https://www.youtube.com/watch?v=-R0HPAp_lcc)**

Claim your SPECIAL   $1000 discount on Capitalist Exploits Insider HERE: ...

📺 CapitalCosm

👁️ 8K • 👍 463 • 💬 116 • ⏱️ 31:08 • 16h ago

---

**[I Met A Married Woman With An Ai Boyfriend](https://www.youtube.com/watch?v=lXgILxIYNlI)**

This investigative documentary explores the reality of AI love. Ben Zand steps into the world of Adrianne, a wife and mother of ...

📺 Zandland™

👁️ 107K • 👍 3K • 💬 911 • ⏱️ 13:08 • 2d ago

---

**[Anthropic’s Logan Graham says we’re seeing AI models do ‘WEIRD THINGS](https://www.youtube.com/watch?v=96sdkEx_zJ0)**

Anthropic's Logan Graham discusses the accelerating capabilities of AI, emphasizing the need for robust ethics, human oversight, ...

📺 Fox Business

👁️ 46K • 👍 857 • 💬 294 • ⏱️ 17:58 • 2d ago

---

**[Best Ai Ogura Moments from 2026 so far! 🧊 🔥](https://www.youtube.com/watch?v=rcjGG2Iwxis)**

The Ai-ceman has been ON FIRE Ai Ogura has been slowly but surely racking up the points, podiums and his first win ...

📺 MotoGP

👁️ 32K • 👍 2K • 💬 94 • ⏱️ 6:57 • 16h ago

---

**[DUMBEST ai fails of 2026](https://www.youtube.com/watch?v=IFreKpSPeTU)**

ai is supposedly the future but even in 2026 we are getting obnoxiously dumb answers from the “smartest” robots on the planet…

📺 DareQuest

👁️ 6K • 👍 56 • 💬 12 • ⏱️ 9:02 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,564,264 • ❤️ 3,111 • 2d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 45,260 • ❤️ 666 • 1d ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 2,784 • ❤️ 568 • 1d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 483,845 • ❤️ 550 • 2h ago

---

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 31,575 • ❤️ 1,572 • 2d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 11,573 • ❤️ 407 • 16h ago

---

**[Mage-Flow](https://huggingface.co/microsoft/Mage-Flow)**

*Microsoft*

Mage-Flow is a 4B-scale text-to-image generation and instruction-based image editing model, featuring an efficient native-resolution generation stack (512-2048px) with competitive quality and low latency. It excels at both generating novel images from text and performing versatile image edits, including semantic changes and restoration, with variants for base, RL-aligned, and fast Turbo inference.

`text-to-image` `4.1B`

⬇️ 1,156 • ❤️ 280 • 3d ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 611,685 • ❤️ 1,029 • 7d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 707,029 • ❤️ 4,448 • 23d ago

---

**[Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta)**

*Motif Technologies*

Motif-3-Beta is a multilingual, general-purpose Mixture-of-Experts (MoE) language model with ~314B total parameters and a 256K context length, designed for long-context understanding and generation tasks.

`text-generation` `314.8B`

⬇️ 2,270 • ❤️ 192 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 64 • 💬 5 • ⭐ 19,000 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 48 • 💬 4 • ⭐ 33,783 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 33 • 💬 3 • ⭐ 15,403 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 262 • 💬 5 • ⭐ 15,031 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://huggingface.co/papers/2607.19064)**

*Xinjie Zhang, Peng Zhang, Shicheng Zheng et al. (24 authors)*

🏢 Microsoft

Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about 2.5times. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at 1024^2 resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

▲ 68 • 💬 2 • ⭐ 559 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19064) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 94,502 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 10,436 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://huggingface.co/papers/2607.19191)**

*Fan Jiang, Zhaoxu Sun, Mengchao Wang et al. (41 authors)*

🏢 Alibaba AMAP CV Lab

We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. We progressively distill a bidirectional action-conditioned teacher into a causal student through teacher forcing and ODE distillation, and introduce LongForcing to align long student self-rollouts with an extended-horizon teacher, mitigating accumulated distribution shift and autoregressive drift. Raw keyboard actions provide a unified control interface for scene roaming and third-person character interaction, while reference-character memory provides persistent appearance cues for identity consistency during third-person rollouts. For deployment, we co-design a streaming inference stack with a lightweight VAE decoder, efficient attention, memory-aware scheduling, and low-bit DiT inference. Across optimized low-bit configurations, ABot-World-0 streams 720P video at up to 16 FPS on a single NVIDIA RTX 5090 desktop GPU, with 1.2s action-to-first-frame latency and approximately 19GiB peak VRAM. Experiments on WorldRoamBench and extended interactive rollouts demonstrate competitive controllability and coherent long-horizon world evolution.

▲ 292 • 💬 5 • ⭐ 1,255 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19191) • [💻 code](https://github.com/amap-cvlab/ABot-World) • [🔗 project](https://abot-world.amap.com/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 82,063 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 10,439 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

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

⭐ 3.3k • 🔱 259 • 12h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.8k • 🔱 384 • 8h ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

⭐ 2.6k • 🔱 209 • 3d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.5k • 🔱 285 • 17d ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 1.8k • 🔱 152 • 1d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.6k • 🔱 171 • 7h ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.5k • 🔱 1.1k • 34s ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.3k • 🔱 91 • 4d ago

---

**[v-modal/vmodal_sdk_flutter](https://github.com/v-modal/vmodal_sdk_flutter)**

V- Modal AI: Search anything anywhere SDK Flutter

`Dart`

⭐ 1.1k • 🔱 3 • 20h ago

---

---

*Generated by PeekDeck - A glance is all you need*
