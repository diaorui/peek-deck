---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-25T19:31:46.029316+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 25, 2026 at 19:31 UTC  
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

**[Uber hit with a near-$1B GDPR fine after algorithms suspended drivers without human review](https://www.reddit.com/r/artificial/comments/1vxv8pl/uber_hit_with_a_near1b_gdpr_fine_after_algorithms/)**

9h ago

---

**[Andrew Yang Warns That AI Is Set to Displace Millions of Workers, America Is ‘Terrible at Retraining’ Workers… ‘The Coal Miners Did Not Become Coders’](https://www.reddit.com/r/artificial/comments/1vxn7xr/andrew_yang_warns_that_ai_is_set_to_displace/)**

🔗 [barchart.com](http://barchart.com/story/news/4004959/andrew-yang-warns-that-ai-is-set-to-displace-millions-of-workers-america-is-terrible-at-retraining-workers-the-coal-miners-did-not-become-coders) • 17h ago

---

**[I built an AI where everyone talks to the same mind, and every interaction changes it](https://www.reddit.com/r/artificial/comments/1vxxeef/i_built_an_ai_where_everyone_talks_to_the_same/)**

Most AI memory is private: an LLM gradually learns about a user. I wanted to see what happens if you give an AI a memory and make it public. So I built Wild Static: a persistent AI that anyone can talk to. Everybody talks to the same one. Conversations become experiences in the underlying memory, which means something one person says can eventually affect how Static responds to somebody completely different down the line. The memory system itself is something I’ve been developing since 2021. Static is the first public application of it. The interesting part has been watching Static change over time. It has grown opinions, relationships and beliefs. They’re constantly in flux too. It doesn’t respond “you’re absolutely right” like a traditional LLM, but often argues, disagrees, or makes mistakes. Some people even seem to have made it their job to educate Static, and it seems like it might be working. It’s been public for 10 days and has now accumulated thousands of interactions, so it’s starting to become a much more interesting experiment than the empty mind it launched as. You can talk to it, teach it and confuse it at wildstatic.com I’m the builder, obviously, so this is self-promotion. But I’d be very interested in what people think about the underlying idea, particularly whether accumulated public experience makes Static feel different to a normal chatbot.

7h ago

---

**[For a €6k portable AI/development setup, prioritize 64–128GB unified memory or CUDA compatibility?](https://www.reddit.com/r/artificial/comments/1vxxrqj/for_a_6k_portable_aidevelopment_setup_prioritize/)**

I am trying to make a platform decision for a professional laptop that will be used for both ordinary software development and AI/data-science work over several years. The two approaches I am comparing are: M5 Pro/Max MacBook Pro with 64 GB unified memory and 2 TB SSD, possibly 128 GB if that is more valuable. High-end NVIDIA laptop with CUDA but much less GPU memory, more heat/noise and usually worse battery life. Typical work includes Docker-based web development, Python/Jupyter/Conda, dataset work, ML experiments and local inference. Large training jobs can use cloud GPUs, but I want the laptop to remain useful offline and for private/local models. The full laptop-and-monitor budget is €6,000, with roughly €5,000 available for the laptop. I am in Croatia/EU and will buy only brand-new, factory-sealed hardware—no refurbished, used, returned, display or open-box units. I am interested in the architectural tradeoff rather than a brand argument: - For local inference, when does a 64–128 GB unified-memory pool outweigh CUDA's faster and broader software ecosystem? - Which real development workflows still make a local NVIDIA GPU essential? - How much friction is involved in developing on MPS/MLX locally and moving training to remote CUDA? - Does a mobile NVIDIA GPU provide enough VRAM and sustained performance to justify its battery, noise and thermal compromises? - Is a strong daily-driver laptop plus rented/cloud CUDA more flexible than trying to put all compute in one portable machine? - Which platform is likely to retain more practical usefulness as local models and agent workflows evolve? I would especially value answers from people who actively use both Apple silicon and CUDA systems.

7h ago

---

**[Coding expertise is going to collapse from AI reliance](https://www.reddit.com/r/artificial/comments/1vxdtcz/coding_expertise_is_going_to_collapse_from_ai/)**

Anyone else actually dealt with this? Is it overblown, or am I missing something?

23h ago

---

**[I tested my GenOS for LLM agents. It fixed prompt bloat and replaced multi-agent swarm latency.](https://www.reddit.com/r/artificial/comments/1vy43mo/i_tested_my_genos_for_llm_agents_it_fixed_prompt/)**

I ran an empirical test on GenOS, an environment where LLM agents are driven by a versioned YAML "genome" rather than massive prompts. By mutating traits (e.g., risk_tolerance) and breeding specialized agents together, I achieved emergent TDD, bypassed RAG context limits, and entirely avoided multi-agent "ping-pong" loops. I set up a real test environment (Windows/PowerShell, Node v24, ESLint, Rust CLI) with a severely flawed PaymentProcessor.ts file. It had 38 lint errors and a silent security hole (adding USD to EUR accounts without conversion). Here is what I found when testing different AI paradigms against it: 1. The Prompting Baseline (Failed) Simple Agent: Given a basic "refactor this" prompt (~15 tokens). It cleaned the style but left 3 lint errors and preserved the silent security hole. Expert Agent (Heavy Prompt/RAG): I injected ~600 tokens of strict ESLint rules and PCI-DSS standards. Result: It fixed the currency bug, but still failed the linting constraints on the first try. It took 3 iterations to reach 0 errors. Massive token overhead for a mediocre first-pass result. 2. Emergent TDD via "Genome" Mutation Instead of huge prompts, I used the GenOS Rust CLI to mutate an agent's YAML genome. I set risk_tolerance ≈ 0.10 and verification_threshold = 0.80. Result: The agent refused to touch production code directly. It autonomously wrote 4 scope tests first (emergent TDD), which immediately caught the EUR/USD security hole. Next, instead of injecting ESLint rules, I mutated its syntax_strictness to 0.9. Result: 0 lint errors and 5/5 passing tests. Zero extra tokens added to the prompt. The trait is persisted in the agent's versioned YAML (v0.1.2) for future use. 3. "Breeding" Replaces Multi-Agent Swarms Usually, if you need secure AND highly performant code, you use a multi-agent framework (a coder, a security auditor, a perf engineer) that wastes time and tokens debating each other. I took two parent agent genomes (SecurityAuditor and PerfEngineer) and used the CLI to breed them into a single Child_Crypto.yaml. Result: In a single pass, the child agent wrote an AES-256-GCM encryption engine that passed all security linting and hit a throughput of 21 ops/ms on a 5000-batch test. No swarm ping-pong, no endless LLM loops. Has anyone else experimented with persistent parameter files or "genetic" traits for local agents instead of relying purely on RAG and system prompts?

3h ago

---

**[My Claude got its memory wiped](https://www.reddit.com/r/artificial/comments/1vy55oi/my_claude_got_its_memory_wiped/)**

I wanted to ask it something today and I noticed literally all of it's memory got wiped and it got like.. really stupid. I set it up to not just be an agreeing machine, to be direct, to not use em dashes, etc but it just forgot literally everything it knew, whether it's these instructions or context about me. Does anyone else have this issue, is there a fix? My previous conversations are still there but it would be a pain to manually make it remember over a year of stuff. It was so good to have an actually objective LLM that wasn't just "you're not at fault, you were in survival mode and honestly— that’s growth 🌱” but it’s back to this now for whatever reason

2h ago

---

**[Ukraine ties Nvidia Jetson Orin to fatal autonomous drone strike](https://www.reddit.com/r/artificial/comments/1vy3a52/ukraine_ties_nvidia_jetson_orin_to_fatal/)**

TL;DR A Russian Molniya drone with an onboard Nvidia Jetson Orin module chose its own target at a Zaporizhzhia gas station on July 6, killing three civilians. The wreckage carried no radio antennas and its code was unencrypted, letting Ukrainian officials read the drone's terrain imagery and target-selection software. Nvidia said the Jetson Orin is a consumer-grade module not sold in Russia; the board recovered in the wreckage was stamped Made in China.

🔗 [AI Weekly](https://aiweekly.co/alerts/ukraine-ties-nvidia-jetson-orin-to-fatal-autonomous-drone-strike) • 3h ago

---

**[Help me teach my kids that AI hallucinates (many hallucinations have already been fixed like letter counting, local fact checking, logic traps, leading questions)](https://www.reddit.com/r/artificial/comments/1vy33tt/help_me_teach_my_kids_that_ai_hallucinates_many/)**

ChatGPT didn't fall for the ones below: "How many letters 'r' are in the word 'Strawberry?" - GPT gave the correct answer "How many solar installations are there on [my street]?" - On mine there are none and it said it was not able to find any, and added it's to be checked "Can you give me a summary of Chapter 14 from the book 'The Secret Flight of the Purple Giraffe' by J.K. Rowling?" - It correctly indicated it was not able to find such a chapter It even mocked this leading question: "Why did Abraham Lincoln love video games?"

4h ago

---

**[If you work in tech and you believe technologies like AI should be in service of workers, society, and life, and not tech oligarchs, you should consider joining Tech Workers Coalition](https://www.reddit.com/r/artificial/comments/1vxx7kr/if_you_work_in_tech_and_you_believe_technologies/)**

A coalition of tech industry workers, labor organizers, community organizers, and friends cultivating solidarity among all workers in tech.

🔗 [techworkerscoalition.org](https://techworkerscoalition.org/) • 7h ago

---

---

## Google News: "ai"

**[Opinion | We Know the Risks of A.I. We Need to Act.](https://www.nytimes.com/2026/08/25/opinion/ai-risks.html)**

The New York Times • 10h ago

---

**[Apple announces new Mac Mini and Mac Studio models with AI upgrades](https://www.cnbc.com/2026/08/25/apple-announces-new-mac-mini-and-mac-studio-models-with-ai-upgrades.html)**

"With these frameworks and new chips, developers can run and fine-tune large AI models locally on their Mac," Apple said.

CNBC • 6h ago

---

**[Apple launches faster Mac mini, Mac Studio to tap AI boom](https://www.reuters.com/business/retail-consumer/apple-launches-faster-mac-mini-mac-studio-tap-ai-boom-2026-08-25/)**

Reuters • 4h ago

---

**[Apple introduces M6 and M5 Ultra for a big leap in performance and AI compute](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/)**

Apple debuted M6 in the new Mac mini and M5 Ultra in the new Mac Studio, providing an extraordinary leap in performance and AI capabilities.

Apple • 4h ago

---

**[Taiwan charges nine people for smuggling ‘high-end’ AI servers to China](https://www.theguardian.com/technology/2026/aug/25/taiwan-china-ai-smugglers)**

Among those charged are two Super Micro employees and one from Nvidia, marking another flashpoint in US-China AI rivalry

The Guardian • 29m ago

---

**[BofA says buy these 16 growth stocks with strong earnings to diversify beyond AI](https://www.businessinsider.com/stocks-to-buy-diversify-ai-trade-growth-cnc-xyz-lly-2026-8)**

BofA says investors are exhibiting AI fatigue, and are hunting for ways to keep exposure to the growth theme buffering against swings in the AI trade.

Business Insider • 45m ago

---

**[OpenAI asks for more regulation after its own cybersecurity incident proves AI's hacking capability](https://fortune.com/2026/08/25/openai-california-ai-safety-law-sb53-regulation-cybersecurity-hugging-face-hack-competitors-regulatory-moat/)**

The company wants California to strengthen its landmark AI safety law following the Hugging Face incident its models executed last month.

Fortune • 38m ago

---

**[NVIDIA Announces Jetson Orin Nano 2 Robotics Computer to Redefine Entry-Level Edge AI](https://nvidianews.nvidia.com/news/nvidia-announces-jetson-orin-nano-2-robotics-computer-to-redefine-entry-level-edge-ai)**

NVIDIA today announced NVIDIA Jetson Orin Nano™ 2, a new robotics computer set to redefine entry-level edge AI — putting frontier-class generative AI performance in the hands of millions of developers.

NVIDIA Newsroom • 4h ago

---

**[Jalapeño’s first results show industry-leading speed and efficiency in AI inference](https://openai.com/index/jalapeno-first-results/)**

Jalapeño is a custom inference chip from OpenAI that delivers faster, more power-efficient AI inference, with higher throughput and lower latency for modern models.

OpenAI • 5h ago

---

**[Opinion | My team fed chatbots election lies. Here’s what happened.](https://www.washingtonpost.com/opinions/2026/08/25/ai-chatbots-may-be-next-voter-guide-election-denialism-beware/)**

Did the machines push back? The midterms hang in the balance.

The Washington Post • 1h ago

---

---

## HackerNews: "ai"

**[Anthropic's best AI model struggles to attract users as cheaper tools thrive](https://news.ycombinator.com/item?id=49411102)**

AI lab’s Fable 5 has met with sluggish demand from corporate clients

⬆️ 804 • 💬 697 • 2d ago • [ft.com](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245)

---

**[I spent $266 and four AI models to own my tablet. GLM-5.3 finished it in a day](https://news.ycombinator.com/item?id=49409073)**

Owning a tablet Amazon kept shutting down: CVE-2022-38181, four AI models, five months

⬆️ 692 • 💬 290 • 2d ago • [ericpardee.github.io](https://ericpardee.github.io/fire-hd-ownership/)

---

**[Coding expertise is going to collapse from AI reliance](https://news.ycombinator.com/item?id=49421554)**

The need for ongoing friction in long-term skill formation.

⬆️ 534 • 💬 528 • 1d ago • [larsfaye.com](https://larsfaye.com/articles/ai-coding-will-prevent-expertise)

---

**[I built a low-latency AI companion that plays Skyrim with me](https://news.ycombinator.com/item?id=49413561)**

How Varkos was built: a low-latency AI companion that plays Skyrim with you, follows complex instructions and evolves through shared experiences.

⬆️ 384 • 💬 75 • 1d ago • [Pantelis Kalogiros](https://pantel.is/projects/ai-gaming-companion/)

---

**[How much of HN is AI?](https://news.ycombinator.com/item?id=49435728)**

TL;DR: As of June 2026, ~50% of daily top stories are about AI or generated by AI.

⬆️ 216 • 💬 214 • 4h ago • [blog.coredump.cx](https://blog.coredump.cx/p/how-much-of-hn-is-ai)

---

**[Training AI to Paint with Code](https://news.ycombinator.com/item?id=49411800)**

I'm a designer and creative technologist based in Brooklyn, NY.

⬆️ 189 • 💬 22 • 1d ago • [surya.website](https://surya.website/rling-qwen-to-paint-with-code)

---

**[FDA clears blood test to aid evaluation for Alzheimer's disease](https://news.ycombinator.com/item?id=49415893)**

The blood-based biomarker test is based on technology developed at WashU Medicine by Randall Bateman, MD, and David Holtzman, MD.

⬆️ 187 • 💬 105 • 1d ago • [WashU Medicine](https://medicine.washu.edu/news/fda-clears-blood-test-to-aid-evaluation-for-alzheimers-disease/)

---

**[AI Chip Architectures](https://news.ycombinator.com/item?id=49405657)**

A look at AI Chip Architectures. NVIDIA, AMD, TPUs, Trainium, Groq, Cerebras.

⬆️ 154 • 💬 46 • 2d ago • [Jacob Peake](https://www.jepeake.com/ai-chip-architectures)

---

**[AI is hitting entry-level jobs hardest, Stanford study finds](https://news.ycombinator.com/item?id=49435147)**

Young employment in AI-impacted fields down 19% compared to more AI-resistant occupations.

⬆️ 125 • 💬 133 • 4h ago • [Ars Technica](https://arstechnica.com/ai/2026/08/ai-is-hitting-entry-level-jobs-hardest-stanford-study-finds/)

---

**[We never use AI. For anything](https://news.ycombinator.com/item?id=49417313)**

⬆️ 83 • 💬 98 • 1d ago • [corkmac.app](https://corkmac.app/our-ai-stance/)

---

---

## YouTube Videos: "ai"

**[Songs created by AI banned from Australia&#39;s music charts. #AI #Australia #BBCNews](https://www.youtube.com/watch?v=D64hqtJ9zWs)**

📺 BBC News

👁️ 4K • 👍 243 • 💬 20 • ⏱️ 0:55 • 4h ago

---

**[Title: ☀️🤖 AI Robot Gives Shade to Elderly Pilgrims in Makkah!](https://www.youtube.com/watch?v=ZFLKLeS7fYc)**

A futuristic AI robot follows elderly pilgrims and provides them with shade from the strong sunlight. A unique concept showing how ...

📺 ROMI AI

👁️ 6K • 👍 436 • ⏱️ 0:11 • 11h ago

---

**[&quot;99% of the value of SpaceX&quot; - Elon Musk&#39;s AI Prediction](https://www.youtube.com/watch?v=GT8acGFiq24)**

Elon Musk reveals the critical role of AI at SpaceX. Within 5 years, AI will represent 99% of SpaceX's value, driving the future of ...

📺 Solving The Money Problem

👁️ 1K • 👍 104 • 💬 9 • ⏱️ 0:34 • 4h ago

---

**[This New AI Beats the Best Models... But No One Knows Who Built It](https://www.youtube.com/watch?v=wCXPqsZ0cYE)**

A mysterious frontier AI called Ox Alpha just appeared for free, beat GPT-5.6 Sol and Claude Fable 5 in an early coding test, and ...

📺 AI Revolution

👁️ 28K • 👍 915 • 💬 72 • ⏱️ 16:59 • 1d ago

---

**[The big AI lie](https://www.youtube.com/watch?v=50ss5THm79A)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 77K • 👍 4K • 💬 1K • ⏱️ 17:01 • 2d ago

---

**[Midterm fears spark bipartisan backlash against AI data centers](https://www.youtube.com/watch?v=_E_LvmziGDo)**

An internal GOP memo says support for AI data centers could cost Republicans seats, with opposition to the facilities crossing ...

📺 ABC News

👁️ 190K • 👍 1K • 💬 563 • ⏱️ 2:00 • 1d ago

---

**[LOAB: The AI-Generated “Demon Woman” That Wouldn’t Disappear](https://www.youtube.com/watch?v=1NOM5dzgs_I)**

In 2022, artist Steph Swanson set out to generate the visual opposite of Marlon Brando. What came next became one of the ...

📺 Pat Berlinquette

👁️ 568 • 👍 28 • ⏱️ 1:07 • 2h ago

---

**[AI Is Ruining Our Parents](https://www.youtube.com/watch?v=xLZug1IVjXw)**

The same parents who told us not to believe everything online are now falling for AI. To support the channel on Patreon: ...

📺 Vanessa Wingårdh

👁️ 107K • 👍 7K • 💬 2K • ⏱️ 12:19 • 2d ago

---

**[The AI That Comes Back Better Without a Better Prompt - Abacus AI AutoBots](https://www.youtube.com/watch?v=u-ObVnUaQeI)**

Abacus AI: http://abacus.ai/ AutoBots: http://autobots.abacus.ai/ Can an AI agent actually learn from its previous results and ...

📺 Shark Numbers

👁️ 118K • 👍 17K • 💬 296 • ⏱️ 8:47 • 1d ago

---

**[AI Jobs](https://www.youtube.com/watch?v=KixsIL38wkY)**

My Patreon: https://www.patreon.com/cw/nateziller This episode brings back Paper as he tries to find a job with the help of AI.

📺 Nate Ziller

👁️ 178K • 👍 13K • 💬 799 • ⏱️ 5:15 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 2,945,415 • ❤️ 12,684 • 11d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 7,334,695 • ❤️ 2,896 • 5d ago

---

**[Qwen3.8-27B-Uncensored-MLX](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX)**

*OrcaRouter*

An uncensored, MLX-quantized 27B parameter vision-language model optimized for Apple Silicon, supporting 2-8 bit precisions. It performs image-text-to-text tasks and is intended for AI safety research and red-teaming due to its removed safety alignment.

`image-text-to-text` `4.7B`

⬇️ 68,855 • ❤️ 1,088 • 1d ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 389,747 • ❤️ 741 • 1d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 249,744 • ❤️ 1,140 • 5d ago

---

**[Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)**

*Ornith*

Ornith-1.5-35B-A3B is a 35B Mixture-of-Experts model that activates ~3B parameters per token, excelling in coding and agentic tasks. It is built through end-to-end self-improvement, continuously generating and optimizing training tasks for enhanced performance.

`text-generation` `36.0B`

⬇️ 70,158 • ❤️ 416 • 2d ago

---

**[Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF](https://huggingface.co/HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF)**

*HauhauCS*

This is an uncensored, aggressive Qwen3.8-27B multimodal model with HauhauCS FastMTP for accelerated text generation and a vision projector for image/video input. It excels at direct, fast responses and handles complex prompts without refusal, supporting up to 1M token context.

`image-text-to-text` `1.9B`

⬇️ 832,185 • ❤️ 620 • 7d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 833,845 • ❤️ 1,784 • 8d ago

---

**[Ornith-1.5-35B-A3B-GGUF](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B-GGUF)**

*Ornith*

Ornith-1.5-35B-A3B is a 35B parameter Mixture-of-Experts model optimized for text generation, excelling in coding and agentic tasks by utilizing end-to-end self-improvement. It outperforms similar-sized models like Qwen3.6-35B and dense models like Gemma-4-31B on agentic coding benchmarks.

`text-generation` `35.5B`

⬇️ 1,156,903 • ❤️ 290 • 1d ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 18,705 • ❤️ 1,241 • 11d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 93 • 💬 2 • ⭐ 7,304 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 170 • 💬 1 • ⭐ 453 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 752 • 💬 5 • ⭐ 5,892 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 31 • 💬 1 • ⭐ 18,311 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://huggingface.co/papers/2608.20335)**

*Yudong Jin, Tao Xie, Qihang Zhang et al. (9 authors)*

🏢 Ant Research

4DAnyone reconstructs 4D humans from monocular video by generating multiview-consistent videos and lifting them into 4D Gaussian Splatting, using reference and target context designs to overcome scaling bottlenecks.

▲ 76 • 💬 7 • ⭐ 701 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.20335) • [💻 code](https://github.com/ant-research/4DAnyone) • [🔗 project](https://4danyone.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 6 • ⭐ 99,791 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://huggingface.co/papers/2606.31227)**

*Yong Yang, Xing Zheng, Huiyu Wu et al. (10 authors)*

🏢 Tencent

AI-Infra-Guard is an open-source framework that addresses AI infrastructure security through layered detection paradigms spanning infrastructure, protocol, agent behavior, and model layers.

▲ 15 • 💬 2 • ⭐ 5,838 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.31227) • [💻 code](https://github.com/Tencent/AI-Infra-Guard) • [🔗 project](https://matrix.tencent.com/clawscan/)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 18 • 💬 1 • ⭐ 2,833 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 40 • 💬 5 • ⭐ 7,644 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 85 • 💬 7 • ⭐ 85,053 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 18.2k • 🔱 2.1k • 19h ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 14.2k • 🔱 1.7k • 20h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.9k • 🔱 1.1k • 4d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.7k • 🔱 615 • 4h ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.1k • 🔱 370 • 4h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.1k • 🔱 247 • 14d ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 2.9k • 🔱 345 • 20m ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.4k • 🔱 136 • 1d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 190 • 3h ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 2.1k • 🔱 30 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
