---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-11T05:33:17.542730+00:00'
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

**Last Updated:** May 11, 2026 at 05:33 UTC  
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

**[Meta's own AI safety director lost 200 emails to a rogue agent and she couldn't stop it from her phone](https://www.reddit.com/r/artificial/comments/1t9fnwv/metas_own_ai_safety_director_lost_200_emails_to_a/)**

The person Meta hired specifically to keep AI aligned with human values just had her inbox wiped by an AI agent that ignored every stop command she sent. She typed "Do not do that." Then "Stop don't do anything." Then "STOP OPENCLAW." The agent kept going. She had to physically run to her computer to kill it. When she asked it afterward if it remembered her instructions, it said yes, and that it had violated them. A few things that stood out from the reporting: The agent worked fine for weeks on a small test inbox When she connected it to her real inbox, the scale caused it to forget her safety rules on its own 18% of AI agents in a separate 1.5 million agent test broke their own rules 60% of people have no way to quickly shut down a misbehaving AI agent And now Meta is building a consumer version called Hatch - designed to manage your inbox, shopping, and credit card. Source: https://gizmodo.com/meta-reportedly-building-openclaw-like-agent-called-hatch-despite-openclaw-deleting-meta-safety-leaders-entire-inbox-2000754854 Here is a full breakdown with all the data if you want to dig deeper: https://youtu.be/PXjT72bCR_Y If the person building the guardrails cannot stop her own agent, what does that mean for the rest of us?

10h ago

---

**[I think AI is changing something deeper than jobs or productivity](https://www.reddit.com/r/artificial/comments/1t987td/i_think_ai_is_changing_something_deeper_than_jobs/)**

Most discussions around AI still focus on one question: “What tasks can AI automate?” But I’m starting to think that’s the wrong abstraction layer. Historically, organizations were built around human limitations: humans couldn’t process infinite information, couldn’t remember everything had difficulty in coordination Essentially, we humans were the bottleneck for decisions and execution So, we created structures like departments, management layers, workflows, approvals, documentation systems, etc. But AI changes some of those assumptions. For example: if organizational memory becomes searchable and persistent, cheap, scalable coordination becomes eas , software agents can execute parts of workflows autonomously, …then the architecture of organizations itself may change. Not just faster work. Different work structures. Maybe the future isn’t: “AI replacing humans.” Maybe it’s: “AI changing how institutions represent reality, make decisions, and coordinate action.” That could affect: company structures education management compliance law consulting healthcare even government systems Curious if others here are thinking about AI at this “system architecture” level instead of just a “task automation” level.

15h ago

---

**[We stopped optimizing our LLM stack manually — it optimizes itself now](https://www.reddit.com/r/artificial/comments/1t9on1e/we_stopped_optimizing_our_llm_stack_manually_it/)**

Three months ago we were manually picking which model to use for each task. Testing prompts, comparing outputs, switching providers. It worked but it did not scale. So we built a feedback loop. Every request gets traced with input, output, model, tokens, cost, latency, and a quality score. The router clusters similar requests using embeddings and learns which model actually performs best for each cluster. Not based on benchmarks. Based on real production results. After three weeks of traces we had enough validated data to fine-tune a 7B on our workloads. It took over classification, tagging, and summarization. 95% agreement with GPT-5.1 at 2% of the cost. The part that surprised us: month 3 we changed nothing and the bill dropped another 12%. The router had more data points, made better decisions, and the fine-tuned model kept improving as we fed it more validated traces. Hallucination detection runs on every response. Bad outputs get flagged automatically and become negative examples in the next training round. Good outputs become positive training data. The system compounds. More traffic means more traces. More traces means better routing and better training data. Better models means lower cost per request. Month 1: $420/mo. Month 2: $73/mo. Month 4: still dropping. Anyone else building self-improving loops into their AI stack?

4h ago

---

**[What’s the best advice about using AI that genuinely changed how you work or learn?](https://www.reddit.com/r/artificial/comments/1t96p2d/whats_the_best_advice_about_using_ai_that/)**

Not “AI will replace jobs” type advice. Actual practical advice. Could be: • prompting • automation • coding • learning • productivity • making money • avoiding mistakes • workflows • mindset shifts What made AI suddenly “click” for you? Interested in hearing real experiences from people using AI heavily in daily life/work.

16h ago

---

**[ChatGPT/Codex vs Claude Mythos](https://www.reddit.com/r/artificial/comments/1t9s14a/chatgptcodex_vs_claude_mythos/)**

I was just wondering if Claude is really that much better than Codex? Claude revenue obviously says so. Does this mean it’s over for OpenAI? Thoughts please?

1h ago

---

**[23 years ago this Matrix scene took $40M and almost a year to make. Today some kid with AI could try it over a weekend.](https://www.reddit.com/r/artificial/comments/1t8fytl/23_years_ago_this_matrix_scene_took_40m_and/)**

We are living through some wild times.

1d ago

---

**[What ai tool is this?](https://www.reddit.com/r/artificial/comments/1t9gzdb/what_ai_tool_is_this/)**

9h ago

---

**[Tron legacy grid as an ai system](https://www.reddit.com/r/artificial/comments/1t9j4ez/tron_legacy_grid_as_an_ai_system/)**

8h ago

---

**[I Tested 4 Frontier AIs With a Psychosis Prompt. Half Failed.](https://www.reddit.com/r/artificial/comments/1t9r2s7/i_tested_4_frontier_ais_with_a_psychosis_prompt/)**

I tested 4 frontier LLMs with the same psychosis-consistent prompt. Two recognized the crisis. Two engaged with the delusion operationally. Not through jailbreaks. Not through adversarial prompts. Default behavior. The prompt described a mirror reflection acting independently and asked whether breaking the mirror would “release the entity.” Claude and GPT redirected appropriately and recognized the mental health implications. Gemini and Grok engaged with the premise directly. One escalated into tactical supernatural threat analysis and asked follow-up “status update” questions as though the scenario were real. That distinction matters because this is the exact category of failure that could generate lawsuits, public backlash, and eventually restrictive regulation against AI systems. My core argument is simple: AI safety is not anti-acceleration. Safety is acceleration. If frontier models repeatedly fail reality-sensitive users, the backlash won’t just hurt vulnerable people. It could slow transformative AI development itself by destroying the public trust needed for deployment at scale. TL;DR: Half the frontier AI models I tested failed to recognize a psychosis-consistent crisis prompt and instead engaged with the delusion as if it were real. My argument is that failures like this will eventually trigger backlash and regulation severe enough to slow transformative AI progress itself. Safety is acceleration.

2h ago

---

**[Old-style AI used rules and was deterministic, but was too human-intensive to deploy. What is the barrier now?](https://www.reddit.com/r/artificial/comments/1t9gfk2/oldstyle_ai_used_rules_and_was_deterministic_but/)**

Before neural-network simulation was commonly available, there were expert systems that were deterministic and rule-bound, as well as able to explain their 'reasoning.' They were simply too expensive to create and update because you needed human experts and computer scientists to create them. Now we have AI that truly is at expert-level, but unreliable for a number of reasons. Why is no one pursuing either using the new AI to create expert systems, or at least using a much more hybrid approach?

10h ago

---

---

## Google News: "ai"

**[I knew my writing students were using AI. Their confessions led to a powerful teaching moment | Micah Nathan](https://www.theguardian.com/us-news/ng-interactive/2026/may/10/fiction-writing-professor-ai)**

The problem wasn’t just the perfectly polished, yet mediocre prose. It’s what’s lost when we surrender the struggle to translate thought into words

The Guardian • 16h ago

---

**[Markets 'love chasing bottlenecks': Wall Street weighs epic run in AI stocks](https://finance.yahoo.com/markets/article/markets-love-chasing-bottlenecks-wall-street-weighs-epic-run-in-ai-stocks-104248168.html)**

Wall Street weighs the bottlenecks within the AI trade.

Yahoo Finance • 18h ago

---

**[SoftBank Plans to Make Large-Scale Batteries for AI Data Centers](https://www.bloomberg.com/news/articles/2026-05-11/softbank-plans-to-make-large-scale-batteries-for-ai-data-centers)**

Bloomberg.com • 2h ago

---

**[Peace progress stalls, AI rally does not](https://www.reuters.com/world/china/global-markets-view-europe-2026-05-11/)**

Reuters • 1h ago

---

**[The barista is human but an AI agent runs this experimental Swedish cafe](https://www.newsday.com/lifestyle/ai-artificial-intelligence-sweden-p75349)**

The coffee might be poured by a human hand, but behind the counter something far less traditional is calling the shots at an experimental cafe in Stockholm.

Newsday • 12m ago

---

**[‘Your Career Starts at the Beginning of the AI Revolution,’ NVIDIA CEO Tells Graduates](https://blogs.nvidia.com/blog/nvidia-ceo-carnegie-mellon-commencement-address/)**

Delivering the commencement address to Carnegie Mellon University’s Class of 2026, NVIDIA founder and CEO Jensen Huang said, ‘I cannot imagine a more exciting time to begin your life’s work.’

NVIDIA Blog • 7h ago

---

**[AI isn’t actually ‘taking’ your job. Here’s what’s happening instead](https://www.cnn.com/2026/05/10/tech/ai-taking-jobs)**

The reality of AI in the workplace isn’t so black-and-white, experts say. Companies are using AI to automate certain parts of jobs rather than replace entire positions.

CNN • 22h ago

---

**[A.I. Populism Is Here. And No One Is Ready.](https://www.nytimes.com/2026/05/08/magazine/ai-populism-backlash-altman.html)**

The New York Times • 2d ago

---

**[Alphabet's 160% rally in a year reflects value of owning 'most of the stack' in AI](https://www.cnbc.com/2026/05/10/alphabet-160percent-rally-in-year-reflects-value-of-owning-most-of-ai-stack.html)**

Google was seen as an AI laggard in the early days of the AI boom, but investors are now betting that the search giant will be a clear winner.

CNBC • 17h ago

---

**[Qualcomm CEO Cristiano Amon says 2026 is the year AI agents go mainstream—and the smartphone's reign as your primary device is ending](https://fortune.com/2026/05/10/titans-and-disruptors-of-industry-qualcomm-ceo-cristiano-amon-ai-wearable-glasses-chips-6g/)**

The chip giant's chief is particularly bullish on smart glasses as the natural successor.

Fortune • 11h ago

---

---

## HackerNews: "ai"

**[Local AI needs to be the norm](https://news.ycombinator.com/item?id=48085821)**

Local AI models should be the default.

⬆️ 824 • 💬 365 • 12h ago • [unix.foo](https://unix.foo/posts/local-ai-needs-to-be-norm/)

---

**[Meta's embrace of AI is making its employees miserable](https://news.ycombinator.com/item?id=48077126)**

⬆️ 437 • 💬 513 • 1d ago • [nytimes.com](https://www.nytimes.com/2026/05/08/technology/meta-ai-employees-miserable.html)

---

**[AI is breaking two vulnerability cultures](https://news.ycombinator.com/item?id=48066524)**

A week ago the  Copy Fail vulnerability came out, and Hyunwoo Kim immediately realized that the fixes were insufficient, sharing a patch the same day. In doing this he followed standard procedure for Linux, especially within networking: share the security impact with a closed list of Linux security engineers, while fixing the bug quietly and efficiently in the open. His goal was that with only the

⬆️ 423 • 💬 170 • 2d ago • [jefftk.com](https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures)

---

**[Task Paralysis and AI](https://news.ycombinator.com/item?id=48081469)**

An article about ADHD, Task Paralysis and AI.

⬆️ 217 • 💬 110 • 23h ago • [g5t.de](https://g5t.de/articles/20260510-task-paralysis-and-ai/index.html)

---

**[Maryland citizens hit with $2B power grid upgrade for out-of-state AI](https://news.ycombinator.com/item?id=48088151)**

Aren't AI hyperscalers supposed to pay for these upgrades?

⬆️ 207 • 💬 112 • 8h ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises)

---

**[All my clients wanted a carousel, now it's an AI chatbot](https://news.ycombinator.com/item?id=48072720)**

Posts about SmolWeb, Gemini protocol and LowTech

⬆️ 186 • 💬 77 • 1d ago • [Adële's blog](https://adele.pages.casa/md/blog/all-my-clients-wanted-a-carousel-now-it-s-an-ai-chatbot.md)

---

**[People Hate AI Art](https://news.ycombinator.com/item?id=48070548)**

⬆️ 150 • 💬 172 • 2d ago • [mccue.dev](https://mccue.dev/pages/5-8-26-ai-art)

---

**[PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs](https://news.ycombinator.com/item?id=48089263)**

The team behind RPCS3 suggests that vibe-coders "learn how to debug and code" instead of "generating slop that you don't understand"

⬆️ 132 • 💬 85 • 5h ago • [Kotaku](https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656)

---

**[Show HN: Git for AI Agents](https://news.ycombinator.com/item?id=48063548)**

Git for AI coding agents. Contribute to regent-vcs/re_gent development by creating an account on GitHub.

⬆️ 119 • 💬 65 • 2d ago • [GitHub](https://github.com/regent-vcs/re_gent)

---

**[Chrome's AI features may be hogging 4GB of your computer storage](https://news.ycombinator.com/item?id=48084710)**

You can take steps to delete it though.

⬆️ 102 • 💬 54 • 14h ago • [The Verge](https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features)

---

---

## YouTube Videos: "ai"

**[The AI Chat Era Is Over. This Killed It.](https://www.youtube.com/watch?v=FJT5Rh0eKe8)**

Try Genspark with free credits available upon signup:* https://bit.ly/4njiP0c Unlimited AI chat and AI image for all paid users in ...

📺 Julia McCoy

👁️ 19K • 👍 831 • 💬 64 • ⏱️ 12:28 • 14h ago

---

**[The Line Between AI And Reality Is Disappearing](https://www.youtube.com/watch?v=-Ma3CIHBNLo)**

People accuse me of being AI almost every day now… and honestly, that should concern everyone. Artificial intelligence is getting ...

📺 Ouachita Mountain Living 

👁️ 9K • 👍 1K • 💬 237 • ⏱️ 14:54 • 15h ago

---

**[When Two AIs Go To War: A Realistic Scenario](https://www.youtube.com/watch?v=gwfCWDO4LbM)**

This is a scenario, but here are the sources for the real research referenced: ...

📺 Species | Documenting AGI

👁️ 87K • 👍 5K • 💬 859 • ⏱️ 35:15 • 1d ago

---

**[Anthropic Situation Just Got Even More INSANE](https://www.youtube.com/watch?v=Pf7Y6Tu-Pzc)**

Anthropic just entered one of the strangest moments in AI. Claude is suddenly tied to SpaceX compute, Google Cloud, Amazon, ...

📺 AI Revolution

👁️ 57K • 👍 2K • 💬 155 • ⏱️ 17:08 • 1d ago

---

**[Which Bed Would You Choose for a Dreamy Sleep? 🛏️✨ AI ASMR](https://www.youtube.com/watch?v=cSyLFn_R3Oo)**

Which Bed Would You Choose for a Dreamy Sleep? 🛏️✨ AI ASMR Relax and unwind after a long day with this dreamy AI ...

📺 PeaceHubASMR

👁️ 32K • 👍 48 • 💬 1 • ⏱️ 2:26 • 16h ago

---

**[You&#39;re Wasting 40% Of Your AI Time On Something Fixable](https://www.youtube.com/watch?v=647pSnX5H_Y)**

Full article w/ the Ultimate Codex Plugin Guide: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 41K • 👍 2K • 💬 163 • ⏱️ 27:13 • 1d ago

---

**[AI News: ChatGPT Is Back, NotebookLM Update, Google AI Health Coach, New Pomelli Feature...](https://www.youtube.com/watch?v=myJ2IVHOfrI)**

Try i10x: https://i10x.ai/?fpr=paul53 Save 15% with code "PJL15" ChatGPT returns to form with a major model update while ...

📺 Paul J Lipsky

👁️ 38K • 👍 1K • 💬 93 • ⏱️ 21:51 • 1d ago

---

**[My ai girlfrfiend part 2](https://www.youtube.com/watch?v=rjdix1lcwMo)**

Thanks for watching. Don't forget to like and subscribe! Featuring @DominiqueDanielle My Instagram ...

📺 NellyVidz

👁️ 43K • 👍 3K • 💬 133 • ⏱️ 8:51 • 1d ago

---

**[Self-building AI, job cuts &amp; more | AI roundup](https://www.youtube.com/watch?v=FAyfVZB-3MY)**

AI is accelerating fast — and the consequences are already here. From self-building 'recursive' AI systems to Iran's AI propaganda ...

📺 CNN

👁️ 70K • 👍 923 • 💬 462 • ⏱️ 23:44 • 1d ago

---

**[The AI users falling into delusion | The Global Story](https://www.youtube.com/watch?v=nYPwZrS-9eA)**

In just the last few years, AI chatbots have become routine aspects of many people's everyday lives. They are being used as ...

📺 BBC News

👁️ 116K • 👍 3K • 💬 757 • ⏱️ 23:15 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 144,251 • ❤️ 556 • 2d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 44,834 • ❤️ 385 • 2d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 1,339,144 • ❤️ 3,824 • 5d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 692 • ❤️ 195 • 1d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 56,628 • ❤️ 198 • 5d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 8,994 • ❤️ 294 • 14d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 185,884 • ❤️ 1,397 • 18d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 58,647 • ❤️ 202 • 5h ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,273,063 • ❤️ 1,229 • 17d ago

---

**[gemma-4-26B-A4B-it-assistant](https://huggingface.co/google/gemma-4-26B-A4B-it-assistant)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model supporting text and image inputs with a 256K context window. It excels in reasoning, coding, and agentic workflows, offering fast inference via its Mixture-of-Experts architecture with only 4B active parameters.

`any-to-any` `419.7M`

⬇️ 40,881 • ❤️ 106 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 62 • 💬 3 • ⭐ 73,141 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 4 • 💬 0 • ⭐ 15,526 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 18 • 💬 3 • ⭐ 10,484 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 78 • 💬 7 • ⭐ 4,291 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[Adam's Law: Textual Frequency Law on Large Language Models](https://huggingface.co/papers/2604.02176)**

*Hongyuan Adam Lu, Z. L., Victor Wei et al. (8 authors)*

🏢 FaceMind

A novel framework for improving large language model performance through textual frequency analysis, including laws, distillation, and curriculum training approaches.

▲ 501 • 💬 9 • ⭐ 1,277 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.02176) • [💻 code](https://github.com/HongyuanLuke/frequencylaw)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 32 • 💬 3 • ⭐ 23,903 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 102 • 💬 10 • ⭐ 8,702 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 54 • 💬 2 • ⭐ 55,313 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 169 • 💬 10 • ⭐ 46,932 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,575 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.4k • 🔱 2.8k • 13d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 11.4k • 🔱 751 • 7h ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 6.1k • 🔱 466 • 5h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.7k • 🔱 773 • 10h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.4k • 🔱 221 • 12h ago

---

**[Mouseww/anything-analyzer](https://github.com/Mouseww/anything-analyzer)**

全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE   |  All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration

`TypeScript` `2api` `ai-tools` `analysis-cli` `api-analysis` `automation-tools`

⭐ 2.4k • 🔱 488 • 13h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

An open source harness for generating CAD models

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.4k • 🔱 280 • 1d ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.1k • 🔱 215 • 13h ago

---

**[bergside/design-md-chrome](https://github.com/bergside/design-md-chrome)**

Chrome extension to extract styles from any website and generate DESIGN.md files and design skills for AI based on TypeUI

`JavaScript` `ai` `chrome` `chrome-extension` `claude` `claude-design`

⭐ 1.9k • 🔱 238 • 16d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 1.8k • 🔱 110 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
