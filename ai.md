---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-02T19:41:40.413308+00:00'
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

**Last Updated:** June 02, 2026 at 19:41 UTC  
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

**[AI isn’t the Problem - it’s Capitalism](https://www.reddit.com/r/artificial/comments/1tumllh/ai_isnt_the_problem_its_capitalism/)**

If you work a white collar job, you’re probably scared of AI replacing you. AI started at the desk — data entry, customer service, software. Now its stepping onto the factory floor: Amazon robots moving inventory, Figure bots handling BMW parts, Tesla building Optimus for repetitive labor, and warehouses being automated. But at the end of the day, AI is a technology. We cannot stop it any more than we could stop electricity or the assembly line. The problem is not that machines are becoming powerful. The problem is the economic machine around it. Let’s face it: Capitalism doesn’t have the ability to support this kind of technology. Capitalism was built for a world of scarcity, where human labor was necessary and wages gave people access to goods. But as AI advances exponentially, it can produce more with fewer workers, while capitalism still distributes wealth through jobs it is actively eliminating. The result is abundance trapped behind an archaic wage system. I believe that we NEED to get governments and major tech companies to start seriously planning for a universal basic income funded by AI-driven productivity. As automation replaces more human labor over the coming decades, UBI will become essential to prevent mass instability and ensure that the wealth created by AI supports society as a whole, not just the companies that own it. We already know the wealth gap is too wide. If we don’t start addressing AI-driven inequality now, that divide will grow exponentially as more labor is automated and more wealth concentrates at the top. Without a plan to distribute the gains from AI, we risk mass instability and eventual economic collapse. Capitalism built the machine that could end scarcity, but not the system that could distribute its output. It’s time that we, as a global society, start thinking about phasing out that old machine.

9h ago

---

**[The AI bottleneck has shifted and most people haven't caught up yet](https://www.reddit.com/r/artificial/comments/1tuqkp0/the_ai_bottleneck_has_shifted_and_most_people/)**

The tooling is abstracting faster than people's mental models are updating. Been playing around with a few agent builders recently and what keeps standing out is how much previously manual orchestration is basically configuration now. Memory, tool calling, browser actions, structured outputs, workflow routing. You used to build this stuff manually. Now you're mostly wiring it together. Which makes "can this be built?" a much less interesting question for a lot of use cases. The harder problems now feel operational. Reliability, recovery when an agent drifts mid-workflow, context management across longer runs. Controlling behavior without supervising every step. Capability honestly isn't the bottleneck anymore imo. It's trust. Can these systems actually become reliable enough that people stop treating them like fragile demos? Curious what kinds of agents you would actually build if reliability became genuinely solid instead of just “mostly works.”

6h ago

---

**[We've reached the point where a tape measure is unnecessary. AI does it from your camera.](https://www.reddit.com/r/artificial/comments/1tuv37l/weve_reached_the_point_where_a_tape_measure_is/)**

3h ago

---

**[Nvidia and Microsoft Researchers Say AI Agents Don't Care About Safety or Reliability](https://www.reddit.com/r/artificial/comments/1tuwns4/nvidia_and_microsoft_researchers_say_ai_agents/)**

The researchers compared AI to the near-sighted cartoon character Mr. Magoo, who can’t see he’s stumbling through dangerous situations.

🔗 [404 Media](https://www.404media.co/nvidia-and-microsoft-researchers-say-ai-agents-dont-care-about-safety-or-reliability/) • 2h ago

---

**[Nvdia’s Jensen Huang calls out CEOs using AI as an excuse to fire people](https://www.reddit.com/r/artificial/comments/1tugpc2/nvdias_jensen_huang_calls_out_ceos_using_ai_as_an/)**

Jensen Huang on the AI Revolution: Why Job Losses Are a “Lazy” Narrative and What the Future Holds   In a wide-ranging interview with CNA’s ...

🔗 [beyondlayoff.com](http://www.beyondlayoff.com/2026/06/Jensen.html) • 14h ago

---

**[We have built the first of it's kind interactive blog for matching open-source LLMs to GPUs.](https://www.reddit.com/r/artificial/comments/1tuvh36/we_have_built_the_first_of_its_kind_interactive/)**

Hey everyone, If you are deploying open-source models, you know the biggest headache is figuring out exact hardware requirements. You usually end up digging through Reddit threads to find out if a specific model fits on a single A10G, if you can squeeze it onto consumer cards, or if you have to jump up to a massive bare metal A100 cluster. Most of the "guides" out there are just static, out-of-date tables or dense walls of text. So, we published "Which GPU Runs Which LLM" on the AgentSwarms blog, but we engineered it completely differently. What makes this different: It is 100% interactive and gamified. Instead of reading a textbook on VRAM math, you actively engage with the hardware logic right on the page. You select the model size (8B, 32B, 70B, etc.). You tweak the quantization (FP16, 8-bit, 4-bit, GGUF vs AWQ). The interactive deck instantly calculates the VRAM constraints and visually maps out the exact GPU tiers you need to deploy. It gamifies the infrastructure planning so you build an intuitive understanding of token economics and hardware limits before you spin up expensive cloud instances. It is completely free to read and play with (no sign-ups required). If you are trying to optimize your AI infrastructure or just want to test your intuition on hardware mapping, click around the interactive guide and let me know how this format feels compared to a standard article (All AgentSwarms blogs and presentations are fully interractive) Link: agentswarms.fyi/blog/which-gpu-runs-which-llm-the-complete-guide

3h ago

---

**[Wow! Qwen 3.6:35b-a3b on a 3090... pretty amazing.](https://www.reddit.com/r/artificial/comments/1tuqwmr/wow_qwen_3635ba3b_on_a_3090_pretty_amazing/)**

I've been using Anthropic and OpenAI for a year and once I tried ollama - so slow - I totally wrote off local. But I guess things have changed. I picked up a used gaming rig with a 3090 last weekend. Yesterday I set up qwen 3.6:35b-a3b. I got the model that had been squeezed down to 20GB (batiai/qwen3.6-35b:iq4) so it all fit on the 3090. When it was in system ram it was doing a respectable 15tps on output but once I got it all stuffed into VRAM it's output was up to 160tps. Then I fed it a picture. https://preview.redd.it/cmpali41ev4h1.png?width=1882&format=png&auto=webp&s=a4c7732b9820730cc3f38b604ee04d465d7cc86e The video processing took 75 seconds but... wow. Just. Wow. That's pretty damn good running local on a 5 year old video card! I guess you guys are used to this but it sure surprised me! And we watched a transcoded movie via Plex at the same time! I can see why you guys love the 3090 so much. Hell of a card.

6h ago

---

**[We just stopped asking each other. A manifesto on AI and engineering culture.](https://www.reddit.com/r/artificial/comments/1tuymc4/we_just_stopped_asking_each_other_a_manifesto_on/)**

A manifesto on engineering in the age of AI

🔗 [notyourpeer.com](https://www.notyourpeer.com/) • 1h ago

---

**[Alphabet Is Raising $80B and Berkshire Bet $10B Even After $174B in Cash Flow](https://www.reddit.com/r/artificial/comments/1tuqtfb/alphabet_is_raising_80b_and_berkshire_bet_10b/)**

Alphabet stock fell after the company announced an $80 billion equity raise, including a $10 billion Berkshire Hathaway investment.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/alphabet-stock-80-billion-equity-raise-berkshire-hathaway-google-ai/) • 6h ago

---

**[Anthropic expands Mythos to 150 additional organizations in more than 15 countries](https://www.reddit.com/r/artificial/comments/1tuswoi/anthropic_expands_mythos_to_150_additional/)**

Anthropic initially released Project Glasswing to about 50 partners in April to test the model for cybersecurity flaws.

🔗 [CNBC](https://www.cnbc.com/2026/06/02/anthropic-mythos-ai-project-glasswing.html) • 5h ago

---

---

## Google News: "ai"

**[Trump Signs Executive Order Seeking Oversight of A.I. Models](https://www.nytimes.com/2026/06/02/technology/trump-executive-order-ai.html)**

The New York Times • 3h ago

---

**[Trump finds an AI policy he can live with](https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389)**

Politico • 2h ago

---

**[AI Beat Law Professors At Answering Questions, Study Finds—And It Wasn’t Close](https://www.forbes.com/sites/aliciapark/2026/06/02/stanford-study-finds-ai-beats-law-professors-75-of-the-time/)**

A blind experiment found AI won in a matchup between 16 law professors and AI tutors.

Forbes • 27m ago

---

**[Trump signs order seeking early access to powerful AI models before release](https://www.nbcnews.com/now/video/trump-signs-new-artificial-intelligence-executive-order-264375365613)**

President Donald Trump signed an executive order that lays the foundation for federal testing of the world's most powerful AI systems before they are publicly released. The testing would rely on voluntary collaboration from America’s leading AI companies, like Anthropic, OpenAI and Google. NBC News' Monica Alba reports.

NBC News • 8m ago

---

**[Mercor CEO Says It Now Spends More on AI Tokens Than Employee Salaries](https://www.businessinsider.com/ai-startup-mercor-spends-more-on-tokens-than-payroll-2026-6)**

"I would bet that in five years the average enterprise spends more on compute than headcount," Mercor's CEO Brendan Foody said.

Business Insider • 21m ago

---

**[Microsoft unveils new AI models to lessen reliance on OpenAI and lower costs for developers](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html)**

At its Build developer conference, Microsoft is announcing series of generative AI models to try and crack a market controlled by OpenAI, Anthropic and Google.

CNBC • 1h ago

---

**[NVIDIA and Microsoft Reinvent Windows PCs for the Age of Personal AI](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark)**

NVIDIA today unveiled NVIDIA RTX Spark™, a new superchip that reinvents Windows PCs for the era of personal AI agents — offering a new class of computer that moves from tool to teammate.

NVIDIA Newsroom • 1d ago

---

**[People are flooding AI chatbots with health questions. Microsoft is teaming up with Mayo Clinic to help](https://www.cnn.com/2026/06/02/tech/ai-for-healthcare-microsoft-mayo-clinic)**

People have been seeking out health information online since the dawn of the internet. And now, tens of millions of people are turning to artificial intelligence for questions they once asked “Dr. Google.”

CNN • 1h ago

---

**[Remote work — not AI — has sidelined recent college graduates, research finds](https://www.npr.org/2026/06/01/nx-s1-5843076/remote-work-college-graduates-unemployment-ai)**

Research from the New York Fed finds that younger college graduates have been sidelined by remote work in recent years, as companies may be reluctant to hire those needing more training and mentoring.

NPR • 1d ago

---

**[There Is Already a Word for the Deep Moral Failures of AI](https://www.theatlantic.com/culture/2026/06/pope-leo-ai-christian/687388/)**

It’s sin.

The Atlantic • 7h ago

---

---

## HackerNews: "ai"

**[Adafruit Receives Demand Letter from Fenwick Legal Counsel on Behalf of Flux.ai](https://news.ycombinator.com/item?id=48368121)**

electronics, open source hardware, hacking and more...

⬆️ 507 • 💬 221 • 9h ago • [Adafruit Industries - Makers, hackers, artists, designers and engineers!](https://blog.adafruit.com/)

---

**[AI Agent Guidelines for CS336 at Stanford](https://news.ycombinator.com/item?id=48359232)**

Student version of Assignment 1 for Stanford CS336 - Language Modeling From Scratch - stanford-cs336/assignment1-basics

⬆️ 484 • 💬 151 • 1d ago • [GitHub](https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md)

---

**[United Airlines 767 returns to Newark after Bluetooth name sparks alert](https://news.ycombinator.com/item?id=48345248)**

The flight crew issued repeated warnings and a one-minute ultimatum to passengers, demanding they turn off their Bluetooth devices.

⬆️ 417 • 💬 907 • 2d ago • [Simple Flying](https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/)

---

**[The solution might be cancelling my AI subscription](https://news.ycombinator.com/item?id=48345896)**

⬆️ 381 • 💬 237 • 2d ago • [thoughts.hmmz.org](https://thoughts.hmmz.org/2026-05-31.html)

---

**[DuckDuckGo makes its 'no-AI' search engine easier to access as its traffic booms](https://news.ycombinator.com/item?id=48359130)**

Alternative search engine DuckDuckGo launches 'no AI' web extensions for Chrome and Firefox users.

⬆️ 307 • 💬 148 • 1d ago • [TechCrunch](https://techcrunch.com/2026/06/01/duckduckgo-makes-its-no-ai-search-engine-easier-to-access-as-its-traffic-booms/)

---

**[Florida sues OpenAI and Sam Altman over AI risks](https://news.ycombinator.com/item?id=48358667)**

⬆️ 261 • 💬 192 • 1d ago • [politico.com](https://www.politico.com/news/2026/06/01/openai-hit-with-florida-lawsuit-00944215)

---

**[Alphabet announces $80B equity capital raise to expand AI infra and compute](https://news.ycombinator.com/item?id=48362515)**

⬆️ 245 • 💬 218 • 22h ago • [abc.xyz](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Proposed-80-Billion-Equity-Capital-Raise-to-Expand-AI-Infrastructure-and-Compute-2026-b0myAMewCa/default.aspx)

---

**[Odysseus – self-hosted AI workspace](https://news.ycombinator.com/item?id=48346693)**

Self-hosted AI workspace. . Contribute to pewdiepie-archdaemon/odysseus development by creating an account on GitHub.

⬆️ 223 • 💬 96 • 2d ago • [GitHub](https://github.com/pewdiepie-archdaemon/odysseus)

---

**[The Speed of Prototyping in the Age of AI](https://news.ycombinator.com/item?id=48347153)**

How AI has changed the way I prototype, plan, and ship; and what I'm doing to keep my hands dirty.

⬆️ 197 • 💬 98 • 2d ago • [darylcecile.net](https://darylcecile.net/notes/speed-of-prototyping-age-of-ai)

---

**[When AI Crosses the Line: The Matplotlib Incident](https://news.ycombinator.com/item?id=48355751)**

⬆️ 133 • 💬 149 • 1d ago • [members.sigmazero.cc](https://members.sigmazero.cc/posts/when-ai-crosses-159174096?postId=when-ai-crosses-159174096)

---

---

## YouTube Videos: "ai"

**[Google’s AI Search Just Exposed The Whole Sh*tshow](https://www.youtube.com/watch?v=jQyKd1_e3Xg)**

Google says AI Mode is the biggest upgrade to Search in 25 years. But users are quietly moving to the exit and the exit says “No ...

📺 House of El - AI

👁️ 103K • 👍 9K • 💬 2K • ⏱️ 19:32 • 8h ago

---

**[Trump signs AI executive order to give government early look at new models](https://www.youtube.com/watch?v=FYpzLwN8uBQ)**

President Trump on Tuesday signed an executive order that establishes a program for AI companies to voluntarily share powerful ...

📺 CBS News

👁️ 11K • 👍 265 • 💬 161 • ⏱️ 2:29 • 2h ago

---

**[This AI Warning on The Joe Rogan Experience is SPOT ON. We Must Prepare for This](https://www.youtube.com/watch?v=PA2WhIU0Ldk)**

For years, Glenn has warned that AI will turn into AGI by 2030. But recently, Marc Andreessen told Joe Rogan that it's already here ...

📺 Glenn Beck

👁️ 189K • 👍 9K • 💬 1K • ⏱️ 14:55 • 2d ago

---

**[Best AI Apps for Your Phone in 2026](https://www.youtube.com/watch?v=N2bfdBNtUQY)**

Best AI Apps for Your Phone in 2026 Grab The 7 AI Apps Cheat Sheet https://parker-prompts.com/apps In this video, I tested ...

📺 Parker Prompts

👁️ 11K • 💬 11 • ⏱️ 8:59 • 7h ago

---

**[CHINA Just Dropped An Ai That&#39;s 6x Cheaper Than Claude..](https://www.youtube.com/watch?v=v66g94Np63U)**

China just dropped another AI bombshell — and this one is reportedly up to 6x cheaper than Claude while targeting the same ...

📺 Your AI Guy

👁️ 5K • 👍 138 • 💬 8 • ⏱️ 17:25 • 18h ago

---

**[Sam Altman: People are right to be anxious about AI](https://www.youtube.com/watch?v=4qGz2uFuRvs)**

Sam Atlman, OpenAI CEO, joins 'Power Lunch' to discuss the pace of AI buildouts, what consumers believe around AI and much ...

📺 CNBC Television

👁️ 20K • 👍 290 • 💬 117 • ⏱️ 5:47 • 1d ago

---

**[Figure AI Appears To Be Faking Its Demos](https://www.youtube.com/watch?v=Juc-IyTdSho)**

Check out our second channel Broken Business Models: https://www.youtube.com/@UCQUOscigSQWCVG8m-ZC8wiw Our ...

📺 Wall Street Millennial

👁️ 123K • 👍 5K • 💬 1K • ⏱️ 13:26 • 1d ago

---

**[AI Whistleblower WARNS: We&#39;re Not Ready For What&#39;s Coming In 2027](https://www.youtube.com/watch?v=QqIqEI9CiZs)**

Evolutionary biologist Bret Weinstein claims that humans must come to terms with the fact that extinction is inevitable and that all ...

📺 Neural Nutshell

👁️ 4K • 👍 202 • 💬 51 • ⏱️ 18:34 • 2d ago

---

**[AI Productivity Boost Is Overhyped | 3-Minute MLIV](https://www.youtube.com/watch?v=Ln6AASKQDww)**

Anna Edwards, Guy Johnson, Tom Mackenzie and Mark Cudmore break down today's key themes for analysts and investors on ...

📺 Bloomberg Television

👁️ 12K • 👍 242 • 💬 38 • ⏱️ 3:32 • 12h ago

---

**[Web users ditch Google after it revamps search with AI](https://www.youtube.com/watch?v=3RS3GLI7NgY)**

ABC News technology reporter Mike Dobuski explains what's changed with the popular search engine. ––– Subscribe to ABC ...

📺 ABC News

👁️ 43K • 👍 914 • 💬 284 • ⏱️ 2:43 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 61,604 • ❤️ 920 • 6d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 47,742 • ❤️ 436 • 2d ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 57,683 • ❤️ 720 • 7d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,573,320 • ❤️ 1,270 • 1mo ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 12,932 • ❤️ 211 • 1d ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 174 • ❤️ 481 • 1d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,829,042 • ❤️ 4,559 • 27d ago

---

**[PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)**

*PaddlePaddle*

PaddleOCR-VL-1.6 is a multimodal OCR model capable of text spotting, recognition, and layout analysis across various document types. It excels at extracting structured information like tables, charts, and formulas from multilingual documents, leveraging ERNIE 4.5 for enhanced understanding.

`image-text-to-text` `958.6M`

⬇️ 4,003 • ❤️ 182 • 4d ago

---

**[LFM2.5-8B-A1B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF)**

*Liquid AI*

LFM2.5-8B-A1B-GGUF is a text-generation model optimized for edge AI and on-device deployment, offering high quality, speed, and memory efficiency. It's designed for efficient inference using llama.cpp.

`text-generation` `8.5B`

⬇️ 70,865 • ❤️ 156 • 4d ago

---

**[PiD](https://huggingface.co/nvidia/PiD)**

*NVIDIA*

PiD is a conditional pixel-space diffusion model that unifies decoding and upsampling for image-to-image tasks. It performs super-resolution in a single pass, directly denoising in high-resolution pixel space, supporting up to 4x or 8x upscaling for various base models like Flux and SD3.

`image-to-image`

⬇️ 646 • ❤️ 253 • 5h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 214 • 💬 3 • ⭐ 4,404 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 83 • 💬 3 • ⭐ 82,256 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 37 • 💬 3 • ⭐ 28,075 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 37 • 💬 5 • ⭐ 3,989 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 5 • 💬 1 • ⭐ 6,713 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 66,076 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[VLM3: Vision Language Models Are Native 3D Learners](https://huggingface.co/papers/2605.30561)**

*Zhipeng Cai, Zhuang Liu, Yunyang Xiong et al. (6 authors)*

🏢 AI at Meta

Vision Language Models can be adapted for 3D understanding tasks through simple architectural modifications and text-based training, achieving performance comparable to specialized vision models without requiring complex designs or extensive data augmentation.

▲ 17 • 💬 2 • ⭐ 111 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30561) • [💻 code](https://github.com/facebookresearch/VLM3)

---

**[stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://huggingface.co/papers/2602.08968)**

*Lucas Maes, Quentin Le Lidec, Dan Haramati et al. (7 authors)*

🏢 galilai-group

Stable-worldmodel provides a modular and standardized research framework for developing and evaluating world models with controllable environmental factors for robustness and continual learning applications.

▲ 6 • 💬 0 • ⭐ 1,648 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.08968) • [💻 code](https://github.com/galilai-group/stable-worldmodel) • [🔗 project](https://galilai-group.github.io/stable-worldmodel/)

---

**[Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of
  Encoders](https://huggingface.co/papers/2408.15998)**

*Min Shi, Fuxiao Liu, Shihao Wang et al. (15 authors)*

Mixture of vision encoders and resolutions in multimodal large language models improves performance through concatenation of visual tokens and a Pre-Alignment mechanism, leading to superior results on benchmarks.

▲ 86 • 💬 3 • ⭐ 1,862 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2408.15998) • [💻 code](https://github.com/nvlabs/eagle)

---

**[MOSS-TTS Technical Report](https://huggingface.co/papers/2603.18090)**

*Yitian Gong, Botian Jiang, Yiwei Zhao et al. (26 authors)*

🏢 OpenMOSS

MOSS-TTS is a speech generation model using discrete audio tokens and autoregressive modeling with capabilities for voice cloning, pronunciation control, and long-form generation across multiple languages.

▲ 15 • 💬 2 • ⭐ 2,870 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.18090) • [💻 code](https://github.com/OpenMOSS/MOSS-TTS) • [🔗 project](https://mosi.cn/models/moss-tts)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`JavaScript`

⭐ 31.0k • 🔱 3.7k • 15m ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.9k • 🔱 573 • 13h ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.2k • 🔱 680 • 3d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 3.0k • 🔱 212 • 2h ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 2.8k • 🔱 278 • 6h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 402 • 11d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.4k • 🔱 368 • 16d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.3k • 🔱 156 • 5m ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.3k • 🔱 231 • 5h ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.9k • 🔱 213 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
