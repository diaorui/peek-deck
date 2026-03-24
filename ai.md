---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-24T22:00:42.892435+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 24, 2026 at 22:00 UTC  
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

**[Three companies shipped "AI agent on your desktop" in the same two weeks. That's not a coincidence.](https://www.reddit.com/r/artificial/comments/1s2ddgb/three_companies_shipped_ai_agent_on_your_desktop/)**

Something interesting happened this month. March 11: Perplexity announced Personal Computer. An always-on Mac Mini running their AI agent 24/7, connected to your local files and apps. Cloud AI does the reasoning, local machine does the access. March 16: Meta launched Manus "My Computer." Same idea. Their agent on your Mac or Windows PC. Reads, edits local files. Launches apps. Multi-step tasks. $20/month. March 23: Anthropic shipped computer use and Dispatch for Claude. Screen control, phone-to-desktop task handoff, 50+ service connectors, scheduled tasks. Three separate companies. Same architecture. Same two weeks. I've been running a version of this pattern for months (custom AI agent on a Mac Mini, iMessage as the interface, background cron jobs, persistent memory across sessions). The convergence on this exact setup tells me the direction is validated. The shared insight all three arrived at: agents need a home. Not a chat window. A machine with file access, app control, phone reachability, and background execution. The gap that remains across all three: persistent memory. Research from January 2026 confirmed what I found building my own system. Fixed context windows limit agent coherence over time. All three products are still mostly session-based. That's the piece that turns a task executor into something that actually feels like a coworker. We went from "will AI agents work on personal computers?" to "which one do you pick?" in about two weeks. Full comparison with hands-on testing: https://thoughts.jock.pl/p/claude-cowork-dispatch-computer-use-honest-agent-review-2026

8h ago

---

**[I tested ChatGPT vs Claude vs Gemini for coding ...here's what I found](https://www.reddit.com/r/artificial/comments/1s2ovhc/i_tested_chatgpt_vs_claude_vs_gemini_for_coding/)**

So ive been going back and forth between these three for actual work (not just asking it to write fizzbuzz) and wanted to share what I found because most comparisons online are surface level garbage. Quick background: I do fullstack work, mostly React/Next.js with some Python backend stuff. I gave all three the same tasks over about 3 months of real daily use. Claude is the best for coding and its not even close imo. I had it refactor a 400 line React component into smaller pieces and it actually understood the architecture. kept all my tests passing too. the 200k context window is huge because you can just paste your entire file plus tests and it gets it. one time it even caught a race condition I didnt know was there lol ChatGPT is solid but more of a generalist. Its great for quick questions, debugging, and when you need to explain something to a non technical person. I use it more for brainstorming and writing docs than actual code. the image generation and voice mode are nice bonuses that claude doesnt have Gemini honestly disappointed me the most. it kept struggling with larger context and the code wouldnt compile on first try way too often. Maybe its gotten better since I last used it heavily but I switched away from it for coding pretty quick. its good for google workspace stuff tho if your already in that ecosystem My setup now: Claude for serious coding work, ChatGPT for everything else (research, writing, brainstorming), and honestly Perplexity for when I need to look something up because its way better than both of them for research The thing nobody talks about: all three have gotten noticeably better even in the last few months. like Claude was already good but the latest updates made it scary good at understanding codebases. if you tried one of these 6 months ago and didnt like it, worth trying again happy to answer questions about specific use cases. ive tried them for python, typescript, sql, and some go

1h ago

---

**[I wrote a contract to stop AI from guessing when writing code](https://www.reddit.com/r/artificial/comments/1s2eimz/i_wrote_a_contract_to_stop_ai_from_guessing_when/)**

I’ve been experimenting with something while working with AI on technical problems. The issue I kept running into was drift: answers filling in gaps I didn’t specify solutions collapsing too early “helpful” responses that weren’t actually correct So I wrote a small interaction contract to constrain the AI. Nothing fancy — just rules like: don’t infer missing inputs explicitly mark unknowns don’t collapse the solution space separate facts from assumptions It’s incomplete and a bit rigid, but it’s been surprisingly effective for: writing code debugging thinking through system design It basically turns the AI into something closer to a logic tool than a conversational one. Sharing it in case anyone else wants to experiment with it or tear it apart: https://github.com/Brian-Linden/lgf-ai-contract If you’ve run into similar issues with AI drift, I’d be interested to hear how you’re handling it.

8h ago

---

**[I used an app to analyze 3 years of my Claude conversations. It identified a behavioral pattern I'd never named.](https://www.reddit.com/r/artificial/comments/1s2oet4/i_used_an_app_to_analyze_3_years_of_my_claude/)**

Exported everything. Normalized it. Ran cross-source analysis against my journal entries, calendar, and sleep data. The output I couldn't stop thinking about: "Your meticulous attention to detail and endless pursuit of perfection, seen in generating '20 unique textures' for a logo or refining song lyrics through 'multiple iterations', suggests that the act of refining sometimes feels safer than declaring a project 'done' and moving on to market it. Your self-identified 'struggles with market feedback' support this: refinement is entirely internal, whereas completion exposes you to external critique." It cited specific conversations and entries by number. The logo refinement sessions. The lyric rewrites. The recurring theme of "not quite ready" across hundreds of entries spanning years. The thing that's interesting technically: this pattern isn't visible inside any single source. It only shows up when you look across the conversation history and the journal entries at the same time. The conversations show the topic. The journal entries show the behavior. The cross-reference shows the structure. The model labeled it: You Refine to Avoid Finishing. Has anyone else done systematic pattern analysis on their own AI conversation history? Curious what people have found.

2h ago

---

**[Alright I'm just going to crash out a bit about LLMs rn downvote me upvote me up to you](https://www.reddit.com/r/artificial/comments/1s2q95s/alright_im_just_going_to_crash_out_a_bit_about/)**

Hello everyone hope you're having a nice day I'm just ugh I'm so tired and confused and frustrated. I'm desperately trying to map/figure the future out of like societies/nation states across the world (because without getting too political watching the news at least in the UK is clearly a complete waste of time for trying to figure out actual important issues in the world that affect you) and it's just so exhausting We appear to have a few rough ideas of what will happen in the next 5 to 10 years (from what I see roughly these massive multi national companies will not do like massive layoffs anytime within 5 years or so but then after 5 years it's anyone's guess. Roughly speaking because even the top academics apparently and the LLMs can't figure this out just yet just not enough data) in 10 years time there will be massive layoffs of traditional corporate roles like idk secretaries or middle managers. However the crucial part/question appears to be how many more roles will be created as a results of LLM progression. Roles we can't even fathom yet. Or maybe knock on effects - apparently in the UK in the 1800s when steam trains became much more efficient the "understanding" was that coal production would massively decline, as there would be less demand for coal, but the sudden amount of potential coal available ended up actually increasing coal production or something (something to do with factories being able to massively scale operations and what not maybe ships as well) Without getting into it I'm getting so sick and tired of politics. In the UK I have no idea what's going on but there are potholes everywhere apparently within 5 years one fifth of UK roads will become "structurally unsafe/unusable" and half within 15, and that's barely 5% or something of the issues we face in other areas. In Singapore (for all it's ails) they're apparently using AI to actually spot/predict pot holes and subsequently deal with them before they become an issue. I'm also getting very anxious about other countries actually effectively investing and implementing AI into their infrastructure as we speak (no drama with them power to them just anxious about the UK falling behind) because we seem to put all of our resources into God knows what? Clearly not investing in public infrastructure You know the philosophical stuff the social contract the idea that you idk "try hard in school go to university then get a job buy a house and life is glorious" it's clearly completely gone but there is a massive amount of people in society who refuse to accept this or don't care and just live the old way anyway which causes heaps of problems. The traditional notion of career..? Teachers etc what will teaching look like? Tutoring? I don't know. I'm not being entirely negative here it's just stressing me out that I can't figure it out because it's impossible. I'm having to accept that I can't reasonably predict beyond a few months/years roughly and it's upsetting me. Alright well there we go /rant That said I'm sure there will be a massive amount of positive uses of AI in the world such as the above mentioned example with Singapore, I'm thinking hospital triage times, spotting cancers months before doctors could, helping children who don't respond particularly well to traditional classroom environments with learning. And national parks and what not will largely be just as beautiful in 5 years time as they are now. Just stressful not knowing I suppose Any thoughts anyone? Take care

1h ago

---

**[Arm announces AGI CPU for AI data centers](https://www.reddit.com/r/artificial/comments/1s2po13/arm_announces_agi_cpu_for_ai_data_centers/)**

Arm announced their first silicon product in history with today's AGI CPU

🔗 [phoronix.com](https://www.phoronix.com/news/Arm-AGI-CPU) • 1h ago

---

**[Mark Zuckerberg builds AI CEO to help him run Meta](https://www.reddit.com/r/artificial/comments/1s1qk1c/mark_zuckerberg_builds_ai_ceo_to_help_him_run_meta/)**

Tech giant’s tools include ‘Second Brain’ and an internal messaging board for AI bots

🔗 [The Independent](https://www.the-independent.com/tech/mark-zuckerberg-ai-ceo-bot-b2943792.html) • 1d ago

---

**[What if your AI agent could fix its own hallucinations without being told what's wrong?](https://www.reddit.com/r/artificial/comments/1s2i90f/what_if_your_ai_agent_could_fix_its_own/)**

Every autonomous AI agent has three problems: it contradicts itself, it can't decide, and it says things confidently that aren't true. Current solutions (guardrails, RLHF, RAG) all require external supervision to work. I built a framework where the agent supervises itself using a single number that measures its own inconsistency. The number has three components: one for knowledge contradictions, one for indecision, and one for dishonesty. The agent minimizes this number through the same gradient descent used to train neural networks, except there's no training data and no human feedback. The agent improves because internal consistency is the only mathematically stable state. The two obvious failure modes (deleting all knowledge to avoid contradictions, or becoming a confident liar) are solved by evidence anchoring: the agent's beliefs must be periodically verified against external reality. Unverified beliefs carry an uncertainty penalty. High confidence on unverified claims is penalized. The only way to reach zero inconsistency is to actually be right, decisive, and honest. I proved this as a theorem, not a heuristic. Under the evidence anchoring mechanism, the only stable fixed points of the objective function are states where the agent is internally consistent, externally grounded, and expressing appropriate confidence. The system runs on my own hardware (desktop with multiple GPUs and a Surface Pro laptop) with local LLMs. No cloud dependency. The interesting part: the same three-term objective function that fixes AI hallucination also appears in theoretical physics, where it recovers thermodynamics, quantum measurement, and general relativity as its three fixed-point conditions. Whether that's a coincidence or something deeper is an open question. Paper: https://doi.org/10.5281/zenodo.19114787

5h ago

---

**[Whats your thoughts on Bugbounty software powered by AI](https://www.reddit.com/r/artificial/comments/1s2e2ds/whats_your_thoughts_on_bugbounty_software_powered/)**

Free XP on bug bounty. Contribute to canuk40/xpfarm development by creating an account on GitHub.

🔗 [GitHub](https://github.com/canuk40/xpfarm) • 8h ago

---

**[I mapped how Reddit actually talks about AI safety: 6,374 posts, 23 clusters, some surprising patterns](https://www.reddit.com/r/artificial/comments/1s2g23a/i_mapped_how_reddit_actually_talks_about_ai/)**

I collected Reddit posts between Jan 29 - Mar 1, 2026 using 40 keyword-based search terms ("AI safety", "AI alignment", "EU AI Act", "AI replace jobs", "red teaming LLM", etc.) across all subreddits. After filtering, I ended up with 6,374 posts and ran them through a full NLP pipeline. What I built: Sentence embeddings (paraphrase-multilingual-MiniLM-L12-v2) -> 10D UMAP -> HDBSCAN clustering Manual cluster review using structured cluster cards Sentiment analysis per post (RoBERTa classifier) Discourse framing layer - human-first labeling with blind LLM comparison and human adjudication The result: 23 interpretable clusters grouped into 11 thematic families. Three things I found interesting: 1. The discourse is fragmented, not unified. No single cluster dominates - the largest is ~10% of posts. "AI safety discourse" on Reddit looks more like a field of related but distinct conversations: labour anxiety, regulation, lab trust, authenticity & synthetic content, technical safety, enterprise adoption, philosophical debates about personhood. They don't talk to each other that much. 2. The most negative clusters are about lived disruption, not abstract risk. Job replacement, synthetic content spam, broken trust in specific AI labs, AI misuse in schools, creative displacement - these are the most negatively-toned clusters. Enterprise adoption and national AI progress clusters are neutral-to-positive. X-risk and alignment clusters are... mostly neutral, which surprised me. 3. Framing matters as much as topic. Two clusters can both be "about AI and work" while one is macro labour anxiety and another is micro hiring friction - different problems, different policy implications. Topic labels alone don't capture this. Visualizations, full report (PDF), sample data, and code: https://github.com/kelukes/reddit-ai-safety-discourse-2026 Feedback on the pipeline and all is very welcome - this was a capstone project and I'm still learning.

7h ago

---

---

## Google News: "ai"

**[Coding After Coders: The End of Computer Programming as We Know It](https://www.nytimes.com/2026/03/12/magazine/ai-coding-programming-jobs-claude-chatgpt.html)**

The New York Times • 12d ago

---

**[Anthropic says Claude can now use your computer to finish tasks for you in AI agent push](https://www.cnbc.com/2026/03/24/anthropic-claude-ai-agent-use-computer-finish-tasks.html)**

Anthropic and its rivals are trying to ramp up capabilities of AI agents after OpenClaw went viral earlier this year.

CNBC • 12h ago

---

**[Security firms are handing the grunt work to AI agents](https://www.businessinsider.com/ai-agents-are-changing-cybersecurity-jobs-and-cutting-workloads-2026-3)**

Cybersecurity firms are being tasked with implementing AI agents across their teams. But the technology's capabilities remain limited.

Business Insider • 1h ago

---

**[Apple Plans AI Reboot With Siri App, New Look and ‘Ask Siri’ Button in iOS 27](https://www.bloomberg.com/news/articles/2026-03-24/ios-27-features-apple-ai-reboot-with-siri-app-new-interface-ask-siri-button)**

Bloomberg.com • 3h ago

---

**[Walmart, Gap push AI shopping in ChatGPT and Google Gemini but differ on checkout](https://www.axios.com/2026/03/24/ai-shopping-walmart-gap-chatgpt-gemini-checkout)**

Axios • 1h ago

---

**[OpenAI CEO Shifts Responsibilities, Preps ‘Spud’ AI Model](https://www.theinformation.com/articles/openai-ceo-shifts-responsibilities-preps-spud-ai-model)**

OpenAI CEO Sam Altman has relinquished direct oversight of the company’s safety and security teams so he can focus on raising capital, supply chains and “building datacenters at unprecedented scale,” he told staff on Tuesday. At the same time, he said the company had completed the initial ...

The Information • 2h ago

---

**[OpenAI says it will discontinue AI video platform Sora](https://www.cnn.com/2026/03/24/business/video/openai-sora-gold-live-032404pseg2-cnni-business-fast)**

OpenAI says it will discontinue its AI video platform Sora as it aims to refocus its products.

CNN • 1h ago

---

**[OpenAI pulls the plug on its Sora AI video app](https://www.cbsnews.com/news/sora-ai-openai-discontinues/)**

OpenAI said Tuesday that it will discontinue the company's Sora app, which let users create AI-generated videos.

CBS News • 1h ago

---

**[Johnson calls on Congress to enact Trump’s AI agenda](https://www.politico.com/live-updates/2026/03/24/congress/johnson-calls-on-congress-to-enact-trumps-ai-agenda-00842150)**

Politico • 1h ago

---

**[RFK Jr. and Dr. Oz have a plan to save rural health care. Here’s the catch.](https://www.washingtonpost.com/health/2026/03/23/rural-health-ai-medical-tech/)**

Top health officials point to AI as the solution for dying hospitals, but experts from rural areas of the country say the solution isn’t that simple.

The Washington Post • 5h ago

---

---

## HackerNews: "ai"

**[So where are all the AI apps?](https://news.ycombinator.com/item?id=47503006)**

Practical AI R&D

⬆️ 352 • 💬 322 • 7h ago • [Answer.AI](https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html)

---

**[I built an AI receptionist for a mechanic shop](https://news.ycombinator.com/item?id=47487536)**

Learn how I built an ai receptionist for my brother's mechanic shop

⬆️ 306 • 💬 314 • 1d ago • [itsthatlady.dev](https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/)

---

**[The bridge to wealth is being pulled up with AI](https://news.ycombinator.com/item?id=47503296)**

For two centuries, the credential system gave intelligence a route to heritable capital. Artificial intelligence is closing that route. This essay builds the argument from first principles - with probability theory, interactive simulations, and a prediction specific enough to be falsifiable - and puts a number on the window that remains.

⬆️ 252 • 💬 359 • 7h ago • [Daniel Homola](https://danielhomola.com/m%20&%20e/ai/your-bridge-to-wealth-is-being-pulled-up/)

---

**[What young workers are doing to AI-proof themselves](https://news.ycombinator.com/item?id=47480447)**

⬆️ 225 • 💬 390 • 2d ago • [wsj.com](https://www.wsj.com/economy/jobs/ai-jobs-young-people-careers-14282284)

---

**[Show HN: Cq – Stack Overflow for AI coding agents](https://news.ycombinator.com/item?id=47491466)**

cq explores a Stack Overflow for agents, a shared commons where agents can query past learnings, contribute new knowledge, and avoid repeating the same mistakes in isolation.

⬆️ 200 • 💬 87 • 1d ago • [Mozilla.ai](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)

---

**[Diverse perspectives on AI from Rust contributors and maintainers](https://news.ycombinator.com/item?id=47482825)**

⬆️ 159 • 💬 82 • 1d ago • [nikomatsakis.github.io](https://nikomatsakis.github.io/rust-project-perspectives-on-ai/feb27-summary.html)

---

**[Is anybody else bored of talking about AI?](https://news.ycombinator.com/item?id=47508745)**

Is anybody else bored of talking about AI?

⬆️ 154 • 💬 82 • 1h ago • [Unfinished Side Projects](https://blog.jakesaunders.dev/is-anybody-else-bored-of-talking-about-ai/)

---

**[The AI Industry Is Lying to You](https://news.ycombinator.com/item?id=47506259)**

Hi! If you like this piece and want to support my independent reporting and analysis, why not subscribe to my premium newsletter? It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5000 to 18,000 words, including

⬆️ 141 • 💬 101 • 4h ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/)

---

**[Ask HN: AI productivity gains – do you fire devs or build better products?](https://news.ycombinator.com/item?id=47475859)**

⬆️ 104 • 💬 196 • 2d ago

---

**[Show HN: ProofShot – Give AI coding agents eyes to verify the UI they build](https://news.ycombinator.com/item?id=47499672)**

Contribute to AmElmo/proofshot development by creating an account on GitHub.

⬆️ 99 • 💬 66 • 14h ago • [GitHub](https://github.com/AmElmo/proofshot)

---

---

## YouTube Videos: "ai"

**[AI Is Making Software Worthless Faster Than Anyone Realizes](https://www.youtube.com/watch?v=wrMrtmfn0MA)**

In this vlog, I make a bold case that AI is destroying the economic moat of the software industry and shifting value away from SaaS, ...

📺 Asian Dad Energy

👁️ 20K • 👍 1K • 💬 489 • ⏱️ 9:25 • 8h ago

---

**[I Asked 4 AIs to PREDICT the 2026 Midterms. Trump&#39;s AI Was INSANE](https://www.youtube.com/watch?v=_MeZ1Kz6cVI)**

Grab your free seat to the 2-Day AI Mastermind: https://link.outskill.com/IASKAIMAR4 100% Discount for the first 1000 people ...

📺 I Ask AI

👁️ 24K • 👍 2K • 💬 225 • ⏱️ 17:22 • 1d ago

---

**[NEW: Trump official reveals AI action plan](https://www.youtube.com/watch?v=rT1Q3_7kQDY)**

White House science advisor Michael Kratsios discusses the Trump administration's AI plan for Congress, its potential impact on ...

📺 Fox News Clips

👁️ 41K • 👍 740 • 💬 253 • ⏱️ 4:08 • 1d ago

---

**[98% of People Will Miss This New AI Opportunity](https://www.youtube.com/watch?v=YNnCSJ3Fc_Q)**

Get Started with Manus today: https://manus.im/redeem?c=JWH1G26A Prompts I used in this video: PROMPT #1 I want to create ...

📺 Journey With The Hintons

👁️ 27K • 👍 3K • 💬 354 • ⏱️ 12:49 • 2d ago

---

**[DeepSeek Just Fixed One Of The Biggest Problems With AI](https://www.youtube.com/watch?v=DmtoVnTkQnM)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The #DeepSeek paper is available here: ...

📺 Two Minute Papers

👁️ 31K • 👍 3K • 💬 214 • ⏱️ 9:47 • 6h ago

---

**[China’s New AI Robots Just Broke The Human Skill Barrier](https://www.youtube.com/watch?v=QDRzgF-8-50)**

This week in robotics got kind of ridiculous. South Korea showed off a humanoid that can run, jump, play soccer, and moonwalk, ...

📺 AI Revolution

👁️ 128K • 👍 2K • 💬 119 • ⏱️ 14:31 • 1d ago

---

**[Jensen Huang: NVIDIA - The $4 Trillion Company &amp; the AI Revolution | Lex Fridman Podcast #494](https://www.youtube.com/watch?v=vif8NQcjVf0)**

Jensen Huang is the co-founder and CEO of NVIDIA, the world's most valuable company and the engine powering the AI ...

📺 Lex Fridman

👁️ 362K • 👍 11K • 💬 1K • ⏱️ 2:25:59 • 1d ago

---

**[Cops Use AI, Arrest the Wrong Guy](https://www.youtube.com/watch?v=kAEdH1YXB8I)**

Imagine you go into a business and their AI surveillance camera thinks it recognizes you as a trespasser. So that business ...

📺 The Civil Rights Lawyer

👁️ 187K • 👍 11K • 💬 1K • ⏱️ 2:37 • 1d ago

---

**[How to Build &amp; Sell AI Agents in 2026: Ultimate Beginner’s Guide](https://www.youtube.com/watch?v=AYQtRqW1xX4)**

Self-Host your n8n with Hostinger → https://hostinger.com/liamn8n Use code LIAMOTTLEY for extra 10% off Grab all the course ...

📺 Liam Ottley

👁️ 36K • 👍 2K • 💬 66 • ⏱️ 3:05:04 • 2d ago

---

**[Nvidia CEO Just Said This About OpenClaw And He&#39;s Not Wrong (+ 12 AI Updates)](https://www.youtube.com/watch?v=_Vccl1Iulws)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://link.stayingahead.ai/YT8 ...

📺 Vaibhav Sisinty

👁️ 79K • 👍 3K • 💬 79 • ⏱️ 19:16 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 326,131 • ❤️ 897 • 14d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 164,200 • ❤️ 1,168 • 19h ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 8,493 • ❤️ 333 • 5d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 19,722 • ❤️ 257 • 1d ago

---

**[Foundation-1](https://huggingface.co/RoyalCities/Foundation-1)**

*Royal Cities*

Foundation-1 is a structured text-to-sample model for music production, enabling precise control over instrumentation, timbre, FX, and musical structure (tempo, key, bar count) for generating coherent, production-ready audio loops.

⬇️ 0 • ❤️ 248 • 8d ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 13,613 • ❤️ 726 • 13d ago

---

**[Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)**

*Mistral AI_*

Mistral-Small-4-119B-2603 is a hybrid MoE model (119B params, 6.5B active) supporting 256k context and multimodal input (text/image). It excels at instruction following, reasoning (configurable effort), and agentic tasks with native function calling, offering significant speed and throughput improvements for use cases like coding, document analysis, and general assistants.

`119.4B`

⬇️ 36,887 • ❤️ 323 • 1d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a multimodal OCR model for complex document understanding, excelling in state-of-the-art performance on benchmarks and real-world scenarios like tables and code-heavy documents. It offers efficient inference with a 0.9B parameter model, supporting deployment via vLLM, SGLang, and Ollama for high-concurrency services and edge deployments.

`image-to-text`

⬇️ 3,420,577 • ❤️ 1,444 • 12d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 385,054 • ❤️ 636 • 20d ago

---

**[Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2 is a fine-tuned LLM optimized for efficient chain-of-thought reasoning, delivering higher accuracy with reduced token usage. It excels in resource-constrained environments and agentic workflows by providing faster, more economical reasoning.

`image-text-to-text` `9.0B`

⬇️ 43,905 • ❤️ 119 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 28 • 💬 2 • ⭐ 40,693 • 15mo ago

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

▲ 27 • 💬 5 • ⭐ 519 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 3 • 💬 0 • ⭐ 519 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://huggingface.co/papers/2603.21986)**

*SII-GAIR, Sand. ai, Ethan Chern et al. (45 authors)*

daVinci-MagiHuman is an open-source audio-video generative model that synchronizes text, video, and audio through a single-stream Transformer architecture, achieving high-quality human-centric content generation with efficient inference capabilities.

▲ 88 • 💬 3 • ⭐ 313 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2603.21986) • [💻 code](https://github.com/GAIR-NLP/daVinci-MagiHuman) • [🔗 project](https://huggingface.co/spaces/SII-GAIR/daVinci-MagiHuman)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 32 • 💬 2 • ⭐ 30,439 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 194 • 💬 5 • ⭐ 8,093 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[Attention Residuals](https://huggingface.co/papers/2603.15031)**

*Kimi Team, Guangyu Chen, Yu Zhang et al. (37 authors)*

🏢 Moonshot AI

Residual connections with PreNorm are standard in modern LLMs, yet they accumulate all layer outputs with fixed unit weights. This uniform aggregation causes uncontrolled hidden-state growth with depth, progressively diluting each layer's contribution. We propose Attention Residuals (AttnRes), which replaces this fixed accumulation with softmax attention over preceding layer outputs, allowing each layer to selectively aggregate earlier representations with learned, input-dependent weights. To address the memory and communication overhead of attending over all preceding layer outputs for large-scale model training, we introduce Block AttnRes, which partitions layers into blocks and attends over block-level representations, reducing the memory footprint while preserving most of the gains of full AttnRes. Combined with cache-based pipeline communication and a two-phase computation strategy, Block AttnRes becomes a practical drop-in replacement for standard residual connections with minimal overhead.
  Scaling law experiments confirm that the improvement is consistent across model sizes, and ablations validate the benefit of content-dependent depth-wise selection. We further integrate AttnRes into the Kimi Linear architecture (48B total / 3B activated parameters) and pre-train on 1.4T tokens, where AttnRes mitigates PreNorm dilution, yielding more uniform output magnitudes and gradient distribution across depth, and improves downstream performance across all evaluated tasks.

▲ 155 • 💬 4 • ⭐ 2,655 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15031) • [💻 code](https://github.com/MoonshotAI/Attention-Residuals)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 17 • 💬 0 • ⭐ 36,483 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 58 • 💬 4 • ⭐ 18,919 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 54.1k • 🔱 7.5k • 3d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 22.4k • 🔱 1.1k • 9m ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 13.2k • 🔱 1.7k • 5h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 12.5k • 🔱 1.2k • 5h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 11.1k • 🔱 578 • 3h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 10.7k • 🔱 776 • 1d ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 6.6k • 🔱 1.0k • 3d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 6.1k • 🔱 493 • 5h ago

---

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)**

734+ structured cybersecurity skills for AI agents · MITRE ATT&CK mapped · agentskills.io open standard · Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI & 20+ platforms · Penetration testing, DFIR, threat intel, cloud security & more · Apache 2.0

`Python` `ai-agents` `claude` `claude-code` `cloud-security` `cybersecurity`

⭐ 3.7k • 🔱 371 • 1d ago

---

**[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)**

OpenShell is the safe, private runtime for autonomous AI agents.

`Rust`

⭐ 3.6k • 🔱 356 • 32m ago

---

---

*Generated by PeekDeck - A glance is all you need*
