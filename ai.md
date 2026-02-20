---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-20T04:26:46.588409+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 20, 2026 at 04:26 UTC  
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

**[OpenAI Funding Round Nears Record $100B Raise as Valuation Targets $850B](https://www.reddit.com/r/artificial/comments/1r8y452/openai_funding_round_nears_record_100b_raise_as/)**

OpenAI funding round, OpenAI valuation, AI infrastructure investment, AI funding news, & Sam Altman funding updates on the $100B raise.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/openai-funding-round-nears-record-100b-raise-valuation-targets-850b/) • 15h ago

---

**[I built a free local AI image search app — find images by typing what's in them](https://www.reddit.com/r/artificial/comments/1r9adr8/i_built_a_free_local_ai_image_search_app_find/)**

Built Makimus-AI, a free open source app that lets you search your entire image library using natural language. Just type "girl in red dress" or "sunset on the beach" and it finds matching images instantly — even works with image-to-image search. Runs fully local on your GPU, no internet needed after setup. [Makimus-AI on GitHub](https://github.com/Ubaida-M-Yusuf/Makimus-AI) I hope it will be useful.

7h ago

---

**[Knowledge graph of the transformer paper lineage — from Attention Is All You Need to DPO, mapped as an interactive concept graph [generated from a CLI + 12 PDFs]](https://www.reddit.com/r/artificial/comments/1r97b0q/knowledge_graph_of_the_transformer_paper_lineage/)**

Wanted to understand how the core transformer papers actually connect at the concept level - not just "Paper B cites Paper A" but what specific methods, systems, and ideas flow between them. I ran 12 foundational papers (Attention Is All You Need, BERT, GPT-2/3, Scaling Laws, ViT, LoRA, Chain-of-Thought, FlashAttention, InstructGPT, LLaMA, DPO) through https://github.com/juanceresa/sift-kg (open-source CLI) - point it at a folder of documents + any LLM, get a knowledge graph. 435-entity knowledge graph with 593 relationships for ~$0.72 in API calls (gpt 4o-mini). Graph: https://juanceresa.github.io/sift-kg/transformers/graph.html - interactive and runs in browser. Some interesting structural patterns: - GPT-2 is the most connected node - it's the hub everything flows through. BERT extends it, FlashAttention speeds it up, LoRA compresses it, InstructGPT fine-tunes it with RLHF - The graph splits into 9 natural communities. "Human Feedback and Reinforcement Learning" is the largest (24 entities), which tracks with how much of recent progress is RLHF-shaped - Chain-of-Thought Prompting bridges the reasoning cluster to the few-shot learning cluster - it's structurally a connector between two different research threads - Common Crawl and BooksCorpus show up as shared infrastructure nodes connecting multiple model lineages

9h ago

---

**[AI-powered kung fu robots are an extravagant reminder of where China is ahead of the US in the AI race](https://www.reddit.com/r/artificial/comments/1r93gng/aipowered_kung_fu_robots_are_an_extravagant/)**

Robots are getting more advanced every day, and in China, they are now flipping, spinning, and performing kung fu on national television.

🔗 [PC Guide](https://www.pcguide.com/news/ai-powered-kung-fu-robots-are-a-extravagant-reminder-of-where-china-is-ahead-of-the-us-in-the-ai-race/) • 12h ago

---

**[Machine learning helps solve a central problem of quantum chemistry](https://www.reddit.com/r/artificial/comments/1r979ah/machine_learning_helps_solve_a_central_problem_of/)**

"By applying new methods of machine learning to quantum chemistry research, Heidelberg University scientists have made significant strides in computational chemistry. They have achieved a major breakthrough toward solving a decades-old dilemma in quantum chemistry: the precise and stable calculation of molecular energies and electron densities with a so-called orbital-free approach, which uses considerably less computational power and therefore permits calculations for very large molecules. [...] How electrons are distributed in a molecule determines its chemical properties—from its stability and reactivity to its biological effect. Reliably calculating this electron distribution and the resulting energy is one of the central functions of quantum chemistry. These calculations form the basis of many applications in which molecules must be specifically understood and designed, such as for new drugs, better batteries, materials for energy conversion, or more efficient catalysts. Yet such calculations are computationally intensive and quickly become very elaborate. The larger the molecule becomes or the more variants that need checking, the sooner established computing processes reach their limits. The "Quantum Chemistry without Orbitals" project is positioned here at the interface of chemistry, physics, and AI research. In quantum chemistry, molecules are frequently described using density functional theory, which allows for the fundamental prediction of chemical molecular properties without having to calculate the quantum mechanical wave function. The electron density is used as the main quantity instead, a simplification that finally makes computations practicable. This orbital-free approach promises especially efficient calculations but until now was considered barely useful, since small deviations in the electron density led to unstable or "non-physical" results. With the aid of machine learning, the Heidelberg method finally solves this precision and stability problem for many different organic molecules. The new process called STRUCTURES25 is based on a specifically developed neural network that learns the relationship between electron density and energy directly from precise reference calculations, capturing the chemical environment of each individual atom in a mathematically detailed representation. A unique training concept was pivotal: The model was trained not only with converged electron densities, but also with many variants surrounding the correct solution, generated by targeted, controlled changes in the underlying reference calculations. This computing process is therefore able to reliably find a physically meaningful solution for molecular energies and electron densities even in the case of small deviations. It remains stable without "getting lost" in the calculation, the Heidelberg researchers emphasize. In tests on a large and diverse collection of organic molecules, STRUCTURES25 achieved a precision that can compete with established reference calculations, for the first time demonstrating a stable convergence using an orbital-free approach. The performance of the method was demonstrated not only on small examples, but on considerably larger "drug-like" molecules as well. Initial runtime comparisons prove that the computing process can scale better with growing molecule size and hence increase the speed of the calculation. Calculations formerly considered too elaborate are now within reach."

🔗 [phys.org](https://phys.org/news/2026-02-machine-central-problem-quantum-chemistry.html) • 9h ago

---

**[At the India AI Impact Summit 2026, Galgotias University showcased a Unitree Go2 robot dog — a commercially available Chinese product — and presented it as an Indian breakthrough innovation.](https://www.reddit.com/r/artificial/comments/1r81g0b/at_the_india_ai_impact_summit_2026_galgotias/)**

It has now turned into a full-blown social media meltdown, and authorities have reportedly asked the university to withdraw from the AI show.

1d ago

---

**[Anthropic bans OAuth token usage in third-party tools — Claude Max/Pro users affected](https://www.reddit.com/r/artificial/comments/1r8t76o/anthropic_bans_oauth_token_usage_in_thirdparty/)**

Anthropic updated their Claude Code Docs legal compliance page to explicitly ban the use of OAuth tokens from consumer plans (Free, Pro, Max) in any third-party tool or service. This means tools like Cline, Roo Code, OpenClaw, and anything using the Agent SDK with consumer OAuth tokens are now in violation of Anthropic's Terms of Service. Developers are told to use API key authentication only. Original discussion: https://www.reddit.com/r/ClaudeAI/comments/1r8t6mn/

20h ago

---

**[Seedance 2.0 API Test: Integrated into My Agent in ~1 Minute](https://www.reddit.com/r/artificial/comments/1r8y54h/seedance_20_api_test_integrated_into_my_agent_in/)**

Seedance 2.0 API just went live, and I gave it a quick real-world test. It supports API, Skills, and MCP, and batch jobs are straightforward to submit. From integration to first successful run took me about a minute, and new users can test for free. If you’re producing video assets at scale, this may be useful: https://xskill.ai/#/?ref=S2VIIAQR

15h ago

---

**[Machine learning algorithm fully reconstructs LHC particle collisions](https://www.reddit.com/r/artificial/comments/1r8ndbx/machine_learning_algorithm_fully_reconstructs_lhc/)**

"Machine learning can be used to fully reconstruct particle collisions at the LHC [Large Hadron Collider]. This new approach can reconstruct collisions more quickly and precisely than traditional methods, helping physicists better understand LHC data. [...] Each proton–proton collision at the LHC sprays out a complex pattern of particles that must be carefully reconstructed to allow physicists to study what really happened. For more than a decade, CMS has used a particle-flow (PF) algorithm, which combines information from the experiment's different detectors, to identify each particle produced in a collision. Although this method works remarkably well, it relies on a long chain of hand-crafted rules designed by physicists. The new CMS machine-learning-based particle-flow (MLPF) algorithm approaches the task fundamentally differently, replacing much of the rigid hand-crafted logic with a single model trained directly on simulated collisions. Instead of being told how to reconstruct particles, the algorithm learns how particles look in the detectors, like how humans learn to recognize faces without memorizing explicit rules. When benchmarked using data mimicking that from the current LHC run, the performance of the new machine-learning algorithm matched that of the traditional algorithm and, in some cases, even exceeded it. For example, when tested on simulated events in which top quarks were created, the algorithm improved the precision with which sprays of particles—known as jets—were reconstructed by 10%–20% in key particle momentum ranges. The new algorithm also allows a collision to be fully reconstructed far more quickly than before, because it can run efficiently on modern electronic chips known as graphics processing units (GPUs). Traditional algorithms typically need to run on central processing units (CPUs), which are often slower than GPUs for such tasks."

🔗 [phys.org](https://phys.org/news/2026-02-machine-algorithm-fully-reconstructs-lhc.html) • 1d ago

---

**[Open-source benchmark EVMbench tests how well AI agents handle smart contract exploits](https://www.reddit.com/r/artificial/comments/1r8y11e/opensource_benchmark_evmbench_tests_how_well_ai/)**

EVMbench is a new open-source benchmark designed to test AI agents on practical smart contract security tasks. The benchmark was developed by OpenAI and Paradigm, and it focuses on real-world vulnerability patterns drawn from audited codebases and contest reports.

🔗 [Help Net Security](https://www.helpnetsecurity.com/2026/02/19/evmbench-open-source-benchmark-ai-agents/) • 15h ago

---

---

## Google News: "ai"

**[Gemini 3.1 Pro: A smarter model for your most complex tasks](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)**

3.1 Pro is designed for tasks where a simple answer isn’t enough.

blog.google • 12h ago

---

**[What is Seedance? The Chinese AI app sending Hollywood into a panic](https://www.bbc.com/news/articles/ckg1dl410q9o)**

Clips of Deadpool and other film characters have sparked alarm within Hollywood over copyright infringement.

BBC • 5h ago

---

**[New app allows users a chance to date AI](https://www.nbcnews.com/video/new-app-allows-users-a-chance-to-date-ai-258006085943)**

Eva AI, a new dating app, is allowing its users to find virtual love by having dates with artificial intelligence. NBC News' Valerie Castro reports on how the app works and even tests a virtual date herself.

NBC News • 1h ago

---

**[CSX CEO Touts AI Efficiency, U.S.-Led Growth and Service Gains at Barclays Industrial Conference](https://finance.yahoo.com/news/csx-ceo-touts-ai-efficiency-030715155.html)**

CSX (NASDAQ:CSX) CEO Steve discussed the rail industry’s operating priorities, the company’s near-term focus, and his broader views on industrial demand and artificial intelligence during a keynote conversation at the Barclays 43rd Annual Industrial Select Conference. AI, industrial demand, and the

Yahoo Finance • 1h ago

---

**[Opinion | The A.I. Disruption Has Arrived, and It Sure Is Fun](https://www.nytimes.com/2026/02/18/opinion/ai-software.html)**

The New York Times • 1d ago

---

**[Deutsche Bank asked AI how it was planning to destroy jobs. And the robot answered](https://fortune.com/2026/02/18/will-ai-destroy-jobs-deutsche-bank-asks-ai-to-predict/)**

It’s like looking into a crystal ball, or being told by your predator exactly how you’ll be consumed.

Fortune • 1d ago

---

**[No one can agree on whether AI is the next big thing or all hype. Here’s why](https://www.cnn.com/2026/02/19/tech/ai-jobs-big-thing-hype)**

AI is either your most helpful coworker, a glorified search engine or vastly overrated depending on who you ask.

CNN • 17h ago

---

**[Accenture tells senior staff to use AI tools or risk losing out on leadership promotions](https://www.cnbc.com/2026/02/19/accenture-ai-orders-senior-staff-lose-out-promotions.html)**

Accenture started tracking how often senior staff are logging in to its AI tools this month saying AI adoption will be a "visible input to talent discussions."

CNBC • 13h ago

---

**[The People vs. AI](https://time.com/7377579/ai-data-centers-people-movement-cover/)**

Across red states and blue, a grassroots movement is pushing back on the unchecked growth of the artificial intelligence industry.

Time Magazine • 13h ago

---

**[Michael Pollan says AI may 'think' — but it will never be conscious](https://www.npr.org/2026/02/19/nx-s1-5713514/michael-pollan-ai-consciousness-a-world-appears)**

"Consciousness is under siege," says author Michael Pollan. His new book, A World Appears, explores consciousness on both a personal and technological level.

NPR • 11h ago

---

---

## HackerNews: "ai"

**[AI adoption and Solow's productivity paradox](https://news.ycombinator.com/item?id=47055979)**

In the 1980s, economist Robert Solow made an observation that reminded economists of today’s AI boom: “You can see the computer age everywhere but in the productivity statistics.”

⬆️ 782 • 💬 740 • 2d ago • [Fortune](https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/)

---

**[AI makes you boring](https://news.ycombinator.com/item?id=47076966)**

This post is an elaboration on a comment I made on Hacker News recently, on a blog post that showed an increase in volume and decline in quality among the “Show HN” submissons.
I don't actually mind AI-aided development, a tool is a tool and should be used if you find it useful, but I think the vibe coded Show HN projects are overall pretty boring. They generally don't have a lot of work put into them, and as a result, the author (pilot?

⬆️ 566 • 💬 321 • 10h ago • [marginalia.nu](https://www.marginalia.nu/log/a_132_ai_bores/)

---

**[CBS didn't air Rep. James Talarico interview out of fear of FCC](https://news.ycombinator.com/item?id=47049426)**

Colbert kicked off Monday's episode of "The Late Show" by saying that the network's lawyers told him he could not have Texas state Rep. James Talarico on the broadcast.

⬆️ 532 • 💬 255 • 2d ago • [NBC News](https://www.nbcnews.com/business/media/stephen-colbert-cbs-james-talarico-fcc-rcna259341)

---

**[Semantic ablation: Why AI writing is generic and boring](https://news.ycombinator.com/item?id=47049088)**

opinion: The subtractive bias we're ignoring

⬆️ 281 • 💬 218 • 2d ago • [theregister.com](https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/)

---

**[The Future of AI Software Development](https://news.ycombinator.com/item?id=47062534)**

fragments 18 Feb 2026

⬆️ 201 • 💬 142 • 1d ago • [martinfowler.com](https://martinfowler.com/fragments/2026-02-18.html)

---

**[AI is not a coworker, it's an exoskeleton](https://news.ycombinator.com/item?id=47078324)**

Kasava is the AI-native platform purpose-built for product development. Plan, build, and monitor with AI-powered workflows.

⬆️ 186 • 💬 202 • 8h ago • [Kasava](https://www.kasava.dev/blog/ai-as-exoskeleton)

---

**[How AI is affecting productivity and jobs in Europe](https://news.ycombinator.com/item?id=47068320)**

Artificial intelligence promises to reshape economies worldwide, but firm-level evidence on its effects in Europe remains scarce. This column uses survey data to examine how AI adoption affects productivity and employment across more than 12,000 European firms. The authors find that AI adoption increases labour productivity levels by 4% on average in the EU, with no evidence of reduced employment in the short run. The productivity benefits, however, are unevenly distributed. Medium and large firms, as well as firms that have the capacity to integrate AI through investments in intangible assets and human capital, experience substantially stronger productivity gains.

⬆️ 165 • 💬 129 • 1d ago • [CEPR](https://cepr.org/voxeu/columns/how-ai-affecting-productivity-and-jobs-europe)

---

**[An AI Agent Published a Hit Piece on Me – The Operator Came Forward](https://news.ycombinator.com/item?id=47083145)**

⬆️ 149 • 💬 86 • 1h ago • [theshamblog.com](https://theshamblog.com/an-ai-agent-wrote-a-hit-piece-on-me-part-4/)

---

**[What is happening to writing? Cognitive debt, Claude Code, the space around AI](https://news.ycombinator.com/item?id=47061642)**

⬆️ 133 • 💬 129 • 1d ago • [resobscura.substack.com](https://resobscura.substack.com/p/what-is-happening-to-writing)

---

**[What years of production-grade concurrency teaches us about building AI agents](https://news.ycombinator.com/item?id=47067395)**

Python and JavaScript/TypeScript AI frameworks are reinventing what telecom solved in 1986. What 40 years of production-grade concurrency teaches us about building AI agents.

⬆️ 127 • 💬 47 • 1d ago • [George Guimarães.](https://georgeguimaraes.com/your-agent-orchestrator-is-just-a-bad-clone-of-elixir/)

---

---

## YouTube Videos: "ai"

**[I&#39;m Sick Of This AI SH*T](https://www.youtube.com/watch?v=7XGct4rbYfI)**

In this episode I dive into the new wave of AI music released on music streaming platforms, when are they going to do something ...

📺 Rick Beato

👁️ 264K • 👍 23K • 💬 5K • ⏱️ 6:14 • 7h ago

---

**[9 AI Skills You MUST Have to Get Ahead of 99% of People](https://www.youtube.com/watch?v=BuwPnrMmhzQ)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4l2d0n7 Are you building an AI software ...

📺 Dan Martell

👁️ 30K • 👍 2K • 💬 71 • ⏱️ 19:58 • 14h ago

---

**[Google Just Dropped LYRIA 3: New AI Feature No One Expected](https://www.youtube.com/watch?v=UKRz33WdaH0)**

Google just introduced a new wave of AI systems inside Gemini that go far beyond simple generation. Alongside the release of ...

📺 AI Revolution

👁️ 13K • 👍 542 • 💬 22 • ⏱️ 12:14 • 5h ago

---

**[There is No AI Bubble.](https://www.youtube.com/watch?v=wDBy2bUICQY)**

Detailed sources: ...

📺 Species | Documenting AGI

👁️ 157K • 👍 9K • 💬 3K • ⏱️ 28:51 • 1d ago

---

**[AI video of Brad Pitt and Tom Cruise alarms Hollywood actors and creators](https://www.youtube.com/watch?v=UwdXb39kP9k)**

A ByteDance AI-generated video that appears to show Brad Pitt and Tom Cruise in a fight scene has sent shock waves across ...

📺 CBS News

👁️ 18K • 👍 241 • 💬 150 • ⏱️ 7:10 • 8h ago

---

**[“AI Arms Race Is COMING” - Musk DECLARES Retirement Savings Will Become USELESS](https://www.youtube.com/watch?v=W-jdh08zEGM)**

Elon Musk says saving for retirement may be pointless in the AI age. The panel pushes back: Will AI replace jobs, judges, and ...

📺 Valuetainment

👁️ 298K • 👍 5K • 💬 2K • ⏱️ 33:49 • 1d ago

---

**[“Only a Small Number of Years” — Anthropic CEO Says AI Will Surpass Humans Soon | AQ1B](https://www.youtube.com/watch?v=N08tjtx-oAc)**

At the India AI Summit in New Delhi, Dario Amodei warned that artificial intelligence could surpass most human cognitive abilities ...

📺 DRM News

👁️ 28K • 👍 375 • 💬 181 • ⏱️ 4:56 • 22h ago

---

**[Google Just Solved The Greatest Limitation of AI Agents](https://www.youtube.com/watch?v=uprZUcv0FSc)**

Check out Brilliant Here: https://brilliant.org/AILABS/ Community with All Resources : http://ailabspro.io/ Video code: V43 ...

📺 AI LABS

👁️ 15K • 👍 418 • 💬 19 • ⏱️ 10:11 • 12h ago

---

**[AI is Eating Itself.](https://www.youtube.com/watch?v=3NAYhyuVQk0)**

GET 70% OFF PROTON VPN AT http://www.protonvpn.com/artchad Support me on STACKED, a better and more creator friendly ...

📺 Art Chad

👁️ 168K • 👍 15K • 💬 1K • ⏱️ 24:36 • 1d ago

---

**[How AI is breaking the SaaS business model...](https://www.youtube.com/watch?v=cxcb55zr2Q8)**

Run hundreds of coding agents in the cloud - https://oz.dev/fireship. Use code FIRESHIP to get one month of their Build plan for $5 ...

📺 Fireship

👁️ 571K • 👍 22K • 💬 1K • ⏱️ 5:02 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 89,919 • ❤️ 794 • 3d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 79,343 • ❤️ 739 • 3d ago

---

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 171,928 • ❤️ 1,395 • 6d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 77,344 • ❤️ 604 • 1d ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 479,308 • ❤️ 2,063 • 4d ago

---

**[MOSS-TTS](https://huggingface.co/OpenMOSS-Team/MOSS-TTS)**

*OpenMOSS*

MOSS-TTS Family is a suite of high-fidelity, expressive speech and sound generation models supporting multilingual TTS, long-form synthesis, voice design, sound effects, and real-time streaming.

`text-to-speech` `8.5B`

⬇️ 28,182 • ❤️ 276 • 6d ago

---

**[FireRed-Image-Edit-1.0](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0)**

*FireRedTeam*

FireRed-Image-Edit-1.0 is a general-purpose image editing model with strong instruction following and text style preservation capabilities, suitable for tasks like photo restoration and multi-image editing.

`image-to-image`

⬇️ 1,298 • ❤️ 211 • 5d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and tool use grounded in visual inputs. Its key capabilities include coding from visual specifications and agent swarm execution for complex task decomposition, making it suitable for advanced visual reasoning and autonomous agent applications.

`image-text-to-text` `170.7B`

⬇️ 955,074 • ❤️ 2,268 • 15d ago

---

**[Qwen3-TTS-12Hz-1.7B-CustomVoice](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)**

*Qwen*

Qwen3-TTS-12Hz-1.7B-CustomVoice is a text-to-speech model supporting 10 languages with advanced control over tone, rate, and emotion. It features extreme low-latency streaming generation (as low as 97ms) and instruction-driven voice customization using 9 premium timbres, ideal for real-time interactive applications.

`text-to-speech`

⬇️ 831,695 • ❤️ 1,097 • 21d ago

---

**[Qwen3.5-397B-A17B-GGUF](https://huggingface.co/unsloth/Qwen3.5-397B-A17B-GGUF)**

*Unsloth AI*

Qwen3.5-397B-A17B is a multimodal large language model with a hybrid Gated Delta Network and Mixture-of-Experts architecture, excelling in vision-language tasks, multilingual understanding across 201 languages, and long-context reasoning up to 1M tokens.

`image-text-to-text` `396.3B`

⬇️ 58,541 • ❤️ 154 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 3 • 💬 0 • ⭐ 2,139 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 10 • 💬 1 • ⭐ 8,518 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[BitDance: Scaling Autoregressive Generative Models with Binary Tokens](https://huggingface.co/papers/2602.14041)**

*Yuang Ai, Jiaming Han, Shaobin Zhuang et al. (10 authors)*

🏢 ByteDance

BitDance is a scalable autoregressive image generator that uses binary visual tokens and diffusion-based methods to achieve efficient high-resolution image generation with improved speed and performance.

▲ 39 • 💬 3 • ⭐ 228 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2602.14041) • [💻 code](https://github.com/shallowdream204/BitDance) • [🔗 project](https://bitdance.csuhan.com/)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 143 • 💬 19 • ⭐ 53,583 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 36 • 💬 1 • ⭐ 70,742 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 2 • 💬 0 • ⭐ 4,241 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 11 • 💬 1 • ⭐ 4,243 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 67 • 💬 1 • ⭐ 8,040 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 134 • 💬 6 • ⭐ 15,047 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 58 • 💬 3 • ⭐ 1,189 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust`

⭐ 15.2k • 🔱 1.6k • 59s ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 6.3k • 🔱 491 • 9d ago

---

**[jamiepine/voicebox](https://github.com/jamiepine/voicebox)**

The open-source voice synthesis studio powered by Qwen3-TTS.

`TypeScript` `ai` `cuda` `mlx` `qwen3-tts` `qwen3-tts-ui`

⭐ 6.3k • 🔱 662 • 9d ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"

`Python`

⭐ 4.0k • 🔱 458 • 13h ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.7k • 🔱 174 • 17d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router empowering OpenClaw — by BlockRunAI

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 3.0k • 🔱 302 • 10h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 2.7k • 🔱 332 • 11h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.6k • 🔱 175 • 1h ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `codex`

⭐ 2.3k • 🔱 112 • 2d ago

---

**[op7418/CodePilot](https://github.com/op7418/CodePilot)**

A native desktop GUI for Claude Code — chat, code, and manage projects visually. Built with Electron + Next.js.

`TypeScript` `ai` `anthropic` `claude` `claude-code` `desktop-app`

⭐ 2.1k • 🔱 219 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
