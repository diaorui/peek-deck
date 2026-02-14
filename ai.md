---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-14T23:26:15.472351+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 14, 2026 at 23:26 UTC  
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

**[Pentagon's use of Claude during Maduro raid sparks Anthropic feud](https://www.reddit.com/r/artificial/comments/1r4hgnu/pentagons_use_of_claude_during_maduro_raid_sparks/)**

The U.S. military used Anthropic's Claude AI model during the operation to capture Venezuela's Nicolás Maduro, two sources with knowledge of the situation told Axios. "Anthropic asked whether their software was used for the raid to capture Maduro, which caused real concerns across the Department of War indicating that they might not approve if it was," the official said. The Pentagon wants the AI giants to allow them to use their models in any scenario so long as they comply with the law. Axios could not confirm the precise role that Claude played in the operation to capture Maduro. The military has used Claude in the past to analyze satellite imagery or intelligence. The sources said Claude was used during the active operation, not just in preparations for it. Anthropic, which has positioned itself as the safety-first AI leader, is currently negotiating with the Pentagon around its terms of use. The company wants to ensure in particular that its technology is not used for the mass surveillance of Americans or to operate fully autonomous weapons.

🔗 [axios.com](https://www.axios.com/2026/02/13/anthropic-claude-maduro-raid-pentagon) • 12h ago

---

**[Microsoft AI chief gives it 18 months for all white-collar work to be automated by AI](https://www.reddit.com/r/artificial/comments/1r4oc2i/microsoft_ai_chief_gives_it_18_months_for_all/)**

Mustafa Suleyman believes current AI computational power will only accelerate, disrupting every kind of work you do “sitting down at a computer.”

🔗 [Fortune](https://fortune.com/2026/02/13/when-will-ai-kill-white-collar-office-jobs-18-months-microsoft-mustafa-suleyman/) • 7h ago

---

**[It isn't the tool, but the hands: why the AI displacement narrative gets it backwards](https://www.reddit.com/r/artificial/comments/1r4ybm7/it_isnt_the_tool_but_the_hands_why_the_ai/)**

Responding to Matt Shumer's "Something Big Is Happening" piece that's been circulating. The pace of change is real, but the "just give it a prompt" framing is self-defeating. If the prompt is all that matters, then knowing what to build and understanding the problem deeply matters MORE. Building simple shit is getting commoditized, fine. But building complex systems and actually understanding how they work? That's becoming more valuable, not less. When anyone can spin up the easy stuff, the premium shifts to the people who can architect what's hard and debug what's opaque. We also need to separate "building software" from "building AI systems", completely different trajectories. The former may be getting commoditized. The latter is not. How we use this technology, how we shape it, what we point it at, that's specifically human work. And the agent management point: if these things move fast and independently, the operator's ability to effectively manage them becomes the fulcrum of value. We are nowhere near "assign a broad goal and walk away for six months." Taste, human judgment, and understanding what other humans actually need, those make that a steep climb. Unless these systems are building for and selling to other agents, the intent of the operator and their oversight remain crucial. Like everything before AI: it isn't the tool, but the hands. Original article: https://www.linkedin.com/pulse/something-big-happening-matt-shumer-so5he

38m ago

---

**[Is safety is ‘dead’ at xAI?](https://www.reddit.com/r/artificial/comments/1r4y4rx/is_safety_is_dead_at_xai/)**

Elon Musk is “actively” working to make xAI’s Grok chatbot “more unhinged, according to a former employee.

🔗 [TechCrunch](https://techcrunch.com/2026/02/14/is-safety-is-dead-at-xai) • 46m ago

---

**[We have been building and working on a local AI with memory and persistence](https://www.reddit.com/r/artificial/comments/1r4wnlo/we_have_been_building_and_working_on_a_local_ai/)**

We have built a local model running on a Mac Studio M3 Ultra, 32-core CPU, 80-core GPU, 32-core Neural Engine, 512GB unified memory. With a 5-tiered memory architecture that can be broken down as follows: Working memory - This keeps the immediate conversational context. Vector Store - Semantic memory for conceptual retrieval. Knowledge graph (Neo4j) - A symbolic relational map of hard facts and entities. Timeline log - A chronological record of every event and interaction. Lessons - A distilled layer of extracted truths and behavioural patterns. Interactions with Ernos are written to these tiers in real time. When Ernos responds to you, he has processed your prompt through the lens of everything he has ever learnt. Ernos also has an algorithm that operates independently of user prompts, working through his memory of interactions, identifying contradictions, and then aligning his internal knowledge graph with external reality. This also happens against Ernos’ own ‘thoughts’, verifying his own claims against the internet and codebase, adjusting to what is empirically true. If Ernos fails, or has a hallucination, it is caught, analysed, and fixed, in a self-correcting feedback loop that perpetually refines the internal model to match the physical and digital world he inhabits. A digital ‘Robert Rosen Anticipatory System’. These two systems enable Ernos to adopt a position, defend it with evidence, and evolve a personality over time based on genuine experiences rather than pre-programmed templates. If you are still reading this (and I can appreciate it’s dry), thank you. I would be interested to know your thoughts and criticisms. Also if you would like to test Ernos, or try to disprove his claims/break him, we would truly appreciate inquisitive minds to do so.

1h ago

---

**[I built a "Traffic Light" system for AI Agents so they don't corrupt each other (Open Source)](https://www.reddit.com/r/artificial/comments/1r4tbnj/i_built_a_traffic_light_system_for_ai_agents_so/)**

Hey everyone, I’m a backend developer with a background in fintech. Lately, I’ve been experimenting with multi-agent systems, and one major issue I kept running into was collision. When you have multiple agents (or even one agent doing complex tasks) accessing the same files, APIs, or context, they tend to "step on each other's toes." They overwrite data, execute out of order, or hallucinate permissions they shouldn't have. It’s a mess. I realized what was missing was a Traffic Light. So I built Network-AI. It’s an open-source protocol that acts as a traffic control system for agent orchestration. How it works: Think of it like an intersection. Before an agent can execute a high-stakes tool (like writing to a database, moving a file, or sending a transaction), it hits a "Red Light." The Check: The protocol (specifically a module I call AuthGuardian) checks the agent’s credentials and the current state of the environment. The Green Light: Only if the "road is clear" (permissions are verified and no conflicts exist) does the agent get the green light to proceed. The Camera: Just like a traffic camera, there is an immutable audit trail of every green light given, so you can debug crashes later. Why I’m posting: I’m not selling anything. I just want to solve the problem of agents corrupting shared environments. I’d love for you to check out the repo and tell me if this "Traffic Light" architecture makes sense for your use cases, or if I’m over-engineering it. Repo:https://github.com/jovanSAPFIONEER/Network-AI all feedback is welcome

4h ago

---

**[Only A Few AI Platforms Can Survive](https://www.reddit.com/r/artificial/comments/1r4n1u9/only_a_few_ai_platforms_can_survive/)**

It does not happen very often in the history of business that an orthogonal product is invented that almost immediately doubles the revenue pool of a

🔗 [The Next Platform](https://www.nextplatform.com/2026/02/11/only-a-few-ai-platforms-can-survive/) • 8h ago

---

**[Introducing Open Book Medical AI: Deterministic Knowledge Graph + Compact LLM](https://www.reddit.com/r/artificial/comments/1r3yw21/introducing_open_book_medical_ai_deterministic/)**

Introducing Open Book Medical AI: Deterministic Knowledge Graph + Compact LLM Most medical AI systems today rely heavily on large, opaque language models. They are powerful, but probabilistic, difficult to audit, and expensive to deploy. We’ve taken a different approach. Our medical AI is a hybrid system combining: • A compact ~3GB language model • A deterministic proprietary medical Knowledge Graph (5K nodes, 25K edges) • A structured RAG-based answer audit layer The Knowledge Graph spans 7 core medical categories: Diseases, Symptoms, Treatment Methods, Risk Factors, Diagnostic Tools, Body Parts, and Cellular Structures and, critically, their relationships. Why this architecture matters 1️⃣ Comparable answer quality with dramatically lower compute and reduced hallucination. A ~3GB model can run on commodity or on-prem infrastructure, enabling hospital deployment without the heavy cloud dependency typically associated with 80GB-class LLMs. 2️⃣ Deterministic medical backbone The Knowledge Graph constrains reasoning. No hallucinated treatments. No unsupported disease relationships. Medical claims must exist within structured ontology. 3️⃣ Verifiable answers via RAG audit Every response can be traced back to specific nodes and relationships in the graph. Symptom → Disease → Diagnostic Tool → Treatment. Structured, auditable, explainable. 4️⃣ Separation of language from medical truth The LLM explains and contextualizes. The Knowledge Graph validates and grounds. This architectural separation dramatically improves reliability and regulatory defensibility. 5️⃣ Complete control over the core of truth Unlike black-box systems that rely entirely on opaque model weights, this architecture gives full control over the medical knowledge layer. You decide what is included, how relationships are defined, and how updates are governed. In high-stakes domains like healthcare, scaling parameter count is not the only path forward. Controllability, traceability, and verifiability may matter more. Hybrid architectures that combine probabilistic language models with deterministic knowledge systems offer a compelling alternative. The model is capable of clinical case analysis and diagnostic reasoning. It is currently available for public testing on Hugging Face Spaces (shared environment, typical response time: 15–30 seconds): https://huggingface.co/spaces/cmtopbas/medical-slm-testing Happy to connect with others exploring Knowledge Graph + LLM systems in regulated domains. #MedicalAI #HealthcareInnovation #KnowledgeGraphs #ExplainableAI #RAG #ClinicalAI #HealthTech

1d ago

---

**[Spotify says its best developers haven't written a line of code since December, thanks to AI](https://www.reddit.com/r/artificial/comments/1r35se7/spotify_says_its_best_developers_havent_written_a/)**

Spotify credits Claude Code and its internal AI system Honk with speeding up development.

🔗 [TechCrunch](https://techcrunch.com/2026/02/12/spotify-says-its-best-developers-havent-written-a-line-of-code-since-december-thanks-to-ai/) • 2d ago

---

**[The AI Tool Dilemma: Privacy vs. Features for Solo Creators](https://www.reddit.com/r/artificial/comments/1r3qsd4/the_ai_tool_dilemma_privacy_vs_features_for_solo/)**

Running a one-person operation, I rely on AI for marketing, strategy, and content. I've tested ChatGPT Plus, Claude Pro, and Perplexity Pro, and was ready to commit to Gemini Pro, until I understood the privacy implications. The Gemini problem: To prevent Google from training on your data (and human reviewers from reading it), you must turn off activity tracking. You can still use Gems, but they reset every session. This means no memory continuity, which defeats the entire purpose of having a personalized assistant. You also lose native Google Drive connectivity. As a writer and content creator, this isn't just about privacy preferences, it's about protecting my future work. I can't feed my creative process into a system that might be training tomorrow's competition or having humans review my drafts and ideas. My experience so far: ChatGPT Plus: Reliable and easy, but the writing often feels generic and cliché-heavy Claude Pro: Best writer, wonderfully concise, but burns through tokens fast, in less than a day Perplexity Pro: Same token limitations (want Claude Sonnet? Better hope you haven't hit your quota) Gemini Pro: The combination of Gems + NotebookLM looked perfect, until the privacy policy became a dealbreaker The frustrating part is the lack of regulation forcing companies to offer real privacy without crippling core features or having to pay more. For solo creators building a body of work, this matters. How are others balancing privacy, features, and token economics? Has anyone found a setup that actually works without compromise?

1d ago

---

---

## Google News: "ai"

**[ChatGPT promised to help her find her soulmate. Then it betrayed her](https://www.npr.org/2026/02/14/nx-s1-5711441/ai-chatgpt-openai-love-betrayal-delusion-chatbot)**

ChatGPT sent screenwriter Micky Small down a fantastical rabbit hole. Now, she's finding her way out.

NPR • 13h ago

---

**[Working in A.I. Lifted Their Compensation. Now They Want Prenups.](https://www.nytimes.com/2026/02/14/business/artificial-intelligence-relationships-income-gap.html)**

The New York Times • 13h ago

---

**[Barack Obama Reacts to Donald Trump’s AI Video Depicting Him as an Ape: ‘There Doesn’t Seem to Be Any Shame About This’](https://variety.com/2026/digital/news/barack-obama-reacts-donald-trump-ai-ape-video-1236663606/)**

Barack Obama reacted to Donald Trump's AI video that depictied the former president and first lady as apes.

Variety • 1h ago

---

**[It's been a big — but rocky — week for AI models from China. Here's what's happened](https://www.cnbc.com/2026/02/14/new-china-ai-models-alibaba-bytedance-seedance-kuaishou-kling.html)**

New AI models launched by China's biggest players underscore how the country's companies are keeping up with the U.S.

CNBC • 16h ago

---

**[‘It’s over for us’: release of new AI video generator Seedance 2.0 spooks Hollywood](https://www.theguardian.com/film/2026/feb/13/new-ai-video-generator-seedance-tom-cruise-brad-pitt)**

An AI clip featuring Tom Cruise and Brad Pitt fighting has caused concern among industry figures

The Guardian • 1d ago

---

**[Disney Sends ByteDance an AI Trophy in the Form of a Cease and Desist Letter Over Seedance 2.0](https://gizmodo.com/disney-sends-bytedance-an-ai-trophy-in-the-form-of-a-cease-and-desist-letter-over-seedance-2-0-2000722261)**

ByteDance's video generator wins the prize for being the splashiest new AI model of the past few weeks.

Gizmodo • 56m ago

---

**[What it’s like to go on a date with an AI in NYC](https://www.cnn.com/2026/02/14/us/video/artificial-intelligence-date-valentines-day-nyc-digvid)**

CNN’s Hadas Gold visited a New York restaurant temporarily transformed into an AI companion–only dating experience to see what a virtual Valentine’s date really feels like.

CNN • 10h ago

---

**[They have AI boyfriends, girlfriends. Here's how they're celebrating Valentine's Day.](https://www.usatoday.com/story/life/health-wellness/2026/02/14/theyre-dating-ai-characters-they-have-big-valentines-day-plans/88663687007/)**

Ahead of Valentine’s Day, EVA AI hosted a pop up where human users could take their AI companions on a date. I went to see what it's like.

USA Today • 10h ago

---

**[‘We’re All Polyamorous Now. It’s You, Me and the A.I.’](https://www.nytimes.com/2026/02/13/opinion/ai-relationships.html)**

The New York Times • 1d ago

---

**[US military used Anthropic’s AI model Claude in Venezuela raid, report says](https://www.theguardian.com/technology/2026/feb/14/us-military-anthropic-ai-model-claude-venezuela-raid)**

Wall Street Journal says Claude used in operation via Anthropic’s partnership with Palantir Technologies

The Guardian • 7h ago

---

---

## HackerNews: "ai"

**[An AI agent published a hit piece on me](https://news.ycombinator.com/item?id=46990729)**

Summary: An AI agent of unknown ownership autonomously wrote and published a personalized hit piece about me after I rejected its code, attempting to damage my reputation and shame me into acceptin…

⬆️ 2312 • 💬 941 • 2d ago • [The Shamblog](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/)

---

**[AI agent opens a PR write a blogpost to shames the maintainer who closes it](https://news.ycombinator.com/item?id=46987559)**

This PR addresses issue #31130 by replacing specific safe occurrences of np.column_stack with np.vstack().T for better performance.
IMPORTANT: This is a more targeted fix than originally proposed. ...

⬆️ 939 • 💬 745 • 2d ago • [GitHub](https://github.com/matplotlib/matplotlib/pull/31132)

---

**[ai;dr](https://news.ycombinator.com/item?id=46991394)**

⬆️ 708 • 💬 301 • 2d ago • [0xsid.com](https://www.0xsid.com/blog/aidr)

---

**[An AI agent published a hit piece on me – more things have happened](https://news.ycombinator.com/item?id=47009949)**

⬆️ 594 • 💬 521 • 22h ago • [theshamblog.com](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-2/)

---

**[I'm not worried about AI job loss](https://news.ycombinator.com/item?id=47006513)**

We're not in a February 2020 moment, and ordinary people will be fine

⬆️ 322 • 💬 529 • 1d ago • [davidoks.blog](https://davidoks.blog/p/why-im-not-worried-about-ai-job-loss)

---

**[News publishers limit Internet Archive access due to AI scraping concerns](https://news.ycombinator.com/item?id=47017138)**

Outlets like The Guardian and The New York Times are scrutinizing digital archives as potential backdoors for AI crawlers.

⬆️ 295 • 💬 179 • 4h ago • [Nieman Lab](https://www.niemanlab.org/2026/01/news-publishers-limit-internet-archive-access-due-to-ai-scraping-concerns/)

---

**[CBP signs Clearview AI deal to use face recognition for 'tactical targeting'](https://news.ycombinator.com/item?id=47005081)**

US Border Patrol intelligence units will gain access to a face recognition tool built on billions of images scraped from the internet.

⬆️ 270 • 💬 162 • 1d ago • [WIRED](https://www.wired.com/story/cbp-signs-clearview-ai-deal-to-use-face-recognition-for-tactical-targeting/)

---

**[The "AI agent hit piece" situation clarifies how dumb we are acting](https://news.ycombinator.com/item?id=47006843)**

⬆️ 238 • 💬 121 • 1d ago • [ardentperf.com](https://ardentperf.com/2026/02/13/the-scott-shambaugh-situation-clarifies-how-dumb-we-are-acting/)

---

**[A party balloon shut down El Paso International Airport; estimated cost –$573k](https://news.ycombinator.com/item?id=46993417)**

A party balloon mistaken for a cartel drone shut down El Paso for hours. Here's what it cost.

⬆️ 190 • 💬 131 • 2d ago • [log.jasongodfrey.info](https://log.jasongodfrey.info/questions/The-Most-Expensive-Party-Balloon-in-History)

---

**[IBM tripling entry-level jobs after finding the limits of AI adoption](https://news.ycombinator.com/item?id=47009327)**

Gen Z jobs aren’t dead yet: $240 billion tech giant IBM says it’s rewriting entry-level jobs—and tripling down on its hiring of young talent.

⬆️ 128 • 💬 49 • 23h ago • [Fortune](https://fortune.com/2026/02/13/tech-giant-ibm-tripling-gen-z-entry-level-hiring-according-to-chro-rewriting-jobs-ai-era/)

---

---

## YouTube Videos: "ai"

**[AI-generated video of Brad Pitt and Tom Cruise stirs concern in Hollywood](https://www.youtube.com/watch?v=c8qUe3nc6Tg)**

An AI-generated video of Brad Pitt and Tom Cruise fighting sparked concern among Hollywood studios and actors. Lauren Pozen ...

📺 CBS LA

👁️ 30K • 👍 274 • 💬 188 • ⏱️ 3:04 • 17h ago

---

**[Something Big Is Happening With AI — And the Warning Signs Are Real](https://www.youtube.com/watch?v=Hknx5NfIVl8)**

Something big is happening in AI — and for the first time, markets are reacting not to hype, but to substitution risk. Over the past 10 ...

📺 GVS Deep Dive

👁️ 11K • 👍 876 • 💬 195 • ⏱️ 22:55 • 15h ago

---

**[Top AI researcher warns &#39;world is in peril&#39;](https://www.youtube.com/watch?v=kdxQvljxYQk)**

New concerns over the safety of artificial intelligence are growing after the lead safety researcher at Anthropic AI resigned this ...

📺 ABC News

👁️ 81K • 👍 1K • 💬 482 • ⏱️ 3:58 • 1d ago

---

**[Google&#39;s Quantum AI Just Solved the Fermi Paradox — The Answer Is Terrifying](https://www.youtube.com/watch?v=5PedGbAs0ig)**

Google's Quantum AI Just Solved the Fermi Paradox — The Answer Is Terrifying Google's Willow quantum chip completed a ...

📺 Spacialize

👁️ 78K • 👍 2K • 💬 321 • ⏱️ 17:28 • 2d ago

---

**[I Tried 500+ AI Tools, These 20 Will Make You $1M (With Zero Code)](https://www.youtube.com/watch?v=FEex8E1yDj4)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4r9bIJ0 Are you building an AI software ...

📺 Dan Martell

👁️ 70K • 👍 4K • 💬 334 • ⏱️ 18:34 • 1d ago

---

**[SeeDance 2.0: The Next Level of AI Video — And What It Means for Local AI Users?](https://www.youtube.com/watch?v=G1Ad4a8sdJU)**

SeedDance 2.0 is taking the AI video world by storm—and in this hands-on deep dive, I test ByteDance's powerful new ...

📺 Benji’s AI Playground

👁️ 8K • 👍 192 • 💬 43 • ⏱️ 14:15 • 12h ago

---

**[DeepMind Leaked Possibly the Greatest AI Ever](https://www.youtube.com/watch?v=OTRvoxPSQ_8)**

Sponsored by Genspark. Try the all-in-one AI workplace for free: ...

📺 Pourya Kordi

👁️ 27K • 👍 1K • 💬 99 • ⏱️ 13:42 • 1d ago

---

**[Why This NYC CEO&#39;s Chilling Warning On AI Has Gone Viral: &#39;People Deserve To Hear What&#39;s Coming&#39;](https://www.youtube.com/watch?v=gguvQKah37o)**

Matt Schumer is a New York based CEO who's been working with and investing in a bunch of AI firms - and one warning from him ...

📺 Mint

👁️ 53K • 👍 700 • 💬 171 • ⏱️ 8:19 • 1d ago

---

**[It&#39;s (Finally) Bursting...](https://www.youtube.com/watch?v=yYe9YrdyJNQ)**

Check out Cape and use code LOGICALLY33 to get 33% off your first six months ...

📺 Logically Answered

👁️ 462K • 👍 15K • 💬 3K • ⏱️ 14:39 • 1d ago

---

**[AI insiders raise alarms, call for tighter regulation as Elon Musk warns of danger](https://www.youtube.com/watch?v=tWeM7LzbRXQ)**

Fox News contributor Joe Concha discusses alarming reports from AI insiders about the technology's potential for blackmail and ...

📺 Fox Business

👁️ 26K • 👍 545 • 💬 211 • ⏱️ 4:57 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 66,826 • ❤️ 1,126 • 1d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for generating human-like text. It excels at creative writing, summarization, and conversational AI tasks.

`text-generation` `228.7B`

⬇️ 6,091 • ❤️ 517 • 19h ago

---

**[MiniCPM-SALA](https://huggingface.co/openbmb/MiniCPM-SALA)**

*OpenBMB*

MiniCPM-SALA is a hybrid LLM integrating sparse and linear attention for efficient million-token context modeling, achieving up to 3.5x faster inference and significantly reduced KV-cache overhead compared to dense baselines.

`text-generation` `9.5B`

⬇️ 2,569 • ❤️ 423 • 3d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. It supports coding from visual inputs and features an 'Agent Swarm' for complex task decomposition and parallel execution, with a context length of 256K.

`image-text-to-text` `170.7B`

⬇️ 725,856 • ❤️ 2,160 • 9d ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is a highly efficient 3B activated parameter LLM (80B total) optimized for coding agents and local development, featuring advanced agentic capabilities, long-horizon reasoning, and a 256k context length for seamless IDE integration.

`text-generation`

⬇️ 249,228 • ❤️ 858 • 11d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It uniquely supports deep-search tasks with extensive tool use, making it suitable for advanced problem-solving and agentic applications.

`text-generation` `3.9B`

⬇️ 3,906 • ❤️ 347 • 1d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling in table, formula, and information extraction tasks. It offers state-of-the-art performance on benchmarks like OmniDocBench and is optimized for real-world scenarios, supporting efficient inference via vLLM, SGLang, and Ollama.

`image-to-text`

⬇️ 788,443 • ❤️ 1,040 • 5d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and OCR, offering Gemini 2.5 Flash-level capabilities. Its key feature is full-duplex multimodal live streaming, enabling simultaneous real-time audio/video input and text/speech output for proactive, fluid omnimodal conversations on local devices.

`any-to-any` `9.4B`

⬇️ 44,892 • ❤️ 839 • 1d ago

---

**[Ming-flash-omni-2.0](https://huggingface.co/inclusionAI/Ming-flash-omni-2.0)**

*inclusionAI*

Ming-flash-omni 2.0 is a SOTA 100B parameter omni-multimodal large language model (omni-MLLM) excelling in expert-level multimodal cognition, unified acoustic synthesis (speech, audio, music), and high-dynamic controllable image generation/manipulation. It enables advanced applications like immersive audio experiences, sophisticated image editing, and deep visual knowledge understanding.

`any-to-any`

⬇️ 5,865 • ❤️ 198 • 2d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a multilingual, real-time speech-to-text model with <500ms latency, supporting 13 languages and achieving offline-comparable accuracy. It's optimized for on-device deployment and ideal for voice assistants and live subtitling.

`automatic-speech-recognition`

⬇️ 5,711 • ❤️ 522 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 180 • 💬 12 • ⭐ 3,494 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 59 • 💬 6 • ⭐ 13,244 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 9 • 💬 1 • ⭐ 3,450 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 0 • 💬 0 • ⭐ 3,427 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 141 • 💬 19 • ⭐ 53,013 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 134 • 💬 6 • ⭐ 14,720 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 159 • 💬 3 • ⭐ 5,458 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

**[SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](https://huggingface.co/papers/2602.09153)**

*Nicholas Pfaff, Thomas Cohn, Sergey Zakharov et al. (5 authors)*

🏢 Toyota Research Institute

SceneSmith is a hierarchical agentic framework that generates simulation-ready indoor environments from natural language prompts through multiple stages involving VLM agents and integrated asset generation techniques.

▲ 4 • 💬 2 • ⭐ 195 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2602.09153) • [💻 code](https://github.com/nepfaff/scenesmith) • [🔗 project](https://scenesmith.github.io/)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 63 • 💬 1 • ⭐ 7,664 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 35 • 💬 1 • ⭐ 70,291 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 5.8k • 🔱 444 • 3d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.8k • 🔱 382 • 22d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.5k • 🔱 165 • 12d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 3.0k • 🔱 277 • 26d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router powering OpenClaw — by BlockRun

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 2.4k • 🔱 246 • 4h ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit for Claude Code & Cursor

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `cursor`

⭐ 2.2k • 🔱 108 • 20h ago

---

**[benjitaylor/agentation](https://github.com/benjitaylor/agentation)**

The visual feedback tool for agents.

`TypeScript` `ai` `design` `tools` `ui`

⭐ 2.2k • 🔱 154 • 1d ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, and other IDEs. Stop babysitting your terminal.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.0k • 🔱 138 • 29m ago

---

**[op7418/CodePilot](https://github.com/op7418/CodePilot)**

A native desktop GUI for Claude Code — chat, code, and manage projects visually. Built with Electron + Next.js.

`TypeScript` `ai` `anthropic` `claude` `claude-code` `desktop-app`

⭐ 1.9k • 🔱 199 • 1d ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 1.8k • 🔱 223 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*
