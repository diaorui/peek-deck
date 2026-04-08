---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-08T21:10:53.551848+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 08, 2026 at 21:10 UTC  
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

**[this is how an AI generated cow looked 12 years ago](https://www.reddit.com/r/artificial/comments/1sfqix8/this_is_how_an_ai_generated_cow_looked_12_years/)**

now it just look 💯 real

9h ago

---

**[Project Glasswing is inherently Cartel Behaviour](https://www.reddit.com/r/artificial/comments/1sg1mxm/project_glasswing_is_inherently_cartel_behaviour/)**

If the large companies always get access to the latest models first to "sure up cybersecurity" they will always have a head start on the competition and new contenders in the tech space. If Glasswing is locked down to only be allowed for cybersecurity thats a different story but I doubt it is.

2h ago

---

**[What actually makes something the best AI meeting recorder?](https://www.reddit.com/r/artificial/comments/1sfu0m9/what_actually_makes_something_the_best_ai_meeting/)**

I’ve been trying a few meeting tools lately and realized I care way less about flashy summaries than I thought. What I actually want is pretty simple: record the conversation, help me remember what mattered, and make it easy to find things later without turning the meeting into a weird “AI is here too” situation. So far, Bluedot has been one of the better ones I’ve used because it records quietly, gives a clean transcript, and usually does a decent job pulling out the useful bits afterward like summaries and action items. The searchable transcript part has honestly been the most practical feature for me. What do people here actually prioritize in the best AI meeting recorder? Accuracy, privacy, no bot, better memory, something else?

6h ago

---

**[Why would Anthropic keep a cyber model like Project Glasswing invite-only?](https://www.reddit.com/r/artificial/comments/1sfnauw/why_would_anthropic_keep_a_cyber_model_like/)**

Anthropic’s Project Glasswing caught my attention less as a cybersecurity headline than as a signal about how frontier AI may be commercialized. The model was released under unusually tight access controls, with premium pricing, selected partners, and emphasis on enterprise deployment. That raises a few questions I think are worth discussing: Are we moving toward a world where the most capable models are not broadly released, but reserved for a small set of customers and partners? Does that reflect safety concerns first, or capacity limits and business strategy? If highly capable cyber models stay restricted, does that meaningfully reduce risk, or does it just delay wider diffusion? Could invite-only access become the norm for the most commercially valuable frontier systems? My own view is that this launch looks like a preview of a different AI market structure: fewer open releases at the top end, more controlled deployment and more premium enterprise positioning. Curious how others here read it. Disclosure: I wrote a longer analysis here: https://www.forbes.com/sites/paulocarvao/2026/04/08/five-reasons-anthropic-kept-its-cybersecurity-breakthrough-invite-only/

12h ago

---

**[~77% of all new "Success" self-help books on Amazon are likely written by AI, with 1 author, Noah Felix Bennett, publishing a stunning 74 books in mid-2025 alone, at a rate of >1 per day. Richard Trillion Mantey, who has published hundreds of books, was assessed to have used AI for every single book](https://www.reddit.com/r/artificial/comments/1sg5cuz/77_of_all_new_success_selfhelp_books_on_amazon/)**

"Ironically, one of the 844 books in this dataset is called 'How to Write for Humans in an AI World: Cutting Through Digital Noise and Reaching Real People'. In it, the author laments the proliferation of AI-written content: 'The words we see online, in our inboxes, even in news articles, often feel like they were written by no one in particular,' he writes. 'They’re grammatically perfect and emotionally empty. They’re fluent, but soulless. The irony is that we’ve never written more than we do today. We’re producing mountains of content: posts, captions, pitches, texts, and endless emails. At the same time, in the midst of all that noise, something essential is fading. It’s the sense that a real person is speaking to another real person.' That book’s contents were flagged as likely AI-generated."

11m ago

---

**[Finally Abliterated Sarvam 30B and 105B!](https://www.reddit.com/r/artificial/comments/1sg58qr/finally_abliterated_sarvam_30b_and_105b/)**

I abliterated Sarvam-30B and 105B - India's first multilingual MoE reasoning models - and found something interesting along the way! Reasoning models have 2 refusal circuits, not one. The <think> block and the final answer can disagree: the model reasons toward compliance in its CoT and then refuses anyway in the response. Killer finding: one English-computed direction removed refusal in most of the other supported languages (Malayalam, Hindi, Kannada among few). Refusal is pre-linguistic. Full writeup: https://medium.com/@aloshdenny/uncensoring-sarvamai-abliterating-refusal-mechanisms-in-indias-first-moe-reasoning-model-b6d334f85f42 30B model: https://huggingface.co/aoxo/sarvam-30b-uncensored 105B model: https://huggingface.co/aoxo/sarvam-105b-uncensored

15m ago

---

**[MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU](https://www.reddit.com/r/artificial/comments/1sfsogm/megatrain_full_precision_training_of_100b/)**

https://arxiv.org/abs/2604.05091 Abstract: "We present MegaTrain, a memory-centric system that efficiently trains 100B+ parameter large language models at full precision on a single GPU. Unlike traditional GPU-centric systems, MegaTrain stores parameters and optimizer states in host memory (CPU memory) and treats GPUs as transient compute engines. For each layer, we stream parameters in and compute gradients out, minimizing persistent device state. To battle the CPU-GPU bandwidth bottleneck, we adopt two key optimizations. 1) We introduce a pipelined double-buffered execution engine that overlaps parameter prefetching, computation, and gradient offloading across multiple CUDA streams, enabling continuous GPU execution. 2) We replace persistent autograd graphs with stateless layer templates, binding weights dynamically as they stream in, eliminating persistent graph metadata while providing flexibility in scheduling. On a single H200 GPU with 1.5TB host memory, MegaTrain reliably trains models up to 120B parameters. It also achieves 1.84x the training throughput of DeepSpeed ZeRO-3 with CPU offloading when training 14B models. MegaTrain also enables 7B model training with 512k token context on a single GH200."

7h ago

---

**[Agents: Isolated vrs Working on same file system](https://www.reddit.com/r/artificial/comments/1sg4mmk/agents_isolated_vrs_working_on_same_file_system/)**

What are ur views on this topic. Isolated, sandboxed etc. Most platforms run with isolated. Do u think its the only way or can a trusted system work. multi agents in the same filesystem togethet with no toe stepping?

38m ago

---

**[Built a demo where an agent can provision 2 GPUs, then gets hard-blocked on the 3rd call](https://www.reddit.com/r/artificial/comments/1sfy8qf/built_a_demo_where_an_agent_can_provision_2_gpus/)**

Policy: - budget = 1000 - each `provision_gpu(a100)` call = 500 Result: - call 1 -> ALLOW - call 2 -> ALLOW - call 3 -> DENY (`BUDGET_EXCEEDED`) Key point: the 3rd tool call is denied before execution. The tool never runs. Also emits: - authorization artifacts - hash-chained audit events - verification envelope - strict offline verification: `verifyEnvelope() => ok` Feels like this is the missing layer for side-effecting agents: proposal -> authorization -> execution rather than agent -> tool directly. Are you doing execution-time authorization, or mostly relying on approvals / retries / sandboxing. Happy to share the exact output / demo flow if useful.

4h ago

---

**[I built a game where you hack your employer by night and an entity called the CONDUIT starts responding to your keystrokes. Half horror, half labor dispute.](https://www.reddit.com/r/artificial/comments/1sfy52b/i_built_a_game_where_you_hack_your_employer_by/)**

Wishlist here on Steam if you dig the concept!

4h ago

---

---

## Google News: "ai"

**[Anthropic Teams Up With Its Rivals to Keep AI From Hacking Everything](https://www.wired.com/story/anthropic-mythos-preview-project-glasswing/)**

The AI lab's Project Glasswing will bring together Apple, Google, and more than 45 other organizations. They'll use the new Claude Mythos Preview model to test advancing AI cybersecurity capabilities.

WIRED • 1d ago

---

**[Opinion | A.I. May Worsen Wealth Inequality](https://www.nytimes.com/2026/04/08/opinion/ai-wealth-inequality-jobs-investment.html)**

The New York Times • 12h ago

---

**[Expert sounds off on the AI boom in San Francisco: ‘Anything is possible’](https://www.foxbusiness.com/video/6392765305112)**

DreamWorks SKG co-founder Jeffrey Katzenberg and WndrCo general partner Justin Wexler join ‘The Claman Countdown’ to discuss the AI revolution, rising cybersecurity risks and the surge of young innovators reshaping Silicon Valley.

Fox Business • 46m ago

---

**[Canva doubles down on AI and marketing automation with Simtheory, Ortto acquisitions](https://techcrunch.com/2026/04/08/canva-doubles-down-on-ai-and-marketing-automation-with-simtheory-ortto-acquisitions/)**

Canva says the acquisitions add strengths in agentic AI, data infrastructure, marketing automation, and customer engagement.

TechCrunch • 10m ago

---

**[Meta launches Muse Spark AI model as part of its AI turnaround](https://finance.yahoo.com/sectors/technology/article/meta-launches-muse-spark-ai-model-as-part-of-its-ai-turnaround-171109510.html)**

Meta's Meta Superintelligence Lab released its first AI model, called Muse Spark, on Wednesday.

Yahoo Finance • 3h ago

---

**[Meta Unveils New A.I. Model, Its First From the Superintelligence Lab](https://www.nytimes.com/2026/04/08/technology/meta-muse-spark-ai-model.html)**

The New York Times • 4h ago

---

**[Meta Releases First New AI Model Since Shaking Up Team](https://www.barrons.com/news/meta-releases-first-new-ai-model-since-shaking-up-team-ab504718)**

Barron's • 14m ago

---

**[The demise of software engineering jobs has been greatly exaggerated](https://www.cnn.com/2026/04/08/tech/ai-software-developer-jobs)**

Although AI coding tools have stoked fears that the technology will replace software engineers, jobs in the field are growing. As companies pump out more software, there’s increasing demand for seasoned engineers that can shape these products.

CNN • 11h ago

---

**[‘It’s not AI, it’s real’: shock as RSPCA releases images of 250 dogs found at property](https://www.theguardian.com/world/2026/apr/08/rspca-ai-images-dogs-property-uk)**

Dozens of dogs were found crammed into single living room space at property in undisclosed location in UK

The Guardian • 1h ago

---

**[The New Ivies: 20 Great Employer-Friendly Colleges Embracing AI](https://www.forbes.com/sites/aliciapark/2026/04/08/the-new-ivies-20-great-employer-friendly-colleges-embracing-ai/)**

Forbes • 10h ago

---

---

## HackerNews: "ai"

**[Project Glasswing: Securing critical software for the AI era](https://news.ycombinator.com/item?id=47679121)**

A new initiative to secure the world’s most critical software and give defenders a durable advantage in the coming AI-driven era of cybersecurity.

⬆️ 1471 • 💬 790 • 1d ago • [anthropic.com](https://www.anthropic.com/glasswing)

---

**[Taste in the age of AI and LLMs](https://news.ycombinator.com/item?id=47677241)**

AI makes competent output cheap. That makes taste more valuable, but also more incomplete. The real edge comes from pairing judgment with context, stakes, and the willingness to build.

⬆️ 262 • 💬 203 • 1d ago • [Raj Nandan Sharma](https://rajnandan.com/posts/taste-in-the-age-of-ai-and-llms/)

---

**[AI singer now occupies eleven spots on iTunes singles chart](https://news.ycombinator.com/item?id=47662596)**

iTunes was really bamboozled on April Fools Day. Dallas Little, content creator, unleashed four more songs by his AI creation, Eddie Dalton. Now Little has ELEVEN spots on the iTunes top 100. He also has the number three album on iTunes! All by a singer named “Eddie Dalton,” who does not exist. He’s Little’s Artificial […]

⬆️ 241 • 💬 376 • 2d ago • [Showbiz411](https://www.showbiz411.com/2026/04/05/itunes-takeover-by-fake-ai-singer-eddie-dalton-now-occupies-eleven-spots-on-chart-despite-not-being-human-or-real-exclusive)

---

**[AI may be making us think and write more alike](https://news.ycombinator.com/item?id=47673541)**

Large language models may be standardizing human expression and subtly influencing how we think, says study led by USC Dornsife researcher

⬆️ 227 • 💬 242 • 1d ago • [USC Dornsife News](https://dornsife.usc.edu/news/stories/ai-may-be-making-us-think-and-write-more-alike/)

---

**[Show HN: Gemma Gem – AI model embedded in a browser – no API keys, no cloud](https://news.ycombinator.com/item?id=47655367)**

Gemma Gem runs Google's Gemma 4 model entirely on-device via WebGPU — no API keys, no cloud, no data leaving your machine. - kessler/gemma-gem

⬆️ 154 • 💬 21 • 2d ago • [GitHub](https://github.com/kessler/gemma-gem)

---

**[AI helps add 10k more photos to OldNYC](https://news.ycombinator.com/item?id=47664836)**

⬆️ 141 • 💬 50 • 2d ago • [danvk.org](https://www.danvk.org/2026/03/08/oldnyc-updates.html)

---

**[Show HN: Hippo, biologically inspired memory for AI agents](https://news.ycombinator.com/item?id=47667672)**

Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero dependencies. - kitfunso/hippo-memory

⬆️ 127 • 💬 25 • 1d ago • [GitHub](https://github.com/kitfunso/hippo-memory)

---

**[Bernie Sanders: "AI Is a Threat to Everything the American People Hold Dear"](https://news.ycombinator.com/item?id=47667798)**

⬆️ 76 • 💬 65 • 1d ago • [wsj.com](https://www.wsj.com/opinion/ai-is-a-threat-to-everything-the-american-people-hold-dear-a3286459)

---

**[Show HN: We fingerprinted 178 AI models' writing styles and similarity clusters](https://news.ycombinator.com/item?id=47690415)**

⬆️ 70 • 💬 21 • 7h ago • [rival.tips](https://rival.tips/research/model-similarity)

---

**[Wikipedia's AI agent row likely just the beginning of the bot-ocalypse](https://news.ycombinator.com/item?id=47665902)**

An AI agent was banned from editing Wikipedia pages... and that's when things got weird, with the agent publishing its complaints publicly.

⬆️ 69 • 💬 91 • 2d ago • [Malwarebytes](https://www.malwarebytes.com/blog/ai/2026/04/wikipedias-ai-agent-row-likely-just-the-beginning-of-the-bot-ocalypse)

---

---

## YouTube Videos: "ai"

**[Claude’s New AI Just Changed the Internet Forever](https://www.youtube.com/watch?v=DG1wRgEpdO4)**

Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=claude-mythos-security All my FREE ...

📺 Nate Herk | AI Automation

👁️ 128K • 👍 4K • 💬 377 • ⏱️ 7:50 • 21h ago

---

**[Anthropic&#39;s Mythos AI Is Too Dangerous to Release. They&#39;re Using It Anyway.](https://www.youtube.com/watch?v=pGeh7tYRCJM)**

Anthropic revealed Mythos, a new AI model so powerful they won't let the public use it. Instead, they're deploying it to defend ...

📺 AI For Humans

👁️ 5K • 👍 359 • 💬 125 • ⏱️ 32:56 • 7h ago

---

**[Gemma 4   Google just made AI free forever](https://www.youtube.com/watch?v=hk6go5jioTk)**

What if you could run ChatGPT-level AI on your Mac and iPhone for free, with no internet? Google just made it possible with ...

📺 The Tech Girl

👁️ 33K • 👍 1K • 💬 88 • ⏱️ 8:27 • 15h ago

---

**[How I Use AI To Build A $10,000 App in 20 Minutes](https://www.youtube.com/watch?v=cszCH1ye5Mk)**

Best AI App Builder is Base44 https://base44.pxf.io/c/6440076/2049275/25619?trafcat=base&sharedid=video115 ✓ FREE ...

📺 Mikey No Code

👁️ 12K • ⏱️ 27:43 • 6h ago

---

**[NEW AI Video Generator Creates Long AI Videos With ONE Prompt](https://www.youtube.com/watch?v=KbgIQSWp450)**

This New AI video generator creates Long AI Videos Get 1000 Agent Opus credits https://www.opus.pro/agent?via=opusagent ...

📺 Dan Kieft

👁️ 11K • 💬 7 • ⏱️ 16:53 • 4h ago

---

**[Hank and Bernie talk about AI (for real)](https://www.youtube.com/watch?v=hLcY30KEeNs)**

Bernie and I do not agree on everything, but we agree on a lot!! I wish we could've talked longer but here's where we went!

📺 Hank Green

👁️ 500K • 👍 29K • 💬 3K • ⏱️ 30:54 • 1d ago

---

**[OpenAI Just Dropped The Real Plan After AGI Hits](https://www.youtube.com/watch?v=u9Azd3weYCY)**

OpenAI just dropped a policy blueprint built around one huge idea: superintelligence could hit hard enough to force a whole new ...

📺 AI Revolution

👁️ 21K • 👍 778 • 💬 103 • ⏱️ 13:17 • 22h ago

---

**[They just found &quot;emotions&quot; inside AI](https://www.youtube.com/watch?v=j9LoyiUlv9I)**

Anthropic researchers prove AI has emotions & other shocking findings. #ai #aitools #agi #ainews #llm #claude #mythos Thanks ...

📺 AI Search

👁️ 21K • 👍 2K • 💬 409 • ⏱️ 29:07 • 17h ago

---

**[NVIDIA’s New AI Just Changed Everything](https://www.youtube.com/watch?v=ZQAz_HrUq68)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The #NVIDIA paper on Nemotron 3 Super is ...

📺 Two Minute Papers

👁️ 126K • 👍 9K • 💬 729 • ⏱️ 8:11 • 1d ago

---

**[Every Paid AI Video — Now FREE &amp; UNLIMITED (100% Legal)](https://www.youtube.com/watch?v=iya9UJQ3aqk)**

Create AI videos, images & voices all in one place with Higgsfield https://higgsfield.ai/?fpr=malva Download the FREE PDF ...

📺 Malva AI

👁️ 10K • 👍 506 • 💬 83 • ⏱️ 8:06 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 1,106,883 • ❤️ 1,443 • 6d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`text-generation` `6.4B`

⬇️ 44,246 • ❤️ 777 • 4d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 1,300 • ❤️ 719 • 8h ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 635 • 2d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 835,825 • ❤️ 534 • 6d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 560,798 • ❤️ 2,498 • 2d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 622,963 • ❤️ 503 • 6d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 605 • ❤️ 426 • 14h ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 144,864 • ❤️ 392 • 3d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 41,667 • ❤️ 1,126 • 13d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 156 • 💬 7 • ⭐ 37,459 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 39 • 💬 2 • ⭐ 48,505 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 23 • 💬 1 • ⭐ 15,521 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[VOID: Video Object and Interaction Deletion](https://huggingface.co/papers/2604.02296)**

*Saman Motamed, William Harvey, Benjamin Klein et al. (6 authors)*

🏢 Netflix

VOID is a video object removal framework that uses vision-language models and video diffusion models to generate physically plausible scenes by leveraging causal reasoning and counterfactual reasoning.

▲ 47 • 💬 5 • ⭐ 1,280 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02296) • [💻 code](https://github.com/Netflix/void-model) • [🔗 project](https://void-model.github.io/)

---

**[Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Understanding](https://huggingface.co/papers/2604.05015)**

*Chaoyou Fu, Haozhi Yuan, Yuhao Dong et al. (19 authors)*

🏢 MME-Benchmarks

Video-MME-v2 presents a comprehensive benchmark for evaluating video understanding models through a progressive hierarchy and group-based evaluation to assess robustness and faithfulness.

▲ 193 • 💬 6 • ⭐ 250 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.05015) • [💻 code](https://github.com/MME-Benchmarks/Video-MME-v2) • [🔗 project](https://video-mme-v2.netlify.app/)

---

**[TriAttention: Efficient Long Reasoning with Trigonometric KV Compression](https://huggingface.co/papers/2604.04921)**

*Weian Mao, Xi Lin, Wei Huang et al. (8 authors)*

🏢 NVIDIA

TriAttention addresses KV cache memory bottlenecks in LLMs by leveraging Q/K vector concentration in pre-RoPE space to improve key importance estimation and enable efficient long-context generation.

▲ 79 • 💬 4 • ⭐ 267 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.04921) • [💻 code](https://github.com/WeianMao/triattention) • [🔗 project](https://weianmao.github.io/tri-attention-project-page/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 155 • 💬 2 • ⭐ 58,826 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 17 • 💬 0 • ⭐ 37,826 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[DeepScientist: Advancing Frontier-Pushing Scientific Findings
  Progressively](https://huggingface.co/papers/2509.26603)**

*Yixuan Weng, Minjun Zhu, Qiujie Xie et al. (7 authors)*

🏢 Text Intelligence Lab of Westlake University

DeepScientist autonomously conducts scientific discovery through Bayesian Optimization, surpassing human state-of-the-art methods on multiple AI tasks.

▲ 18 • 💬 4 • ⭐ 1,875 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.26603) • [💻 code](https://github.com/ResearAI/DeepScientist) • [🔗 project](https://ai-researcher.net)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 38 • 💬 2 • ⭐ 32,636 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[milla-jovovich/mempalace](https://github.com/milla-jovovich/mempalace)**

The highest-scoring AI memory system ever benchmarked. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 26.1k • 🔱 3.2k • 2h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 23.7k • 🔱 4.4k • 3h ago

---

**[jackwener/OpenCLI](https://github.com/jackwener/OpenCLI)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 14.4k • 🔱 1.3k • 1h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, OpenClaw, Factory Droid, Trae). Turn any folder of code, docs, papers, or images into a queryable knowledge graph

`Python` `claude-code` `codex` `graphrag` `knowledge-graph` `openclaw`

⭐ 12.1k • 🔱 1.2k • 2h ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 9.1k • 🔱 1.2k • 9d ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.6k • 🔱 1.4k • 5d ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 7.3k • 🔱 292 • 11h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 7.1k • 🔱 431 • 1h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.3k • 🔱 1.6k • 4d ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.8k • 🔱 469 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
