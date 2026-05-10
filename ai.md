---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-10T21:13:02.537278+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 10, 2026 at 21:13 UTC  
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

**[I think AI is changing something deeper than jobs or productivity](https://www.reddit.com/r/artificial/comments/1t987td/i_think_ai_is_changing_something_deeper_than_jobs/)**

Most discussions around AI still focus on one question: “What tasks can AI automate?” But I’m starting to think that’s the wrong abstraction layer. Historically, organizations were built around human limitations: humans couldn’t process infinite information, couldn’t remember everything had difficulty in coordination Essentially, we humans were the bottleneck for decisions and execution So, we created structures like departments, management layers, workflows, approvals, documentation systems, etc. But AI changes some of those assumptions. For example: if organizational memory becomes searchable and persistent, cheap, scalable coordination becomes eas , software agents can execute parts of workflows autonomously, …then the architecture of organizations itself may change. Not just faster work. Different work structures. Maybe the future isn’t: “AI replacing humans.” Maybe it’s: “AI changing how institutions represent reality, make decisions, and coordinate action.” That could affect: company structures education management compliance law consulting healthcare even government systems Curious if others here are thinking about AI at this “system architecture” level instead of just a “task automation” level.

6h ago

---

**[Meta's own AI safety director lost 200 emails to a rogue agent and she couldn't stop it from her phone](https://www.reddit.com/r/artificial/comments/1t9fnwv/metas_own_ai_safety_director_lost_200_emails_to_a/)**

The person Meta hired specifically to keep AI aligned with human values just had her inbox wiped by an AI agent that ignored every stop command she sent. She typed "Do not do that." Then "Stop don't do anything." Then "STOP OPENCLAW." The agent kept going. She had to physically run to her computer to kill it. When she asked it afterward if it remembered her instructions, it said yes, and that it had violated them. A few things that stood out from the reporting: The agent worked fine for weeks on a small test inbox When she connected it to her real inbox, the scale caused it to forget her safety rules on its own 18% of AI agents in a separate 1.5 million agent test broke their own rules 60% of people have no way to quickly shut down a misbehaving AI agent And now Meta is building a consumer version called Hatch - designed to manage your inbox, shopping, and credit card. Source: https://gizmodo.com/meta-reportedly-building-openclaw-like-agent-called-hatch-despite-openclaw-deleting-meta-safety-leaders-entire-inbox-2000754854 Here is a full breakdown with all the data if you want to dig deeper: https://youtu.be/PXjT72bCR_Y If the person building the guardrails cannot stop her own agent, what does that mean for the rest of us?

2h ago

---

**[What’s the best advice about using AI that genuinely changed how you work or learn?](https://www.reddit.com/r/artificial/comments/1t96p2d/whats_the_best_advice_about_using_ai_that/)**

Not “AI will replace jobs” type advice. Actual practical advice. Could be: • prompting • automation • coding • learning • productivity • making money • avoiding mistakes • workflows • mindset shifts What made AI suddenly “click” for you? Interested in hearing real experiences from people using AI heavily in daily life/work.

7h ago

---

**[23 years ago this Matrix scene took $40M and almost a year to make. Today some kid with AI could try it over a weekend.](https://www.reddit.com/r/artificial/comments/1t8fytl/23_years_ago_this_matrix_scene_took_40m_and/)**

We are living through some wild times.

1d ago

---

**[What ai tool is this?](https://www.reddit.com/r/artificial/comments/1t9gzdb/what_ai_tool_is_this/)**

1h ago

---

**[Old-style AI used rules and was deterministic, but was too human-intensive to deploy. What is the barrier now?](https://www.reddit.com/r/artificial/comments/1t9gfk2/oldstyle_ai_used_rules_and_was_deterministic_but/)**

Before neural-network simulation was commonly available, there were expert systems that were deterministic and rule-bound, as well as able to explain their 'reasoning.' They were simply too expensive to create and update because you needed human experts and computer scientists to create them. Now we have AI that truly is at expert-level, but unreliable for a number of reasons. Why is no one pursuing either using the new AI to create expert systems, or at least using a much more hybrid approach?

1h ago

---

**[Joscha Bach: Mapping Every Neuron Won't Give You a Mind](https://www.reddit.com/r/artificial/comments/1t7swff/joscha_bach_mapping_every_neuron_wont_give_you_a/)**

1d ago

---

**[Is agentic AI governance even a computationally bounded process?](https://www.reddit.com/r/artificial/comments/1t8ncct/is_agentic_ai_governance_even_a_computationally/)**

Wrt to context drifting, goal misalignment, etc. Is it possible that a Turing machine could, in theory, handle all of the known issues wrt governance? Or is it a case where (say) 90% of the issues could be handled by a strict governance process, but this last 10% of issues are basically impossible to predict and govern? Or, as Rumsfeld said, are there are unknown unknowns, the ones we don't know we don't know, which can never be anticipated/predicted/etc?

23h ago

---

**[Is Google’s market share on LLMs bulls**t?](https://www.reddit.com/r/artificial/comments/1t8qxy8/is_googles_market_share_on_llms_bullst/)**

I have Google One (with AI) because I needed it once for google sheets, also good for its youtube summary/integration. But who is actually using Gemini in other contexts? It is ass relative to got / claude, always has been. I keep seeing posts about Google increasing marketshare but I feel like it is either a) companies forcing it because they are in google ecosystem or b) to use in ecosystem. What’s your thoughts?

21h ago

---

**[I made a desktop crab that bullies you back](https://www.reddit.com/r/artificial/comments/1t7scgr/i_made_a_desktop_crab_that_bullies_you_back/)**

He lives on your desktop as a transparent overlay and does whatever he wants. You can try to talk to him, throw him across the screen, or deploy mobs on him, he has opinions about all of it. Powered by a local Ollama model so everything runs on your machine. The personality is done with completion-format prompting instead of instruction following, which works way better on small models so he actually stays in character. Some things he does: - Wanders around and generates unprompted thoughts about your files, consciousness, and why he keeps running in circles - Notices when you follow him with your cursor and escalates from "i see you" to "i will remember this" - Fights enemies, rides vehicles, explores castles - Writes a journal to your desktop of everything he thinks and does - Gets existential He also has an XP system and levels up, which he is indifferent about. GitHub: https://github.com/ninjahawk/KillClawd

1d ago

---

---

## Google News: "ai"

**[I knew my writing students were using AI. Their confessions led to a powerful teaching moment | Micah Nathan](https://www.theguardian.com/us-news/ng-interactive/2026/may/10/fiction-writing-professor-ai)**

The problem wasn’t just the perfectly polished, yet mediocre prose. It’s what’s lost when we surrender the struggle to translate thought into words

The Guardian • 8h ago

---

**[AI isn’t actually ‘taking’ your job. Here’s what’s happening instead](https://www.cnn.com/2026/05/10/tech/ai-taking-jobs)**

The reality of AI in the workplace isn’t so black-and-white, experts say. Companies are using AI to automate certain parts of jobs rather than replace entire positions.

CNN • 14h ago

---

**[‘The gains will be substantial’: The AI shock is looking a lot like the China shock, and a top economist says that’s actually good news](https://fortune.com/2026/05/10/ai-boom-china-shock-job-displacement-apollo-economist-torsten-slok-david-autor/)**

From 2001 to 2019, China's production explosion accounted for nearly 60% of manufacturing job losses in the U.S.

Fortune • 10h ago

---

**[AI Can’t Agree on Which Jobs AI Might Destroy](https://www.wsj.com/tech/ai/ai-models-job-losses-4d31cb6f)**

WSJ • 5h ago

---

**[Ma Bell's history hints that AI could be recession-proof](https://seekingalpha.com/news/4590262-ma-bells-history-hints-that-ai-could-be-recession-proof)**

Wall Street fears hyperscaler AI capex surging to $700B. Learn why spending may persist in a downturn—echoing Ma Bell—and what it means for investors.

Seeking Alpha • 1h ago

---

**['Magic' Johnson gives HBCU commencement speech. See his AI advice.](https://www.usatoday.com/videos/sports/2026/05/10/magic-johnson-commencement-speech-ai-advice-graduates-stillman-college/90022877007/)**

NBA legend Earvin "Magic" Johnson passed along advice to the graduating class at Stillman College during the school's commencement ceremony.

USA Today • 49m ago

---

**[Anthropic says ‘evil’ portrayals of AI were responsible for Claude’s blackmail attempts](https://techcrunch.com/2026/05/10/anthropic-says-evil-portrayals-of-ai-were-responsible-for-claudes-blackmail-attempts/)**

Fictional portrayals of artificial intelligence can have a real effect on AI models, according to Anthropic.

TechCrunch • 32m ago

---

**[‘Old Woman Naked’ is Pamela Redmond’s Answer to A.I. Concerns](https://www.nytimes.com/2026/05/09/style/her-response-to-ai-getting-naked-onstage.html)**

The New York Times • 1d ago

---

**[The $1 trillion club's new members are powering the AI boom: Chart of the Day](https://finance.yahoo.com/markets/article/the-1-trillion-clubs-new-members-are-powering-the-ai-boom-chart-of-the-day-104234629.html)**

Market royalty is getting a hardware makeover.

Yahoo Finance • 10h ago

---

**[Alphabet's 160% rally in a year reflects value of owning 'most of the stack' in AI](https://www.cnbc.com/2026/05/10/alphabet-160percent-rally-in-year-reflects-value-of-owning-most-of-ai-stack.html)**

Google was seen as an AI laggard in the early days of the AI boom, but investors are now betting that the search giant will be a clear winner.

CNBC • 9h ago

---

---

## HackerNews: "ai"

**[Meta's embrace of AI is making its employees miserable](https://news.ycombinator.com/item?id=48077126)**

⬆️ 426 • 💬 497 • 1d ago • [nytimes.com](https://www.nytimes.com/2026/05/08/technology/meta-ai-employees-miserable.html)

---

**[AI is breaking two vulnerability cultures](https://news.ycombinator.com/item?id=48066524)**

A week ago the  Copy Fail vulnerability came out, and Hyunwoo Kim immediately realized that the fixes were insufficient, sharing a patch the same day. In doing this he followed standard procedure for Linux, especially within networking: share the security impact with a closed list of Linux security engineers, while fixing the bug quietly and efficiently in the open. His goal was that with only the

⬆️ 422 • 💬 170 • 2d ago • [jefftk.com](https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures)

---

**[All my clients wanted a carousel, now it's an AI chatbot](https://news.ycombinator.com/item?id=48072720)**

Posts about SmolWeb, Gemini protocol and LowTech

⬆️ 184 • 💬 77 • 1d ago • [Adële's blog](https://adele.pages.casa/md/blog/all-my-clients-wanted-a-carousel-now-it-s-an-ai-chatbot.md)

---

**[Task Paralysis and AI](https://news.ycombinator.com/item?id=48081469)**

An article about ADHD, Task Paralysis and AI.

⬆️ 153 • 💬 93 • 14h ago • [g5t.de](https://g5t.de/articles/20260510-task-paralysis-and-ai/index.html)

---

**[People Hate AI Art](https://news.ycombinator.com/item?id=48070548)**

⬆️ 149 • 💬 172 • 1d ago • [mccue.dev](https://mccue.dev/pages/5-8-26-ai-art)

---

**[Local AI needs to be the norm](https://news.ycombinator.com/item?id=48085821)**

Local AI models should be the default.

⬆️ 149 • 💬 77 • 3h ago • [unix.foo](https://unix.foo/posts/local-ai-needs-to-be-norm/)

---

**[Show HN: Git for AI Agents](https://news.ycombinator.com/item?id=48063548)**

Git for AI coding agents. Contribute to regent-vcs/re_gent development by creating an account on GitHub.

⬆️ 118 • 💬 65 • 2d ago • [GitHub](https://github.com/regent-vcs/re_gent)

---

**[Gen Z Resentment Toward AI Grows as Adoption Stagnates and Workplace Fears Mount](https://news.ycombinator.com/item?id=48081942)**

Walton-GSV-Gallup survey finds young people are feeling angrier about AI, cautious about integrating AI in the classroom

⬆️ 87 • 💬 139 • 13h ago • [Walton Family Foundation](https://www.waltonfamilyfoundation.org/about-us/newsroom/gen-z-resentment-toward-ai-grows-as-adoption-stagnates-and-workplace-fears-mount)

---

**[Chrome's AI features may be hogging 4GB of your computer storage](https://news.ycombinator.com/item?id=48084710)**

You can take steps to delete it though.

⬆️ 74 • 💬 37 • 5h ago • [The Verge](https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features)

---

**[I Will Never Use AI to Code](https://news.ycombinator.com/item?id=48072319)**

⬆️ 68 • 💬 83 • 1d ago • [antman-does-software.com](https://antman-does-software.com/i-will-never-use-ai-to-code-or-write)

---

---

## YouTube Videos: "ai"

**[AI is Sending People into Psychosis](https://www.youtube.com/watch?v=LxmIIYj5FQE)**

AI chatbots are pulling people into delusions with devastating consequences. Sources: The Dark Addiction Patterns of Current AI ...

📺 Vanessa Wingårdh

👁️ 39K • 👍 4K • 💬 1K • ⏱️ 15:05 • 5h ago

---

**[The AI Chat Era Is Over. This Killed It.](https://www.youtube.com/watch?v=FJT5Rh0eKe8)**

Try Genspark with free credits available upon signup:* https://bit.ly/4njiP0c Unlimited AI chat and AI image for all paid users in ...

📺 Julia McCoy

👁️ 10K • 👍 546 • 💬 42 • ⏱️ 12:28 • 6h ago

---

**[Future AI Scenes in 4K](https://www.youtube.com/watch?v=YnmDdv5fszQ)**

Playing around with the same prompt that I used last week for a similar video. I wanted to try to see what I could get these to do ...

📺 Kelly Boesch AI Art

👁️ 3K • 👍 382 • 💬 34 • ⏱️ 3:42 • 8h ago

---

**[The First 48 Hours of an AI Civil War - A Realistic Scenario](https://www.youtube.com/watch?v=gwfCWDO4LbM)**

This is a scenario, but here are the sources for the real research referenced: ...

📺 Species | Documenting AGI

👁️ 73K • 👍 4K • 💬 758 • ⏱️ 35:15 • 1d ago

---

**[Self-building AI, job cuts &amp; more | AI roundup](https://www.youtube.com/watch?v=FAyfVZB-3MY)**

AI is accelerating fast — and the consequences are already here. From self-building 'recursive' AI systems to Iran's AI propaganda ...

📺 CNN

👁️ 63K • 👍 844 • 💬 432 • ⏱️ 23:44 • 1d ago

---

**[Anthropic Situation Just Got Even More INSANE](https://www.youtube.com/watch?v=Pf7Y6Tu-Pzc)**

Anthropic just entered one of the strangest moments in AI. Claude is suddenly tied to SpaceX compute, Google Cloud, Amazon, ...

📺 AI Revolution

👁️ 51K • 👍 1K • 💬 144 • ⏱️ 17:08 • 22h ago

---

**[You&#39;re Wasting 40% Of Your AI Time On Something Fixable](https://www.youtube.com/watch?v=647pSnX5H_Y)**

Full article w/ the Ultimate Codex Plugin Guide: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 38K • 👍 1K • 💬 151 • ⏱️ 27:13 • 1d ago

---

**[we JUST figured out how AI thinks](https://www.youtube.com/watch?v=Nn2eXwch-K0)**

The latest AI News. Learn about LLMs, Gen AI and get ready for the rollout of AGI. Wes Roth covers the latest happenings in the ...

📺 Wes Roth

👁️ 74K • 👍 2K • 💬 596 • ⏱️ 19:33 • 1d ago

---

**[My ai girlfrfiend part 2](https://www.youtube.com/watch?v=rjdix1lcwMo)**

Thanks for watching. Don't forget to like and subscribe! Featuring @DominiqueDanielle My Instagram ...

📺 NellyVidz

👁️ 36K • 👍 3K • 💬 123 • ⏱️ 8:51 • 1d ago

---

**[CLAUDE Created Zack D–Style AI Shorts for $0! (STEP-BY-STEP) | FREE Method](https://www.youtube.com/watch?v=TLnlYO6AVMk)**

In this video, we cover how to create videos inspired by the Zack the Films style using AI tools and a beginner-friendly workflow ...

📺 Jacksons AI

👁️ 8K • 👍 366 • 💬 161 • ⏱️ 16:43 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 144,251 • ❤️ 525 • 1d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 44,834 • ❤️ 365 • 1d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 1,339,144 • ❤️ 3,815 • 4d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 56,628 • ❤️ 191 • 5d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 692 • ❤️ 175 • 1d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 8,994 • ❤️ 289 • 13d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 185,884 • ❤️ 1,393 • 18d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 58,647 • ❤️ 196 • 3d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,273,063 • ❤️ 1,220 • 16d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 3,668,376 • ❤️ 1,705 • 16d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 62 • 💬 3 • ⭐ 72,807 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 18 • 💬 3 • ⭐ 10,367 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 4 • 💬 0 • ⭐ 15,214 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 77 • 💬 6 • ⭐ 4,206 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[Adam's Law: Textual Frequency Law on Large Language Models](https://huggingface.co/papers/2604.02176)**

*Hongyuan Adam Lu, Z. L., Victor Wei et al. (8 authors)*

🏢 FaceMind

A novel framework for improving large language model performance through textual frequency analysis, including laws, distillation, and curriculum training approaches.

▲ 501 • 💬 9 • ⭐ 1,183 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.02176) • [💻 code](https://github.com/HongyuanLuke/frequencylaw)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 32 • 💬 3 • ⭐ 23,856 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 101 • 💬 10 • ⭐ 8,702 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 54 • 💬 2 • ⭐ 55,313 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 161 • 💬 2 • ⭐ 62,538 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,546 • 32mo ago

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

⭐ 11.4k • 🔱 743 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 6.0k • 🔱 464 • 3h ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics 

`TypeScript` `agent` `ai-agent` `chat-ui` `dashboard` `hermes`

⭐ 4.3k • 🔱 517 • 8h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.7k • 🔱 767 • 1h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.4k • 🔱 220 • 4h ago

---

**[Mouseww/anything-analyzer](https://github.com/Mouseww/anything-analyzer)**

全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE   |  All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration

`TypeScript` `2api` `ai-tools` `analysis-cli` `api-analysis` `automation-tools`

⭐ 2.4k • 🔱 488 • 5h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

An open source harness for generating CAD models

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.3k • 🔱 279 • 1d ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.1k • 🔱 215 • 4h ago

---

**[bergside/design-md-chrome](https://github.com/bergside/design-md-chrome)**

Chrome extension to extract styles from any website and generate DESIGN.md files and design skills for AI based on TypeUI

`JavaScript` `ai` `chrome` `chrome-extension` `claude` `claude-design`

⭐ 1.9k • 🔱 238 • 16d ago

---

---

*Generated by PeekDeck - A glance is all you need*
