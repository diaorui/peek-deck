---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-21T12:08:03.693809+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 21, 2026 at 12:08 UTC  
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

**[I thought AI would reduce my mental load](https://www.reddit.com/r/artificial/comments/1v297mb/i_thought_ai_would_reduce_my_mental_load/)**

I use AI constantly when coding, and in terms of output it’s amazing. The strange part is that I feel more drained at the end of the day than before. Instead of thinking through one solution myself, I’m reviewing pages of generated code trying to convince myself it’s actually correct. I don’t even know if it’s a trust issue or just information overload, but reviewing AI-generated code is becoming the most exhausting part of my workflow. Is this something other people are running into too, or have you found a better way to deal with it?

6h ago

---

**[Why I Left Google DeepMind By Alex Turner](https://www.reddit.com/r/artificial/comments/1v2f8df/why_i_left_google_deepmind_by_alex_turner/)**

I fought against Google’s Pentagon AI deal from the inside. Powerful people and institutions failed to keep their AI ethics promises under pressure.

🔗 [The Pond](https://turntrout.com/why-i-left-google-deepmind) • 1h ago

---

**[Looking for unique AI/ML project ideas (advanced level, research-worthy) — open to any field besides healthcare](https://www.reddit.com/r/artificial/comments/1v2a5z9/looking_for_unique_aiml_project_ideas_advanced/)**

Hey everyone, I'm working on a major/final-year AI/ML project and want to go beyond the usual "CNN on X-ray" or "chatbot with RAG" territory. Looking for something genuinely novel with a real use case — not just a rehash of a Kaggle tutorial. A bit about me/constraints: Comfort level: advanced, comfortable with deep learning, NLP, GNNs, etc. Timeframe: roughly a semester Open to any field — finance, agriculture, climate, cybersecurity, robotics, education, whatever has an interesting unsolved problem Ideally something with public datasets available (no lab/hardware access) Would love if it has a clear "why does this matter" story I can pitch to evaluators If you've seen a cool underexplored problem in a recent paper, worked on something similar, or have a "someone should really build this" idea sitting in your head — I'd love to hear it. Happy to share more details if anyone wants to dig in. Thanks in advance!

5h ago

---

**[SunoAI Data Breach: Discord mods giving timeouts to those who discuss it](https://www.reddit.com/r/artificial/comments/1v2f7pm/sunoai_data_breach_discord_mods_giving_timeouts/)**

Discover the magic of the internet at Imgur, a community powered entertainment destination. Lift your spirits with funny jokes, trending memes, entertaining gifs, inspiring stories, viral videos, and so much more from users.

🔗 [Imgur](https://i.imgur.com/cSTIB4d.png) • 1h ago

---

**[Measuring engineering productivity is harder than ever. Thanks AI!](https://www.reddit.com/r/artificial/comments/1v2c9eb/measuring_engineering_productivity_is_harder_than/)**

At OpenAI, engineers who lean heavily on Codex open roughly 70% more pull requests than colleagues who don’t – and the gap keeps widening, according to Sherwin Wu, who leads engineering for OpenAI’s API platform. Measuring engineering productivity has never been straightforward, and AI has made it harder.

🔗 [LeadDev](https://leaddev.com/reporting/measuring-engineering-productivity-is-harder-than-ever) • 3h ago

---

**[AheadForm Origin F1 at the World Artificial Intelligence Conference '26 in Shanghai](https://www.reddit.com/r/artificial/comments/1v2969s/aheadform_origin_f1_at_the_world_artificial/)**

6h ago

---

**[OxDeAI: I built a deterministic pre-execution authorization boundary for AI agents (fail-closed, signed artifacts, adapters for LangGraph/CrewAI/AutoGen, etc...), looking for feedback.](https://www.reddit.com/r/artificial/comments/1v2fp40/oxdeai_i_built_a_deterministic_preexecution/)**

Hey everyone. I'm the author of OxDeAI, an open-source protocol (Apache 2.0). Posting it here because I want critical feedback from people building real agents, not applause. The problem I keep hitting: as agents move from generating text to doing things (API calls, payments, infra provisioning, tool use), most stacks still enforce policy with best-effort checks inside the agent loop. That produces failure modes like retry amplification on non-idempotent actions, budget leaks, stale-state executions, and permission drift, all because the "check" and the "action" live in the same trust boundary. Core idea. Separate the decision from the enforcement. Agent proposes an intent, OxDeAI evaluates (intent, state, policy) deterministically, and if the result is ALLOW it issues a signed AuthorizationV1 artifact. A Guard/PEP then verifies that artifact before any side effect. No valid authorization means no execution path. Fail-closed by default, with single-use replay protection, explicit trust (trustedKeySets), and artifacts you can verify offline. What's actually there today: Signed decision artifacts plus a non-bypassable guard (the execution fn is only reachable through the guarded closure; there's a demo where a direct call gets refused). Adapters for LangGraph, CrewAI, AutoGen, OpenAI Agents SDK, and OpenClaw, all thin bindings that route through one universal guard. Single-hop scoped delegation (narrowing-only capabilities between agents). Cross-language conformance vectors (TS reference plus Go/Python harnesses) with byte-equivalence anchors on the canonicalization and revocation-list surfaces. Hash-chained audit envelopes for offline verification. Where I'm being honest about the stage: Cross-language reproducibility is complete on the serialization and KRL surfaces, but not yet on every authorization verdict (Go/Python don't harness the full verification surface yet). I don't want to claim "deterministic across all languages" when the vectors don't cover all of it. There's a micro-benchmark suggesting low per-action overhead, but it's single-process on my hardware, so treat it as indicative, not a production number. The harness is in bench/ if you want to poke at it. Open issues include an active hardening item around self-declared intent fields (an agent can currently influence which per-agent limits apply by choosing its own agent_id, which is being fixed) and a scoping issue for an eventual independent security review. No third-party security review yet, and I say so in the docs. It's early. TypeScript is the reference; the protocol surface is specified but evolving. This is not a prompt guardrail or a monitoring/observability tool. It sits at the execution boundary and is meant to compose with your existing framework, not replace it. Repo: https://github.com/oxdeai/oxdeai What I'd genuinely like to know: Have you hit these tool-calling / side-effect failure modes in production? How are you enforcing action-level policy today: inside the loop, at an API gateway, or somewhere else? If you tried an adapter, where did the integration hurt? For the security-minded: does the fail-closed / signed-artifact boundary hold up to how you'd attack it? Contributors welcome, especially for new adapters, policy examples, and the cross-language verdict coverage. See CONTRIBUTING.md and the open issues.

40m ago

---

**[Tinder: does anyone know how AI bots are now easily passing the "oval-shape live camera face challenge" Tinder is using for account signup? I hopped on tinder to see the state of the art in AI bots (selling crypto on Signal and the usual).](https://www.reddit.com/r/artificial/comments/1v1rsof/tinder_does_anyone_know_how_ai_bots_are_now/)**

Is there a simple kit someone has come up with to get through the "oval-shape live camera face challenge" .. or? Could it be as simple as the minimum wage scammer teams hold up a image of "Hen" there and move it in front of the camera? Does anyone know much about how the "oval-shape live camera face challenge" works, and/or how AI is defeating it? Using a small-city market location with about 100-150 swipees, I found ~3 hey-lets-use-signal bots, so there's 3% AI-signal-crypto bots on Tinder. Now .. Tinder's policy is, the instant someone taps "report" on a profile, and, selects the line from the chat where the profile mentions either "Signal" or "Telegram", Tinder axes it automatically there and then. Given that, I can't believe these bots survive very long, so there's gotta be quite a lot of production of them. Anyone have any ideas? BTW for the fake conversation, they are not using great models. It's still rather stilted. Even a non-AI-aware person, well guy, would be aware it's not a human with a (funny, really) form letter feel. ("I understand that you have been having a busy day. It must be demanding leading a commercial company.") fascinating stuff! Anyway I'm interested in how they pass the "oval-shape live camera face challenge" .. anyone?

18h ago

---

**[Trying free Claude from browser and it used my hardware!](https://www.reddit.com/r/artificial/comments/1v2dwc9/trying_free_claude_from_browser_and_it_used_my/)**

https://preview.redd.it/avh2o4bz1keh1.png?width=1085&format=png&auto=webp&s=79c46074ad757fba82755507217f3961e62111a9 -disclaimer: I am a layman- Is this normal? If so wtf why are people paying them to have it use their own hardware? Is this the future? They hold the terminal while we pay for everything? As soon as I send my prompt my gpu went 100% blasting fans

2h ago

---

**[Mercor: The $20 Billion Machine Feeding Frontier AI](https://www.reddit.com/r/artificial/comments/1v28n5s/mercor_the_20_billion_machine_feeding_frontier_ai/)**

Mercor got sued, hacked, and infiltrated by North Korean operatives—and investors are queuing up to write checks at a $20 billion valuation....

🔗 [beyondlayoff.com](http://www.beyondlayoff.com/2026/07/mercor.html) • 7h ago

---

---

## Google News: "ai"

**[Trump administration's head of AI safety agency resigns after 3 months on job](https://www.cnbc.com/2026/07/20/trumps-head-of-ai-safety-agency-caisi-resigns-after-months-on-job.html)**

Arvind Raman, the director of National Institute of Standards and Technology, will serve as acting director of CAISI, according to a spokesperson

CNBC • 16h ago

---

**[Scoop: Trump AI security agency head resigns](https://www.axios.com/2026/07/20/trump-ai-security-agency-head-resigns)**

Axios • 21h ago

---

**[Trump's AI Chief Resigns After Just Three Months](https://www.ndtv.com/artificial-intelligence/us-ai-safety-agency-head-chris-fall-resigns-after-three-months-amid-leadership-instability-11800897)**

US President Donald Trump's AI chief has resigned just three months after taking charge.

NDTV • 1h ago

---

**[How Google’s A.I. Search Is Imperiling the Open Web](https://www.nytimes.com/2026/07/20/technology/google-ai-open-web.html)**

The New York Times • 22h ago

---

**[Nebius stock surged after Nvidia disclosed a 9.3% stake in the AI cloud company](https://qz.com/nvidia-nebius-stake-ai-cloud-072126)**

Nebius stock rose 7% in premarket trading Tuesday after a filing showed Nvidia holds roughly 22.26 million shares in the neocloud firm

qz.com • 23m ago

---

**[Xi and Trump Can Both Claim Big Wins in AI Race](https://www.bloomberg.com/news/newsletters/2026-07-21/china-s-world-ai-conference-and-tsmc-s-arizona-investment-mark-wins-for-leaders)**

Bloomberg.com • 6m ago

---

**[The Pentagon Is Using This $1.2 Billion Startup’s AI To Automate Cyberwarfare](https://www.forbes.com/sites/thomasbrewster/2026/07/21/the-pentagon-is-using-this-12-billion-startups-ai-to-automate-cyberwarfare/)**

Khosla Ventures is putting $30 million into Twenty, a cyber startup that uses AI models from Anthropic and OpenAI to run hacking campaigns for the Department of War.

Forbes • 13m ago

---

**[Google parent Alphabet to report Q2 earnings in latest test of AI trade](https://finance.yahoo.com/technology/article/google-parent-alphabet-to-report-q2-earnings-in-latest-test-of-ai-trade-110000124.html)**

Google will report its second quarter earnings after the bell on Wednesday.

Yahoo Finance • 1h ago

---

**[AI-generated sexual content is starting to affect how teenagers view sex, consent and body image](https://www.cnn.com/2026/07/21/health/teens-generative-ai-sexual-content-wellness)**

As generative AI becomes more widespread and sophisticated, experts urge parents to keep an eye on how teens use the technology to create explicit content.

CNN • 3h ago

---

**[Opinion | The AI tax movement is built on a myth](https://www.washingtonpost.com/opinions/2026/07/21/ai-taxes-hurt-american-workers/)**

Washington wants to help American workers. Taxing artificial intelligence would do the opposite.

The Washington Post • 1h ago

---

---

## HackerNews: "ai"

**[China’s open-weights AI strategy is winning](https://news.ycombinator.com/item?id=48979269)**

China's open-weights AI strategy is winning: its companies are taking the lead. America's closed-first, locked-down strategy is doomed to failure - and it could take the US economy down with it.

⬆️ 1136 • 💬 857 • 21h ago • [Ben Werdmuller](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/)

---

**[Airport Simulator](https://news.ycombinator.com/item?id=48976846)**

The sky (and your endurance) is the limit!

⬆️ 806 • 💬 154 • 1d ago • [Airport Simulator](https://airport.apunen.com/)

---

**[NYC may require landlords and realtors to disclose the use of AI in listings](https://news.ycombinator.com/item?id=48962983)**

No more AI-edited listings without disclosures.

⬆️ 591 • 💬 265 • 2d ago • [PetaPixel](https://petapixel.com/2026/07/16/mayor-mamdani-says-landlords-cant-secretly-use-ai-images-to-advertise-properties/)

---

**[AI Mania Is Eviscerating Global Decision-Making](https://news.ycombinator.com/item?id=48964185)**

⬆️ 440 • 💬 282 • 2d ago • [ludic.mataroa.blog](https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/#fnref:3)

---

**[AI advice made people less accurate but more confident – sudy](https://news.ycombinator.com/item?id=48971738)**

A study found that access to AI advice collapsed people's willingness to say "I don't know" from 44% to 3%, while accuracy dropped from 27% to 9%.

⬆️ 360 • 💬 207 • 1d ago • [TNW | Artificial-Intelligence](https://thenextweb.com/news/ai-advice-suppresses-critical-thinking-wrong-answers-study)

---

**[Five US tech giants' hidden debts soar to $1.65T on opaque AI funding](https://news.ycombinator.com/item?id=48987863)**

Data center leases, GPU supply contracts raise liabilities at Meta, Oracle, Nikkei study shows

⬆️ 297 • 💬 199 • 8h ago • [Nikkei Asia](https://asia.nikkei.com/business/technology/five-us-tech-giants-hidden-debts-soar-to-1.65tn-on-opaque-ai-funding)

---

**[Moonshot AI suspends new subscriptions due to Kimi K3 demand](https://news.ycombinator.com/item?id=48969291)**

Kimi K3 has received far more love than we expected, and our GPUs are feeling it.

Over the past 48 hours, demand has pushed close to the limits of our current capacity. To protect the experience of existing subscribers, we're temporarily pausing new subscriptions and

⬆️ 283 • 💬 112 • 1d ago • [X (formerly Twitter)](https://twitter.com/kimi_moonshot/status/2078855608565207130)

---

**[How we measured AI writing across arXiv, and where the measurement breaks](https://news.ycombinator.com/item?id=48981206)**

We scored the full text of 12,750 arXiv papers and found that about a third of new ones read as machine-written. Here is the method, the results, and an honest account of the limitations.

⬆️ 226 • 💬 156 • 19h ago • [unslop](https://unslop.run/blog/measuring-ai-writing-on-arxiv)

---

**[Airbus Takes Flight from AWS](https://news.ycombinator.com/item?id=48976682)**

Which way to the Land of the Free again?

⬆️ 207 • 💬 163 • 1d ago • [theregister](https://www.theregister.com/columnists/2026/07/20/airbus-takes-flight-from-aws-what-happens-next-is-critical/5274109)

---

**[Launch HN: Bloomy (YC S26) – AI-powered mastery learning for K-12](https://news.ycombinator.com/item?id=48981136)**

⬆️ 89 • 💬 92 • 19h ago

---

---

## YouTube Videos: "ai"

**[AI Companies Are Terrified.](https://www.youtube.com/watch?v=eLCF6LdkzAQ)**

Thanks to Micro Center for sponsoring this video! Shop Back to School Tech Deals: https://micro.center/a6ef91 Sign up for a FREE ...

📺 TechLinked

👁️ 195K • 👍 12K • 💬 777 • ⏱️ 8:30 • 11h ago

---

**[Can An AI Punish You In The Future? 😨](https://www.youtube.com/watch?v=nPqO8z21i5I)**

📺 Zack D. Films

👁️ 2.3M • 👍 168K • 💬 8K • ⏱️ 0:46 • 1d ago

---

**[South Korea’s AI Bubble Just Popped](https://www.youtube.com/watch?v=hy90LdpEUvQ)**

South Korea's AI Bubble Just Popped ▻ Get 20% off DeleteMe US consumer plans when you go to ...

📺 Andrei Jikh

👁️ 1.3M • 👍 38K • 💬 3K • ⏱️ 25:10 • 19h ago

---

**[The Real Motive Behind Windows 11 AI](https://www.youtube.com/watch?v=hWJRDvQuTDA)**

Ever wonder why Microsoft continues to aggressively shove AI and Copilot into every corner of Windows 11, despite massive ...

📺 CyberCPU Tech

👁️ 12K • 👍 1K • 💬 515 • ⏱️ 16:52 • 22h ago

---

**[China World AI Conference Mocked: No Western Nations Attend, Turns Into A “Beggar’s Fair”](https://www.youtube.com/watch?v=B1ThwmDJmn0)**

On July 17, the Shanghai Pudong World Expo Center hosted a heavily promoted event by Chinese authorities — the 2026 World ...

📺 China Observer

👁️ 36K • 👍 2K • 💬 402 • ⏱️ 16:56 • 2d ago

---

**[Chinese open source AI model threatens to disrupt tech market boom: Verrender | ABC NEWS](https://www.youtube.com/watch?v=xBS2Sn7AL6o)**

Chinese startup Moonshot is preparing to release its AI model Kimi K3, which it claims will rival flagship platforms from Anthropic ...

📺 ABC News (Australia)

👁️ 7K • 👍 146 • ⏱️ 4:58 • 2h ago

---

**[Urgent Update- AI Sputnik Moment: Kimi K3 Released w/ Emad Mostaque | Ep. 272](https://www.youtube.com/watch?v=pSUyLfirP8Y)**

The mates chat with Emad Mostaque on an urgent update regarding the AI Sputnik Moment of Kimi K3 being released. Get access ...

📺 Peter H. Diamandis

👁️ 232K • 👍 6K • 💬 1K • ⏱️ 2:07:31 • 1d ago

---

**[Alex Hormozi’s Warning: Stop Chasing AI, Build This Instead!](https://www.youtube.com/watch?v=HwmwyBgzj8c)**

Every founder is being told to build an AI company. Alex Hormozi says almost all of them will be gone within months, that the best ...

📺 The Diary Of A CEO

👁️ 526K • 👍 13K • 💬 1K • ⏱️ 2:22:38 • 1d ago

---

**[The AI Apocalypse Has a Plot Hole](https://www.youtube.com/watch?v=_4FfTkOCmCM)**

Subscribe to Absolutely Agentic https://absolutelyagentic.com/upgrade Sign up to our newsletter ...

📺 Absolutely Agentic

👁️ 14K • 👍 683 • 💬 375 • ⏱️ 36:11 • 19h ago

---

**[China&#39;s AI just shocked Wall Street](https://www.youtube.com/watch?v=_fNhzoiZdNI)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 144K • 👍 7K • 💬 2K • ⏱️ 14:15 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 16,441 • ❤️ 1,312 • 18h ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 432,196 • ❤️ 880 • 3d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,404,962 • ❤️ 558 • 3d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 2,237,351 • ❤️ 2,516 • 1h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 545,109 • ❤️ 4,247 • 19d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,133,420 • ❤️ 2,379 • 6d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 62,842 • ❤️ 200 • 1d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 465 • 37m ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 1,997,690 • ❤️ 2,950 • 3mo ago

---

**[OvisOCR2](https://huggingface.co/ATH-MaaS/OvisOCR2)**

*ATH-MaaS*

OvisOCR2 is a compact 0.8B multimodal model for end-to-end document parsing, generating Markdown from document images. It excels at extracting text, formulas, tables, and visual regions in natural reading order, achieving state-of-the-art performance on benchmarks like OmniDocBench.

`image-text-to-text` `853.0M`

⬇️ 17,162 • ❤️ 227 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 30 • 💬 3 • ⭐ 14,386 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 55 • 💬 5 • ⭐ 15,867 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 9,993 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 9,904 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 259 • 💬 4 • ⭐ 13,653 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 93,826 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://huggingface.co/papers/2607.15330)**

*Xiaomi Robotics Team, Jun Guo, Piaopiao Jin et al. (34 authors)*

🏢 Xiaomi Robotics

We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data. We propose a two-stage training recipe consisting of pre-training and post-training. During pre-training, we imbue the model with broad and generalizable action-generation capabilities by training on over 100k hours of real-world manipulation trajectories collected via UMI devices. Crucially, we develop a scalable auto-labeling pipeline that annotates trajectory clips with natural languages describing scene state transitions, providing rich and precise conditioning for action learning. During post-training, we aim to align these capabilities with robot embodiments and imperative instructions that humans naturally use to prompt robots. Extensive experiments demonstrate strong scaling behavior. Xiaomi-Robotics-1 consistently improves with increased data scales and model sizes during pre-training. This scaling behavior directly transfers to post-training, where a stronger pre-training model yields better out-of-the-box real-robot performance in unseen environments. Furthermore, Xiaomi-Robotics-1 serves as a strong robot foundation policy that can be efficiently fine-tuned on complex, dexterous tasks with high data efficiency. Across multiple simulation benchmarks, Xiaomi-Robotics-1 outperforms state-of-the-art methods. Notably, it establishes a new state-of-the-art with a 57.6% success rate on RoboCasa365, surpassing the previous best of 46.6%. Furthermore, it achieves an average score of 20.07 on RoboDojo, significantly outperforming the prior state-of-the-art (13.07). Code and model checkpoints will be released. Project page: https://robotics.xiaomi.com/xiaomi-robotics-1.html

▲ 59 • 💬 2 • ⭐ 172 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.15330) • [💻 code](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) • [🔗 project](https://robotics.xiaomi.com/xiaomi-robotics-1.html)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,451 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 75,239 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 18 • 💬 2 • ⭐ 21,028 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.1k • 🔱 1.0k • 13h ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.0k • 🔱 231 • 16m ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.7k • 🔱 372 • 4d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.4k • 🔱 270 • 12d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 1.0k • 🔱 62 • 7d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 988 • 🔱 17 • 13d ago

---

**[HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC)**

OpenOPC: Build Your Personal AI-Native Company — Self-Built, Self-Run, Self-Grown

`Python`

⭐ 940 • 🔱 153 • 29m ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 931 • 🔱 208 • 10d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 898 • 🔱 38 • 20d ago

---

**[ai4s-research/open-science](https://github.com/ai4s-research/open-science)**

Open Science Desktop — local-first, model-agnostic AI research workbench for macOS, Windows & Linux. Open-source Claude Science desktop alternative built on Tauri + MCP + agent skills.

`TypeScript` `ai-agent` `ai-for-science` `ai-scientist` `ai4s` `claude-science`

⭐ 863 • 🔱 98 • 31m ago

---

---

*Generated by PeekDeck - A glance is all you need*
