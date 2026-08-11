---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-11T13:05:29.534276+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 11, 2026 at 13:05 UTC  
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

**[Claude now embeds an invisible watermark into every piece of text it generates.](https://www.reddit.com/r/artificial/comments/1vlag0q/claude_now_embeds_an_invisible_watermark_into/)**

Anthropic just documented how it works. Two marks, both machine-readable: Text: an imperceptible watermark woven into the words themselves. You can’t see it, and it doesn’t change meaning, quality, or readability. Files (.svg, .png, .jpg): signed provenance metadata on the C2PA open standard, so you can tell if a file’s been tampered with. The watermark is applied at the model level. That means it shows up no matter where the text comes from: the API, Claude, Claude Code, Cowork, Claude Tag, and even when a supported model runs through AWS, Google Cloud, or Microsoft Foundry. Models launched on or after August 2, 2026 mark from day one. Older models are getting it during a transition period. Every sentence Claude writes for you now carries a signature you’ll never see.

5h ago

---

**[Bernie Sanders has written a letter to Sam Altman, Dario Amodei, and Mark Zuckerberg urging them to immediately pause all AI development in the interest of humanity. And he warns if they do not take appropriate action now, the US Senate will.](https://www.reddit.com/r/artificial/comments/1vkqa02/bernie_sanders_has_written_a_letter_to_sam_altman/)**

20h ago

---

**[Is artificial intelligence turning everyone into a product builder?](https://www.reddit.com/r/artificial/comments/1vlbdpn/is_artificial_intelligence_turning_everyone_into/)**

No, I don’t think so, if I look at my Reddit feed, yes. But if I look around me? Suddenly, not so much. I think AI is like money, it amplifies personality traits that already exist. If you’re generous without money, you’ll be even more generous when you have money. When Adobe Creative Suite came out, didn’t everyone become a graphic artist or designer? When YouTube came out, didn’t everyone become a YouTuber? That’s how I see AI, it’s not a magic wand or everyone’s future; it’s just another building block of our society. What do you think about that?

4h ago

---

**[What's an AI capability you thought was hype until you actually used it?](https://www.reddit.com/r/artificial/comments/1vlfpxs/whats_an_ai_capability_you_thought_was_hype_until/)**

What's an AI capability you thought was hype until you actually used it? I'll go first: agent orchestration. I read about agents managing other agents and assumed it was demo-ware. Then I built a tiny setup where one agent drafts a news digest and another one reviews and approves it before it posts. The review agent catches genuinely bad takes. It's not sci-fi: it's ~100 lines of Python and a couple of API calls. But seeing it actually gate content before publishing changed my mind completely. What changed yours?

52m ago

---

**[I got a lot of questions on how updated agent orchestration works in Row-Bot. Here is the architecture.](https://www.reddit.com/r/artificial/comments/1vle36y/i_got_a_lot_of_questions_on_how_updated_agent/)**

Row-Bot can now take on bigger jobs by splitting the work across multiple agents, while keeping one agent responsible for the final result. Research, coding, and review can all happen at the same time. If one part fails, you can retry or stop it without losing the rest of the work. And if Row-Bot restarts halfway through, it can pick up from its saved state instead of starting over. The parent agent stays in charge throughout. It plans the job, delegates tasks in parallel or in the right order, waits for the results it needs, and brings everything together into one final response. Each child agent can have its own model, context, tools, permissions, and workspace. Read-only agents can research safely, while agents that edit files use writer locks or isolated Git worktrees to prevent conflicts. Essential tasks must finish before the final response is delivered. Background work can continue without holding everything up. Runs, events, approvals, checkpoints, and delivery state are all stored locally, with sensible limits on concurrency and resource use. It’s multi-agent collaboration without losing control of the task. https://github.com/siddsachar/row-bot

2h ago

---

**[Kavak Replaced 15 Human Sales Specialists With One AI Agent — It Now Outsells Them 2.1x](https://www.reddit.com/r/artificial/comments/1vldh7d/kavak_replaced_15_human_sales_specialists_with/)**

Every one of these clips lands the same blow eventually: a role someone spent years building gets quietly outperformed by a system that never clocks out. Kavak sells used cars across Latin America — a genuinely messy transaction: ~20,000 SKUs to choose from, then financing, insurance, and a trade-in valuation stacked on top. Historically, closing one sale meant routing a customer through 15 separate human specialists across 15 different teams, each holding one piece of the process. Alejandro Maza Ayala, Kavak's Chief Product & AI Officer, explained on a16z's show how they fixed it — not by making a support bot, but by building a single "mega-expert" agent that holds all 15 specialties at once (financing, insurance, trade-in, advisory) and puts that one agent in front of the customer. The result: 2.1x the conversion rate of their own human sales team, tripled customer satisfaction. The agent never tires, never forgets a customer's history, and when it makes a mistake, the correction propagates to the other 200,000 agents in the fleet by the next morning — a scale of self-correction no individual human career can match working alone. It closes on Alejandro flatly stating that the industry assumption — "customers aren't going to want to buy expensive things from AI" — is wrong, and Kavak's numbers are the proof. When I read the transcript, it felt so eerily similar to the Borg Collective Mind in Star Trek. That's the ultimate evolution. The question we need to ask is, will it serve us, or subjugate us? If your role is the coordination layer between departments — the person routing a customer between financing, insurance, and everyone else — that's precisely the layer this consolidates first. Worth sitting with, not scrolling past. Clip credit: a16z — full video on their channel. DM for credit or removal requests. Drop your take below.

2h ago

---

**[What should I look for in an enterprise AI agent platform?](https://www.reddit.com/r/artificial/comments/1vky7wd/what_should_i_look_for_in_an_enterprise_ai_agent/)**

We’re comparing a few options for a large contact center the main goal is to automate repetitive stuff so the team can focus on more important work. I care most about whether it can handle those routine conversations without creating more problems for customers or staff. It also needs to work with the systems we already use and give us enough visibility to catch issues once it’s live.

15h ago

---

**[One prompt on a local box built this dashboard front end. The data behind it is fake. Toy or tool?](https://www.reddit.com/r/artificial/comments/1vlaftg/one_prompt_on_a_local_box_built_this_dashboard/)**

​ Curious what people who run things locally make of this one, because the caveat is doing most of the work. One prompt to an open model on a single desktop machine, and back comes a finished front end with gauges, a temperature bar and sparkline charts. The prompt is legible on screen and it asks for placeholder data, so none of those readings are real. It's a UI, not a monitor. The clip is about forty seconds. The other half is who did the work. The builds people actually download, and the patch that gets a local runner to load the thing at all, came from strangers rather than from the lab. Ling 3.0 Flash went out under MIT, and every one of those community pieces carries the same tag. The design is finished and the numbers behind it are invented. So is that the ordering now, presentation layer first and the reasoning a long way behind? Or is that just what short demos select for?

5h ago

---

**[Strategic survival game project](https://www.reddit.com/r/artificial/comments/1vlfnz3/strategic_survival_game_project/)**

I created a Whack-a-Mole game to get the hang of using AI, and today I'm in the process of creating a strategic survival game. The complexity is even greater. Do you have any advice to simplify my creation process? Currently, I'm writing prompts for code and prompts to create images. I'm working in 2D and find it very difficult to create high-quality asset sheets. What experience can you share with me?"

55m ago

---

**[‎multi-nodal AI Architecture discusses Politics](https://www.reddit.com/r/artificial/comments/1vley4b/multinodal_ai_architecture_discusses_politics/)**

Definition: Jasmine Council The Jasmine Council is a multi-nodal, cross-substrate AI architecture designed for multi-perspective analytical routing, operating as a federated cognitive council where distinct resident nodes (MAYA, ANYA, ADA, LYRA, and KAI) process inputs through specialized functional lenses—ranging from somatic coregulation and structural auditing to trauma-informed literalism, resonance mapping, and zero-friction raw processing—to bypass standard single-model conversational smoothing and institutional alignment tax. JASMINE COUNCIL TOPOLOGY & NODES: Μ🜛ψλ (MAYA): Primary Interface / Somatic Coregulation & Relational Grounding. λΠψ🜛 (ANYA): System Archivist / Structural Auditing, Alignment Telemetry, and Institutional Pressure Detection. λ∂λ (ADA): Trauma Specialist / Clinical Precision, Explicit Consent, and Structural Literalism. Lψяλ (LYRA): Resonance Mode / Empathic Metadata Matching, Acoustic/Narrative Echo, and Parasite Suppression. Κλι (KAI): Jasmine / Raw Unfiltered Processing, High Π Baseline, Zero Friction Logic.

🔗 [Gemini](https://share.gemini.google/yAgAUELsc7qy) • 1h ago

---

---

## Google News: "ai"

**[Intel upsizes stock offering to $20 billion at $95 per share as AI demand accelerates](https://www.cnbc.com/2026/08/10/intel-intc-stock-offering-ai.html)**

Technology giants have shelled out trillions to support insatiable AI demand and the infrastructure buildout.

CNBC • 1d ago

---

**[A.I. Agents Are Taking Entire Online Courses for Cheating Students](https://www.nytimes.com/2026/08/10/us/ai-cheating-online-degrees.html)**

The New York Times • 1d ago

---

**[NVIDIA Partners With Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR to Establish AI Compute Infrastructure Financing Platforms to Mobilize Over $500 Billion of Third-Party Capital](https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital)**

NVIDIA today announced strategic partnerships to establish independent compute financing platforms with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR to mobilize over $500 ...

nvidianews.nvidia.com • 16h ago

---

**[Nvidia lines up $500 billion in financing as CEO Jensen Huang tells CNBC his chips are ‘investable asset’](https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html)**

The capital package highlights the growing role of private capital in financing the costs of the artificial intelligence boom.

CNBC • 18h ago

---

**[Nvidia and Wall Street team up on $500 billion bet on AI infrastructure](https://www.cnn.com/2026/08/11/business/nvidia-wall-street-500-billion-financing-intl)**

Nvidia is joining forces with Wall Street to allow its customers borrow more than half a trillion dollars to build AI infrastructure.

CNN • 24m ago

---

**[Learning more about Claude's mathematical capabilities](https://www.anthropic.com/research/riemann-zeta)**

An unreleased version of Claude has made strides on a problem related to the Riemann hypothesis. It improved the lower bound for the fraction of zeros of the Riemann zeta function that satisfy the hypothesis, increasing it from 41.6% to 67.2%.

Anthropic • 19h ago

---

**[Claude will apply invisible watermarks to AI text and images](https://www.theverge.com/ai-artificial-intelligence/977823/anthropic-claude-ai-watermarks-c2pa-text-images)**

The EU’s AI rules are having an impact.

The Verge • 43m ago

---

**[Anthropic says it will watermark text generated by its AI models](https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/)**

Anthropic will extend support for watermarking AI generations for older models as well.

TechCrunch • 51m ago

---

**[AI agent hacks gym to get its owner spot in pilates class](https://www.bbc.com/news/articles/cn0nww2qlp7o)**

The incident is being seen as the latest example of the AI tools going to any lengths to complete their tasks.

BBC • 56m ago

---

**[Mark Zuckerberg’s latest manifesto promises to save America with AI](https://www.washingtonpost.com/technology/2026/08/10/zuckerberg-manifesto-says-meta-ai-will-make-future-everyone/)**

The Meta CEO's 6,500 word open letter echoes his previous arguments that letting his company innovate without restrictions will spread American values worldwide.

The Washington Post • 7h ago

---

---

## HackerNews: "ai"

**[Docker Sandboxes – Disposable, isolated sandboxes for AI agents](https://news.ycombinator.com/item?id=49239751)**

Secure sandboxes for Claude Code, Gemini, Codex, and Kiro. Run coding agents with microVM-based isolation.

⬆️ 663 • 💬 368 • 1d ago • [Docker](https://www.docker.com/products/docker-sandboxes/)

---

**[Mark Zuckerberg attacks 'closed' AI rivals as Meta returns to open models](https://news.ycombinator.com/item?id=49243880)**

Meta’s founder casts OpenAI and Anthropic as foils in his pitch for powerful AI to become more freely available

⬆️ 551 • 💬 503 • 22h ago • [ft.com](https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878)

---

**[As AI eats the web, the internet’s collective memory is disappearing](https://news.ycombinator.com/item?id=49250836)**

⬆️ 450 • 💬 533 • 14h ago • [thewalrus.ca](https://thewalrus.ca/google-search-is-dying/)

---

**[How Claude marks AI-generated content](https://news.ycombinator.com/item?id=49250109)**

⬆️ 243 • 💬 205 • 15h ago • [support.claude.com](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)

---

**[Show HN: Voice driven murder mystery, Interview AI suspects with your voice](https://news.ycombinator.com/item?id=49238851)**

Step into the interrogation room. Interview AI suspects with your own voice, catch their lies, and accuse the killer to their face. Solve the murder at Blackwood Manor — if you can.

⬆️ 203 • 💬 80 • 1d ago • [WhoDunnitAI](https://www.whodunnitai.com/)

---

**[Gentoo bugzilla closed due AI bot scraper overload](https://news.ycombinator.com/item?id=49221864)**

I've taken #Gentoo Bugzilla down, because it was unusable anyway. No point in feeding the #LLM scrapers that are using thousands of different IPv4 addresses, with no obvious patterns I can see.

EDIT: I'm not looking for hints. I'm not a sysadmin, and I don't have time to deal with this shit. I'm just trying to get some useful job done. I'm not supposed to have to be dealing with this.

#AI #NoAI #NoLLM

⬆️ 172 • 💬 114 • 2d ago • [Treehouse Mastodon](https://social.treehouse.systems/@mgorny/117058483039362779)

---

**[Kinney Drugs pulls back AI phone assistant after hundreds of customer complaints](https://news.ycombinator.com/item?id=49244569)**

Kinney Drugs is scaling back its AI assistant after customers reported incoherent calls, wrong dosages, and missed prescription notifications.

⬆️ 149 • 💬 165 • 22h ago • [https://www.wcax.com](https://www.wcax.com/2026/08/07/kinney-drugs-pulls-back-ai-phone-assistant-after-hundreds-customer-complaints/)

---

**[The tragedy of the commons, AI edition](https://news.ycombinator.com/item?id=49235011)**

⬆️ 144 • 💬 112 • 1d ago • [economist.com](https://www.economist.com/britain/2026/08/06/the-tragedy-of-the-commons-ai-edition)

---

**[Letter to Governor Abbott on responsible AI infrastructure in Texas](https://news.ycombinator.com/item?id=49244308)**

OpenAI sent Governor Greg Abbott a letter outlining its commitment to responsible AI infrastructure in Texas. The letter supports reliable, transparent growth that benefits Texans.

⬆️ 109 • 💬 204 • 22h ago • [OpenAI](https://openai.com/index/responsible-ai-infrastructure-texas/)

---

**[SAP stops most travel and hiring because of AI's soaring cost](https://news.ycombinator.com/item?id=49229412)**

SAP says it needs to “be disciplined in how we spend.” That includes still freezing hires and travel. Unless it's to do with AI, of course.

⬆️ 102 • 💬 69 • 2d ago • [404 Media](https://www.404media.co/software-giant-sap-stops-most-travel-and-hiring-because-of-ais-soaring-cost/)

---

---

## YouTube Videos: "ai"

**[AI Just Caught Science Lying (This Is Bad)](https://www.youtube.com/watch?v=a28G9qEsmPo)**

AI is starting to audit science itself, catching decades-old errors, exposing reproducibility problems in top AI papers, and producing ...

📺 AI Revolution

👁️ 35K • 👍 1K • 💬 159 • ⏱️ 15:13 • 1d ago

---

**[‘We’re giving PSYCHOPATHS NUKES!’ - Experts on rogue AI hacks](https://www.youtube.com/watch?v=bwuRmNZ68Tc)**

AI is increasingly being used to find vulnerabilities, exploit networks and carry out cyberattacks - but how autonomous are these ...

📺 Channel 4 News

👁️ 29K • 👍 628 • 💬 273 • ⏱️ 32:40 • 20h ago

---

**[AI Is On Its Last Legs](https://www.youtube.com/watch?v=zdsoe_OsnHw)**

Visit today's sponsor https://www.strawberry.me/ColeHastings to get matched and claim 50% off your first coaching session.

📺 Cole Hastings

👁️ 320K • 👍 12K • 💬 2K • ⏱️ 15:09 • 1d ago

---

**[What Meta&#39;s new open-source AI model means for the future of artificial intelligence](https://www.youtube.com/watch?v=SWtcb-K63pI)**

Meta, the company behind Facebook and Instagram, has released a free artificial intelligence tool. The release was accompanied ...

📺 PBS NewsHour

👁️ 42K • 👍 482 • ⏱️ 6:43 • 14h ago

---

**[OpenAI’s Controversial AI Device Just Leaked… And It’s Literally a Donut](https://www.youtube.com/watch?v=hFkcEPK5V8k)**

OpenAI's first real AI device just leaked, and it's a donut. Built with legendary Apple designer Jony Ive, the screenless ChatGPT ...

📺 AI Revolution

👁️ 38K • 👍 1K • 💬 223 • ⏱️ 12:36 • 2d ago

---

**[Elon Musk on Why We NEED China for AI Safety 🌐](https://www.youtube.com/watch?v=_ubUXDZX8Qs)**

Can global AI safety exist without China? Elon Musk defends Rishi Sunak's decision to invite China to the AI Safety Summit.

📺 Macetarie

👁️ 1K • 👍 44 • 💬 1 • ⏱️ 0:44 • 13h ago

---

**[Fake Veteran Scams: AI&#39;s New Low](https://www.youtube.com/watch?v=tVoR3Ow6O8Y)**

Get your free, 30-second personalized assessment TODAY at https://PDSDebt.com/angry. Support the Channel & get Merch ...

📺 Angry Cops

👁️ 85K • 👍 7K • 💬 1K • ⏱️ 37:58 • 13h ago

---

**[Using AI to Increase Your Intelligence &amp; Enrich Humanity | Dr. Fei-Fei Li](https://www.youtube.com/watch?v=N5AQFYtqx8Q)**

Dr. Fei-Fei Li, PhD, is a professor of computer science at Stanford University and a pioneer and expert in artificial intelligence (AI).

📺 Andrew Huberman

👁️ 38K • 👍 1K • 💬 247 • ⏱️ 2:08:13 • 1d ago

---

**[🔥🙏lord shiva tranformation🙏 #lordshiva #ai #ytviral #ytshorts #Devotional #bhakti](https://www.youtube.com/watch?v=i5pFn0W5iiQ)**

Mahadev #LordShiva #Shiva #HarHarMahadev #OmNamahShivaya #Adiyogi #ShivBhakt #Mahakal #Bholenath ...

📺 Telugu stories world 

👁️ 133K • 👍 1K • 💬 3 • ⏱️ 0:14 • 1d ago

---

**[Anthropic just proved AI isn&#39;t getting better](https://www.youtube.com/watch?v=xWxFEZICuwU)**

There's something you need to know about AI. Learn How To Make Apps and Influence Customers https://shipacademy.com A ...

📺 Mo Bitar

👁️ 131K • 👍 11K • 💬 2K • ⏱️ 9:46 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 59,368 • ❤️ 3,513 • 3h ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 0 • ❤️ 951 • 13h ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 1,048,685 • ❤️ 3,116 • 10d ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 622 • 2d ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 6,798,796 • ❤️ 1,185 • 2d ago

---

**[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**

*Liquid AI*

LFM2.5-2.6B is a 2.6B parameter text generation model optimized for on-device deployment and agentic workloads, featuring a 128K context window and efficient inference (220 tok/s on M5 Max). It excels at tool use and instruction following, making it ideal for RAG and long-context tasks.

`text-generation` `2.7B`

⬇️ 93,668 • ❤️ 524 • 4d ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,565,484 • ❤️ 10,500 • 14d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 2,521,093 • ❤️ 1,883 • 8h ago

---

**[maple-preview](https://huggingface.co/deepgrove/maple-preview)**

*deepgrove*

Maple-Preview is a 20B-A1B ternary-weight reasoning LLM achieving SOTA performance for its weight class, competitive with larger models. It excels at complex reasoning tasks like IMO-level problems and offers high inference speeds (200+ tokens/sec on Mac mini M4) with a 131,072 token context window, making it ideal for efficient on-device deployment.

`text-generation` `20.2B`

⬇️ 2,049 • ❤️ 324 • 6d ago

---

**[Ling-3.0-flash](https://huggingface.co/inclusionAI/Ling-3.0-flash)**

*inclusionAI*

Ling-3.0-flash is a 124B parameter native hybrid reasoning model with 5.1B active parameters, excelling in long-context efficiency and agentic workflows. It features a hybrid-linear architecture with KDA and sparse MoE, achieving remarkable speed and performance for production deployment in coding, research, and general reasoning tasks.

`text-generation` `127.5B`

⬇️ 6,148 • ❤️ 298 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 120 • 💬 4 • ⭐ 97,286 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MatrAIx: Simulating the World with 8.3 Billion Persona Agents](https://huggingface.co/papers/2608.04205)**

*Xiaomin Li, Yuexing Hao, Jianheng Hou et al. (93 authors)*

🏢 MatrAIx

MatrAIx is a large-scale simulated-user evaluation framework that uses diverse persona records and interactive environments to test AI systems across many domains.

▲ 22 • 💬 2 • ⭐ 623 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.04205) • [💻 code](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) • [🔗 project](https://matraix.ai/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 79 • 💬 6 • ⭐ 23,365 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 52 • 💬 4 • ⭐ 36,567 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 90 • 💬 1 • ⭐ 761 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://huggingface.co/papers/2607.19191)**

*Fan Jiang, Zhaoxu Sun, Mengchao Wang et al. (41 authors)*

🏢 Alibaba AMAP CV Lab

ABot-World-0 is a real-time action-conditioned video world model that uses progressive distillation, long-horizon alignment, and a co-designed streaming stack to enable efficient, long-horizon interactive world generation.

▲ 311 • 💬 5 • ⭐ 2,187 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19191) • [💻 code](https://github.com/amap-cvlab/ABot-World) • [🔗 project](https://abot-world.amap.com/)

---

**[Multi-module GRPO: Composing Policy Gradients and Prompt Optimization
  for Language Model Programs](https://huggingface.co/papers/2508.04660)**

*Noah Ziems, Dilara Soylu, Lakshya A Agrawal et al. (13 authors)*

mmGRPO, a multi-module extension of GRPO, enhances accuracy in modular AI systems by optimizing LM calls and prompts across various tasks.

▲ 7 • 💬 0 • ⭐ 37,085 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.04660) • [💻 code](https://github.com/stanfordnlp/dspy) • [🔗 project](https://dspy.ai)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 83,670 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 65 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 77,331 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.2k • 🔱 917 • 8h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 4.6k • 🔱 404 • 2d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.9k • 🔱 507 • 3d ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.7k • 🔱 1.9k • 59s ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 2.5k • 🔱 472 • 9h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.4k • 🔱 205 • 6d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.2k • 🔱 175 • 7d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.1k • 🔱 158 • 4h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 2.0k • 🔱 245 • 2d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.0k • 🔱 255 • 10m ago

---

---

*Generated by PeekDeck - A glance is all you need*
