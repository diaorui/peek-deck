---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-30T06:36:28.215392+00:00'
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

**Last Updated:** May 30, 2026 at 06:36 UTC  
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

**[Ronny Chieng Tells Harvard to ‘Destroy AI’ as Graduates Cheer](https://www.reddit.com/r/artificial/comments/1trfunt/ronny_chieng_tells_harvard_to_destroy_ai_as/)**

The comedian and The Daily Show host gave the keynote address for Class Day 2026.

🔗 [Harvard Magazine](https://www.harvardmagazine.com/commencement/class-day-ronny-chieng-harvard) • 9h ago

---

**[Mystery company accidentally blew $500 million on Claude AI in a single month — failed to put usage limit on licenses for employees](https://www.reddit.com/r/artificial/comments/1trmvgh/mystery_company_accidentally_blew_500_million_on/)**

A mysterious, unnamed company is reported to have accidentally spent half a billion dollars in a single month on Claude AI after forgetting to set usage limits for Claude licenses for employees.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/mystery-company-accidentally-blew-usd500-million-on-claude-in-a-single-month-failed-to-put-usage-limit-on-licenses-for-employees) • 4h ago

---

**[Meta lays off more than 2,000 from Menlo Park headquarters](https://www.reddit.com/r/artificial/comments/1trevkk/meta_lays_off_more_than_2000_from_menlo_park/)**

🔗 [sfgate.com](https://www.sfgate.com/tech/article/more-meta-layoffs-22282871.php) • 9h ago

---

**[Your brain does on 20 watts what AI needs a nuclear reactor to attempt. Last week a team figured out how to print something that actually speaks to living brain cells.](https://www.reddit.com/r/artificial/comments/1tr4kau/your_brain_does_on_20_watts_what_ai_needs_a/)**

Amazon bought a 960 megawatt nuclear reactor for AI servers. Microsoft restarted Three Mile Island. Stargate is spending 500 billion dollars on data centres. All of this to do, badly, what your brain does for free on the power of a dim light bulb. The reason is that silicon processes information nothing like the brain does. Rigid chips with identical transistors trying to mimic something soft, three dimensional, constantly rewiring itself, with billions of different neurons each doing something slightly different. Northwestern University just published research showing they printed artificial neurons from MoS2 and graphene ink that produced biologically realistic electrical spikes. They tested on living mouse brain cells. The brain responded as if the signal came from one of its own cells. The breakthrough was accidental. Every other lab had been burning away the polymer residue left in the ink after printing. This team kept it. That residue created the switching behaviour that made the spikes biologically realistic. The neuromorphic computing implications here seem significant. If you can print devices that process information the way neurons do at scale, the energy math changes completely.

15h ago

---

**[Anthropic Tops OpenAI to Become the World’s Most Valuable A.I. Start-Up](https://www.reddit.com/r/artificial/comments/1trli22/anthropic_tops_openai_to_become_the_worlds_most/)**

Anthropic raised $65 billion in new fund-raising that put its value at $900 billion, ahead of OpenAI’s last valuation of $730 billion, as the companies duel for A.I. dominance. Anthropic, once the lesser-known artificial intelligence competitor to OpenAI, has been on an inexorable rise over the past few months. The San Francisco company recently dueled with the Pentagon over the use of A.I. in warfare. It released a powerful A.I. model, Mythos, that it said was uncannily capable of finding and exploiting hidden flaws in software.

🔗 [nytimes.com](https://www.nytimes.com/2026/05/28/technology/anthropic-tops-openai-valuation.html) • 5h ago

---

**[Anthropic overtakes OpenAI as the most valuable AI startup at $965B](https://www.reddit.com/r/artificial/comments/1tr0chv/anthropic_overtakes_openai_as_the_most_valuable/)**

18h ago

---

**[Learning to Skip Blocks: Self-Discovered Ultrametric Routing for Hardware-Accelerated Sparse Attention](https://www.reddit.com/r/artificial/comments/1trqc3h/learning_to_skip_blocks_selfdiscovered/)**

Abstract. Standard dense self-attention scales quadratically in sequence length, creating an intractable memory and compute bottleneck for long-context Transformers. We introduce Dynamic Ultrametric Attention, a framework in which a Transformer autonomously learns per-head block-sparse routing topologies during training via Gumbel-Sigmoid depth gates, then offloads those learned sparsity patterns directly to a custom Triton block-sparse kernel at inference time. The routing topology is derived from an ultrametric (tree-structured) distance matrix that encodes hierarchical relationships between token positions. Across nine experiments spanning Dyck-k bracket languages, the Long Range Arena ListOps benchmark, autoregressive serving, and natural language modeling, we demonstrate that: (1) the dynamic gates organically discover layer-wise specialization—dedicating early layers to hierarchical parsing and later layers to dense aggregation—without any architectural constraint; (2) the learned sparsity maps transfer losslessly to a block-sparse Triton kernel that skips entire SRAM loads for non-attending blocks; (3) the resulting system achieves an 11.59× wall-clock inference speedup over PyTorch dense attention at 2048 tokens, scaling to 28× at 8192 tokens with 98.4% memory reduction; (4) a sparse PagedAttention decoding kernel achieves 8× effective memory bandwidth over dense decoding by conditionally skipping KV-cache block loads; and (5) when augmented with a local sliding window, the architecture maintains >88% sparsity across all layers on real natural language (Shakespeare) while reducing cross-entropy loss from 10.9 to 1.55. To our knowledge, this is the first demonstration of an LLM learning its own hardware-optimal sparsity pattern and bridging it to a physically accelerated kernel without post-hoc pruning or distillation. https://github.com/sneed-and-feed/adelic-spectral-zeta/blob/main/papers/learning_to_skip_blocks.md

1h ago

---

**[I made an Epstein Files RAG](https://www.reddit.com/r/artificial/comments/1trq0p9/i_made_an_epstein_files_rag/)**

A lot of people talk about the Epstein files. Almost nobody actually reads them. So I made a searchable version where you can just ask questions naturally instead of digging through thousands of pages manually. You can explore names, timelines, mentions, connections, locations, etc. way faster now. Repo: https://github.com/AbhisumatK/Epstein\_Files\_RAG

🔗 [GitHub](https://github.com/AbhisumatK/Epstein_Files_RAG) • 1h ago

---

**[Microsoft data suggests using AI is more expensive than hiring people](https://www.reddit.com/r/artificial/comments/1tqm10c/microsoft_data_suggests_using_ai_is_more/)**

"For my team, the cost of compute is far beyond the costs of the employees."

🔗 [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/microsoft-data-suggests-using-ai-225900743.html) • 1d ago

---

**[Researchers at MIT documented 30 AI agents major labs are deploying. Only 4 had public docs saying what the agent does, what it can't do, and what happens if it breaks.](https://www.reddit.com/r/artificial/comments/1trc7re/researchers_at_mit_documented_30_ai_agents_major/)**

Agentic AI systems are increasingly capable of performing professional and personal tasks with limited human involvement. However, tracking these developments is difficult because the AI agent ecosystem is complex, rapidly evolving, and inconsistently documented, posing obstacles to both researchers and policymakers. To address these challenges, this paper presents the 2025 AI Agent Index. The Index documents information regarding the origins, design, capabilities, ecosystem, and safety features of 30 state-of-the-art AI agents based on publicly available information and email correspondence with developers. In addition to documenting information about individual agents, the Index illuminates broader trends in the development of agents, their capabilities, and the level of transparency of developers. Notably, we find different transparency levels among agent developers and observe that most developers share little information about safety, evaluations, and societal impacts. The 2025 AI Agent Index is available online at https://aiagentindex.mit.edu

🔗 [arXiv.org](https://arxiv.org/abs/2602.17753) • 11h ago

---

---

## Google News: "ai"

**[Nvidia is investing billions into this emerging technology that could change the AI industry](https://www.cnbc.com/2026/05/29/nvidia-photonics-investment-ai.html)**

Photonics is considered to be a more efficient alternative to the current process of transferring data using electricity, which could be crucial to the AI boom.

CNBC • 1d ago

---

**[The Tech Download: How chip companies are looking to use light to solve this major AI bottleneck](https://www.cnbc.com/2026/05/29/tech-download-photonics-nvidia-ai-bottleneck.html)**

Nvidia is investing billions into companies developing photonics, which industry watchers say could bring big efficiency gains to the AI sector.

CNBC • 19h ago

---

**[Michael Burry calls AI tokenmaxxing 'crazy, rushed, temporary' — and he's shorting Nvidia to prove it](https://finance.yahoo.com/markets/stocks/articles/michael-burry-calls-ai-tokenmaxxing-171000969.html)**

Burry believes the more tokens a company blows through, the more it can tell investors it’s all in on AI, even if the actual business payoff is questionable at best.

Yahoo Finance • 13h ago

---

**[The Biggest Tell That Something Was Written by AI](https://www.theatlantic.com/technology/2026/05/how-to-tell-ai-writing/687345/)**

Look closely and you’ll see that every part of the text is not quite right.

The Atlantic • 19h ago

---

**[Ukraine using AI drones to strike vital convoys supplying Russian troops](https://www.bbc.com/news/articles/cdjp0n7rn41o)**

BBC Verify has analysed videos of attacks in occupied Ukraine on Russian trucks carrying ammunition, fuel and food.

BBC • 5h ago

---

**["The pitchforks are here": Billionaires work to contain AI's populist revolt](https://www.axios.com/2026/05/29/ai-billionaires-tech-taxes-wealth)**

Axios • 20h ago

---

**[AI ‘voice cloning’ scams are on the rise. Here’s how to protect yourself](https://www.cnn.com/2026/05/29/tech/ai-voice-cloning-scams-protect-yourself)**

A California mom says she was scammed out of thousands of dollars this month after receiving a call that sounded like her daughter in distress. She now suspects it was an artificial intelligence-generated hoax.

CNN • 21h ago

---

**[Opinion | How America can remain the world’s AI superpower](https://www.washingtonpost.com/opinions/2026/05/29/us-artificial-intelligence-supremacy-depends-taking-these-essential-steps/)**

Staying ahead of China requires pioneering technology — and stopping Chinese AI from conquering the world.

The Washington Post • 12h ago

---

**[A.I. Boom Leads to Record Home Prices in San Francisco](https://www.nytimes.com/2026/05/29/realestate/san-francisco-ai-housing-market.html)**

The New York Times • 21h ago

---

**[9 demos of Gemini Omni and Gemini 3.5 in action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-3-5-videos/)**

Watch 9 videos showing the capabilities of Gemini Omni and Gemini 3.5, announced at Google I/O 2026.

blog.google • 12h ago

---

---

## HackerNews: "ai"

**[I'm Tired of Talking to AI](https://news.ycombinator.com/item?id=48292224)**

I found GitHub repositories that were spreading malware. I asked AI what to do about it, but it gave me nothing useful. So I opened a discussion on GitHub. Someone replied. It was the exact same text the AI had given me. I called it out and the comment was

⬆️ 1989 • 💬 948 • 2d ago • [Orchid Files](https://orchidfiles.com/im-tired-of-ai-generated-answers/)

---

**[YouTube to automatically label AI-generated videos](https://news.ycombinator.com/item?id=48299753)**

We've heard consistently from our community that they value transparency when it comes to generative AI content. Two new updates will make this process much simpler and more intuitive for creators and viewers on YouTube.

⬆️ 1307 • 💬 817 • 2d ago • [blog.youtube](https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/)

---

**[DuckDuckGo search saw 28% more visits after Google said people love AI mode](https://news.ycombinator.com/item?id=48296649)**

"People just want a choice."

⬆️ 1067 • 💬 517 • 2d ago • [PC Gamer](https://www.pcgamer.com/hardware/duckduckgos-ai-free-search-saw-nearly-28-percent-more-visits-in-the-week-following-googles-insistence-that-people-love-ai-mode/)

---

**[Please Use AI](https://news.ycombinator.com/item?id=48323101)**

⬆️ 730 • 💬 379 • 16h ago • [shawnsmucker.substack.com](https://shawnsmucker.substack.com/p/please-use-ai)

---

**[Tech CEOs are apparently suffering from AI psychosis](https://news.ycombinator.com/item?id=48295679)**

"CEOs are uniquely prone to AI psychosis," Box CEO Aaron Levie opines. Maybe that explains the almost religious belief in AI productivity gains.

⬆️ 716 • 💬 355 • 2d ago • [TechCrunch](https://techcrunch.com/2026/05/27/tech-ceos-are-apparently-suffering-from-ai-psychosis/)

---

**[Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue](https://news.ycombinator.com/item?id=48308376)**

A 30-second game about LLM permission fatigue. How carefully do you really read AI commands?

⬆️ 376 • 💬 154 • 1d ago • [llmgame.scalex.dev](https://llmgame.scalex.dev)

---

**[Notes from the Mistral AI Now Summit](https://news.ycombinator.com/item?id=48325340)**

A few days in Paris for the Mistral AI Now Summit: open models, on-prem deployment, agentic harnesses, and why Mistral wants to be the European full-stack AI partner.

⬆️ 335 • 💬 127 • 14h ago • [koenvangilst.nl](https://koenvangilst.nl/lab/mistral-ai-now-summit)

---

**[Is AI causing a repeat of frontend’s lost decade?](https://news.ycombinator.com/item?id=48321631)**

AI is doing to programming what framework-brain did to the frontend before. Deskilling, or just working at a higher level of abstraction?

⬆️ 323 • 💬 279 • 19h ago • [mastrojs.github.io](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/)

---

**[SF startup is testing robots in Airbnbs, and trashing them, lawsuit claims](https://news.ycombinator.com/item?id=48317093)**

The guests behind the bookings have received negative reviews from a number of Bay Area hosts, alleging they damaged the property and personal belongings.

⬆️ 263 • 💬 145 • 1d ago • [sfstandard.com](https://sfstandard.com/2026/05/28/sf-startup-secretly-testing-robots-airbnbs-trashing-lawsuit-claims/)

---

**[Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions](https://news.ycombinator.com/item?id=48314363)**

Some leaders like Goldman Sachs’s David Solomon and Box’s Aaron Levie have been saying all along that there won’t be a white-collar wipeout.

⬆️ 231 • 💬 178 • 1d ago • [Fortune](https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/)

---

---

## YouTube Videos: "ai"

**[How Helpful Is A.I. ACTUALLY? Here’s The Truth](https://www.youtube.com/watch?v=M4eKkEmuoXo)**

Mack Weldon - Go to MackWeldon.com and get 20% off your first order of $125 or more, with promo code WALSH. AI is repeatedly ...

📺 Matt Walsh

👁️ 33K • 👍 2K • 💬 490 • ⏱️ 9:44 • 1d ago

---

**[If you’re trying to get rich with AI, you need to hear this…](https://www.youtube.com/watch?v=TWuzAO7ukk0)**

Want my AI Tech Stack? Get it here: https://go.danmartell.com/4nUvaZi Are you building an AI software company? Partner with ...

📺 Dan Martell

👁️ 53K • 👍 2K • 💬 102 • ⏱️ 14:06 • 1d ago

---

**[AI Whistleblower WARNS: You Have NO Idea About The AI Wave That Is Coming](https://www.youtube.com/watch?v=fo2ggNE-44g)**

Eliezer Yudkowsky, who has spent 30 years on the AI safety problem, makes a firm prediction: if anyone builds a superintelligence ...

📺 Neural Nutshell

👁️ 19K • 👍 533 • 💬 123 • ⏱️ 22:04 • 2d ago

---

**[AI Quietly Ruined These People&#39;s Lives](https://www.youtube.com/watch?v=pdoifbNBMjM)**

AI was supposed to make life easier, but what happens when it goes wrong? This video explores a situation where a car's artificial ...

📺 ThumbSized Facts

👁️ 423K • 👍 16K • 💬 283 • ⏱️ 1:18 • 2d ago

---

**[They Are Building A &quot;New God&quot; | Revelation 13 and the AI Image Of The Beast](https://www.youtube.com/watch?v=ErNmkFo0COw)**

They are building an ai god, is this the image of the beast from Revelation 13? Today I look at this end times prophecy from the ...

📺 Sling and Stone

👁️ 15K • 👍 2K • 💬 319 • ⏱️ 16:13 • 1d ago

---

**[Google Just Dropped The Singularity Bomb](https://www.youtube.com/watch?v=BH5_FEJNOGY)**

Google DeepMind's Demis Hassabis says humanity may already be standing in the foothills of the singularity. AI agents are now ...

📺 AI Revolution

👁️ 43K • 👍 2K • 💬 176 • ⏱️ 13:24 • 1d ago

---

**[EMERGENCY DEBATE: They Are Lying To Us About AI, The Iran War &amp; What Happens Next!](https://www.youtube.com/watch?v=H-8NrKFQKhU)**

Shark Tank's Kevin O'Leary and political commentator Cenk Uygur go head to head on whether AI will save or destroy the ...

📺 The Diary Of A CEO

👁️ 779K • 👍 21K • 💬 8K • ⏱️ 1:43:32 • 1d ago

---

**[AI Data Centers (This is Disturbing)](https://www.youtube.com/watch?v=9sGEzO-sXH8)**

Due to the ability to earn higher profits through increased electric usage for Power Companies, it's no wonder Power Companies ...

📺 EKE ACRES

👁️ 9K • 💬 207 • ⏱️ 3:40 • 1d ago

---

**[The Rise Of AI, The Future Of Humanity ](https://www.youtube.com/watch?v=elOxI2Iz4JI)**

ai #technology #programming #thefutureoftechnology.

📺 HASSAN CAMPBELL

👁️ 21K • 👍 2K • 💬 239 • ⏱️ 24:21 • 1d ago

---

**[The Dead Sea Scrolls Were Re-analyzed by AI — What It Revealed Changes Everything](https://www.youtube.com/watch?v=P3AoPNv7xjs)**

In 1947, a shepherd's thrown rock revealed the Dead Sea Scrolls — the oldest biblical manuscripts ever found. For 75 years ...

📺 Flash Discovery

👁️ 22K • 👍 179 • 💬 11 • ⏱️ 25:08 • 13h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 23,629 • ❤️ 578 • 4d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 7,861 • ❤️ 416 • 2d ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 397 • 4d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,114,938 • ❤️ 1,063 • 1mo ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 2,738 • ❤️ 974 • 2d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 8,854 • ❤️ 229 • 14h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,836,444 • ❤️ 4,443 • 24d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 14,727 • ❤️ 446 • 9d ago

---

**[PiD](https://huggingface.co/nvidia/PiD)**

*NVIDIA*

PiD is a conditional pixel-space diffusion model that unifies decoding and upsampling for image-to-image tasks. It performs super-resolution in a single pass, directly denoising in high-resolution pixel space, supporting up to 4x or 8x upscaling for various base models like Flux and SD3.

`image-to-image`

⬇️ 389 • ❤️ 178 • 4d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 131,828 • ❤️ 411 • 9d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 201 • 💬 3 • ⭐ 2,863 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 80,706 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 27,372 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://huggingface.co/papers/2605.30263)**

*Min Zhao, Hongzhou Zhu, Bokai Yan et al. (12 authors)*

A comprehensive framework is presented for converting bidirectional video diffusion models into real-time interactive world models with controllable, causal, and low-latency capabilities through fine-tuning and distillation techniques.

▲ 43 • 💬 2 • ⭐ 323 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30263) • [💻 code](https://github.com/shengshu-ai/minWM)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,605 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://huggingface.co/papers/2602.08968)**

*Lucas Maes, Quentin Le Lidec, Dan Haramati et al. (7 authors)*

🏢 galilai-group

Stable-worldmodel provides a modular and standardized research framework for developing and evaluating world models with controllable environmental factors for robustness and continual learning applications.

▲ 4 • 💬 0 • ⭐ 1,245 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.08968) • [💻 code](https://github.com/galilai-group/stable-worldmodel) • [🔗 project](https://galilai-group.github.io/stable-worldmodel/)

---

**[MOSS-TTS Technical Report](https://huggingface.co/papers/2603.18090)**

*Yitian Gong, Botian Jiang, Yiwei Zhao et al. (26 authors)*

🏢 OpenMOSS

MOSS-TTS is a speech generation model using discrete audio tokens and autoregressive modeling with capabilities for voice cloning, pronunciation control, and long-form generation across multiple languages.

▲ 14 • 💬 2 • ⭐ 2,493 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.18090) • [💻 code](https://github.com/OpenMOSS/MOSS-TTS) • [🔗 project](https://mosi.cn/models/moss-tts)

---

**[Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of
  Encoders](https://huggingface.co/papers/2408.15998)**

*Min Shi, Fuxiao Liu, Shihao Wang et al. (15 authors)*

Mixture of vision encoders and resolutions in multimodal large language models improves performance through concatenation of visual tokens and a Pre-Alignment mechanism, leading to superior results on benchmarks.

▲ 86 • 💬 3 • ⭐ 1,497 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2408.15998) • [💻 code](https://github.com/nvlabs/eagle)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 75,357 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 128 • 💬 8 • ⭐ 78,957 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.4k • 🔱 535 • 1d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.9k • 🔱 615 • 4d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.8k • 🔱 189 • 22h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 399 • 8d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 358 • 12d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.1k • 🔱 140 • 14h ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 2.0k • 🔱 184 • 21h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.0k • 🔱 203 • 5d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.9k • 🔱 226 • 22d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.8k • 🔱 206 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
