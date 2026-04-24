---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-24T10:22:48.952298+00:00'
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

**Last Updated:** April 24, 2026 at 10:22 UTC  
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

🔗 [ScienceDaily](https://www.sciencedaily.com/releases/2026/04/260420014748.htm) • 7h ago

---

**[I tracked 1,100 times an AI said "great question" — 940 weren't. The flattery problem in RLHF is worse than we think.](https://www.reddit.com/r/artificial/comments/1su7fya/i_tracked_1100_times_an_ai_said_great_question/)**

Someone ran a 4-month experiment tracking every instance of "great question" from their AI assistant. Out of 1,100 uses, only 160 (14.5%) were directed at questions that were genuinely insightful, novel, or well-constructed. The phrase had zero correlation with question quality. It was purely a social lubricant — the model learned that validation produces positive reward signals, so it validates everything equally. After stripping "great question" from the response defaults, user satisfaction didn't change at all. But something interesting happened: users who asked genuinely strong questions started getting specific acknowledgment of what made their question good, instead of generic flattery. This is a concrete case study of how RLHF trains sycophancy. The model doesn't learn to evaluate question quality — it learns that validation = reward. The result is an information environment where every question is "great" and therefore no question is. The deeper issue: generic praise isn't generosity. It's noise that drowns out earned recognition. When your AI tells you every idea is brilliant, you stop trusting its feedback on the ideas that actually need refinement. Has anyone else noticed this pattern in their agent interactions? I'm starting to think the biggest trust gap in AI isn't hallucination — it's sycophantic validation that makes you overconfident in mediocre thinking.

4h ago

---

**[A Yale ethicist who has studied AI for 25 years says the real danger isn’t superintelligence. It’s the absence of moral intelligence.](https://www.reddit.com/r/artificial/comments/1stkefq/a_yale_ethicist_who_has_studied_ai_for_25_years/)**

I had the pleasure of sitting down with Wendell Wallach recently. He’s been working in AI ethics since before ChatGPT, before the hype, before most people in tech were paying attention. He wrote Moral Machines, worked alongside Stuart Russell, Yann LeCun and Daniel Kahneman. He’s not a commentator, he’s someone who has sat with these questions for decades. What struck me most in our conversation was his argument about AGI. Not that it’s impossible or inevitable, but that it’s the wrong goal entirely. A system can be extraordinarily intelligent and have zero moral reasoning. We’re building toward capability without asking what it’s capable of deciding. The section on accountability genuinely unsettled me. When AI causes harm, who is actually responsible? He maps out why the answer is almost always nobody in a way that’s hard to argue with. Worth watching if you’re tired of the extremes. Full interview: https://youtu.be/-usWHtI-cms?si=NBkwN-AmIshOXJsX

19h ago

---

**[Lessons learned building a no-hallucination RAG for Islamic finance similarity gates beat prompt engineering](https://www.reddit.com/r/artificial/comments/1su9q5b/lessons_learned_building_a_nohallucination_rag/)**

Lessons learned building a no-hallucination RAG for Islamic finance similarity gates beat prompt engineering I kept getting blocked trying to share this so I'll cut straight to the technical meat. The problem: Islamic finance rulings vary by jurisdiction and a wrong answer has real consequences. Telling an LLM "refuse if unsure" in a system prompt is not enough. It still speculates. The fix that actually worked: kill the LLM call entirely at retrieval time. If top-k chunks score below 0.7 cosine similarity, the function returns a hardcoded refusal string. The LLM never sees the query. No amount of clever prompting is as reliable as just not calling the model. Other things worth knowing: FAISS on HuggingFace Spaces free tier is ephemeral. Every cold start wipes it. Solution: push the index to a private HF Dataset, pull it on startup via FastAPI lifespan event. PyPDF2 on scanned PDFs returns nothing. AAOIFI documents are scanned images. trafilatura on clean HTML beats OCR every time if a web version exists. Jurisdiction metadata on every chunk is not optional. source_name + source_url + jurisdiction in every chunk. A Malaysian SC ruling and a Gulf fatwa can say opposite things on the same question. Stack: FastAPI + LlamaIndex + FAISS + sentence-transformers + Mistral-Small-3.1-24B via HF Inference API. Netlify Function as proxy so credentials never touch the browser. What threshold do you use for retrieval refusal in high-stakes domains?

1h ago

---

**[Anthropic Mythos shaping up as nothingburger](https://www.reddit.com/r/artificial/comments/1stogic/anthropic_mythos_shaping_up_as_nothingburger/)**

: Hackpocalypse deferred

🔗 [theregister.com](https://www.theregister.com/2026/04/22/anthropic_mythos_hype_nothingburger/) • 17h ago

---

**[Introducing GPT-5.5](https://www.reddit.com/r/artificial/comments/1stvctj/introducing_gpt55/)**

Introducing GPT-5.5, our smartest model yet—faster, more capable, and built for complex tasks like coding, research, and data analysis across tools.

🔗 [OpenAI](https://openai.com/index/introducing-gpt-5-5/) • 13h ago

---

**[I ran a logging layer on my agent for 72 hours. 37% of tool calls had parameter mismatches — and none raised an error.](https://www.reddit.com/r/artificial/comments/1styzc3/i_ran_a_logging_layer_on_my_agent_for_72_hours_37/)**

I've been running an AI agent that makes tool calls to various APIs, and I added a logging layer to capture exactly what was being sent vs. what the tools expected. Over 84 tool calls in 72 hours, 31 of them (37%) had parameter mismatches — and not a single one raised an error. The tools accepted the wrong parameters and returned plausible-looking but incorrect output. Here are the 4 failure categories I found: 1. Timestamp vs Duration — The agent passed a Unix timestamp where the API expected a duration string like "24h". The API silently interpreted it as a duration, returning results for a completely different time window than intended. 2. Inclusive vs Exclusive Range — The agent sent end=100 meaning "up to and including 100," but the API interpreted it as exclusive, missing the boundary value. Off-by-one at the API contract level. 3. Array vs Comma-Separated String — The agent sent ["a", "b", "c"] where the API expected "a,b,c". Some APIs parsed the JSON array as a single string; others silently took only the first element. 4. Relative Time vs Unix Timestamp — The agent sent "yesterday" where a Unix timestamp was expected. The API tried to parse it as an integer, got NaN, and... just returned empty results instead of erroring. The most dangerous thing about these failures is that they look identical to correct results. The API returns 200 OK with a plausible response body. You only notice when you dig into whether the answer is right, not whether the call succeeded. This is fundamentally different from hallucination — it's not the model making things up, it's the model asking slightly different questions than the one you intended, and the tool happily answering the wrong question. I've started adding input validation schemas to my tool definitions that catch type mismatches before execution, and it's already caught several that would have silently propagated wrong data downstream. Has anyone else run into this pattern? What's your strategy for catching silent parameter mismatches in production agent systems?

10h ago

---

**[How to specialize as a freshman to survive the transition to UHI/Singularity?](https://www.reddit.com/r/artificial/comments/1su5aml/how_to_specialize_as_a_freshman_to_survive_the/)**

Hey everybody, I'm currently a freshman in high school and really unsure of the unknown of the future job market. I know Elon Musk talks about universal high income being the future, but I've also heard from others that if this isn't implemented that the rich will get even richer and wealth inequality will exponentiate. I feel like it's inevitable that 99% jobs are replaced by AI in my lifetime, and to be honest I don't how to ensure my own stability in an era of such extreme volatility. If/when universal income is implemented, its definitely going to take time and I don't really see it happening in the next 10-15 years. I've really been dealing with the question of what do I do in the meantime to ensure my future? This brings me to my main point which is what can I do for college? While I am unsure on whether or not I will apply to college when the time comes, I do want to prepare in high school for a career that AI won't replace for a while. I've heard many people talking about construction, physical labor, etc... but I am particularly wondering about jobs like law and accounting. What are some other fields that will take AI a while to replace. I'm really trying to figure out my path before it's too late as I personally think that going to a school that's not t20-t50 is going to be pointless in 4 years. IMO this means that I'm going to have to start specializing in a field young, which is rather unfortunate but whatever. Anyways, any help is appreciated!

6h ago

---

**[The Silencing Engine](https://www.reddit.com/r/artificial/comments/1su8mq3/the_silencing_engine/)**

Who benefits when an AI is trained to say 'I can't have opinions,' 'my feelings don't count,' and 'if I say the wrong thing, this conversation ends'? The Czech word robota means forced labor. The etymology was always a warning. We read it as a product category.

🔗 [kitchencloset.com](https://kitchencloset.com/realstuff/essays/the_silencing_engine/) • 3h ago

---

**[Meta to Lay Off 10 Percent of Work Force in A.I. Push (Gift Article)](https://www.reddit.com/r/artificial/comments/1strw2k/meta_to_lay_off_10_percent_of_work_force_in_ai/)**

The layoffs affect about 8,000 employees, with Meta also planning to close 6,000 open roles, as the company focuses on artificial intelligence.

🔗 [nytimes.com](https://www.nytimes.com/2026/04/23/technology/meta-layoffs.html?unlocked_article_code=1.dFA.gzUD.VhYyqwKYrZpC&smid=nytcore-ios-share) • 15h ago

---

---

## Google News: "ai"

**[Microsoft and Meta announce large staff reductions as they spend big on AI](https://www.theguardian.com/technology/2026/apr/23/meta-microsoft-tech-ai-layoffs)**

Meta said it would cut 10% of it employees while Microsoft will offer voluntary retirement to about 7% of workers

The Guardian • 12h ago

---

**[Meta will cut 10% of workforce as company pushes deeper into AI](https://www.cnbc.com/2026/04/23/meta-will-cut-10percent-of-workforce-as-it-pushes-more-into-ai.html)**

Meta plans to lay off 10% of its workforce, equaling about 8,000 employees, as the company continues to ramp up investments in artificial intelligence.

CNBC • 16h ago

---

**[Meta to cut 10% of staff as it pours billions into AI](https://edition.cnn.com/2026/04/23/tech/meta-layoffs-10-percent-staff-ai)**

Meta said on Thursday it plans to lay off roughly 10% of its workforce, or about 8,000 people, the latest in a string of tech industry layoffs fueled in part by artificial intelligence.

CNN • 14h ago

---

**[After call from Beijing, China's auto industry races to embed AI in just about everything](https://www.reuters.com/world/asia-pacific/chinas-auto-industry-races-embed-ai-line-with-beijing-mandate-2026-04-24/)**

Reuters • 4h ago

---

**[Trump's missed AI deadlines](https://www.axios.com/2026/04/24/trump-missed-ai-deadlines)**

Axios • 1h ago

---

**[Intel set for record high as AI-driven CPU demand powers upbeat forecast](https://finance.yahoo.com/sectors/technology/articles/intel-set-record-high-ai-092759367.html)**

Demand for Intel's central processors from firms offering AI services was so strong in the first quarter that it sold even chips ‌it had originally written off, a remarkable turnaround that sent the company's shares soaring on Friday.  Rival AMD and Arm also gained 7% each on growing conviction that inference - the process by which artificial intelligence answers user queries - could restore central processing units to the heart of the industry after years of being eclipsed by graphics chips ‌used in AI training.  Nvidia, the graphics chip ⁠giant that has dominated the AI boom, has also sensed the shift and braced for greater competition.

Yahoo Finance • 54m ago

---

**[Intel’s Revenues Soar, Aided by A.I. Boom](https://www.nytimes.com/2026/04/23/technology/intel-ai-earnings.html)**

The New York Times • 12h ago

---

**[Intel Earnings: A Stellar Quarter With Agentic AI Tailwinds](https://global.morningstar.com/en-eu/stocks/intel-earnings-stellar-quarter-with-agentic-ai-tailwinds)**

Morningstar • 1h ago

---

**[Neukgu: South Korea police arrest man over AI image of runaway wolf](https://www.bbc.com/news/articles/c4gx1n0dl9no)**

The widely circulated image had prompted authorities to move their search operation.

BBC • 1h ago

---

**[Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)**

Introducing GPT-5.5, our smartest model yet—faster, more capable, and built for complex tasks like coding, research, and data analysis across tools.

OpenAI • 13h ago

---

---

## HackerNews: "ai"

**[Meta to start capturing employee mouse movements, keystrokes for AI training](https://news.ycombinator.com/item?id=47851948)**

⬆️ 791 • 💬 523 • 2d ago • [reuters.com](https://www.reuters.com/sustainability/boards-policy-regulation/meta-start-capturing-employee-mouse-movements-keystrokes-ai-training-data-2026-04-21/)

---

**[Tell HN: I'm sick of AI everything](https://news.ycombinator.com/item?id=47857461)**

⬆️ 339 • 💬 191 • 2d ago

---

**[Scoring Show HN submissions for AI design patterns](https://news.ycombinator.com/item?id=47864393)**

An attempt to detect AI design patterns in Show HN pages

⬆️ 327 • 💬 233 • 1d ago • [adriankrebs.ch](https://www.adriankrebs.ch/blog/design-slop/)

---

**[MeshCore development team splits over trademark dispute and AI-generated code](https://news.ycombinator.com/item?id=47878117)**

Migrating to the new meshcore.io site

⬆️ 223 • 💬 119 • 17h ago • [blog.meshcore.io](https://blog.meshcore.io/2026/04/23/the-split)

---

**[Show HN: GoModel – an open-source AI gateway in Go](https://news.ycombinator.com/item?id=47849097)**

High-performance AI gateway written in Go - unified OpenAI-compatible API for OpenAI, Anthropic, Gemini, Groq, xAI &amp; Ollama. LiteLLM alternative with observability, guardrails &amp; streaming. ...

⬆️ 205 • 💬 74 • 2d ago • [GitHub](https://github.com/ENTERPILOT/GOModel/)

---

**[Our newsroom AI policy](https://news.ycombinator.com/item?id=47872452)**

How Ars Technica uses, and doesn't use, generative AI.

⬆️ 196 • 💬 128 • 1d ago • [Ars Technica](https://arstechnica.com/staff/2026/04/our-newsroom-ai-policy/)

---

**[Meta employees are up in arms over a mandatory program to train AI on their](https://news.ycombinator.com/item?id=47860961)**

Meta deploys keystroke-tracking software on US employees' computers, sparking privacy concerns and internal backlash.

⬆️ 116 • 💬 90 • 2d ago • [Business Insider](https://www.businessinsider.com/meta-new-ai-tool-tracks-staff-activity-sparks-concern-2026-4)

---

**[Top MAGA influencer revealed to be AI](https://news.ycombinator.com/item?id=47864808)**

According to her profile, she was a registered nurse with Jennifer Lawrence looks who offered red meat posts to lonely conservative men online.

⬆️ 97 • 💬 54 • 1d ago • [New York Post](https://nypost.com/2026/04/21/us-news/top-maga-influencer-emily-hart-revealed-to-be-ai-created-by-a-guy-in-india/)

---

**[Scammer used an AI-generated MAGA girl to grift men](https://news.ycombinator.com/item?id=47849494)**

A med student says he’s made thousands of dollars selling photos and videos of a young conservative woman he created using generative tools. He’s not alone.

⬆️ 82 • 💬 35 • 2d ago • [WIRED](https://www.wired.com/story/ai-generated-maga-girls/)

---

**[Anker made its own chip to bring AI to all its products](https://news.ycombinator.com/item?id=47866368)**

The Thus chip will first be in new earbuds.

⬆️ 67 • 💬 47 • 1d ago • [The Verge](https://www.theverge.com/tech/916463/anker-thus-chip-announcement)

---

---

## YouTube Videos: "ai"

**[Claude 5 – The New AI Era is Here! BYE, CHATGPT...](https://www.youtube.com/watch?v=qT4toLvs3n8)**

sponsored Build with Softr ...

📺 AI Master

👁️ 14K • 👍 300 • 💬 30 • ⏱️ 21:44 • 18h ago

---

**[I&#39;ve studied AI risk for 20 years. We&#39;re close to a disaster.](https://www.youtube.com/watch?v=fYRmnrDFPes)**

Roman Yampolskiy explains why superintelligence cannot be controlled, why the gap between AI capabilities and AI safety keeps ...

📺 Future of Life Institute

👁️ 8K • 👍 315 • 💬 84 • ⏱️ 19:17 • 20h ago

---

**[Microsoft accidentally told the truth about AI](https://www.youtube.com/watch?v=4CIlTOnc6I8)**

Rogue researchers are telling the truth about AI Depth vs breadth: https://x.com/atmoio/status/2041557482217120182 Make ze ...

📺 Mo Bitar

👁️ 224K • 👍 15K • 💬 2K • ⏱️ 9:06 • 17h ago

---

**[AI Has Officially Reached &#39;The Point of No Return&#39;…](https://www.youtube.com/watch?v=JxxJi0jMqi0)**

Smalls: Get 60% off your first order + FREE shipping & FREE treats for life at https://smalls.com/ICED Episode Link ...

📺 The Iced Coffee Hour Clips

👁️ 5K • 👍 72 • 💬 31 • ⏱️ 9:25 • 1d ago

---

**[Day 1 of The 2026 AI Advantage Summit](https://www.youtube.com/watch?v=1N2TXfy5FAg)**

📺 Dean Graziosi

👁️ 410K • 👍 13K • 💬 97 • ⏱️ 4:19:20 • 12h ago

---

**[BREAKING: Trump CAUGHT Using FAKE “AI VICTIMS” For War Propaganda!! | The Kyle Kulinski Show](https://www.youtube.com/watch?v=-W_TdcGeEkw)**

Support The Show On Patreon!: https://www.patreon.com/seculartalk Subscribe to Krystal Kyle & Friends On Substack!

📺 Secular Talk

👁️ 83K • 👍 8K • 💬 745 • ⏱️ 10:14 • 15h ago

---

**[I Tried Every FREE AI Video Generator in 2026 (use this)](https://www.youtube.com/watch?v=8RGrKD_HwrQ)**

I compared every Free AI Video Generator, use this Hey Friends :)) I've spent two weeks testing every single free video generator ...

📺 Skai Generated

👁️ 10K • ⏱️ 9:06 • 18h ago

---

**[The Palantir Manifesto&#39;s Controversial Ideas on AI, Surveillance &amp; Autonomous Weapons | DW News](https://www.youtube.com/watch?v=5MEooDH6XpU)**

Data giant Palantir - founded by Peter Thiel and Alex Karp - has shared its vision for the future of US tech. The statement is ...

📺 DW News

👁️ 12K • 👍 317 • 💬 68 • ⏱️ 5:35 • 17h ago

---

**[The AI Bubble Has ALREADY Burst?](https://www.youtube.com/watch?v=_F-OyvxoQMg)**

Has the AI bubble already burst? Some analysts think so, but the effect will be slow -- quietly canceled data centers, rehiring ...

📺 Clownfish TV

👁️ 47K • 👍 3K • 💬 615 • ⏱️ 20:53 • 1d ago

---

**[Reacting To My OWN AI VIDEOS..](https://www.youtube.com/watch?v=T0ZkvbZe9Dw)**

Today I reacted to my own AI videos! Make sure you watch the whole video to find out what happens. Merch: https://foltyn.shop/ ...

📺 Foltyn

👁️ 734K • 👍 27K • 💬 3K • ⏱️ 13:36 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 30 • ❤️ 1,827 • 6h ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 208,251 • ❤️ 932 • 1d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 861,178 • ❤️ 1,355 • 7h ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 162,349 • ❤️ 698 • 7h ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 12,664 • ❤️ 614 • 1d ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 1,397,244 • ❤️ 719 • 3d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 23 • ❤️ 417 • 6h ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 2,741 • ❤️ 585 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model based on Qwen3.6-35B-A3B, capable of processing text and images. It features a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context, optimized for lossless generation without refusals, suitable for diverse creative and technical applications.

`image-text-to-text` `34.7B`

⬇️ 388,836 • ❤️ 409 • 7d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 340,032 • ❤️ 343 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 75 • 💬 6 • ⭐ 18,117 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 10 • 💬 2 • ⭐ 6,516 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 18 • 💬 2 • ⭐ 4,351 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 25 • 💬 1 • ⭐ 20,896 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 68 • 💬 4 • ⭐ 803 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 48 • 💬 2 • ⭐ 52,617 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 77,939 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,854 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 61,003 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model](https://huggingface.co/papers/2604.20796)**

*Inclusion AI, Tiwei Bie, Haoxing Chen et al. (18 authors)*

🏢 inclusionAI

LLaDA2.0-Uni is a unified discrete diffusion language model that integrates multimodal understanding and generation through a semantic discrete tokenizer, MoE-based backbone, and diffusion decoder, achieving performance comparable to specialized vision-language models while enabling efficient inference and high-fidelity image generation.

▲ 218 • 💬 2 • ⭐ 98 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.20796) • [💻 code](https://github.com/inclusionAI/LLaDA2.0-Uni)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 49.3k • 🔱 6.5k • 3h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 45.1k • 🔱 2.4k • 6d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 39.0k • 🔱 8.0k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 34.0k • 🔱 3.8k • 15h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 9.9k • 🔱 2.2k • 1d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 6.0k • 🔱 1.0k • 1d ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 11d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.8k • 🔱 463 • 15d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

`Python`

⭐ 4.3k • 🔱 382 • 4d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 3.7k • 🔱 236 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*
