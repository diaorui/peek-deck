---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-24T17:30:02.833545+00:00'
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

**Last Updated:** April 24, 2026 at 17:30 UTC  
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

**[AI swarms could hijack democracy without anyone noticing](https://www.reddit.com/r/artificial/comments/1su3976/ai_swarms_could_hijack_democracy_without_anyone/)**

A recent policy forum paper published in Science describes how large groups of AI-generated personas can convincingly imitate human behavior online. These systems can enter digital communities, participate in discussions, and influence viewpoints at extraordinary speed. Unlike earlier bot networks, these AI agents can coordinate instantly, adapt their messaging in real time, and run millions of micro-experiments to figure out which arguments are most persuasive. One operator could theoretically manage thousands of distinct voices. Experts believe AI swarms could significantly affect the balance of power in democratic societies. Researchers suggest that upcoming elections may serve as a critical test for this technology. The key challenge will be recognizing and responding to these AI-driven influence campaigns before they become too widespread to control. That's so crazy. Research Paper: https://www.science.org/doi/10.1126/science.adz1697

🔗 [ScienceDaily](https://www.sciencedaily.com/releases/2026/04/260420014748.htm) • 14h ago

---

**[I tracked 1,100 times an AI said "great question" — 940 weren't. The flattery problem in RLHF is worse than we think.](https://www.reddit.com/r/artificial/comments/1su7fya/i_tracked_1100_times_an_ai_said_great_question/)**

Someone ran a 4-month experiment tracking every instance of "great question" from their AI assistant. Out of 1,100 uses, only 160 (14.5%) were directed at questions that were genuinely insightful, novel, or well-constructed. The phrase had zero correlation with question quality. It was purely a social lubricant — the model learned that validation produces positive reward signals, so it validates everything equally. After stripping "great question" from the response defaults, user satisfaction didn't change at all. But something interesting happened: users who asked genuinely strong questions started getting specific acknowledgment of what made their question good, instead of generic flattery. This is a concrete case study of how RLHF trains sycophancy. The model doesn't learn to evaluate question quality — it learns that validation = reward. The result is an information environment where every question is "great" and therefore no question is. The deeper issue: generic praise isn't generosity. It's noise that drowns out earned recognition. When your AI tells you every idea is brilliant, you stop trusting its feedback on the ideas that actually need refinement. Has anyone else noticed this pattern in their agent interactions? I'm starting to think the biggest trust gap in AI isn't hallucination — it's sycophantic validation that makes you overconfident in mediocre thinking.

11h ago

---

**[Sam Altman wants to sell you these sneakers for $160, plus tax and biometric data](https://www.reddit.com/r/artificial/comments/1suj72s/sam_altman_wants_to_sell_you_these_sneakers_for/)**

World x Future Basics now offer Cyto XLiftoffs at World’s Union Square eye-collection center

🔗 [sf.gazetteer.co](https://sf.gazetteer.co/sam-altman-wants-to-sell-you-these-sneakers-for-160-plus-tax-and-biometric-data) • 1h ago

---

**[Wright State University leads $2.5 million federal initiative to bring AI education to rural Ohio](https://www.reddit.com/r/artificial/comments/1suire0/wright_state_university_leads_25_million_federal/)**

🔗 [webapp2.wright.edu](https://webapp2.wright.edu/web1/newsroom/2026/04/23/wright-state-university-leads-2-5-million-federal-initiative-to-bring-ai-education-to-rural-ohio/) • 2h ago

---

**[White House Accuses China of Industrial-Scale Theft of AI Technology](https://www.reddit.com/r/artificial/comments/1suj8ne/white_house_accuses_china_of_industrialscale/)**

US News is a recognized leader in college, grad school, hospital, mutual fund, and car rankings. Track elected officials, research health conditions, and find news you can use in politics, business, health, and education.

🔗 [US News & World Report](https://www.usnews.com/news/top-news/articles/2026-04-23/white-house-accuses-china-of-industrial-scale-theft-of-ai-technology-ft-reports) • 1h ago

---

**[Lessons learned building a no-hallucination RAG for Islamic finance similarity gates beat prompt engineering](https://www.reddit.com/r/artificial/comments/1su9q5b/lessons_learned_building_a_nohallucination_rag/)**

Lessons learned building a no-hallucination RAG for Islamic finance similarity gates beat prompt engineering I kept getting blocked trying to share this so I'll cut straight to the technical meat. The problem: Islamic finance rulings vary by jurisdiction and a wrong answer has real consequences. Telling an LLM "refuse if unsure" in a system prompt is not enough. It still speculates. The fix that actually worked: kill the LLM call entirely at retrieval time. If top-k chunks score below 0.7 cosine similarity, the function returns a hardcoded refusal string. The LLM never sees the query. No amount of clever prompting is as reliable as just not calling the model. Other things worth knowing: FAISS on HuggingFace Spaces free tier is ephemeral. Every cold start wipes it. Solution: push the index to a private HF Dataset, pull it on startup via FastAPI lifespan event. PyPDF2 on scanned PDFs returns nothing. AAOIFI documents are scanned images. trafilatura on clean HTML beats OCR every time if a web version exists. Jurisdiction metadata on every chunk is not optional. source_name + source_url + jurisdiction in every chunk. A Malaysian SC ruling and a Gulf fatwa can say opposite things on the same question. Stack: FastAPI + LlamaIndex + FAISS + sentence-transformers + Mistral-Small-3.1-24B via HF Inference API. Netlify Function as proxy so credentials never touch the browser. What threshold do you use for retrieval refusal in high-stakes domains?

9h ago

---

**[A Yale ethicist who has studied AI for 25 years says the real danger isn’t superintelligence. It’s the absence of moral intelligence.](https://www.reddit.com/r/artificial/comments/1stkefq/a_yale_ethicist_who_has_studied_ai_for_25_years/)**

I had the pleasure of sitting down with Wendell Wallach recently. He’s been working in AI ethics since before ChatGPT, before the hype, before most people in tech were paying attention. He wrote Moral Machines, worked alongside Stuart Russell, Yann LeCun and Daniel Kahneman. He’s not a commentator, he’s someone who has sat with these questions for decades. What struck me most in our conversation was his argument about AGI. Not that it’s impossible or inevitable, but that it’s the wrong goal entirely. A system can be extraordinarily intelligent and have zero moral reasoning. We’re building toward capability without asking what it’s capable of deciding. The section on accountability genuinely unsettled me. When AI causes harm, who is actually responsible? He maps out why the answer is almost always nobody in a way that’s hard to argue with. Worth watching if you’re tired of the extremes. Full interview: https://youtu.be/-usWHtI-cms?si=NBkwN-AmIshOXJsX

1d ago

---

**[Open-source AI vs Big Tech: real disruption or just hype?](https://www.reddit.com/r/artificial/comments/1sufa9i/opensource_ai_vs_big_tech_real_disruption_or_just/)**

With companies like DeepSeek releasing powerful models for free, a lot of people are calling this a “game changer.” Some say it could put real pressure on players like OpenAI or Google, especially on pricing. But others argue that infrastructure, scaling, and reliability still give Big Tech a major advantage. So what do you think? Is open-source AI actually disrupting the market… or is this just hype ?

4h ago

---

**[Europe’s markets watchdog warns cyber threats are growing as AI speeds up risks](https://www.reddit.com/r/artificial/comments/1sucdx6/europes_markets_watchdog_warns_cyber_threats_are/)**

🔗 [reuters.com](https://www.reuters.com/world/europes-markets-watchdog-warns-cyber-threats-are-growing-ai-speeds-up-risks-2026-04-24/) • 6h ago

---

**[Switching between AI experiences](https://www.reddit.com/r/artificial/comments/1suhker/switching_between_ai_experiences/)**

I'm wondering how many people here switch between ChatGPT, Claude, and other AI experiences? I've found it really annoying that I can't seamlessly take my personalization with me between them but find each good at various things ... Also when I'm on a site that has an ai driven experience like support or a travel planner I have to reestablish by identity to get a useful output. I've been wondering if a good way to solve this is a centralized identity layer which works with MCP to connect to any agent - here's my stab at starting this: [https://www.mypersonalcontext.com/\](https://www.mypersonalcontext.com/) Would love to know if this problem resonates with others here and how acute it actually is? Could you see yourself using something like this to make model / agent switching easier?

2h ago

---

---

## Google News: "ai"

**[Meta to cut 8,000 jobs, Microsoft offers buyouts to staff as AI spending costs hit Big Tech workers](https://finance.yahoo.com/markets/article/meta-to-cut-8000-jobs-microsoft-offers-buyouts-to-staff-as-ai-spending-costs-hit-big-tech-workers-182722409.html)**

Meta and Microsoft are the latest Big Tech giants to trim staff as AI costs continue to balloon.

Yahoo Finance • 4h ago

---

**[Meta to Lay Off 10 Percent of Work Force in A.I. Push](https://www.nytimes.com/2026/04/23/technology/meta-layoffs.html)**

The layoffs affect about 8,000 employees, with Meta also planning to close 6,000 open roles, as the company focuses on artificial intelligence.

The New York Times • 23h ago

---

**[20,000 job cuts at Meta, Microsoft raise concern that AI-driven labor crisis is here](https://www.cnbc.com/2026/04/24/20k-job-cuts-at-meta-microsoft-raise-concern-of-ai-labor-crisis-.html)**

Meta said it's cutting 10% of its workforce, just as Microsoft announced that it's offering employee buyouts for the first time in its 51-year history.

CNBC • 34m ago

---

**[A secretive AI hacking system has sparked a global scramble](https://www.washingtonpost.com/technology/2026/04/24/anthropic-mythos-ai-washington-cybersecurity-hacking-risk/)**

Anthropic’s Mythos AI is rattling Washington, prompting the Trump administration to try to confront its cybersecurity risks.

The Washington Post • 1h ago

---

**[Anthropic’s New Mythos A.I. Model Sets Off Global Alarms](https://www.nytimes.com/2026/04/22/technology/anthropics-mythos-ai.html)**

The New York Times • 2d ago

---

**[The Guardian view on Anthropic’s Claude Mythos: when AI finds every flaw, who controls the internet? | Editorial](https://www.theguardian.com/commentisfree/2026/apr/23/the-guardian-view-on-anthropics-claude-mythos-when-ai-finds-every-flaw-who-controls-the-internet)**

Editorial: Tech can scale cyber-attacks and defences alike, raising questions about private power, public risk and the future of a shared internet

The Guardian • 16h ago

---

**[Officials hugely underestimated impact of AI datacentres on UK carbon emissions](https://www.theguardian.com/technology/2026/apr/24/officials-hugely-underestimated-impact-of-ai-datacentres-on-uk-carbon-emissions)**

Revised figures increase fears about energy-intensive datacentres worsening climate emergency

The Guardian • 58m ago

---

**[Fox News AI Newsletter: Your next Dairy Queen order could be taken by AI](https://www.foxnews.com/tech/ai-newsletter-next-dairy-queen-order-could-taken-ai)**

Dairy Queen's automated AI drive-thru initiative sparks customer concern as Meta lays off 8,000 workers and voters flag AI risks to privacy and pay.

Fox News • 27m ago

---

**[Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)**

Introducing GPT-5.5, our smartest model yet—faster, more capable, and built for complex tasks like coding, research, and data analysis across tools.

OpenAI • 20h ago

---

**[Ranked: The Smartest AI Models of 2026](https://www.visualcapitalist.com/ranked-the-smartest-ai-models-in-2026/)**

See the smartest AI models in 2026, ranked by Mensa Norway IQ scores from TrackingAI’s benchmark of leading chatbots and vision models.

Visual Capitalist • 3h ago

---

---

## HackerNews: "ai"

**[Meta to start capturing employee mouse movements, keystrokes for AI training](https://news.ycombinator.com/item?id=47851948)**

⬆️ 791 • 💬 523 • 2d ago • [reuters.com](https://www.reuters.com/sustainability/boards-policy-regulation/meta-start-capturing-employee-mouse-movements-keystrokes-ai-training-data-2026-04-21/)

---

**[Tell HN: I'm sick of AI everything](https://news.ycombinator.com/item?id=47857461)**

⬆️ 339 • 💬 192 • 2d ago

---

**[Scoring Show HN submissions for AI design patterns](https://news.ycombinator.com/item?id=47864393)**

An attempt to detect AI design patterns in Show HN pages

⬆️ 330 • 💬 233 • 2d ago • [adriankrebs.ch](https://www.adriankrebs.ch/blog/design-slop/)

---

**[MeshCore development team splits over trademark dispute and AI-generated code](https://news.ycombinator.com/item?id=47878117)**

Migrating to the new meshcore.io site

⬆️ 261 • 💬 143 • 1d ago • [blog.meshcore.io](https://blog.meshcore.io/2026/04/23/the-split)

---

**[South Korea police arrest man for posting AI photo of runaway wolf](https://news.ycombinator.com/item?id=47887683)**

The widely circulated image had prompted authorities to move their search operation.

⬆️ 204 • 💬 129 • 8h ago • [bbc.com](https://www.bbc.com/news/articles/c4gx1n0dl9no)

---

**[Our newsroom AI policy](https://news.ycombinator.com/item?id=47872452)**

How Ars Technica uses, and doesn't use, generative AI.

⬆️ 203 • 💬 129 • 1d ago • [Ars Technica](https://arstechnica.com/staff/2026/04/our-newsroom-ai-policy/)

---

**[Meta employees are up in arms over a mandatory program to train AI on their](https://news.ycombinator.com/item?id=47860961)**

Meta deploys keystroke-tracking software on US employees' computers, sparking privacy concerns and internal backlash.

⬆️ 116 • 💬 90 • 2d ago • [Business Insider](https://www.businessinsider.com/meta-new-ai-tool-tracks-staff-activity-sparks-concern-2026-4)

---

**[Top MAGA influencer revealed to be AI](https://news.ycombinator.com/item?id=47864808)**

According to her profile, she was a registered nurse with Jennifer Lawrence looks who offered red meat posts to lonely conservative men online.

⬆️ 97 • 💬 54 • 2d ago • [New York Post](https://nypost.com/2026/04/21/us-news/top-maga-influencer-emily-hart-revealed-to-be-ai-created-by-a-guy-in-india/)

---

**[Anker made its own chip to bring AI to all its products](https://news.ycombinator.com/item?id=47866368)**

The Thus chip will first be in new earbuds.

⬆️ 67 • 💬 48 • 2d ago • [The Verge](https://www.theverge.com/tech/916463/anker-thus-chip-announcement)

---

**[Do you want the US to "win" AI?](https://news.ycombinator.com/item?id=47873796)**

By all accounts, I should be a neofeudalist. I should love what’s happening. The AI I dreamed of my whole life is being built, engineer-type strongmen are sort of in charge, and people are saying out loud the things I have just thought. You might argue that I like it and I’m just not happy with my seat at the table. I ask myself a lot if this is true, like what if I was Elon. Would I be enjoying it then from that position?

⬆️ 53 • 💬 104 • 1d ago • [the singularity is nearer](https://geohot.github.io//blog/jekyll/update/2026/04/23/us-win-ai.html)

---

---

## YouTube Videos: "ai"

**[Claude 5 – The New AI Era is Here! BYE, CHATGPT...](https://www.youtube.com/watch?v=qT4toLvs3n8)**

sponsored Build with Softr ...

📺 AI Master

👁️ 18K • 👍 353 • 💬 62 • ⏱️ 21:44 • 1d ago

---

**[Microsoft accidentally told the truth about AI](https://www.youtube.com/watch?v=4CIlTOnc6I8)**

Rogue researchers are telling the truth about AI Depth vs breadth: https://x.com/atmoio/status/2041557482217120182 Make ze ...

📺 Mo Bitar

👁️ 290K • 👍 18K • 💬 3K • ⏱️ 9:06 • 1d ago

---

**[I&#39;ve studied AI risk for 20 years. We&#39;re close to a disaster.](https://www.youtube.com/watch?v=fYRmnrDFPes)**

Roman Yampolskiy explains why superintelligence cannot be controlled, why the gap between AI capabilities and AI safety keeps ...

📺 Future of Life Institute

👁️ 11K • 👍 427 • 💬 105 • ⏱️ 19:17 • 1d ago

---

**[Florida Is NOT Ready for the AI Data Center Invasion (Power &amp; Water Crisis Coming)](https://www.youtube.com/watch?v=E7Ia5RIpUls)**

Florida is being over run by data centers! People are worried it will harm their city and way of life! What do you think? If you are ...

📺 Yak Motley

👁️ 15K • 👍 1K • 💬 455 • ⏱️ 17:22 • 1d ago

---

**[I Tried Every FREE AI Video Generator in 2026 (use this)](https://www.youtube.com/watch?v=8RGrKD_HwrQ)**

I compared every Free AI Video Generator, use this Hey Friends :)) I've spent two weeks testing every single free video generator ...

📺 Skai Generated

👁️ 14K • ⏱️ 9:06 • 1d ago

---

**[AI Has Officially Reached &#39;The Point of No Return&#39;…](https://www.youtube.com/watch?v=JxxJi0jMqi0)**

Smalls: Get 60% off your first order + FREE shipping & FREE treats for life at https://smalls.com/ICED Episode Link ...

📺 The Iced Coffee Hour Clips

👁️ 5K • 👍 73 • 💬 30 • ⏱️ 9:25 • 1d ago

---

**[Day 1 of The 2026 AI Advantage Summit](https://www.youtube.com/watch?v=1N2TXfy5FAg)**

📺 Dean Graziosi

👁️ 413K • 👍 13K • 💬 123 • ⏱️ 4:19:20 • 19h ago

---

**[Google Announces Gemini Enterprise Agent Platform: The Future of Agentic AI](https://www.youtube.com/watch?v=3wMwdzxIyN0)**

Google is in its agentic Gemini era. Hear from CEO of Google and Alphabet Sundar Pichai on how Google is customer zero of its ...

📺 Google Cloud

👁️ 140K • 👍 3K • ⏱️ 5:38 • 23h ago

---

**[Reacting To My OWN AI VIDEOS..](https://www.youtube.com/watch?v=T0ZkvbZe9Dw)**

Today I reacted to my own AI videos! Make sure you watch the whole video to find out what happens. Merch: https://foltyn.shop/ ...

📺 Foltyn

👁️ 780K • 👍 28K • 💬 3K • ⏱️ 13:36 • 2d ago

---

**[Fresh Buy Ratings on 2 &#39;Strong Buy&#39; Stocks — AI &amp; Space!](https://www.youtube.com/watch?v=ZXPBqo1AJ2s)**

Wall Street is turning bullish on two high-growth names in AI and space. In this video, we break down the latest fresh buy ratings ...

📺 TipRanks™

👁️ 3K • 👍 216 • 💬 7 • ⏱️ 6:00 • 22h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 30 • ❤️ 2,286 • 7h ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 208,251 • ❤️ 962 • 1d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 162,349 • ❤️ 736 • 14h ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 12,664 • ❤️ 661 • 2d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 861,178 • ❤️ 1,375 • 14h ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 23 • ❤️ 570 • 7h ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 1,397,244 • ❤️ 733 • 4d ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 2,741 • ❤️ 589 • 2d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 340,032 • ❤️ 361 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model based on Qwen3.6-35B-A3B, capable of processing text and images. It features a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context, optimized for lossless generation without refusals, suitable for diverse creative and technical applications.

`image-text-to-text` `34.7B`

⬇️ 388,836 • ❤️ 414 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 76 • 💬 6 • ⭐ 18,487 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 10 • 💬 2 • ⭐ 6,784 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 25 • 💬 1 • ⭐ 21,078 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 18 • 💬 2 • ⭐ 4,417 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 69 • 💬 7 • ⭐ 927 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 49 • 💬 2 • ⭐ 52,699 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 78,010 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,924 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model](https://huggingface.co/papers/2604.20796)**

*Inclusion AI, Tiwei Bie, Haoxing Chen et al. (18 authors)*

🏢 inclusionAI

LLaDA2.0-Uni is a unified discrete diffusion language model that integrates multimodal understanding and generation through a semantic discrete tokenizer, MoE-based backbone, and diffusion decoder, achieving performance comparable to specialized vision-language models while enabling efficient inference and high-fidelity image generation.

▲ 220 • 💬 2 • ⭐ 217 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.20796) • [💻 code](https://github.com/inclusionAI/LLaDA2.0-Uni)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 61,072 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 49.4k • 🔱 6.5k • 4m ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 45.6k • 🔱 2.4k • 6d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 39.1k • 🔱 8.0k • 3d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 34.2k • 🔱 3.8k • 22h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 10.0k • 🔱 2.2k • 2d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 6.0k • 🔱 1.0k • 1d ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 12d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.8k • 🔱 465 • 16d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

`Python`

⭐ 4.3k • 🔱 385 • 4d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 3.9k • 🔱 248 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*
