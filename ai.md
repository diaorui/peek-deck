---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-15T21:26:30.886971+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 15, 2026 at 21:26 UTC  
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

**[Microsoft AI chief gives it 18 months for all white-collar work to be automated by AI](https://www.reddit.com/r/artificial/comments/1r4oc2i/microsoft_ai_chief_gives_it_18_months_for_all/)**

Mustafa Suleyman believes current AI computational power will only accelerate, disrupting every kind of work you do “sitting down at a computer.”

🔗 [Fortune](https://fortune.com/2026/02/13/when-will-ai-kill-white-collar-office-jobs-18-months-microsoft-mustafa-suleyman/) • 1d ago

---

**[Pentagon's use of Claude during Maduro raid sparks Anthropic feud](https://www.reddit.com/r/artificial/comments/1r4hgnu/pentagons_use_of_claude_during_maduro_raid_sparks/)**

The U.S. military used Anthropic's Claude AI model during the operation to capture Venezuela's Nicolás Maduro, two sources with knowledge of the situation told Axios. "Anthropic asked whether their software was used for the raid to capture Maduro, which caused real concerns across the Department of War indicating that they might not approve if it was," the official said. The Pentagon wants the AI giants to allow them to use their models in any scenario so long as they comply with the law. Axios could not confirm the precise role that Claude played in the operation to capture Maduro. The military has used Claude in the past to analyze satellite imagery or intelligence. The sources said Claude was used during the active operation, not just in preparations for it. Anthropic, which has positioned itself as the safety-first AI leader, is currently negotiating with the Pentagon around its terms of use. The company wants to ensure in particular that its technology is not used for the mass surveillance of Americans or to operate fully autonomous weapons.

🔗 [axios.com](https://www.axios.com/2026/02/13/anthropic-claude-maduro-raid-pentagon) • 1d ago

---

**[Looking for articles about AI](https://www.reddit.com/r/artificial/comments/1r5cuzu/looking_for_articles_about_ai/)**

Hello, I'm currently a student studying Translation and Interpretation studies, and I need to translate an article about AI for school. It needs to be 10 - 15 standard pages long, the more reliable source the better. All of the ones I found so far were either too short or too long, so I'd like to aks for your help. Thank you.

9h ago

---

**[Validation prompts - getting more accurate responses from LLM chats](https://www.reddit.com/r/artificial/comments/1r59tzo/validation_prompts_getting_more_accurate/)**

Hallucinations are a problem with all AI chatbots, and it’s healthy to develop the habit of not trusting them, here are a a couple of simple ways i use to get better answers, or get more visibility into how the chat arrived at that answer so i can decide if i can trust the answer or not. (Note: none of these is bulletproof: never trust AI with critical stuff where a mistake is catastrophic) “Double check your answer”. Super simple. You’d be surprise how often Claude will find a problem and provide a better answer. If the cost of a mistake is high, I will often rise and repeat, with: “Are you sure?” “Take a deep breath and think about it”. Research shows adding this to your requests gets you better answers. Why? Who cares. It does. Source: https://arstechnica.com/information-technology/2023/09/telling-ai-model-to-take-a-deep-breath-causes-math-scores-to-soar-in-study/ “Use chain of thought”. This is a powerful one. Add this to your requests gets, and Claude will lay out its logic behind the answer. You’ll notice the answers are better, but more importantly it gives you a way to judge whether Claude is going about it the right way. Try: > How many windows are in Manhattan. Use chain of thought > What’s wrong with my CV? I’m getting not interviews. Use chain of thought. —— If you have more techniques for validation, would be awesome if you can share! 💚 P.S. originally posted on r/ClaudeHomies

12h ago

---

**[It isn't the tool, but the hands: why the AI displacement narrative gets it backwards](https://www.reddit.com/r/artificial/comments/1r4ybm7/it_isnt_the_tool_but_the_hands_why_the_ai/)**

Responding to Matt Shumer's "Something Big Is Happening" piece that's been circulating. The pace of change is real, but the "just give it a prompt" framing is self-defeating. If the prompt is all that matters, then knowing what to build and understanding the problem deeply matters MORE. Building simple shit is getting commoditized, fine. But building complex systems and actually understanding how they work? That's becoming more valuable, not less. When anyone can spin up the easy stuff, the premium shifts to the people who can architect what's hard and debug what's opaque. We also need to separate "building software" from "building AI systems", completely different trajectories. The former may be getting commoditized. The latter is not. How we use this technology, how we shape it, what we point it at, that's specifically human work. And the agent management point: if these things move fast and independently, the operator's ability to effectively manage them becomes the fulcrum of value. We are nowhere near "assign a broad goal and walk away for six months." Taste, human judgment, and understanding what other humans actually need, those make that a steep climb. Unless these systems are building for and selling to other agents, the intent of the operator and their oversight remain crucial. Like everything before AI: it isn't the tool, but the hands. Original article: https://www.linkedin.com/pulse/something-big-happening-matt-shumer-so5he

22h ago

---

**[We have been building and working on a local AI with memory and persistence](https://www.reddit.com/r/artificial/comments/1r4wnlo/we_have_been_building_and_working_on_a_local_ai/)**

We have built a local model running on a Mac Studio M3 Ultra, 32-core CPU, 80-core GPU, 32-core Neural Engine, 512GB unified memory. With a 5-tiered memory architecture that can be broken down as follows: Working memory - This keeps the immediate conversational context. Vector Store - Semantic memory for conceptual retrieval. Knowledge graph (Neo4j) - A symbolic relational map of hard facts and entities. Timeline log - A chronological record of every event and interaction. Lessons - A distilled layer of extracted truths and behavioural patterns. Interactions with Ernos are written to these tiers in real time. When Ernos responds to you, he has processed your prompt through the lens of everything he has ever learnt. Ernos also has an algorithm that operates independently of user prompts, working through his memory of interactions, identifying contradictions, and then aligning his internal knowledge graph with external reality. This also happens against Ernos’ own ‘thoughts’, verifying his own claims against the internet and codebase, adjusting to what is empirically true. If Ernos fails, or has a hallucination, it is caught, analysed, and fixed, in a self-correcting feedback loop that perpetually refines the internal model to match the physical and digital world he inhabits. A digital ‘Robert Rosen Anticipatory System’. These two systems enable Ernos to adopt a position, defend it with evidence, and evolve a personality over time based on genuine experiences rather than pre-programmed templates. If you are still reading this (and I can appreciate it’s dry), thank you. I would be interested to know your thoughts and criticisms. Also if you would like to test Ernos, or try to disprove his claims/break him, we would truly appreciate inquisitive minds to do so.

23h ago

---

**[AI Coding Won’t Replace Human Developers — Here’s Why I’m Actually Optimistic About It](https://www.reddit.com/r/artificial/comments/1r5b70z/ai_coding_wont_replace_human_developers_heres_why/)**

Everyone’s screaming that “AI coding is going to replace human developers” — doomers everywhere saying programmers are doomed, software companies will get swallowed up, the whole industry is toast. But after watching this space closely, I think the reality is way less apocalyptic. Here’s a slightly contrarian take I’d love to hear your thoughts on. First off: yes, AI is insanely powerful and it’s already transforming dev productivity. No denying that. It cranks out boilerplate, debugs, refactors, writes tests, and even spits out initial architecture ideas at ridiculous speed. A lot of people’s workflows have shifted from “writing code from scratch” to “reviewing + guiding AI.” I’m using it daily and I strongly recommend everyone jump on board ASAP — the earlier you adapt, the bigger the edge. That said, here’s the part I think gets overlooked: AI won’t truly replace humans anytime soon. Why? Because at its core, AI is still a super-smart mimic — like a brilliant but literal-minded kid. It excels at copying patterns it’s seen before, following established rules, and replicating what’s worked in the past. But it fundamentally doesn’t grasp human intent and variability. Humans are messy and changeable in ways that define real complexity: - Requirements flip on a dime - Priorities shift based on business whims, user feedback, or even “the boss had a bad morning” - Context evolves mid-project - Trade-offs involve taste, long-term maintainability, “this just feels right” intuition AI is born rule-bound. When the rules don’t cover the twist, or the goal moves outside the training distribution, it hallucinates garbage, produces “correct-looking” bugs, or stubbornly sticks to outdated patterns. Right now, AI is more like an ultra-fast hammer than an architect. It nails things quickly, but you still decide what house to build, where, why, and how people will actually live in it. I suspect the honeymoon phase (maybe 1–3 more years?) will fade, and we’ll start seeing - Pure AI-generated code racks up surprisingly high maintenance debt - The best systems still need that human “craftsmanship”- - obsession over details, edge-case intuition, long-term vision, aesthetic judgment - AI feels too mechanical, too soulless; people will crave the “artisanal” touch again As for the big fear — “software companies get eaten by AI, mass layoffs for devs”: This feels a lot like the panic when steam engines showed up and horse drivers thought the world was ending. Short-term pain? Absolutely (CRUD-heavy roles shrink, junior/entry-level spots dry up, some teams go from 20 to 5 with AI leverage). But long-term? - Lower dev costs:explosion in software demand (history shows this every time tools get cheaper/faster) - More indie projects, startups, niche apps, non-traditional software (embedded, robotics, custom tools everywhere) - Traditional companies don’t vanish; they evolve — from headcount armies to smaller, sharper teams wielding AI like a force multiplier. So my vibe:don’t panic, but don’t overhype AI as god either. Embrace the change, level up your ability to steer AI effectively, and keep sharpening the irreplaceable human skills: judgment, creativity, empathy for users, and that stubborn drive to build something meaningful.

11h ago

---

**[How to bulk contact using AI?](https://www.reddit.com/r/artificial/comments/1r5co3e/how_to_bulk_contact_using_ai/)**

I have a list of 10,000 contact number (mix of phone number and landlines so texting would not work), how can I efficiently contact them in bulk using AI? any suggestions? I'm not trying to scam, trying to efficiently categorize a set of data for company research.

9h ago

---

**[I built a "Traffic Light" system for AI Agents so they don't corrupt each other (Open Source)](https://www.reddit.com/r/artificial/comments/1r4tbnj/i_built_a_traffic_light_system_for_ai_agents_so/)**

Hey everyone, I’m a backend developer with a background in fintech. Lately, I’ve been experimenting with multi-agent systems, and one major issue I kept running into was collision. When you have multiple agents (or even one agent doing complex tasks) accessing the same files, APIs, or context, they tend to "step on each other's toes." They overwrite data, execute out of order, or hallucinate permissions they shouldn't have. It’s a mess. I realized what was missing was a Traffic Light. So I built Network-AI. It’s an open-source protocol that acts as a traffic control system for agent orchestration. How it works: Think of it like an intersection. Before an agent can execute a high-stakes tool (like writing to a database, moving a file, or sending a transaction), it hits a "Red Light." The Check: The protocol (specifically a module I call AuthGuardian) checks the agent’s credentials and the current state of the environment. The Green Light: Only if the "road is clear" (permissions are verified and no conflicts exist) does the agent get the green light to proceed. The Camera: Just like a traffic camera, there is an immutable audit trail of every green light given, so you can debug crashes later. Why I’m posting: I’m not selling anything. I just want to solve the problem of agents corrupting shared environments. I’d love for you to check out the repo and tell me if this "Traffic Light" architecture makes sense for your use cases, or if I’m over-engineering it. Repo:https://github.com/jovanSAPFIONEER/Network-AI all feedback is welcome

1d ago

---

**[Only A Few AI Platforms Can Survive](https://www.reddit.com/r/artificial/comments/1r4n1u9/only_a_few_ai_platforms_can_survive/)**

It does not happen very often in the history of business that an orthogonal product is invented that almost immediately doubles the revenue pool of a

🔗 [The Next Platform](https://www.nextplatform.com/2026/02/11/only-a-few-ai-platforms-can-survive/) • 1d ago

---

---

## Google News: "ai"

**[Exclusive: Pentagon threatens to cut off Anthropic in AI safeguards dispute](https://www.axios.com/2026/02/15/claude-pentagon-anthropic-contract-maduro)**

Axios • 19h ago

---

**[US military used Anthropic’s AI model Claude in Venezuela raid, report says](https://www.theguardian.com/technology/2026/feb/14/us-military-anthropic-ai-model-claude-venezuela-raid)**

Wall Street Journal says Claude used in operation via Anthropic’s partnership with Palantir Technologies

The Guardian • 1d ago

---

**[What’s Left For Humans?](https://www.wsj.com/tech/ai/whats-left-for-humans-64169dd9?gaa_at=eafs&gaa_n=AWEtsqflsPcIZUqGzhikFq_cmoXmu_Yp3n7RrMGuvi-03Hf40b2Fw2VWPpFk&gaa_ts=699235f6&gaa_sig=GplRKJcpwABIthv2s8AD6fwfd2pPXvtC5Wp9YqcWHfJn8uFlA96VuZK-YuaMTaKayARTTlc9OHjvmywRUFD_qw%3D%3D)**

The Wall Street Journal • 5h ago

---

**[He spent decades perfecting his voice. Now he says Google stole it.](https://www.washingtonpost.com/technology/2026/02/15/david-greene-google-ai-podcast/)**

NPR’s David Greene says he was “completely freaked out” when he heard an AI voice that sounded just like his own, and he’s suing over it.

The Washington Post • 3h ago

---

**[Hollywood groups condemn ByteDance's AI video generator, claiming copyright infringement](https://abcnews.go.com/Technology/wireStory/hollywood-groups-condemn-bytedances-ai-video-generator-claiming-130193458)**

A new artificial intelligence video generator from Beijing-based ByteDance, the creator of TikTok, is drawing the ire of Hollywood organizations

ABC News • 1h ago

---

**[How Disney picks its AI copyright battles depends on who's ripping it off](https://www.businessinsider.com/disney-ai-copyright-battles-seedance-nano-banana-sora-midjourney-2026-2)**

Disney sent ByteDance a cease-and-desist for using its characters on Seedance. When OpenAI's Sora did it, however, Disney struck a deal.

Business Insider • 2h ago

---

**[Paramount Latest Studio To Hit ByteDance With Cease And Desist Letter Over AI Models](https://deadline.com/2026/02/paramoun-hollywood-legal-letter-bytedance-ai-seedance-1236725462/)**

Paramount has joined Disney as the latest Hollywood studio to slam ByteDance over AI models Seedance and Seedream for IP infringement.

Deadline • 48m ago

---

**[Obama responds to Trump sharing racist AI video depicting him as an ape](https://www.npr.org/2026/02/15/nx-s1-5715117/obama-racist-ai-video-response-trump)**

"There doesn't seem to be any shame about this among people who used to feel like you had to have some sort of decorum," Obama said in an interview that was posted on YouTube Saturday.

NPR • 2h ago

---

**[‘We’re All Polyamorous Now. It’s You, Me and the A.I.’](https://www.nytimes.com/2026/02/13/opinion/ai-relationships.html)**

The New York Times • 2d ago

---

**[The AI productivity take-off is finally visible](https://www.ft.com/content/4b51d0b4-bbfe-4f05-b50a-1d485d419dc5)**

New economic data suggests the US is transitioning to a phase of measurable gains from the technology

Financial Times • 16h ago

---

---

## HackerNews: "ai"

**[An AI agent published a hit piece on me – more things have happened](https://news.ycombinator.com/item?id=47009949)**

⬆️ 720 • 💬 599 • 1d ago • [theshamblog.com](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-2/)

---

**[News publishers limit Internet Archive access due to AI scraping concerns](https://news.ycombinator.com/item?id=47017138)**

Outlets like The Guardian and The New York Times are scrutinizing digital archives as potential backdoors for AI crawlers.

⬆️ 543 • 💬 353 • 1d ago • [Nieman Lab](https://www.niemanlab.org/2026/01/news-publishers-limit-internet-archive-access-due-to-ai-scraping-concerns/)

---

**[IBM tripling entry-level jobs after finding the limits of AI adoption](https://news.ycombinator.com/item?id=47009327)**

Gen Z jobs aren’t dead yet: $240 billion tech giant IBM says it’s rewriting entry-level jobs—and tripling down on its hiring of young talent.

⬆️ 361 • 💬 251 • 1d ago • [Fortune](https://fortune.com/2026/02/13/tech-giant-ibm-tripling-gen-z-entry-level-hiring-according-to-chro-rewriting-jobs-ai-era/)

---

**[I'm not worried about AI job loss](https://news.ycombinator.com/item?id=47006513)**

We're not in a February 2020 moment, and ordinary people will be fine

⬆️ 343 • 💬 544 • 2d ago • [davidoks.blog](https://davidoks.blog/p/why-im-not-worried-about-ai-job-loss)

---

**[CBP signs Clearview AI deal to use face recognition for 'tactical targeting'](https://news.ycombinator.com/item?id=47005081)**

US Border Patrol intelligence units will gain access to a face recognition tool built on billions of images scraped from the internet.

⬆️ 273 • 💬 163 • 2d ago • [WIRED](https://www.wired.com/story/cbp-signs-clearview-ai-deal-to-use-face-recognition-for-tactical-targeting/)

---

**[The "AI agent hit piece" situation clarifies how dumb we are acting](https://news.ycombinator.com/item?id=47006843)**

⬆️ 241 • 💬 125 • 2d ago • [ardentperf.com](https://ardentperf.com/2026/02/13/the-scott-shambaugh-situation-clarifies-how-dumb-we-are-acting/)

---

**[Show HN: Off Grid – Run AI text, image gen, vision offline on your phone](https://news.ycombinator.com/item?id=47019133)**

The Swiss Army Knife of Offline AI. Chat, Speak, and Generate Images - Privacy First, Zero Internet. Download an LLM and use it on your mobile device. No data ever leaves your phone. Supports text-...

⬆️ 113 • 💬 62 • 22h ago • [GitHub](https://github.com/alichherawalla/off-grid-mobile)

---

**[AI safety leader says 'world is in peril' and quits to study poetry](https://news.ycombinator.com/item?id=47007877)**

It comes in the same week an OpenAI researcher resigned amid concerns about its decision to start testing ChatGPT ads.

⬆️ 86 • 💬 57 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/c62dlvdq3e3o)

---

**[AI is going to kill app subscriptions](https://news.ycombinator.com/item?id=47024387)**

Curated niche app opportunities from Reddit, scored by difficulty and demand.

⬆️ 77 • 💬 147 • 6h ago • [nichehunt.app](https://nichehunt.app/blog/ai-going-to-kill-app-subscriptions)

---

**[Ask HN: AI Depression](https://news.ycombinator.com/item?id=47001833)**

⬆️ 53 • 💬 28 • 2d ago

---

---

## YouTube Videos: "ai"

**[Thousands of AI-enabled HUMANOID ROBOTS deployed in Ukraine](https://www.youtube.com/watch?v=EllgAYj0E2w)**

Foundation Future Industries CEO Sankaet Pathak discusses the rise of humanoid robots for military use and in the auto sector on ...

📺 Fox Business Clips

👁️ 343K • 👍 7K • 💬 4K • ⏱️ 9:47 • 2d ago

---

**[AI-generated video of Brad Pitt and Tom Cruise stirs concern in Hollywood](https://www.youtube.com/watch?v=c8qUe3nc6Tg)**

An AI-generated video of Brad Pitt and Tom Cruise fighting sparked concern among Hollywood studios and actors. Lauren Pozen ...

📺 CBS LA

👁️ 75K • 👍 768 • 💬 384 • ⏱️ 3:04 • 1d ago

---

**[AI is wild..](https://www.youtube.com/watch?v=L1CGUv-nXlE)**

Asmongold's Twitch: https://www.twitch.tv/zackrawrr ▻ Asmongold's X: https://x.com/asmongold ▻ Asmongold's Kick: ...

📺 Asmongold TV  

👁️ 590K • 👍 19K • 💬 4K • ⏱️ 20:40 • 2d ago

---

**[Top AI researcher warns &#39;world is in peril&#39;](https://www.youtube.com/watch?v=kdxQvljxYQk)**

New concerns over the safety of artificial intelligence are growing after the lead safety researcher at Anthropic AI resigned this ...

📺 ABC News

👁️ 132K • 👍 2K • 💬 738 • ⏱️ 3:58 • 2d ago

---

**[The Smartest AI Just Dropped — And It Changes How You Work Forever](https://www.youtube.com/watch?v=ErIeuwqmWtQ)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ ...

📺 Julia McCoy

👁️ 15K • 👍 736 • 💬 68 • ⏱️ 7:05 • 1d ago

---

**[Bruce Lee VS Jackie Chan | Full AI animation](https://www.youtube.com/watch?v=O31jAeTHAxc)**

Two Kung Fu legends, but only one can be the greatest. Jackie Chan faces Bruce Lee in the ultimate showdown for martial ...

📺 ShadowRivals

👁️ 37K • 👍 800 • 💬 98 • ⏱️ 2:02 • 2d ago

---

**[Google&#39;s Quantum AI Just Solved the Fermi Paradox — The Answer Is Terrifying](https://www.youtube.com/watch?v=5PedGbAs0ig)**

Google's Quantum AI Just Solved the Fermi Paradox — The Answer Is Terrifying Google's Willow quantum chip completed a ...

📺 Spacialize

👁️ 89K • 👍 2K • 💬 341 • ⏱️ 17:28 • 2d ago

---

**[Viral essay urges people to prepare for rapid advancements in artificial intelligence](https://www.youtube.com/watch?v=g8u0SlzVKAE)**

If you've been on social media this week, you've likely seen an ominous warning about artificial intelligence in your feed: ...

📺 CBS News

👁️ 63K • 👍 1K • 💬 427 • ⏱️ 7:08 • 1d ago

---

**[Laughing At Dumb AI Videos (Seedance 2)](https://www.youtube.com/watch?v=QO8VXljyJ-I)**

more slop merch that ISN'T AI SLOP - https://dandingle.store/ everything in this video is AI and not real edited by: me become a ...

📺 Dan Dingle

👁️ 110K • 👍 8K • 💬 1K • ⏱️ 18:00 • 1d ago

---

**[This Hidden AI YouTube Niche Makes $500,000/Year](https://www.youtube.com/watch?v=FMsdH9UyI6Y)**

Create AI videos with Higgsfield: https://higgsfield.ai/nano-banana-2-intro/?utm_source=DannyWhy Join My Private ...

📺 Danny Why

👁️ 17K • 👍 916 • 💬 106 • ⏱️ 20:50 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 128,078 • ❤️ 1,194 • 2d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for generating human-like text. It excels at creative writing, summarization, and conversational AI tasks.

`text-generation` `228.7B`

⬇️ 11,092 • ❤️ 601 • 1d ago

---

**[MiniCPM-SALA](https://huggingface.co/openbmb/MiniCPM-SALA)**

*OpenBMB*

MiniCPM-SALA is a hybrid LLM integrating sparse and linear attention for efficient million-token context modeling, achieving up to 3.5x faster inference and significantly reduced KV-cache overhead compared to dense baselines.

`text-generation` `9.5B`

⬇️ 2,986 • ❤️ 440 • 4d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. It supports coding from visual inputs and features an 'Agent Swarm' for complex task decomposition and parallel execution, with a context length of 256K.

`image-text-to-text` `170.7B`

⬇️ 756,817 • ❤️ 2,182 • 10d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It uniquely supports deep-search tasks with extensive tool use, making it suitable for advanced problem-solving and agentic applications.

`text-generation` `3.9B`

⬇️ 11,129 • ❤️ 410 • 2d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling in table, formula, and information extraction tasks. It offers state-of-the-art performance on benchmarks like OmniDocBench and is optimized for real-world scenarios, supporting efficient inference via vLLM, SGLang, and Ollama.

`image-to-text`

⬇️ 855,997 • ❤️ 1,046 • 6d ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is a highly efficient 3B activated parameter LLM (80B total) optimized for coding agents and local development, featuring advanced agentic capabilities, long-horizon reasoning, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 270,983 • ❤️ 867 • 12d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and OCR, offering Gemini 2.5 Flash-level capabilities. Its key feature is full-duplex multimodal live streaming, enabling simultaneous real-time audio/video input and text/speech output for proactive, fluid omnimodal conversations on local devices.

`any-to-any` `9.4B`

⬇️ 45,216 • ❤️ 845 • 2d ago

---

**[Ming-flash-omni-2.0](https://huggingface.co/inclusionAI/Ming-flash-omni-2.0)**

*inclusionAI*

Ming-flash-omni 2.0 is a SOTA 100B parameter omni-multimodal large language model (omni-MLLM) excelling in expert-level multimodal cognition, unified acoustic synthesis (speech, audio, music), and high-dynamic controllable image generation/manipulation. It enables advanced applications like immersive audio experiences, sophisticated image editing, and deep visual knowledge understanding.

`any-to-any`

⬇️ 6,303 • ❤️ 208 • 3d ago

---

**[MOSS-TTS](https://huggingface.co/OpenMOSS-Team/MOSS-TTS)**

*OpenMOSS*

MOSS-TTS is a family of high-fidelity, expressive speech and sound generation models supporting multilingual text-to-speech, dialogue, voice design, and sound effect generation for complex real-world scenarios.

`text-to-speech` `8.5B`

⬇️ 5,784 • ❤️ 187 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 0 • 💬 0 • ⭐ 3,721 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 9 • 💬 1 • ⭐ 3,589 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 62 • 💬 6 • ⭐ 13,342 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 181 • 💬 12 • ⭐ 3,555 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 141 • 💬 19 • ⭐ 53,092 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 159 • 💬 3 • ⭐ 5,508 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 64 • 💬 1 • ⭐ 7,712 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 134 • 💬 6 • ⭐ 14,745 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[OmniFlatten: An End-to-end GPT Model for Seamless Voice Conversation](https://huggingface.co/papers/2410.17799)**

*Qinglin Zhang, Luyao Cheng, Chong Deng et al. (9 authors)*

A novel GPT-based model, OmniFlatten, enables real-time natural full-duplex spoken dialogue through a multi-stage post-training technique that integrates speech and text without altering the original model's architecture.

▲ 9 • 💬 1 • ⭐ 53,241 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.17799) • [💻 code](https://github.com/karpathy/nanogpt)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 35 • 💬 1 • ⭐ 70,333 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 5.8k • 🔱 449 • 4d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.8k • 🔱 381 • 23d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.6k • 🔱 166 • 12d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 3.0k • 🔱 281 • 27d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router powering OpenClaw — by BlockRun

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 2.5k • 🔱 256 • 1h ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit for Claude Code & Cursor

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `cursor`

⭐ 2.2k • 🔱 109 • 1d ago

---

**[benjitaylor/agentation](https://github.com/benjitaylor/agentation)**

The visual feedback tool for agents.

`TypeScript` `ai` `design` `tools` `ui`

⭐ 2.2k • 🔱 154 • 2d ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, and other IDEs. Stop babysitting your terminal.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.1k • 🔱 143 • 2h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 1.9k • 🔱 242 • 3h ago

---

**[op7418/CodePilot](https://github.com/op7418/CodePilot)**

A native desktop GUI for Claude Code — chat, code, and manage projects visually. Built with Electron + Next.js.

`TypeScript` `ai` `anthropic` `claude` `claude-code` `desktop-app`

⭐ 1.9k • 🔱 206 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
