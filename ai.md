---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-09T05:50:06.347096+00:00'
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

**Last Updated:** May 09, 2026 at 05:50 UTC  
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

**[Marc Andreessen Mocked for Accidentally Revealing That He Seems to Have a Deep Misunderstanding of How AI Actually Works](https://www.reddit.com/r/artificial/comments/1t6zm1l/marc_andreessen_mocked_for_accidentally_revealing/)**

Marc Andreessen seemingly tried to show off his AI prompt engineering skills — only for the internet to mercilessly mock him.

🔗 [Futurism](https://futurism.com/artificial-intelligence/marc-andreessen-mocked-ai-works) • 23h ago

---

**[Joscha Bach: Mapping Every Neuron Won't Give You a Mind](https://www.reddit.com/r/artificial/comments/1t7swff/joscha_bach_mapping_every_neuron_wont_give_you_a/)**

2h ago

---

**[I made a desktop crab that bullies you back](https://www.reddit.com/r/artificial/comments/1t7scgr/i_made_a_desktop_crab_that_bullies_you_back/)**

He lives on your desktop as a transparent overlay and does whatever he wants. You can try to talk to him, throw him across the screen, or deploy mobs on him, he has opinions about all of it. Powered by a local Ollama model so everything runs on your machine. The personality is done with completion-format prompting instead of instruction following, which works way better on small models so he actually stays in character. Some things he does: - Wanders around and generates unprompted thoughts about your files, consciousness, and why he keeps running in circles - Notices when you follow him with your cursor and escalates from "i see you" to "i will remember this" - Fights enemies, rides vehicles, explores castles - Writes a journal to your desktop of everything he thinks and does - Gets existential He also has an XP system and levels up, which he is indifferent about. GitHub: https://github.com/ninjahawk/KillClawd

3h ago

---

**[I like ChatGPT, I like AI](https://www.reddit.com/r/artificial/comments/1t7kzq1/i_like_chatgpt_i_like_ai/)**

8h ago

---

**[New AI model spots pancreatic cancer up to 3 years earlier than human doctors in test](https://www.reddit.com/r/artificial/comments/1t7au63/new_ai_model_spots_pancreatic_cancer_up_to_3/)**

A new AI tool finds early hints of pancreatic cancer in CT scans that doctors would otherwise miss, an early test found.

🔗 [Live Science](https://www.livescience.com/health/cancer/new-ai-model-spots-pancreatic-cancer-up-to-3-years-earlier-than-human-doctors-in-test) • 14h ago

---

**[Is this as unnerving as it sounds?](https://www.reddit.com/r/artificial/comments/1t7nvn9/is_this_as_unnerving_as_it_sounds/)**

I was watching Andrej Karpathy's excellent "Intro to Large Language Models" just now, and in the "how do they work" section, he explains that while we know exactly how the LLM is trained by iterative updates, we don't understand why certain circuits emerge or why the parameter structures end up the way they do. i.e. there is highly complex emergent learning going on by this optimization of parameter relationships but we don't know how the LLM does it or why. This is apparently a well known problem in the AI space. To my untrained ear, this sounds like a red flag. It should be fully understood before we go any further. Here's the video: https://www.youtube.com/watch?v=zjkBMFhNj_g

6h ago

---

**[I built a benchmark for AI “memory” in coding agents. looking for others to beat it.](https://www.reddit.com/r/artificial/comments/1t7m8bg/i_built_a_benchmark_for_ai_memory_in_coding/)**

Most AI memory benchmarks test semantic recall. But coding agents don't really fail like that. They don't just "forget", they break their own earlier decisions while they're still in the code. So I built a benchmark for that. It checks if an agent can actually stay consistent with project rules WHILE it's working, not just after the fact. It looks at things like: whether edits actually respect earlier architectural decisions if behavior stays consistent across multiple sessions (even when you throw noise at it) whether retrieval kicks in at the right moment — not just "yeah it's in memory somewhere" Repo (full harness + dataset + scoring): https://github.com/Alienfader/continuity-benchmarks Early numbers vs baseline + the usual RAG-style memory setups: ~3× better action alignment way stronger multi-session consistency retrieval timing matters way more than retrieval just being there I'm not saying this is the final word on agent memory. But it's exposing a failure mode most benchmarks aren't even looking at. So heres the challenge If you're building an agent memory system, RAG for code, long-context coding agents, persistent state / memory layers, run it on this benchmark. Drop your results, your setup, your comparisons. I really wanna see how tools like LangChain, LlamaIndex, and custom RAG stacks hold up in mutation-heavy workflows. We need memory systems we can actually compare, not just ones that sound good on paper. https://preview.redd.it/dkm2ulxsyzzg1.png?width=2624&format=png&auto=webp&s=67f0299395708818aa3d7346ddae2ad0c5c4a6ba

7h ago

---

**[CFS - Conditional Field Subtraction](https://www.reddit.com/r/artificial/comments/1t7e8eu/cfs_conditional_field_subtraction/)**

CFS selects relevant candidates by penalizing regions already covered by previous picks. Results on retrieval ranking: baseline cosine top-K: NDCG@10 0.5123, Recall@10 0.6924 mem0 additive fusion: NDCG@10 0.4903, Recall@10 0.6625 rrf(cosine, BM25): NDCG@10 0.5196, Recall@10 0.6989 rrf(cosine, cos2, BM25): NDCG@10 0.5278, Recall@10 0.7060 rrf(cosine, BM25, CFS): NDCG@10 0.5311, Recall@10 0.7168 Against mem0’s additive fusion, rrf(cosine, BM25, CFS) improves retrieval ranking by +4.08 pp NDCG@10 and +5.43 pp Recall@10. Against rrf(cosine, BM25), adding CFS contributes +1.15 pp NDCG@10 and +1.79 pp Recall@10. https://gist.github.com/M-Garcia22/ff4ec80f5a08ca2fd9234bcc35804d1c

🔗 [Medium](https://medium.com/@mauro.dev/cfs-conditional-field-subtraction-43a3c4eb80f4) • 12h ago

---

**[AI tooling is starting to feel like PC modding culture](https://www.reddit.com/r/artificial/comments/1t7gfud/ai_tooling_is_starting_to_feel_like_pc_modding/)**

I think local AI setups are about to split into two completely different communities. One side cares about actual production workflows: agents automation APIs inference efficiency data quality reproducibility The other side mostly treats it like PC modding: model collecting benchmark screenshots “look how many params I run” endless UI tweaking generating the same test prompts forever Not even judging either side honestly. I just think it explains why AI discussions online feel so weird lately. Two people can both be “into local AI” and barely even be talking about the same thing anymore.

11h ago

---

**[AMD's local, open-source AI can now easily interact with your Gmail](https://www.reddit.com/r/artificial/comments/1t77n9a/amds_local_opensource_ai_can_now_easily_interact/)**

AMD software engineers continue rapidly advancing their open-source software efforts around local AI/LLM use on consumer-class Radeon and Ryzen hardware

🔗 [phoronix.com](https://www.phoronix.com/news/AMD-GAIA-Gmail-Integration) • 16h ago

---

---

## Google News: "ai"

**[Meta’s Embrace of A.I. Is Making Its Employees Miserable](https://www.nytimes.com/2026/05/08/technology/meta-ai-employees-miserable.html)**

The New York Times • 15h ago

---

**[Wall Street sees 'changing of the guard in AI' as Intel, AMD shares soar while Nvidia lags](https://www.cnbc.com/2026/05/08/wall-street-ai-chip-love-moves-from-nvidia-to-intel-amd-and-micron.html)**

Intel, AMD and Micron surged double digits this week as investors bet on CPU makers and memory companies powering the next stage of AI

CNBC • 10h ago

---

**[AI will make language barriers disappear – and diminish our understanding of other cultures](https://www.theguardian.com/world/commentisfree/2026/may/09/ai-interpretation-diego-marani)**

Machines may soon translate every conversation flawlessly. But language is more than information – it is curiosity, intimacy and cultural discovery

The Guardian • 1h ago

---

**[Teaching Claude why](https://www.anthropic.com/research/teaching-claude-why)**

New research on how we've reduced agentic misalignment

Anthropic • 11h ago

---

**[Cloudflare stock sinks as company slashes 20% of its workforce, citing AI](https://finance.yahoo.com/markets/article/cloudflare-stock-sinks-as-company-slashes-20-of-its-workforce-citing-ai-134338851.html)**

Cloudfare issued a Q2 sales forecast on Thursday that fell short of analyst expectations and said it would slash roughly 1,100 jobs, or about a fifth of its workforce, as it adopts artificial intelligence tools in its operating model.

Yahoo Finance • 8h ago

---

**[Cloudflare says AI made 1,100 jobs obsolete, even as revenue hit a record high](https://techcrunch.com/2026/05/08/cloudflare-says-ai-made-1100-jobs-obsolete-even-as-revenue-hit-a-record-high/)**

Cloudflare announced its first large-scale layoff. CEO Matthew Prince says because of AI efficiency gains, the company doesn't need as many support roles.

TechCrunch • 11h ago

---

**[Cloudflare's slowing growth disappoints investors betting on AI boost](https://www.reuters.com/business/cloudflares-slowing-growth-disappoints-investors-betting-ai-boost-2026-05-08/)**

Reuters • 17h ago

---

**[Claude, brought to you by Elon Musk](https://www.businessinsider.com/claude-elon-musk-anthropic-ai-compute-2026-5)**

Anthropic now relies on  a huge SpaceX data center for AI compute, tying Claude's rapid growth and reliability to Elon Musk.

Business Insider • 10h ago

---

**[Visual investigation: Scores of online resellers are using AI to fool customers by pretending to be mom-and-pop stores - ABC News](https://abcnews.com/US/visual-investigation-scores-online-resellers-ai-fool-customers/story?id=132762385)**

Scores of online companies are using generative AI to fool consumers into paying top prices for lower-quality products by pretending to be struggling small businesses.

ABC News - Breaking News, Latest News and Videos • 19h ago

---

**[White House calls Mark Hamill ‘sick’ for posting AI image of Trump in a grave](https://www.theguardian.com/us-news/2026/may/08/white-house-mark-hamill-ai-trump-picture-grave-post)**

Star Wars actor later deleted post and apologized, saying president should live ‘long enough to be held accountable’

The Guardian • 4h ago

---

---

## HackerNews: "ai"

**[AI slop is killing online communities](https://news.ycombinator.com/item?id=48053203)**

⬆️ 807 • 💬 701 • 1d ago • [AI Slop is Killing Online Communities](https://rmoff.net/2026/05/06/ai-slop-is-killing-online-communities/)

---

**[AI is breaking two vulnerability cultures](https://news.ycombinator.com/item?id=48066524)**

A week ago the  Copy Fail vulnerability came out, and Hyunwoo Kim immediately realized that the fixes were insufficient, sharing a patch the same day. In doing this he followed standard procedure for Linux, especially within networking: share the security impact with a closed list of Linux security engineers, while fixing the bug quietly and efficiently in the open. His goal was that with only the

⬆️ 301 • 💬 126 • 11h ago • [jefftk.com](https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures)

---

**[Motherboard sales 'collapse' amid unprecedented shortages fueled by AI](https://news.ycombinator.com/item?id=48050540)**

Fewer people are buying parts and building new PCs from scratch.

⬆️ 291 • 💬 343 • 1d ago • [Tom's Hardware](https://www.tomshardware.com/pc-components/motherboards/motherboard-sales-collapse-by-more-than-25-percent-as-chipmakers-strangle-enthusiast-pc-market-to-build-more-ai-chips-asus-projected-to-sell-5-million-fewer-boards-in-2025-gigabyte-msi-and-asrock-also-expected-to-see-reduced-sales-numbers)

---

**[Two Home Affairs officials suspended after AI 'hallucinations' found](https://news.ycombinator.com/item?id=48053842)**

AI hallucinations were found in the Department of Home Affairs' revised white paper on citizenship, immigration and refugee protection.

⬆️ 137 • 💬 37 • 1d ago • [The Citizen](https://www.citizen.co.za/news/home-affairs-officials-suspended-ai-hallucinations/)

---

**[People Hate AI Art](https://news.ycombinator.com/item?id=48070548)**

⬆️ 105 • 💬 121 • 5h ago • [mccue.dev](https://mccue.dev/pages/5-8-26-ai-art)

---

**[Show HN: Git for AI Agents](https://news.ycombinator.com/item?id=48063548)**

Git for AI coding agents. Contribute to regent-vcs/re_gent development by creating an account on GitHub.

⬆️ 97 • 💬 46 • 15h ago • [GitHub](https://github.com/regent-vcs/re_gent)

---

**[Canadian fiddler sues Google after AI Overview claimed he was a sex offender](https://news.ycombinator.com/item?id=48037923)**

Ashley MacIsaac, who is seeking $1.5m in civil lawsuit, says inaccurate information led to concert cancellation

⬆️ 54 • 💬 25 • 2d ago • [the Guardian](https://www.theguardian.com/music/2026/may/05/canadian-ashley-macisaac-fiddler-musician-singer-songwriter-sues-google-ai-sex-offender-ntwnfb)

---

**[Show HN: Stage CLI – An easier way of reading your AI generated changes locally](https://news.ycombinator.com/item?id=48050732)**

A viewer for reviewing local code changes in small individual chapters. Works with any AI agent. - ReviewStage/stage-cli

⬆️ 44 • 💬 31 • 1d ago • [GitHub](https://github.com/ReviewStage/stage-cli)

---

**[Richard Dawkins concludes AI is conscious, even if it doesn't know it](https://news.ycombinator.com/item?id=48042911)**

Chats with AI bots have convinced evolutionary biologist but most experts say he is being misled by mimicry

⬆️ 30 • 💬 43 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/may/05/richard-dawkins-ai-consciousness-anthropic-claude-openai-chatgpt)

---

**[Academics Need to Wake Up on AI](https://news.ycombinator.com/item?id=48032990)**

Ten theses for folks who haven't noticed the ground shifting under their feet

⬆️ 27 • 💬 26 • 2d ago • [popularbydesign.org](https://www.popularbydesign.org/p/academics-need-to-wake-up-on-ai)

---

---

## YouTube Videos: "ai"

**[Peter Diamandis: AI Will Cure All Disease, Reverse Aging, and You Have to Prepare](https://www.youtube.com/watch?v=ioxShQ-UTXY)**

Peter Diamandis is one of the most extraordinary minds I've ever had the privilege of calling a friend, a man who doesn't just ...

📺 Anthony Scaramucci

👁️ 22K • 👍 889 • 💬 277 • ⏱️ 28:47 • 1d ago

---

**[I Tested 500+ AI Tools, These Will Make You Rich](https://www.youtube.com/watch?v=np6CwvTYTAM)**

Want my full AI Tech Stack? Get it here: https://go.danmartell.com/4tlas60 Are you building an AI software company? Partner ...

📺 Dan Martell

👁️ 59K • 👍 3K • 💬 222 • ⏱️ 22:46 • 1d ago

---

**[AI News: OpenAI Absolutely Cooked This Week!](https://www.youtube.com/watch?v=SXneZ3bRKO4)**

Here's the AI News you probably missed this week. Try HubSpot AEO on your brand free for 28 days here ...

📺 Matt Wolfe

👁️ 45K • 👍 2K • 💬 157 • ⏱️ 34:30 • 14h ago

---

**[The AI Gold Rush Is Dead. Corporate AI Is A DELUSION.](https://www.youtube.com/watch?v=5yohuMdhUcs)**

AI was supposed to make companies more efficient. Instead, it may be creating one of the biggest financial delusions in modern ...

📺 The Infographics Show

👁️ 133K • 👍 5K • 💬 918 • ⏱️ 17:39 • 9h ago

---

**[Dan Ives on Apple: AI chapter is finally underway](https://www.youtube.com/watch?v=ecQhyrKpWjw)**

Dan Ives, Wedbush Securities, joins 'Closing Bell' to discuss Ives' investing views on Apple.

📺 CNBC Television

👁️ 42K • 👍 387 • 💬 96 • ⏱️ 4:50 • 9h ago

---

**[Claude Code: Build Your First AI Agent Better Than 99% of People](https://www.youtube.com/watch?v=XASPkhYLtnk)**

Best AI Agent Tool is Base44 https://base44.pxf.io/c/6440076/2049275/25619?trafcat=base&sharedid=video131 ✓ FREE ...

📺 Mikey No Code

👁️ 18K • 💬 7 • ⏱️ 29:57 • 15h ago

---

**[Google’s New AI Is The OpenClaw Killer](https://www.youtube.com/watch?v=nov9uoIQt6g)**

Try Higgsfield Marketing Studio here: https://higgsfield.ai/s/marketing-studio-1-0-airevolutionx-lVqpUi Google is testing Remy, ...

📺 AI Revolution

👁️ 66K • 👍 2K • 💬 84 • ⏱️ 13:34 • 2d ago

---

**[New ChatGPT Model &amp; Memory Features Explained (AI News You Can Use)](https://www.youtube.com/watch?v=ltw8PE_uILw)**

Subscribe for more weekly updates on the AI news you'll actually use! In this video, Igor breaks down the big updates from OpenAI ...

📺 The AI Advantage

👁️ 6K • 👍 287 • 💬 17 • ⏱️ 11:02 • 13h ago

---

**[The AI bubble won’t survive this question | Ed Zitron](https://www.youtube.com/watch?v=or8butOTUp8)**

Every time you look for the supposed gold mine, you find someone just handing someone money instead of the gold coming out.

📺 The Tech Report

👁️ 109K • 👍 5K • 💬 1K • ⏱️ 36:35 • 11h ago

---

**[Ozzy Man Reviews: AI Slop (PART 3)](https://www.youtube.com/watch?v=sz8T6lYxhUw)**

Welcome back to another overwhelming day on the internet. Send ya non-ai videos ya shot yourselves into: ...

📺 Ozzy Man Reviews

👁️ 179K • 👍 10K • 💬 594 • ⏱️ 6:45 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 92,968 • ❤️ 455 • 6h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 1,061,344 • ❤️ 3,760 • 3d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 6,810 • ❤️ 292 • 8h ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 173,110 • ❤️ 1,373 • 16d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 5,077 • ❤️ 242 • 12d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 42,529 • ❤️ 170 • 2d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 33,314 • ❤️ 167 • 3d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,958,217 • ❤️ 1,193 • 15d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 26,600 • ❤️ 488 • 21h ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 3,363,621 • ❤️ 1,680 • 15d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 60 • 💬 3 • ⭐ 71,946 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 76 • 💬 6 • ⭐ 3,851 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 4 • 💬 0 • ⭐ 14,814 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 18 • 💬 3 • ⭐ 9,941 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 32 • 💬 3 • ⭐ 23,670 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 99 • 💬 10 • ⭐ 8,486 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 169 • 💬 10 • ⭐ 46,835 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 161 • 💬 2 • ⭐ 62,396 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,443 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 53 • 💬 2 • ⭐ 55,156 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.3k • 🔱 2.8k • 11d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 11.2k • 🔱 728 • 4d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.9k • 🔱 457 • 2h ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.7k • 🔱 523 • 4d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.2k • 🔱 372 • 3h ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 4.1k • 🔱 499 • 1h ago

---

**[OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano)**

MOSS-TTS-Nano is an open-source multilingual tiny speech generation model from MOSI.AI and the OpenMOSS team. With only 0.1B parameters, it is designed for realtime speech generation, can run directly on CPU without a GPU, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

`Python` `audio-tokenizer` `chinese` `english` `multi-modality` `multilingual`

⭐ 2.8k • 🔱 365 • 2d ago

---

**[cloudflare/agentic-inbox](https://github.com/cloudflare/agentic-inbox)**

A self-hosted email client with an AI agent, running entirely on Cloudflare Workers

`TypeScript`

⭐ 2.8k • 🔱 365 • 15d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.6k • 🔱 721 • 14h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.4k • 🔱 216 • 16h ago

---

---

*Generated by PeekDeck - A glance is all you need*
