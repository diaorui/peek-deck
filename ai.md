---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-25T08:53:44.459719+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 25, 2026 at 08:53 UTC  
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

**[Open-source AI system on a $500 GPU outperforms Claude Sonnet on coding benchmarks](https://www.reddit.com/r/artificial/comments/1s2yg3y/opensource_ai_system_on_a_500_gpu_outperforms/)**

What if building more and more datacenters was not the only option? If we are able to get similar levels of performance for top models at a consumer level from smarter systems, then its only a matter of time before the world comes to the realization that AI is a lot less expensive and a whole lot more obtainable. Open source projects like ATLAS are on the frontier of this possibility- where a 22 year old college student from Virginia Tech built and ran a 14B parameter AI model on a single $500 Consumer GPU and scored higher than Claude Sonnet 4.5 on coding benchmarks (74.6% vs 71.4% on LiveCodeBench, 599 problems). No cloud, no API costs, no fine-tuning. Just a consumer graphics card and smart infrastructure around a small model. And the cost? Only around $0.004/task in electricity. The base model used in ATLAS only scores about 55%. The pipeline adds nearly 20 percentage points by generating multiple solution approaches, testing them, and selecting the best one. Proving that smarter infrastructure and systems design is the future of the industry. Repo: https://github.com/itigges22/ATLAS

6h ago

---

**[OpenAI just gave up on Sora and its billion-dollar Disney deal](https://www.reddit.com/r/artificial/comments/1s2s468/openai_just_gave_up_on_sora_and_its_billiondollar/)**

That was quick.

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/899850/openai-sora-ai-chatgpt) • 10h ago

---

**[TurboQuant: Redefining AI efficiency with extreme compression](https://www.reddit.com/r/artificial/comments/1s2y0gy/turboquant_redefining_ai_efficiency_with_extreme/)**

"Vectors are the fundamental way AI models understand and process information. Small vectors describe simple attributes, such as a point in a graph, while “high-dimensional” vectors capture complex information such as the features of an image, the meaning of a word, or the properties of a dataset. High-dimensional vectors are incredibly powerful, but they also consume vast amounts of memory, leading to bottlenecks in the key-value cache, a high-speed "digital cheat sheet" that stores frequently used information under simple labels so a computer can retrieve it instantly without having to search through a slow, massive database. Vector quantization is a powerful, classical data compression technique that reduces the size of high-dimensional vectors. This optimization addresses two critical facets of AI: it enhances vector search, the high-speed technology powering large-scale AI and search engines, by enabling faster similarity lookups; and it helps unclog key-value cache bottlenecks by reducing the size of key-value pairs, which enables faster similarity searches and lowers memory costs. However, traditional vector quantization usually introduces its own "memory overhead” as most methods require calculating and storing (in full precision) quantization constants for every small block of data. This overhead can add 1 or 2 extra bits per number, partially defeating the purpose of vector quantization. Today, we introduce TurboQuant (to be presented at ICLR 2026), a compression algorithm that optimally addresses the challenge of memory overhead in vector quantization. We also present Quantized Johnson-Lindenstrauss (QJL), and PolarQuant (to be presented at AISTATS 2026), which TurboQuant uses to achieve its results. In testing, all three techniques showed great promise for reducing key-value bottlenecks without sacrificing AI model performance. This has potentially profound implications for all compression-reliant use cases, including and especially in the domains of search and AI."

🔗 [research.google](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) • 6h ago

---

**[Claude's computer use changes how I think about AI tooling](https://www.reddit.com/r/artificial/comments/1s3554f/claudes_computer_use_changes_how_i_think_about_ai/)**

I've been watching Claude's computer use announcement settle in, and something clicked for me. This isn't just a feature—it's a shift in how we should be thinking about what AI can do in real workflows. The moment it can navigate your browser, fill spreadsheets, open apps, is the moment you stop thinking about AI as a writing or coding assistant and start thinking about it as something that completes actual work. Not just helps you think through work. Actually does it. What struck me most is how quiet this capability is compared to the hype cycle. No massive marketing push. Just: here's what it does. And people are genuinely shocked when they see it in action—not because it's flashy, but because it actually works on the kinds of tasks that waste time. I think we're at an inflection point where the gap between what people assume AI can do and what it actually does is finally closing. The demos that are circulating aren't polished—they're real. That's the part that matters.

15m ago

---

**[How AI is helping geologists identify thousands of slopes at high risk of slipping](https://www.reddit.com/r/artificial/comments/1s33jxs/how_ai_is_helping_geologists_identify_thousands/)**

Sudden and unexpected, landslides and avalanches claim thousands of lives each year and cause billions of dollars in damage. What if we could see them coming?

🔗 [bbc.com](https://www.bbc.com/future/article/20260323-the-ai-that-warns-people-about-landslides-and-avalanches) • 1h ago

---

**[Three companies shipped "AI agent on your desktop" in the same two weeks. That's not a coincidence.](https://www.reddit.com/r/artificial/comments/1s2ddgb/three_companies_shipped_ai_agent_on_your_desktop/)**

Something interesting happened this month. March 11: Perplexity announced Personal Computer. An always-on Mac Mini running their AI agent 24/7, connected to your local files and apps. Cloud AI does the reasoning, local machine does the access. March 16: Meta launched Manus "My Computer." Same idea. Their agent on your Mac or Windows PC. Reads, edits local files. Launches apps. Multi-step tasks. $20/month. March 23: Anthropic shipped computer use and Dispatch for Claude. Screen control, phone-to-desktop task handoff, 50+ service connectors, scheduled tasks. Three separate companies. Same architecture. Same two weeks. I've been running a version of this pattern for months (custom AI agent on a Mac Mini, iMessage as the interface, background cron jobs, persistent memory across sessions). The convergence on this exact setup tells me the direction is validated. The shared insight all three arrived at: agents need a home. Not a chat window. A machine with file access, app control, phone reachability, and background execution. The gap that remains across all three: persistent memory. Research from January 2026 confirmed what I found building my own system. Fixed context windows limit agent coherence over time. All three products are still mostly session-based. That's the piece that turns a task executor into something that actually feels like a coworker. We went from "will AI agents work on personal computers?" to "which one do you pick?" in about two weeks. Full comparison with hands-on testing: https://thoughts.jock.pl/p/claude-cowork-dispatch-computer-use-honest-agent-review-2026

19h ago

---

**[I built a formal state machine to model how online arguments escalate — IDDS 2.1](https://www.reddit.com/r/artificial/comments/1s2yzgb/i_built_a_formal_state_machine_to_model_how/)**

After getting dogpiled on Reddit (intentionally, for research), I formalized what I observed into a framework called IDDS — Identity-Driven Discourse Systems. The core insight: escalation is not random. It follows predictable state transitions driven by identity layer activation. The key innovation in 2.1 is the D_flag modifier — Identity Activation only accelerates escalation when disagreement is already present. This means someone sharing their identity in a friendly thread (D_flag=0) behaves completely differently from the same disclosure in an adversarial thread (D_flag=1). States: Neutral → Disagreement → Identity Activation → Personalization → Ad Hominem → Dogpile New in 2.1: MPF (Moral Protective Framing): "protecting children" as ethical cover for escalation — invisible to sentiment analysis, requires contextual state awareness Adversarial Seeding: threads born escalated at T=0 before the first reply Silence Bypass: block/mute only terminates the local thread, not the conflict Transient Dogpile Groups: the group never fully resets D_flag between targets Validated across Reddit, Threads, WhatsApp in English and Portuguese. Building a Playwright scraper + ML classifier next. Paper:https://github.com/JohannaWeb/Monarch/releases/tag/2.1.paper

6h ago

---

**[I tested ChatGPT vs Claude vs Gemini for coding ...here's what I found](https://www.reddit.com/r/artificial/comments/1s2ovhc/i_tested_chatgpt_vs_claude_vs_gemini_for_coding/)**

So ive been going back and forth between these three for actual work (not just asking it to write fizzbuzz) and wanted to share what I found because most comparisons online are surface level garbage. Quick background: I do fullstack work, mostly React/Next.js with some Python backend stuff. I gave all three the same tasks over about 3 months of real daily use. Claude is the best for coding and its not even close imo. I had it refactor a 400 line React component into smaller pieces and it actually understood the architecture. kept all my tests passing too. the 200k context window is huge because you can just paste your entire file plus tests and it gets it. one time it even caught a race condition I didnt know was there lol ChatGPT is solid but more of a generalist. Its great for quick questions, debugging, and when you need to explain something to a non technical person. I use it more for brainstorming and writing docs than actual code. the image generation and voice mode are nice bonuses that claude doesnt have Gemini honestly disappointed me the most. it kept struggling with larger context and the code wouldnt compile on first try way too often. Maybe its gotten better since I last used it heavily but I switched away from it for coding pretty quick. its good for google workspace stuff tho if your already in that ecosystem My setup now: Claude for serious coding work, ChatGPT for everything else (research, writing, brainstorming), and honestly Perplexity for when I need to look something up because its way better than both of them for research The thing nobody talks about: all three have gotten noticeably better even in the last few months. like Claude was already good but the latest updates made it scary good at understanding codebases. if you tried one of these 6 months ago and didnt like it, worth trying again happy to answer questions about specific use cases. ive tried them for python, typescript, sql, and some go

12h ago

---

**[I wrote a contract to stop AI from guessing when writing code](https://www.reddit.com/r/artificial/comments/1s2eimz/i_wrote_a_contract_to_stop_ai_from_guessing_when/)**

I’ve been experimenting with something while working with AI on technical problems. The issue I kept running into was drift: answers filling in gaps I didn’t specify solutions collapsing too early “helpful” responses that weren’t actually correct So I wrote a small interaction contract to constrain the AI. Nothing fancy — just rules like: don’t infer missing inputs explicitly mark unknowns don’t collapse the solution space separate facts from assumptions It’s incomplete and a bit rigid, but it’s been surprisingly effective for: writing code debugging thinking through system design It basically turns the AI into something closer to a logic tool than a conversational one. Sharing it in case anyone else wants to experiment with it or tear it apart: https://github.com/Brian-Linden/lgf-ai-contract If you’ve run into similar issues with AI drift, I’d be interested to hear how you’re handling it.

18h ago

---

**[I mapped how Reddit actually talks about AI safety: 6,374 posts, 23 clusters, some surprising patterns](https://www.reddit.com/r/artificial/comments/1s2g23a/i_mapped_how_reddit_actually_talks_about_ai/)**

I collected Reddit posts between Jan 29 - Mar 1, 2026 using 40 keyword-based search terms ("AI safety", "AI alignment", "EU AI Act", "AI replace jobs", "red teaming LLM", etc.) across all subreddits. After filtering, I ended up with 6,374 posts and ran them through a full NLP pipeline. What I built: Sentence embeddings (paraphrase-multilingual-MiniLM-L12-v2) -> 10D UMAP -> HDBSCAN clustering Manual cluster review using structured cluster cards Sentiment analysis per post (RoBERTa classifier) Discourse framing layer - human-first labeling with blind LLM comparison and human adjudication The result: 23 interpretable clusters grouped into 11 thematic families. Three things I found interesting: 1. The discourse is fragmented, not unified. No single cluster dominates - the largest is ~10% of posts. "AI safety discourse" on Reddit looks more like a field of related but distinct conversations: labour anxiety, regulation, lab trust, authenticity & synthetic content, technical safety, enterprise adoption, philosophical debates about personhood. They don't talk to each other that much. 2. The most negative clusters are about lived disruption, not abstract risk. Job replacement, synthetic content spam, broken trust in specific AI labs, AI misuse in schools, creative displacement - these are the most negatively-toned clusters. Enterprise adoption and national AI progress clusters are neutral-to-positive. X-risk and alignment clusters are... mostly neutral, which surprised me. 3. Framing matters as much as topic. Two clusters can both be "about AI and work" while one is macro labour anxiety and another is micro hiring friction - different problems, different policy implications. Topic labels alone don't capture this. Visualizations, full report (PDF), sample data, and code: https://github.com/kelukes/reddit-ai-safety-discourse-2026 Feedback on the pipeline and all is very welcome - this was a capstone project and I'm still learning.

17h ago

---

---

## Google News: "ai"

**[TurboQuant: Redefining AI efficiency with extreme compression](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)**

Research at Google • 12h ago

---

**[OpenAI shutters AI video generator Sora in abrupt announcement](https://www.theguardian.com/technology/2026/mar/24/openai-ai-video-sora)**

App that allowed people to make and share AI videos was popular but received criticism for racist and violent content

The Guardian • 9h ago

---

**[OpenAI ends Disney partnership as it closes Sora video-making app](https://www.bbc.com/news/articles/c3w3e467ewqo)**

The move comes less two years after the launch of the AI video app sent shockwaves through the media industry.

BBC • 4h ago

---

**[Disney Exits OpenAI Deal After AI Giant Shutters Sora](https://www.hollywoodreporter.com/business/digital/openai-shutting-down-sora-ai-video-app-1236546187/)**

The studio giant will no longer move forward with its OpenAI investment, as the AI company exits the video generation business.

The Hollywood Reporter • 11h ago

---

**[Your Defense Code Is Already AI-Generated. Now What?](https://warontherocks.com/2026/03/your-defense-code-is-already-ai-generated-now-what/)**

Somewhere in a defense ministry, someone is drafting a policy on whether to permit AI-assisted software development in defense procurement. The sentiment

War on the Rocks • 51m ago

---

**[Why Every CEO Needs An OpenClaw AI Strategy, Whether They Know It Or Not](https://www.forbes.com/sites/bernardmarr/2026/03/25/why-every-ceo-needs-an-openclaw-ai-strategy-whether-they-know-it-or-not/)**

Forbes • 12m ago

---

**[Anthropic says Claude can now use your computer to finish tasks for you in AI agent push](https://www.cnbc.com/2026/03/24/anthropic-claude-ai-agent-use-computer-finish-tasks.html)**

Anthropic and its rivals are trying to ramp up capabilities of AI agents after OpenClaw went viral earlier this year.

CNBC • 22h ago

---

**[Palantir’s billionaire CEO says only two kinds of people will succeed in the AI era: trade workers — ‘or you’re neurodivergent’](https://fortune.com/2026/03/24/palantir-ceo-alex-karp-two-people-successful-in-ai-era-vocational-skills-neurodivergence-gen-z-career-advice/)**

Billionaire Alex Karp tells Gen Z to skip elite college degrees, as one-fifth of Fortune 500 companies recruit more neurodivergent talent by 2027.

Fortune • 16h ago

---

**[Announcing Arm AGI CPU: The silicon foundation for the agentic AI cloud era](https://newsroom.arm.com/blog/introducing-arm-agi-cpu)**

Arm introduces the Arm AGI CPU to power agentic AI infrastructure with rack-scale performance, efficiency and scalable compute for next-generation data centers.

Arm Newsroom • 15h ago

---

**[Exclusive | Meta Executive Will Spearhead Push to Get Employees Using More AI](https://www.wsj.com/tech/ai/meta-names-new-leader-of-companys-efforts-to-become-ai-native-8d7fe912?gaa_at=eafs&gaa_n=AWEtsqdm5aaWSEeBNlD-_gQMHCfvR0842TTboIXmZa9iHXlrogITVURQn_H1&gaa_ts=69c3a601&gaa_sig=olliW-NXbPuMCz44mMbAxO6b-dQ5n27S7hLZwtoKmCpRB1zsAa76f7faN-j7IdLvMhV7433PeXFg4WcuNIa4Rg%3D%3D)**

WSJ • 15h ago

---

---

## HackerNews: "ai"

**[Is anybody else bored of talking about AI?](https://news.ycombinator.com/item?id=47508745)**

Is anybody else bored of talking about AI?

⬆️ 640 • 💬 435 • 12h ago • [Unfinished Side Projects](https://blog.jakesaunders.dev/is-anybody-else-bored-of-talking-about-ai/)

---

**[So where are all the AI apps?](https://news.ycombinator.com/item?id=47503006)**

Practical AI R&D

⬆️ 394 • 💬 366 • 18h ago • [Answer.AI](https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html)

---

**[I built an AI receptionist for a mechanic shop](https://news.ycombinator.com/item?id=47487536)**

Learn how I built an ai receptionist for my brother's mechanic shop

⬆️ 311 • 💬 319 • 1d ago • [itsthatlady.dev](https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/)

---

**[Flighty Airports](https://news.ycombinator.com/item?id=47511589)**

Search any airport for real-time delays, weather, arrivals, departures, and performance insights powered by Flighty.

⬆️ 301 • 💬 99 • 8h ago • [Flighty](https://flighty.com/airports)

---

**[The bridge to wealth is being pulled up with AI](https://news.ycombinator.com/item?id=47503296)**

For two centuries, the credential system gave intelligence a route to heritable capital. Artificial intelligence is closing that route. This essay builds the argument from first principles - with probability theory, interactive simulations, and a prediction specific enough to be falsifiable - and puts a number on the window that remains.

⬆️ 260 • 💬 380 • 18h ago • [Daniel Homola](https://danielhomola.com/m%20&%20e/ai/your-bridge-to-wealth-is-being-pulled-up/)

---

**[What young workers are doing to AI-proof themselves](https://news.ycombinator.com/item?id=47480447)**

⬆️ 225 • 💬 394 • 2d ago • [wsj.com](https://www.wsj.com/economy/jobs/ai-jobs-young-people-careers-14282284)

---

**[Show HN: Cq – Stack Overflow for AI coding agents](https://news.ycombinator.com/item?id=47491466)**

cq explores a Stack Overflow for agents, a shared commons where agents can query past learnings, contribute new knowledge, and avoid repeating the same mistakes in isolation.

⬆️ 208 • 💬 92 • 1d ago • [Mozilla.ai](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)

---

**[Disney Exits OpenAI Deal After AI Giant Shutters Sora](https://news.ycombinator.com/item?id=47509234)**

The studio giant will no longer move forward with its OpenAI investment, as the AI company exits the video generation business.

⬆️ 201 • 💬 2 • 11h ago • [The Hollywood Reporter](https://www.hollywoodreporter.com/business/digital/openai-shutting-down-sora-ai-video-app-1236546187/)

---

**[Diverse perspectives on AI from Rust contributors and maintainers](https://news.ycombinator.com/item?id=47482825)**

⬆️ 160 • 💬 82 • 2d ago • [nikomatsakis.github.io](https://nikomatsakis.github.io/rust-project-perspectives-on-ai/feb27-summary.html)

---

**[The AI Industry Is Lying to You](https://news.ycombinator.com/item?id=47506259)**

Hi! If you like this piece and want to support my independent reporting and analysis, why not subscribe to my premium newsletter? It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5000 to 18,000 words, including

⬆️ 154 • 💬 123 • 15h ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/)

---

---

## YouTube Videos: "ai"

**[I Asked 4 AIs to PREDICT the 2026 Midterms. Trump&#39;s AI Was INSANE](https://www.youtube.com/watch?v=_MeZ1Kz6cVI)**

Grab your free seat to the 2-Day AI Mastermind: https://link.outskill.com/IASKAIMAR4 100% Discount for the first 1000 people ...

📺 I Ask AI

👁️ 30K • 👍 3K • 💬 251 • ⏱️ 17:22 • 1d ago

---

**[AI Is Making Software Worthless Faster Than Anyone Realizes](https://www.youtube.com/watch?v=wrMrtmfn0MA)**

In this vlog, I make a bold case that AI is destroying the economic moat of the software industry and shifting value away from SaaS, ...

📺 Asian Dad Energy

👁️ 33K • 👍 2K • 💬 638 • ⏱️ 9:25 • 19h ago

---

**[China’s New AI Robots Just Broke The Human Skill Barrier](https://www.youtube.com/watch?v=QDRzgF-8-50)**

This week in robotics got kind of ridiculous. South Korea showed off a humanoid that can run, jump, play soccer, and moonwalk, ...

📺 AI Revolution

👁️ 152K • 👍 2K • 💬 122 • ⏱️ 14:31 • 2d ago

---

**[This Shouldn’t Be Able to Run 120B Locally](https://www.youtube.com/watch?v=RkzCAaIV_cQ)**

I paired a tiny AI box with the MacBook Neo—and it seriously changed what I thought was possible with local AI. Tiiny box: ...

📺 Alex Ziskind

👁️ 198K • 👍 6K • 💬 647 • ⏱️ 12:13 • 1d ago

---

**[98% of People Will Miss This New AI Opportunity](https://www.youtube.com/watch?v=YNnCSJ3Fc_Q)**

Get Started with Manus today: https://manus.im/redeem?c=JWH1G26A Prompts I used in this video: PROMPT #1 I want to create ...

📺 Journey With The Hintons

👁️ 30K • 👍 3K • 💬 384 • ⏱️ 12:49 • 2d ago

---

**[I Asked AI To Predict The 2028 Election... JAW-DROPPING Results!](https://www.youtube.com/watch?v=zo7Nr9jtDds)**

Grab your free seat to the 2-Day AI Mastermind: https://link.outskill.com/ELECTIONTIMEMAR4 100% Discount for the first 1000 ...

📺 Election Time

👁️ 100K • 👍 2K • 💬 630 • ⏱️ 16:50 • 1d ago

---

**[Perplexity&#39;s NEW Computer Just DESTROYED Every AI Tool You&#39;re Paying For](https://www.youtube.com/watch?v=H3ITnJhb8bA)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://link.stayingahead.ai/YT9 I ...

📺 Vaibhav Sisinty

👁️ 31K • 👍 960 • 💬 48 • ⏱️ 10:52 • 17h ago

---

**[DeepSeek Just Fixed One Of The Biggest Problems With AI](https://www.youtube.com/watch?v=DmtoVnTkQnM)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The #DeepSeek paper is available here: ...

📺 Two Minute Papers

👁️ 67K • 👍 4K • 💬 304 • ⏱️ 9:47 • 17h ago

---

**[Cops Use AI, Arrest the Wrong Guy](https://www.youtube.com/watch?v=kAEdH1YXB8I)**

Imagine you go into a business and their AI surveillance camera thinks it recognizes you as a trespasser. So that business ...

📺 The Civil Rights Lawyer

👁️ 298K • 👍 15K • 💬 2K • ⏱️ 2:37 • 1d ago

---

**[Legit $75/hr Remote AI Work? I Found This! (Handshake AI Review)](https://www.youtube.com/watch?v=WVf6wJqOjd8)**

This Handshake AI review will give you an inside look and show if you can really get paid up to $75 per hour to train AI. Or is it a ...

📺 PaidFromSurveys

👁️ 3K • 👍 158 • 💬 34 • ⏱️ 9:42 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 401,358 • ❤️ 913 • 14d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 173,865 • ❤️ 1,219 • 1d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 10,499 • ❤️ 342 • 5d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 38,586 • ❤️ 269 • 10h ago

---

**[Foundation-1](https://huggingface.co/RoyalCities/Foundation-1)**

*Royal Cities*

Foundation-1 is a structured text-to-sample model for music production, enabling precise control over instrumentation, timbre, FX, and musical structure (tempo, key, bar count) for generating coherent, production-ready audio loops.

⬇️ 0 • ❤️ 256 • 8d ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 14,617 • ❤️ 731 • 13d ago

---

**[Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2 is a fine-tuned LLM optimized for efficient chain-of-thought reasoning, delivering higher accuracy with reduced token usage. It excels in resource-constrained environments and agentic workflows by providing faster, more economical reasoning.

`image-text-to-text` `9.0B`

⬇️ 55,120 • ❤️ 131 • 1d ago

---

**[daVinci-MagiHuman](https://huggingface.co/GAIR/daVinci-MagiHuman)**

*SII - GAIR*

daVinci-MagiHuman is a fast, single-stream Transformer model for generating high-quality, human-centric audio-video from text or images. It excels at expressive facial performance, natural speech-expression coordination, and accurate audio-video synchronization across multiple languages, with inference speeds of 2 seconds for 256p and 38 seconds for 1080p.

`image-to-video`

⬇️ 150 • ❤️ 121 • 3h ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 418,903 • ❤️ 644 • 21d ago

---

**[Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)**

*Mistral AI_*

Mistral-Small-4-119B-2603 is a hybrid MoE model (119B params, 6.5B active) supporting 256k context and multimodal input (text/image). It excels at instruction following, reasoning (configurable effort), and agentic tasks with native function calling, offering significant speed and throughput improvements for use cases like coding, document analysis, and general assistants.

`119.4B`

⬇️ 38,985 • ❤️ 324 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 29 • 💬 2 • ⭐ 41,256 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 14 • 💬 1 • ⭐ 13,415 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 28 • 💬 5 • ⭐ 673 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 3 • 💬 0 • ⭐ 620 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://huggingface.co/papers/2603.21986)**

*SII-GAIR, Sand. ai, Ethan Chern et al. (45 authors)*

daVinci-MagiHuman is an open-source audio-video generative model that synchronizes text, video, and audio through a single-stream Transformer architecture, achieving high-quality human-centric content generation with efficient inference capabilities.

▲ 92 • 💬 4 • ⭐ 391 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2603.21986) • [💻 code](https://github.com/GAIR-NLP/daVinci-MagiHuman) • [🔗 project](https://huggingface.co/spaces/SII-GAIR/daVinci-MagiHuman)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 194 • 💬 5 • ⭐ 8,154 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 32 • 💬 2 • ⭐ 30,472 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[Attention Residuals](https://huggingface.co/papers/2603.15031)**

*Kimi Team, Guangyu Chen, Yu Zhang et al. (37 authors)*

🏢 Moonshot AI

Residual connections with PreNorm are standard in modern LLMs, yet they accumulate all layer outputs with fixed unit weights. This uniform aggregation causes uncontrolled hidden-state growth with depth, progressively diluting each layer's contribution. We propose Attention Residuals (AttnRes), which replaces this fixed accumulation with softmax attention over preceding layer outputs, allowing each layer to selectively aggregate earlier representations with learned, input-dependent weights. To address the memory and communication overhead of attending over all preceding layer outputs for large-scale model training, we introduce Block AttnRes, which partitions layers into blocks and attends over block-level representations, reducing the memory footprint while preserving most of the gains of full AttnRes. Combined with cache-based pipeline communication and a two-phase computation strategy, Block AttnRes becomes a practical drop-in replacement for standard residual connections with minimal overhead.
  Scaling law experiments confirm that the improvement is consistent across model sizes, and ablations validate the benefit of content-dependent depth-wise selection. We further integrate AttnRes into the Kimi Linear architecture (48B total / 3B activated parameters) and pre-train on 1.4T tokens, where AttnRes mitigates PreNorm dilution, yielding more uniform output magnitudes and gradient distribution across depth, and improves downstream performance across all evaluated tasks.

▲ 157 • 💬 4 • ⭐ 2,673 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15031) • [💻 code](https://github.com/MoonshotAI/Attention-Residuals)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 17 • 💬 0 • ⭐ 36,503 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 59 • 💬 4 • ⭐ 18,977 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 54.9k • 🔱 7.6k • 4d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 22.4k • 🔱 1.1k • 3h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 13.2k • 🔱 1.7k • 2h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 11.6k • 🔱 599 • 14h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 10.7k • 🔱 779 • 1d ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 6.7k • 🔱 1.0k • 3d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 6.4k • 🔱 518 • 1h ago

---

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)**

734+ structured cybersecurity skills for AI agents · MITRE ATT&CK mapped · agentskills.io open standard · Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI & 20+ platforms · Penetration testing, DFIR, threat intel, cloud security & more · Apache 2.0

`Python` `ai-agents` `claude` `claude-code` `cloud-security` `cybersecurity`

⭐ 3.7k • 🔱 372 • 1d ago

---

**[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)**

OpenShell is the safe, private runtime for autonomous AI agents.

`Rust`

⭐ 3.7k • 🔱 361 • 2h ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.2k • 🔱 213 • 11d ago

---

---

*Generated by PeekDeck - A glance is all you need*
