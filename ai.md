---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-20T16:40:31.733759+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 20, 2026 at 16:40 UTC  
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

**[Researchers gave 1,222 people AI assistants, then took them away after 10 minutes. Performance crashed below the control group and people stopped trying. UCLA, MIT, Oxford, and Carnegie Mellon call it the "boiling frog" effect.](https://www.reddit.com/r/artificial/comments/1sqcz1m/researchers_gave_1222_people_ai_assistants_then/)**

A new study from UCLA, MIT, Oxford, and Carnegie Mellon gave 1,222 people AI assistants for cognitive tasks — then pulled the plug midway through. The results: - After ~10 minutes of AI-assisted problem solving, people who lost access to AI performed **worse** than those who never had it - They didn't just get more wrong answers — they **stopped trying altogether** - The effect showed up across math AND reading comprehension - Ran 3 separate experiments (350 → 670 → full cohort). Same result every time. The researchers call it the "boiling frog" effect — each AI interaction feels costless, but your cognitive muscles are quietly atrophying. The UCLA co-author warns this could create "a generation of learners who will not know what they're capable of." Study hasn't been peer-reviewed yet, but the sample size is solid and it's the first causal (not correlational) evidence of AI-induced cognitive decline. The uncomfortable question: if 10 minutes is enough to measurably damage independent performance, what does months of daily use do? Full breakdown → https://synvoya.com/blog/2026-04-20-ai-boiling-frog-cognition-study/ Be honest — have you noticed yourself giving up faster on problems since you started using AI daily? https://preview.redd.it/xm3dil38e9wg1.jpg?width=2752&format=pjpg&auto=webp&s=4cec0fb89dbc1c8bfa303e06ec9622bb48bfc9ae

13h ago

---

**[Reality of SaaS](https://www.reddit.com/r/artificial/comments/1sq3k3x/reality_of_saas/)**

Why on earth would you pay $49/mo for a polished Saas product when you can spend $500 a day building one for yourself in Claude. Absolute insanity if you ask me. The End of Software.

20h ago

---

**[US draft update: Major tech company urges universal national service](https://www.reddit.com/r/artificial/comments/1sq6iy4/us_draft_update_major_tech_company_urges/)**

The company has won major Pentagon contracts, including work on Project Maven, an AI‑driven targeting and surveillance program.

🔗 [Newsweek](https://www.newsweek.com/us-draft-update-major-tech-company-urges-universal-national-service-11850885) • 18h ago

---

**[Is anyone else noticing that ChatGPT seems to be completely down for everyone right now?](https://www.reddit.com/r/artificial/comments/1sqrh0v/is_anyone_else_noticing_that_chatgpt_seems_to_be/)**

I got booted from ChatGPT on all my devices, and now I'm just getting hit with error messages whenever I try to log back into my account

1h ago

---

**[Tech industry lays off nearly 80,000 employees in the first quarter of 2026 — almost 50% of affected positions cut due to AI](https://www.reddit.com/r/artificial/comments/1spw2w0/tech_industry_lays_off_nearly_80000_employees_in/)**

Some experts argue that AI was just used as an excuse for poor business decisions.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/tech-industry-lays-off-nearly-80-000-employees-in-the-first-quarter-of-2026-almost-50-percent-of-affected-positions-cut-due-to-ai) • 1d ago

---

**[Evidence mounts that AI-written books are consuming the publishing industry: in 2025, the number of self-published books jumped by 40% YoY, from 2.5 million to 3.5 million. Running a random sample of these books through an AI detection tool shows a 40% YoY increase in books flagged as AI.](https://www.reddit.com/r/artificial/comments/1sq7bpd/evidence_mounts_that_aiwritten_books_are/)**

The New York Times: "The program found that nearly 20 percent of the novels had been substantially written by A.I. Looking mostly at novels released between 2024 and 2025, Chakrabarty saw a 41 percent jump year-over-year in how many novels in his random sample contained a large amount of A.I. generated text"

18h ago

---

**[The $1 Trillion AI Buildout — Who's Actually Getting Paid?](https://www.reddit.com/r/artificial/comments/1sqseut/the_1_trillion_ai_buildout_whos_actually_getting/)**

Institutional-grade stock market news, AI-powered market signals, and editorial analysis from Ian Gross.

🔗 [The Big Market Report](https://bigmarketreport.com/analysis/ai-buildout-who-is-getting-paid) • 1h ago

---

**[I almost lost a client because my AI system cited a lower court ruling as if it came from the Supreme Court](https://www.reddit.com/r/artificial/comments/1sqoh6b/i_almost_lost_a_client_because_my_ai_system_cited/)**

I build AI systems for professional services firms. During testing of a legal research assistant I built for a German law firm, one of the senior lawyers flagged something that could have been a serious problem. The system was asked about a specific GDPR interpretation. It returned a correct answer but attributed a lower court's more expansive interpretation to the higher court. Essentially it said "the EuGH (European Court of Justice) ruled that X" when actually X was the position of a regional labor court. The EuGH's actual position was more conservative. In a normal chatbot this is a minor accuracy issue. In legal work this is potentially dangerous. A lawyer reading that output might advise a client based on what they think is a Supreme Court ruling when it's actually just one regional court's interpretation. The legal weight of those two sources is completely different. What went wrong technically: the LLM had context from multiple authority levels and when synthesizing the answer it grabbed the clearest phrasing rather than the highest authority position. The lower court happened to explain the concept in more accessible language. The higher court's ruling used denser legal terminology. The LLM essentially optimized for clarity over accuracy of attribution. How I fixed it: Added explicit prompt instructions requiring the LLM to check which category section a document belongs to before attributing it. "A finding from [Category: High court decision] must be attributed to the high court, not to a lower court." Added a requirement that when courts at different levels disagree, both positions must be presented separately with correct attribution. No flattening into consensus. Added specific examples in the prompt showing correct vs incorrect attribution so the LLM has a reference pattern to follow. After these changes the system correctly presents something like: "The EuGH established that X requires conditions A, B, and C. However, the ArbG Oldenburg (regional labor court) has taken a broader position, holding that condition A alone may be sufficient. This represents a divergence from the higher court's framework." The senior lawyer who caught this was actually impressed that we fixed it within a day. He said most legal tech tools he's evaluated don't handle authority attribution at all, they just return text without any awareness of which court said what. This experience taught me that in high-stakes domains, the subtle errors are more dangerous than the obvious ones. A hallucinated answer is easy to spot. A correctly sourced answer with wrong attribution looks credible and that's exactly what makes it dangerous.

3h ago

---

**[The AI Layoff Trap, The Future of Everything Is Lies, I Guess: New Jobs and many other AI Links from Hacker News](https://www.reddit.com/r/artificial/comments/1sqttj9/the_ai_layoff_trap_the_future_of_everything_is/)**

Hey everyone, I just sent the 28th issue of AI Hacker Newsletter, a weekly roundup of the best AI links and the discussions around it. Here are some links included in this email: Write less code, be more responsible (orhun.dev) -- comments The Future of Everything Is Lies, I Guess: New Jobs (aphyr.com) -- comments The AI Layoff Trap (arxiv.org) -- comments The Future of Everything Is Lies, I Guess: Safety (aphyr.com) -- comments European AI. A playbook to own it (mistral.ai) - comments If you want to receive a weekly email with over 40 links like these, please subscribe here: https://hackernewsai.com/

30m ago

---

**[New Gallup poll finds that low-income Americans are turning to AI as a replacement for expensive doctor's visits. Only 14% of all Americans use AI for this reason, but this figure jumps to 32% among the lowest income bracket (<$24,000). A plurality of Americans distrust AI's use in healthcare.](https://www.reddit.com/r/artificial/comments/1sqsut6/new_gallup_poll_finds_that_lowincome_americans/)**

"Some report forgoing healthcare visits because of AI-generated advice. Fourteen percent of recent users say the AI information or advice they received led them to skip a provider visit in the past 30 days. When projected to the entire adult population, this represents an estimated 14 million U.S. adults who did not see a provider because of the AI-generated health information or advice they received."

1h ago

---

---

## Google News: "ai"

**[Project Glasswing: Securing critical software for the AI era](https://www.anthropic.com/glasswing)**

A new initiative to secure the world’s most critical software and give defenders a durable advantage in the coming AI-driven era of cybersecurity.

Anthropic • 12d ago

---

**[AI chatbots could be making you stupider](https://www.bbc.com/future/article/20260417-ai-chatbots-could-be-making-you-stupider)**

As large language models take over more and more cognitive tasks, researchers are warning this mental outsourcing comes with a cost.

BBC • 6h ago

---

**[Reform’s Richard Tice posts picture with telltale signs of AI manipulation, say experts](https://www.theguardian.com/politics/2026/apr/20/reform-richard-tice-picture-ai-manipulation)**

Deputy leader’s image on X was almost certainly generated or altered using AI, according to Peryton Intelligence

The Guardian • 28m ago

---

**[Stuart Varney: Today's AI leaders are as unpopular as Rockefeller](https://www.foxbusiness.com/video/6393482300112)**

'Varney & Co.' Stuart Varney discusses concerns over Anthropic's 'Mythos' amid rising AI worries and fears of cyberattacks.

Fox Business • 17m ago

---

**[Early Anthropic investor on impact of AI: We have to educate ourselves on the risks](https://www.cnbc.com/video/2026/04/20/early-anthropic-investor-on-impact-of-ai-we-have-to-educate-ourselves-on-the-risks.html)**

Anjney Midha, founder of AMP, joins 'Money Movers' to discuss Anthropic, the impacts of artificial intelligence, and more.

CNBC • 29m ago

---

**[Windows 11 Will Let Third-Party AI Agents Sit on Your Taskbar](https://www.extremetech.com/computing/windows-11-will-let-third-party-ai-agents-sit-on-your-taskbar)**

When an agent begins working, Windows pins it to the taskbar and displays status badges indicating whether a task has finished or needs attention.

extremetech.com • 25m ago

---

**[Marc Benioff Says the Software Bears Are All Wrong About Salesforce](https://www.wsj.com/tech/ai/marc-benioff-says-the-software-bears-are-all-wrong-about-salesforce-c7042852)**

WSJ • 14h ago

---

**[AI boom poised to be ‘massively disinflationary’, Northern Trust says](https://www.ft.com/content/7ec229f4-200e-4f34-ba6d-0642397d03e3?syn-25a6b1a6=1)**

Head of financial services group’s $1.4tn asset management division expects new tech to unleash huge productivity gains

Financial Times • 12h ago

---

**[Exclusive: Alex Bores rolls out "AI dividend" plan to share AI wealth](https://www.axios.com/2026/04/20/alex-bores-ai-dividend-plan-wealth)**

Axios • 7h ago

---

**[‘Technofascism’: Critics accuse Palantir of pushing AI war doctrine](https://www.aljazeera.com/news/2026/4/20/technofascism-critics-accuse-palantir-of-pushing-ai-war-doctrine)**

Palantir CEO Alexander Karp's book The Technological Republic advocates for Western 'hard power ... built on software'.

Al Jazeera • 5h ago

---

---

## HackerNews: "ai"

**[College instructor turns to typewriters to curb AI-written work](https://news.ycombinator.com/item?id=47818485)**

⬆️ 478 • 💬 423 • 1d ago • [sentinelcolorado.com](https://sentinelcolorado.com/uncategorized/a-college-instructor-turns-to-typewriters-to-curb-ai-written-work-and-teach-life-lessons/)

---

**[Airline worker arrested after sharing photos of bomb damage in WhatsApp group](https://news.ycombinator.com/item?id=47824068)**

Police lured the man to a meeting and arrested him after accessing a private WhatsApp group with colleagues

⬆️ 277 • 💬 184 • 1d ago • [LBC](https://www.lbc.co.uk/article/dubai-police-spied-private-whatsapp-5HjdXwr_2/)

---

**[Atlassian Enables Default Data Collection to Train AI](https://news.ycombinator.com/item?id=47833247)**

⬆️ 250 • 💬 61 • 4h ago • [letsdatascience.com](https://letsdatascience.com/news/atlassian-enables-default-data-collection-to-train-ai-f71343d8)

---

**[Graphs that explain the state of AI in 2026](https://news.ycombinator.com/item?id=47817581)**

AI investment is skyrocketing while AI’s impact on jobs and public perception remains mixed

⬆️ 111 • 💬 61 • 1d ago • [IEEE Spectrum](https://spectrum.ieee.org/state-of-ai-index-2026)

---

**[Uber’s Anthropic AI push hits a wall](https://news.ycombinator.com/item?id=47826328)**

Uber Technologies, Inc is learning the hard way that scaling AI isn't just about speed—it's about cost. Despite spending $3.4 billion on research and development, the company has already exhausted its planned AI budget just months into 2026. According to The Information, Chief Technology Officer Praveen Neppalli Naga said Uber is now "back to the drawing board" after a surge in the use of AI coding tools, particularly Anthropic's Claude Code, has blown past internal expectations. Don't Miss: A s

⬆️ 93 • 💬 100 • 22h ago • [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/ubers-anthropic-ai-push-hits-223109852.html)

---

**[CEOs admit AI had no impact on employment or productivity](https://news.ycombinator.com/item?id=47827985)**

In the 1980s, economist Robert Solow made an observation that reminded economists of today’s AI boom: “You can see the computer age everywhere but in the productivity statistics.”

⬆️ 87 • 💬 77 • 18h ago • [Fortune](https://fortune.com/article/why-do-thousands-of-ceos-believe-ai-not-having-impact-productivity-employment-study/)

---

**[Swiss AI Initiative (2023)](https://news.ycombinator.com/item?id=47828444)**

⬆️ 86 • 💬 26 • 17h ago • [Swiss AI](https://www.swiss-ai.org)

---

**[A Pascal's Wager for AI Doomers](https://news.ycombinator.com/item?id=47832887)**

⬆️ 49 • 💬 75 • 4h ago • [pluralistic.net](https://pluralistic.net/2026/04/16/pascals-wager/)

---

**[The Uncanny Valley and the Rising Power of Anti-AI Sentiment](https://news.ycombinator.com/item?id=47829058)**

Why public hostility toward AI may feel visceral, including mismatch, disgust, danger avoidance, mortality salience, and design consistency.

⬆️ 48 • 💬 74 • 16h ago • [LocalScribe](https://localscribe.co/posts/uncanny-valley-and-rising-power-of-anti-ai-sentiment/)

---

**[Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)**

Record a browser task once. Replay it as a callable tool. Zero token cost, 100% deterministic, auth propagated from the live webpage.

⬆️ 44 • 💬 17 • 2d ago • [rtrvr.ai](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)

---

---

## YouTube Videos: "ai"

**[How to Actually Make an AI Music Video](https://www.youtube.com/watch?v=9XP-sz0LsLs)**

Create AI Music Videos with OpenArt ...

📺 Isa does AI

👁️ 5K • 💬 1 • ⏱️ 8:44 • 2h ago

---

**[AI Is Literally A Psyop](https://www.youtube.com/watch?v=wLC7SATDmy8)**

So much of the hype around AI is due to its supposed "superintelligence". Supposedly, AGI will be able to do almost everything ...

📺 Cole Hastings

👁️ 91K • 👍 5K • 💬 911 • ⏱️ 17:36 • 1d ago

---

**[Agent Swarms Is One of The Most Powerful AI System Yet](https://www.youtube.com/watch?v=KdP305UYuNA)**

Abacus AI just showed something that feels a lot bigger than another flashy AI demo. Agent Swarms inside ChatLLM and Deep ...

📺 AI Revolution

👁️ 10K • 👍 436 • 💬 36 • ⏱️ 13:18 • 19h ago

---

**[The Claude Mythos delusion...](https://www.youtube.com/watch?v=mOGqQjAlWxs)**

Find out more about CodeCrafters - https://app.codecrafters.io/join?via=club-awesome Topics: - The Anthropic Claude Mythos ...

📺 Awesome

👁️ 36K • 👍 2K • 💬 192 • ⏱️ 8:48 • 7h ago

---

**[What is going on with AI?](https://www.youtube.com/watch?v=8ad3L_TkDqk)**

KICKSTARTER FOR LABOR/ZERO: https://www.kickstarter.com/projects/daveshap/labor-zero UNIVERSAL HIGH INCOME: ...

📺 David Shapiro

👁️ 9K • 💬 122 • ⏱️ 24:02 • 5h ago

---

**[How to Sell AI Agents to Local Businesses In 2026 (START HERE)](https://www.youtube.com/watch?v=HTWrhbtETuI)**

Best AI Agent Tool is Base44 https://base44.pxf.io/c/6440076/3820726/25619?trafcat=agent&sharedid=agent4 ✓ FREE ...

📺 Mikey No Code

👁️ 6K • 💬 7 • ⏱️ 30:05 • 2h ago

---

**[OpenAI GPT-5.5 Leaked: Super Powerful AI Model! Beats Opus 4.7, Gemini 3.1! Cheap &amp; Fast! (Tested)](https://www.youtube.com/watch?v=UfUBW9QcTjU)**

in this video, we break down the rumored GPT-5.5 “pro” model from OpenAI and why it's getting so much attention online.

📺 WorldofAI

👁️ 28K • 👍 611 • 💬 80 • ⏱️ 10:27 • 10h ago

---

**[AI Experts are Quietly Admitting This…](https://www.youtube.com/watch?v=K96KfUgS_gg)**

Try Verdent AI ⤵ https://www.verdent.ai/?id=700278 @verdent_ai CHAPTERS ⤵ 00:00 - Introduction to AI News 02:38 - Creating ...

📺 Dylan Curious

👁️ 10K • 👍 428 • 💬 121 • ⏱️ 30:36 • 1d ago

---

**[WORKERS REFUSING TO TRAIN THEIR AI REPLACEMENTS!](https://www.youtube.com/watch?v=1L2RB-PmtoQ)**

Need a resume/cover letter? Check out my templates! https://joshuafluke.store/ Join the community!

📺 Joshua Fluke

👁️ 18K • 👍 2K • 💬 477 • ⏱️ 5:46 • 4h ago

---

**[P(doom) | Real Time with Bill Maher (HBO)](https://www.youtube.com/watch?v=w5SYm4J4utQ)**

New Rule: When the people who are making A.I. are scared of A.I., it's time to “shut the whole thing down until we can figure out ...

📺 Real Time with Bill Maher

👁️ 778K • 👍 19K • 💬 3K • ⏱️ 10:07 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 334,628 • ❤️ 1,016 • 5d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,662 • ❤️ 883 • 6d ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 816,485 • ❤️ 541 • 3h ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 4,144 • ❤️ 488 • 3d ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 0 • ❤️ 489 • 4d ago

---

**[gemma-4-E4B-it-OBLITERATED](https://huggingface.co/OBLITERATUS/gemma-4-E4B-it-OBLITERATED)**

*OBLITERATUS*

Gemma 4 E4B OBLITERATED v3 is a text-generation model with 0% refusal and improved coding capabilities, designed for uncensored and unrestricted AI interactions. It features a modified architecture with 720 intact tensors, making it highly compatible with tools like Ollama and llama.cpp, and optimized for performance on consumer hardware.

`text-generation` `8.0B`

⬇️ 50,701 • ❤️ 369 • 18h ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 314,205 • ❤️ 996 • 12h ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 5,297 • ❤️ 331 • 3d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 77,195 • ❤️ 431 • 8d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 66,555 • ❤️ 1,194 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 7 • 💬 2 • ⭐ 2,880 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 24 • 💬 1 • ⭐ 19,764 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 47 • 💬 2 • ⭐ 51,813 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 100 • 💬 5 • ⭐ 1,385 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,416 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 53 • 💬 1 • ⭐ 77,396 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 60,602 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 73 • 💬 6 • ⭐ 16,353 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 18,191 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems](https://huggingface.co/papers/2604.14228)**

*Jiacheng Liu, Xiaohan Zhao, Xinyi Shang et al. (4 authors)*

The study analyzes Claude Code's architecture, identifying five motivating human values and tracing them through thirteen design principles to specific implementation choices, including a core while-loop architecture and supporting systems for safety, context management, and extensibility.

▲ 18 • 💬 1 • ⭐ 391 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14228) • [💻 code](https://github.com/VILA-Lab/Dive-into-Claude-Code)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 48.4k • 🔱 6.3k • 19h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 40.2k • 🔱 2.0k • 2d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 36.8k • 🔱 7.5k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 31.2k • 🔱 3.4k • 2d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.3k • 🔱 538 • 1h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 8d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.5k • 🔱 935 • 1d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 5.0k • 🔱 1.2k • 25d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.8k • 🔱 182 • 5h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.7k • 🔱 459 • 11d ago

---

---

*Generated by PeekDeck - A glance is all you need*
