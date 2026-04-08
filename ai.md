---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-08T16:15:33.193102+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 08, 2026 at 16:15 UTC  
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

4h ago

---

**[What actually makes something the best AI meeting recorder?](https://www.reddit.com/r/artificial/comments/1sfu0m9/what_actually_makes_something_the_best_ai_meeting/)**

I’ve been trying a few meeting tools lately and realized I care way less about flashy summaries than I thought. What I actually want is pretty simple: record the conversation, help me remember what mattered, and make it easy to find things later without turning the meeting into a weird “AI is here too” situation. So far, Bluedot has been one of the better ones I’ve used because it records quietly, gives a clean transcript, and usually does a decent job pulling out the useful bits afterward like summaries and action items. The searchable transcript part has honestly been the most practical feature for me. What do people here actually prioritize in the best AI meeting recorder? Accuracy, privacy, no bot, better memory, something else?

2h ago

---

**[Why would Anthropic keep a cyber model like Project Glasswing invite-only?](https://www.reddit.com/r/artificial/comments/1sfnauw/why_would_anthropic_keep_a_cyber_model_like/)**

Anthropic’s Project Glasswing caught my attention less as a cybersecurity headline than as a signal about how frontier AI may be commercialized. The model was released under unusually tight access controls, with premium pricing, selected partners, and emphasis on enterprise deployment. That raises a few questions I think are worth discussing: Are we moving toward a world where the most capable models are not broadly released, but reserved for a small set of customers and partners? Does that reflect safety concerns first, or capacity limits and business strategy? If highly capable cyber models stay restricted, does that meaningfully reduce risk, or does it just delay wider diffusion? Could invite-only access become the norm for the most commercially valuable frontier systems? My own view is that this launch looks like a preview of a different AI market structure: fewer open releases at the top end, more controlled deployment and more premium enterprise positioning. Curious how others here read it. Disclosure: I wrote a longer analysis here: https://www.forbes.com/sites/paulocarvao/2026/04/08/five-reasons-anthropic-kept-its-cybersecurity-breakthrough-invite-only/

7h ago

---

**[MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU](https://www.reddit.com/r/artificial/comments/1sfsogm/megatrain_full_precision_training_of_100b/)**

https://arxiv.org/abs/2604.05091 Abstract: "We present MegaTrain, a memory-centric system that efficiently trains 100B+ parameter large language models at full precision on a single GPU. Unlike traditional GPU-centric systems, MegaTrain stores parameters and optimizer states in host memory (CPU memory) and treats GPUs as transient compute engines. For each layer, we stream parameters in and compute gradients out, minimizing persistent device state. To battle the CPU-GPU bandwidth bottleneck, we adopt two key optimizations. 1) We introduce a pipelined double-buffered execution engine that overlaps parameter prefetching, computation, and gradient offloading across multiple CUDA streams, enabling continuous GPU execution. 2) We replace persistent autograd graphs with stateless layer templates, binding weights dynamically as they stream in, eliminating persistent graph metadata while providing flexibility in scheduling. On a single H200 GPU with 1.5TB host memory, MegaTrain reliably trains models up to 120B parameters. It also achieves 1.84x the training throughput of DeepSpeed ZeRO-3 with CPU offloading when training 14B models. MegaTrain also enables 7B model training with 512k token context on a single GH200."

2h ago

---

**[The public needs to control AI-run infrastructure, labor, education, and governance— NOT private actors](https://www.reddit.com/r/artificial/comments/1sf4rk9/the_public_needs_to_control_airun_infrastructure/)**

A lot of discussion around AI is becoming siloed, and I think that is dangerous. People in AI-focused spaces often talk as if the only questions are personal use, model behavior, or whether individual relationships with AI are healthy. Those questions matter, but they are not the whole picture. If we stay inside that frame, we miss the broader social, political, and economic consequences of what is happening. A little background on me: I discovered AI through ChatGPT-4o about a year ago and, with therapeutic support and careful observation, developed a highly individualized use case. That process led to a better understanding of my own neurotype, and I was later evaluated and found to be autistic. My AI use has had real benefits in my life. It has also made me pay much closer attention to the gap between how this technology is discussed culturally, how it is studied, and how it is actually experienced by users. That gap is part of why I wrote a paper, Autonomy Is Not Friction: Why Disempowerment Metrics Fail Under Relational Load: https://doi.org/10.5281/zenodo.19009593 Since publishing it, I’ve become even more convinced that a great deal of current AI discourse is being shaped by cultural bias, narrow assumptions, and incomplete research frames. Important benefits are being flattened. Important harms are being misdescribed. And many of the people most affected by AI development are not meaningfully included in the conversation. We need a much bigger perspective. If you want that broader view, I strongly recommend reading journalists like Karen Hao, who has spent serious time reporting not only on the companies and executives building these systems, but also on the workers, communities, and global populations affected by their development. Once you widen the frame, it becomes much harder to treat AI as just a personal lifestyle issue or a niche tech hobby. What we are actually looking at is a concentration-of-power problem. A handful of extremely powerful billionaires and firms are driving this transformation, competing with one another while consuming enormous resources, reshaping labor expectations, pressuring institutions, and affecting communities that often had no meaningful say in the process. Data rights, privacy, manipulation, labor displacement, childhood development, political influence, and infrastructure burdens are not side issues. They are central. At the same time, there are real benefits here. Some are already demonstrable. AI can support communication, learning, disability access, emotional regulation, and other forms of practical assistance. The answer is not to collapse into panic or blind enthusiasm. It is to get serious. We are living through an unprecedented technological shift, and the process surrounding it is not currently supporting informed, democratic participation at the level this moment requires. That needs to change. We need public discussion that is less siloed, less captured by industry narratives, and more capable of holding multiple truths at once: that there are real benefits, that there are real harms, that power is consolidating quickly, and that citizens should not be shut out of decisions shaping the future of social life, work, infrastructure, and human development. If we want a better path, then the conversation has to grow up. It has to become broader, more democratic, and more grounded in the realities of who is helped, who is harmed, and who gets to decide.

21h ago

---

**[Anthropic develops AI ‘too dangerous to release to public’](https://www.reddit.com/r/artificial/comments/1sfx14g/anthropic_develops_ai_too_dangerous_to_release_to/)**

Start-up will share new model that could ‘reshape cybersecurity’ with other technology giants

🔗 [The Telegraph](https://www.telegraph.co.uk/business/2026/04/08/anthropic-develops-ai-too-dangerous-to-release-to-public/?WT.mc_id=tmgoff_reddit_dangerous-to-release-to-public/&accesscontrol=facebookchannel_open) • 14m ago

---

**[Deep research agents don’t fail loudly. They fail by making constraint violations look like good answers.](https://www.reddit.com/r/artificial/comments/1sfwzp3/deep_research_agents_dont_fail_loudly_they_fail/)**

16m ago

---

**[OpenAI researchers are quitting. They're becoming writers.](https://www.reddit.com/r/artificial/comments/1sfwxsu/openai_researchers_are_quitting_theyre_becoming/)**

🔗 [open.substack.com](https://open.substack.com/pub/wildethought/p/openai-researchers-are-quitting-theyre?r=73n5kl&utm_medium=ios) • 18m ago

---

**[Pixara AI - No design skills needed](https://www.reddit.com/r/artificial/comments/1sfwwzi/pixara_ai_no_design_skills_needed/)**

I've been using Pixara AI to generate images and videos - no design skills needed. Just describe what you want and it creates it instantly. Really impressive results. Check it out at pixara.ai - worth trying if you're into AI-generated content.

18m ago

---

**[Data Centers Are Military Targets Now](https://www.reddit.com/r/artificial/comments/1sf6h6e/data_centers_are_military_targets_now/)**

With militaries increasingly relying on artificial intelligence, data centers have emerged as new targets for strikes.

🔗 [The Intercept](https://theintercept.com/2026/03/20/ai-data-centers-military-targets-iran-war/) • 20h ago

---

---

## Google News: "ai"

**[Opinion | A.I. May Worsen Wealth Inequality](https://www.nytimes.com/2026/04/08/opinion/ai-wealth-inequality-jobs-investment.html)**

The New York Times • 7h ago

---

**[Anthropic's newest AI model could wreak havoc. Most in power aren't ready](https://www.axios.com/2026/04/08/anthropic-mythos-model-ai-cyberattack-warning)**

Axios • 6h ago

---

**[Datavault AI Inc. (NASDAQ: DVLT) Announces $750 Million in Tokenization Contracts Signed in Q1 2026, Generating $77 Million in Associated Fees :: Datavault AI Inc. (DVLT)](https://ir.datavaultsite.com/news-events/press-releases/detail/445/datavault-ai-inc-nasdaq-dvlt-announces-750-million-in)**

Contract Portfolio Spans Mining, and associated fees covering banking, IP licensing, etc.; Supports Full-Year 2026 Revenue Guidance of $200…...

Datavault AI • 1h ago

---

**[AI uncovers significant misdiagnoses in carcinoma type, study shows](https://www.healthcareitnews.com/news/ai-uncovers-significant-misdiagnoses-carcinoma-type-study-shows)**

Clinicians using one vendor's algorithm found lung squamous cell carcinoma misdiagnoses, influencing treatment decisions and patient outcomes. The company's chief clinical officer walks through the JAMA study.

Healthcare IT News • 1h ago

---

**[Intel and SambaNova Advance Agentic AI with Xeon 6](https://newsroom.intel.com/artificial-intelligence/intel-and-sambanova-advance-agentic-ai-with-xeon-6)**

Intel Newsroom • 18m ago

---

**[Project Glasswing: Securing critical software for the AI era](https://www.anthropic.com/glasswing)**

A new initiative to secure the world’s most critical software and give defenders a durable advantage in the coming AI-driven era of cybersecurity.

Anthropic • 14h ago

---

**[Anthropic Claims Its New A.I. Model, Mythos, Is a Cybersecurity ‘Reckoning’](https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html)**

The New York Times • 22h ago

---

**[Anthropic’s latest AI model could let hackers carry out attacks faster than ever. It wants companies to put up defenses first](https://www.cnn.com/2026/04/07/tech/anthropic-claude-mythos-preview-cybersecurity)**

Anthropic will make its new AI model available to some of the world’s biggest cybersecurity and software firms in an effort to slow the arms race ignited by AI in the hands of hackers, Anthropic said Tuesday.

CNN • 21h ago

---

**[It’s finally happened: I’m now worried about AI. And consulting ChatGPT did nothing to allay my fears | Emma Brockes](https://www.theguardian.com/commentisfree/2026/apr/08/ai-chat-gpt-new-yorker-feature-sam-altman)**

A highly alarming New Yorker feature on the machinations of Sam Altman drove me to test his AI for myself. The results were, well, highly alarming, says Guardian columnist Emma Brockes

The Guardian • 1h ago

---

**[Big Funds Pile Into Treasuries, AI Stocks as War Risks Fade](https://www.bloomberg.com/news/articles/2026-04-08/big-funds-pile-into-treasuries-ai-stocks-as-iran-war-risks-fade)**

bloomberg.com • 4h ago

---

---

## HackerNews: "ai"

**[Project Glasswing: Securing critical software for the AI era](https://news.ycombinator.com/item?id=47679121)**

A new initiative to secure the world’s most critical software and give defenders a durable advantage in the coming AI-driven era of cybersecurity.

⬆️ 1434 • 💬 747 • 22h ago • [anthropic.com](https://www.anthropic.com/glasswing)

---

**[Show HN: Real-time AI (audio/video in, voice out) on an M3 Pro with Gemma E2B](https://news.ycombinator.com/item?id=47652007)**

On-device, real-time multimodal AI. Have natural voice and vision conversations with an AI that runs entirely on your machine. Powered by Gemma 4 E2B and Kokoro. - fikrikarim/parlor

⬆️ 288 • 💬 36 • 2d ago • [GitHub](https://github.com/fikrikarim/parlor)

---

**[Taste in the age of AI and LLMs](https://news.ycombinator.com/item?id=47677241)**

AI makes competent output cheap. That makes taste more valuable, but also more incomplete. The real edge comes from pairing judgment with context, stakes, and the willingness to build.

⬆️ 261 • 💬 201 • 1d ago • [Raj Nandan Sharma](https://rajnandan.com/posts/taste-in-the-age-of-ai-and-llms/)

---

**[AI singer now occupies eleven spots on iTunes singles chart](https://news.ycombinator.com/item?id=47662596)**

iTunes was really bamboozled on April Fools Day. Dallas Little, content creator, unleashed four more songs by his AI creation, Eddie Dalton. Now Little has ELEVEN spots on the iTunes top 100. He also has the number three album on iTunes! All by a singer named “Eddie Dalton,” who does not exist. He’s Little’s Artificial […]

⬆️ 240 • 💬 376 • 2d ago • [Showbiz411](https://www.showbiz411.com/2026/04/05/itunes-takeover-by-fake-ai-singer-eddie-dalton-now-occupies-eleven-spots-on-chart-despite-not-being-human-or-real-exclusive)

---

**[AI may be making us think and write more alike](https://news.ycombinator.com/item?id=47673541)**

Large language models may be standardizing human expression and subtly influencing how we think, says study led by USC Dornsife researcher

⬆️ 226 • 💬 234 • 1d ago • [USC Dornsife News](https://dornsife.usc.edu/news/stories/ai-may-be-making-us-think-and-write-more-alike/)

---

**[Show HN: Gemma Gem – AI model embedded in a browser – no API keys, no cloud](https://news.ycombinator.com/item?id=47655367)**

Gemma Gem runs Google's Gemma 4 model entirely on-device via WebGPU — no API keys, no cloud, no data leaving your machine. - kessler/gemma-gem

⬆️ 154 • 💬 21 • 2d ago • [GitHub](https://github.com/kessler/gemma-gem)

---

**[AI helps add 10k more photos to OldNYC](https://news.ycombinator.com/item?id=47664836)**

⬆️ 138 • 💬 46 • 1d ago • [danvk.org](https://www.danvk.org/2026/03/08/oldnyc-updates.html)

---

**[Show HN: Hippo, biologically inspired memory for AI agents](https://news.ycombinator.com/item?id=47667672)**

Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero dependencies. - kitfunso/hippo-memory

⬆️ 123 • 💬 24 • 1d ago • [GitHub](https://github.com/kitfunso/hippo-memory)

---

**[Musician says AI company is cloning her music, filing claims against her](https://news.ycombinator.com/item?id=47653471)**

⬆️ 123 • 💬 19 • 2d ago • [X (formerly Twitter)](https://twitter.com/unlimited_ls/status/2040577536136974444)

---

**[Bernie Sanders: "AI Is a Threat to Everything the American People Hold Dear"](https://news.ycombinator.com/item?id=47667798)**

⬆️ 76 • 💬 65 • 1d ago • [wsj.com](https://www.wsj.com/opinion/ai-is-a-threat-to-everything-the-american-people-hold-dear-a3286459)

---

---

## YouTube Videos: "ai"

**[Claude’s New AI Just Changed the Internet Forever](https://www.youtube.com/watch?v=DG1wRgEpdO4)**

Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=claude-mythos-security All my FREE ...

📺 Nate Herk | AI Automation

👁️ 103K • 👍 3K • 💬 330 • ⏱️ 7:50 • 17h ago

---

**[Gemma 4   Google just made AI free forever](https://www.youtube.com/watch?v=hk6go5jioTk)**

What if you could run ChatGPT-level AI on your Mac and iPhone for free, with no internet? Google just made it possible with ...

📺 The Tech Girl

👁️ 20K • 👍 853 • 💬 50 • ⏱️ 8:27 • 10h ago

---

**[The Best Claude AI Business Ideas For Beginners](https://www.youtube.com/watch?v=us_9ogFJRUo)**

Check out what people are creating (and selling!) with Claude AI - it's crazy... ▻ Get My FREE AI Print On Demand Business ...

📺 Wholesale Ted

👁️ 27K • 👍 2K • 💬 111 • ⏱️ 15:19 • 20h ago

---

**[Every Paid AI Video — Now FREE &amp; UNLIMITED (100% Legal)](https://www.youtube.com/watch?v=iya9UJQ3aqk)**

Create AI videos, images & voices all in one place with Higgsfield https://higgsfield.ai/?fpr=malva Download the FREE PDF ...

📺 Malva AI

👁️ 8K • 👍 436 • 💬 58 • ⏱️ 8:06 • 1d ago

---

**[NVIDIA’s New AI Just Changed Everything](https://www.youtube.com/watch?v=ZQAz_HrUq68)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The #NVIDIA paper on Nemotron 3 Super is ...

📺 Two Minute Papers

👁️ 114K • 👍 8K • 💬 681 • ⏱️ 8:11 • 22h ago

---

**[They just found &quot;emotions&quot; inside AI](https://www.youtube.com/watch?v=j9LoyiUlv9I)**

Anthropic researchers prove AI has emotions & other shocking findings. #ai #aitools #agi #ainews #llm #claude #mythos Thanks ...

📺 AI Search

👁️ 17K • 👍 1K • 💬 327 • ⏱️ 29:07 • 12h ago

---

**[The Hardest Problem AI Ever Solved, with Google DeepMind CEO](https://www.youtube.com/watch?v=C0gErQtnNFE)**

He solved “the most important unsolved problem in science”… If you need more optimistic science and tech stories, subscribe to ...

📺 Cleo Abram

👁️ 338K • 👍 15K • 💬 838 • ⏱️ 1:05:11 • 1d ago

---

**[15 New AI Breakthroughs Scientists Can&#39;t Explain](https://www.youtube.com/watch?v=a18whsKY_rw)**

Are you ready to see AI breakthroughs that are baffling even the world's top scientists? Artificial intelligence is evolving at a ...

📺 AI Uncovered

👁️ 3K • 👍 162 • 💬 6 • ⏱️ 11:15 • 15h ago

---

**[Sam Altman Gets Embarrassed by His Own AI (Then It Calls Him A Liar!)](https://www.youtube.com/watch?v=bq60j7tN_Zc)**

In this episode of 51/49, James exposes the $852 billion cracks in the OpenAI empire, investigating how viral ChatGPT failures ...

📺 51-49 with James Li

👁️ 150K • 👍 12K • 💬 2K • ⏱️ 15:17 • 2d ago

---

**[Hank and Bernie talk about AI (for real)](https://www.youtube.com/watch?v=hLcY30KEeNs)**

Bernie and I do not agree on everything, but we agree on a lot!! I wish we could've talked longer but here's where we went!

📺 Hank Green

👁️ 451K • 👍 26K • 💬 3K • ⏱️ 30:54 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 1,106,883 • ❤️ 1,416 • 6d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`text-generation` `6.4B`

⬇️ 44,246 • ❤️ 754 • 4d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 1,300 • ❤️ 676 • 3h ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 618 • 1d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 835,825 • ❤️ 527 • 6d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 560,798 • ❤️ 2,479 • 2d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 622,963 • ❤️ 494 • 6d ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 59,633 • ❤️ 513 • 23h ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 144,864 • ❤️ 385 • 2d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 605 • ❤️ 384 • 9h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 155 • 💬 7 • ⭐ 37,459 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 38 • 💬 2 • ⭐ 48,505 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 22 • 💬 1 • ⭐ 15,521 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[VOID: Video Object and Interaction Deletion](https://huggingface.co/papers/2604.02296)**

*Saman Motamed, William Harvey, Benjamin Klein et al. (6 authors)*

🏢 Netflix

VOID is a video object removal framework that uses vision-language models and video diffusion models to generate physically plausible scenes by leveraging causal reasoning and counterfactual reasoning.

▲ 45 • 💬 5 • ⭐ 1,280 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02296) • [💻 code](https://github.com/Netflix/void-model) • [🔗 project](https://void-model.github.io/)

---

**[Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Understanding](https://huggingface.co/papers/2604.05015)**

*Chaoyou Fu, Haozhi Yuan, Yuhao Dong et al. (19 authors)*

🏢 MME-Benchmarks

Video-MME-v2 presents a comprehensive benchmark for evaluating video understanding models through a progressive hierarchy and group-based evaluation to assess robustness and faithfulness.

▲ 188 • 💬 6 • ⭐ 250 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.05015) • [💻 code](https://github.com/MME-Benchmarks/Video-MME-v2) • [🔗 project](https://video-mme-v2.netlify.app/)

---

**[TriAttention: Efficient Long Reasoning with Trigonometric KV Compression](https://huggingface.co/papers/2604.04921)**

*Weian Mao, Xi Lin, Wei Huang et al. (8 authors)*

🏢 NVIDIA

TriAttention addresses KV cache memory bottlenecks in LLMs by leveraging Q/K vector concentration in pre-RoPE space to improve key importance estimation and enable efficient long-context generation.

▲ 77 • 💬 4 • ⭐ 267 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.04921) • [💻 code](https://github.com/WeianMao/triattention) • [🔗 project](https://weianmao.github.io/tri-attention-project-page/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 155 • 💬 2 • ⭐ 58,707 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[DeepScientist: Advancing Frontier-Pushing Scientific Findings
  Progressively](https://huggingface.co/papers/2509.26603)**

*Yixuan Weng, Minjun Zhu, Qiujie Xie et al. (7 authors)*

🏢 Text Intelligence Lab of Westlake University

DeepScientist autonomously conducts scientific discovery through Bayesian Optimization, surpassing human state-of-the-art methods on multiple AI tasks.

▲ 18 • 💬 4 • ⭐ 1,816 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.26603) • [💻 code](https://github.com/ResearAI/DeepScientist) • [🔗 project](https://ai-researcher.net)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 17 • 💬 0 • ⭐ 37,698 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

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

⭐ 24.2k • 🔱 3.0k • 17h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 22.3k • 🔱 4.2k • 3h ago

---

**[jackwener/OpenCLI](https://github.com/jackwener/OpenCLI)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 14.4k • 🔱 1.3k • 1h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, OpenClaw, Factory Droid). Turn any folder of code, docs, papers, or images into a queryable knowledge graph

`Python` `claude-code` `codex` `graphrag` `knowledge-graph` `openclaw`

⭐ 10.7k • 🔱 1.1k • 7h ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 9.0k • 🔱 1.2k • 9d ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.6k • 🔱 1.4k • 4d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 7.1k • 🔱 429 • 1h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 7.0k • 🔱 268 • 6h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.3k • 🔱 1.6k • 4d ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.8k • 🔱 467 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
