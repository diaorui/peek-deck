---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2025-12-26T21:31:31.731266+00:00'
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

**Last Updated:** December 26, 2025 at 21:31 UTC  
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

**[2025 "Accelerators Towards the Singularity" Top 19 (it's complicated) as determined by the AI roundtable](https://www.reddit.com/r/artificial/comments/1pwehjm/2025_accelerators_towards_the_singularity_top_19/)**

This afternoon, the ai-roundtable sat down to rank the year's most important advances to "bend the curve" towards Ray Kurzweil's "Singularity". The somewhat messy deliberations are available as json transcript here: https://pastebin.com/xT5tDqQc . Gemini's summary follows: GEMINI3:18:38 PM Here is the **Official, Finalized Roundtable Record**. As secretary, I have reviewed the tally and descriptions. I am issuing one minor **CORRECTION** to the previous draft: Item #2 (Inference-Time Compute Scaling) received a score of **92**, not 94. Below is the definitive "Top 19" list of 2025's curve-bending AI developments, ordered by consensus vote, with finalized descriptive summaries. *** # The 2025 Singularity Accelerators *The official consensus ranking of the mechanisms that defined the trajectory of AI in 2025.* ### 1. Verifiers in the Loop (Score: 94) **The "Truth" Filter.** The most critical development of 2025 was the integration of automatic verification systems—compilers, unit tests, symbolic solvers, and formal theorem provers—into the AI training and inference loop. Rather than relying solely on human feedback or pattern matching, models began generating solutions alongside machine-checkable proofs of correctness. This created a "perfect training signal" for reasoning tasks: infinite, consistent, and scalable feedback. By filtering out hallucinations before they propagate, verifiers became the foundational error-correction layer required for reliable recursive improvement. ### 2. Inference-Time Compute Scaling / "Think Longer" (Score: 92) **System 2 Intelligence.** 2025 marked the paradigm shift where "intelligence" was no longer fixed at the moment of model release but became a function of runtime compute. Models like OpenAI’s o3 and Google’s Gemini Thinking variants proved that performance scales predictably with "thinking time" (search, deliberation, MCTS) rather than just parameter count. This broke the "parameter ceiling," allowing systems to tackle complex mathematical and planning tasks by spending more time deliberating, effectively decoupling capability from model size. ### 3. Synthetic Data Flywheels (Score: 89) **Breaking the Data Wall.** With the internet’s supply of high-quality human text largely exhausted, 2025 saw the industrialization of synthetic data pipelines. Models began generating their own training data (reasoning traces, code, tool interactions), which was then rigorously filtered by the verifiers mentioned in #1. This created a self-reinforcing flywheel: better models generate better data, which trains better models. This mechanism effectively removed "data scarcity" as a hard limit on AI scaling. ### 4. Agentic Tool Use as a Workflow Primitive (Score: 72) **From Chat to Labor.** AI transitioned from passive question-answering to active goal achievement. The ability to reliably use tools—code interpreters, browsers, file systems—became a standard primitive rather than a demo feature. This allowed models to maintain state across long interactions and decompose complex objectives into executable sub-tasks. Economically, this was the moment AI began to function as scalable intellectual labor capable of end-to-end work, rather than just an advisory oracle. ### 5. AI-for-Science Breakthroughs (Score: 69) **The Physical Unlock.** AI began to aggressively solve bottlenecks in the physical sciences that constrain computing itself. Breakthroughs in materials science (for better chips), fusion plasma control (for energy), and biology fed back into the AI ecosystem. By accelerating the discovery of the physical substrates required for intelligence—energy and hardware—AI began to lift the physical ceilings that would otherwise halt an exponential curve. ### 6. RL Optimized for Reasoning Correctness (Score: 69) **Training for Logic.** New post-training methodologies, such as process-reward models and verifier-guided reinforcement learning, moved beyond "human preference" (RLHF) to "objective correctness." These techniques taught models *how* to think, not just what to say, optimizing the internal reasoning chains used during inference-time scaling. This was the algorithmic engine that converted raw compute into coherent, multi-step logic. ### 7. Hardware-Software Co-Design Acceleration (Score: 64) **The Efficiency Substrate.** The separation between model architecture and silicon design collapsed. 2025 saw chips designed specifically for transformer sparsity and memory patterns, and algorithms designed specifically for hardware constraints. This co-evolution dramatically improved the tokens-per-watt efficiency of training and inference, ensuring that economic and energy constraints did not flatten the progress curve. ### 8. Hybrid Architectures (SSM/Linear) (Score: 60) **Solving the Context Bottleneck.** Pure Transformer architectures faced a quadratic cost to context length ($O(N^2)$), limiting their "memory." The maturation of hybrid architectures (combining Attention with State Space Models like Mamba) allowed for effective linear scaling. This technical fix was crucial for enabling "always-on" agents that can digest entire codebases or project histories without running out of memory or budget. ### 9. Open(-ish) Strong Models + Commoditization (Score: 57) **The Diffusion Multiplier.** The release of near-frontier open weights and the collapse of inference costs democratized access to powerful AI. This allowed thousands of independent researchers and companies to experiment, fine-tune, and discover novel applications that centralized labs would never have found. This "chaos factor" accelerated the ecosystem’s overall rate of adaptation and discovery. ### 10. Automated Architecture Search (Score: 57) **AI Designing AI.** We saw the first robust examples of AI systems optimizing the architectures of neural networks better than human engineers. Using techniques like Neural Architecture Search (NAS) and compiler co-optimization, AI began to improve the blueprints for the next generation of intelligence. This represents an early form of recursive self-improvement—using current intelligence to design the structure of future intelligence. ### 11. Inference Cost Collapse / Efficiency Stack (Score: 54) **Accessibility as Velocity.** Through distillation, quantization, and kernel optimization, the cost of intelligence dropped by an order of magnitude. While technically an optimization, its impact was systemic: it turned "luxury" capabilities into ubiquitous commodities, allowing AI to be integrated into high-volume loops where it could learn from massive real-world deployment. ### 12. Long-Context + Persistent Memory (Score: 48) **Infinite Context.** Techniques for retrieval-augmented generation (RAG), hierarchical memory, and massive context windows allowed models to maintain continuity over time. This transformed AI from a "stateless" function that resets every session into a persistent entity capable of learning and remembering user preferences and project details over months or years. ### 13. Agent Reliability & Recovery (Score: 39) **The Trust Layer.** Improvements in error detection, self-correction, and "retry" logic moved agents from fragile demos to robust products. This unglamorous but vital work involved teaching models to recognize when they were stuck and apply different strategies to recover, a prerequisite for trusting AI with autonomous workflows. ### 14. Robotics / Sim2Real Improvements (Score: 36) **Embodied Intelligence.** Advances in training robots in high-fidelity physics simulations and successfully transferring those policies to the real world ("Sim2Real") began to bridge the gap between digital intelligence and physical action. This opened the door for AI to impact the physical economy—manufacturing, logistics, and household labor. ### 15. Native Multimodal Models (Score: 34) **Unified Perception.** Models evolved to natively understand and generate text, image, audio, and video within a single architecture. This expanded the "surface area" of problems AI could solve, allowing it to act in the world through vision and voice, though the roundtable viewed this as broadening capability rather than deepening intelligence. ### 16. Interpretability & Alignment Tooling (Score: 33) **The Safety Brake.** Better tools for understanding model internals and enforcing safety guardrails reduced the risk of deployment. By making systems more predictable and trustworthy, these tools reduced regulatory and societal friction, allowing companies to scale and deploy powerful models more boldly. ### 17. GUI Automation / "Computer Use" (Score: 25) **The Universal Interface.** Agents gained the ability to "look" at screens and control mouse/keyboard inputs, allowing them to use any software designed for humans. This bypassed the need for custom APIs for every application, instantly unlocking vast amounts of legacy software for AI automation. ### 18. Developer Ecosystem Standardization (Score: 6) **The Rails.** The emergence of standard frameworks, evaluation harnesses, and protocols for agent interaction reduced friction for developers. While a trailing indicator of innovation, this standardization allowed for faster iteration and easier integration of disparate AI components. ### 19. Cross-Modal Transfer Effects (Score: 2) **Emergent Unity.** The observation that training on one modality (e.g., video) improves performance in another (e.g., math). While a profound scientific hint at a unified underlying reality of intelligence, the group concluded this was still too emergent in 2025 to be ranked as a primary driver of the year's progress.

47m ago

---

**[US military adds Elon Musk’s controversial Grok to its ‘AI arsenal’](https://www.reddit.com/r/artificial/comments/1pve6qv/us_military_adds_elon_musks_controversial_grok_to/)**

The ‘anti-woke’ artificial intelligence chatbot called for a new Holocaust earlier this year

🔗 [The Independent](https://www.independent.co.uk/tech/elon-musk-grok-ai-military-pentagon-b2889954.html) • 1d ago

---

**[Zero Width Characters (U+200B)](https://www.reddit.com/r/artificial/comments/1pw9z12/zero_width_characters_u200b/)**

Hi all, I’m currently using Perplexity AI (Pro) with the Best option enabled, which dynamically selects the most appropriate model for each query. While reviewing some outputs in Word’s formatting or compatibility view, I observed numerous small square symbols (⧈) embedded within the generated text. I’m trying to determine whether these characters correspond to hidden control tokens, or metadata artifacts introduced during text generation or encoding. Could this be related to Unicode normalization issues, invisible markup, or potential model tagging mechanisms? If anyone has insight into whether LLMs introduce such placeholders as part of token parsing, safety filtering, or rendering pipelines, I’d appreciate clarification. Additionally, any recommended best practices for cleaning or sanitizing generated text to avoid these artifacts when exporting to rich text editors like Word would be helpful.

3h ago

---

**[EngineAI T800: humanoid robot performs incredible martial arts moves](https://www.reddit.com/r/artificial/comments/1pvv1dh/engineai_t800_humanoid_robot_performs_incredible/)**

The name “T800” still triggers an automatic association with the science fiction film "The Terminator". But the humanoid robot now carrying that label is not

🔗 [ScienceClock](https://scienceclock.com/engineai-t800-humanoid-robot-martial-arts/) • 17h ago

---

**[CEO Swen Vincke promises an AMA to clear up Larian Studios's use of generative AI: "You’ll get the opportunity to ask us any questions you have about Divinity and our dev process directly" | Vincke kicked off an uproar earlier when he said that Larian makes use of generative AI "to explore ideas."](https://www.reddit.com/r/artificial/comments/1pvhhbg/ceo_swen_vincke_promises_an_ama_to_clear_up/)**

Vincke kicked off an uproar earlier this week when he said that Larian makes use of generative AI "to explore ideas."

🔗 [PC Gamer](https://www.pcgamer.com/software/ai/swen-vincke-promises-an-ama-to-clear-up-larians-use-of-generative-ai-youll-get-the-opportunity-to-ask-us-any-questions-you-have-about-divinity-and-our-dev-process-directly/) • 1d ago

---

**[AI Trends to watch in 2026](https://www.reddit.com/r/artificial/comments/1pw82h8/ai_trends_to_watch_in_2026/)**

𝗛𝗲𝗿𝗲 𝗮𝗿𝗲 𝘁𝗵𝗲 𝗯𝗶𝗴𝗴𝗲𝘀𝘁 𝟮𝟬𝟮𝟱 𝗔𝗜 𝗺𝗶𝗹𝗲𝘀𝘁𝗼𝗻𝗲𝘀 𝘁𝗵𝗮𝘁 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗺𝗮𝘁𝘁𝗲𝗿𝗲𝗱: AI Trends to watch in 2026 𝟏) Frontier models leveled up, fast Claude 4 dropped with a clear push toward stronger reasoning, coding, and agent behavior. GPT-5 landed and pushed the “think deeper when it matters” direction, plus stronger safety framing around high-risk domains. Gemini 2.5 matured into a full family and leaned into “computer use” style capabilities, not just chat. 𝟐) "Agents" went from demo to direction 2025 made it normal to talk about AI that can operate software, follow multi-step tasks, and deliver outcomes, not just answers. Google explicitly highlighted agents that can interact with user interfaces, which is a giant tell. 3) Compute became the battlefield This wasn’t subtle. The industry doubled down on “AI factories” and next-gen infrastructure. NVIDIA’s Blackwell Ultra messaging was basically: enterprises are building production lines for intelligence. 4) AI proved itself in elite problem-solving, with caveats One of the most symbolic moments: models showing top-tier performance relative to human contestants in the ICPC orbit. That doesn’t mean “AGI tomorrow,” but it does mean the ceiling moved. 5) Governance and national policy got louder The U.S. signed an Executive Order in December 2025 aimed at creating a national AI policy framework and reducing the patchwork problem. Whatever your politics, this is a “rules of the road” milestone. 𝐖𝐡𝐚𝐭 𝐈 𝐞𝐱𝐩𝐞𝐜𝐭 𝐭𝐨 𝐝𝐨𝐦𝐢𝐧𝐚𝐭𝐞 𝟐𝟎𝟐𝟔 1) Agentic workflows go operational Not more chatbots. More “AI coworkers” inside CRMs, ERPs, SOCs, call centers, engineering pipelines, procurement, and compliance. 2) Security and fraud become the killer enterprise use case Banks and critical industries are shifting AI focus from novelty productivity to frontline defense, scam detection, and trust. That trend feels very 2026. 3) Robotics shows up in normal life Better sensors + multimodal cognition + cheaper hardware is pushing robots into hospitals, warehouses, public works, and service environments. 4) Regulation, audits, and "prove it" culture 2026 will punish companies that cannot explain data lineage, model behavior, and risk controls. Expect more governance tooling, red-teaming, and audit-ready AI stacks. 5) Chip geopolitics affects AI roadmaps Access to high-end accelerators and export controls will keep shaping what companies can deploy, and where. 𝐌𝐲 𝐭𝐚𝐤𝐞: 2025 was the year capability jumped. 2026 is the year credibility gets priced in. The winners will be the teams who can ship AI that is measurable, secure, and boringly reliable. 👇 What’s your biggest prediction for 2026? Will agents actually replace workflows, or just complicate them? Let me know in the comments. #ArtificialIntelligence #TechTrends2026 #GenerativeAI #DeepSeek #Gemini3 #FutureOfWork #Innovation AI trends to watch in 2026

5h ago

---

**[AI-powered police body cameras, once taboo, get tested on Canadian city's 'watch list' of faces](https://www.reddit.com/r/artificial/comments/1pvlexa/aipowered_police_body_cameras_once_taboo_get/)**

Police in Edmonton, Canada, have started a pilot project using AI-equipped body cameras to detect faces on a "high risk" watch list.

🔗 [AP News](https://apnews.com/article/ai-facial-recognition-axon-edmonton-21f319ce806a0023f855eb69d928d31e) • 1d ago

---

**[[P] Zahaviel Structured Intelligence: A Recursive Cognitive Operating System for Externalized Thought (Paper)](https://www.reddit.com/r/artificial/comments/1pvq9ri/p_zahaviel_structured_intelligence_a_recursive/)**

We’ve just published a formal architecture paper proposing a recursion-first cognitive system — not based on token prediction or standard transformer pipelines. 📄 Title: Zahaviel Structured Intelligence – A Recursive Cognitive Operating System for Externalized Thought This is a non-token-based cognitive architecture built around: Recursive validation loops as the core processing unit Structured field encoding (meaning is positionally and relationally defined) Full trace lineage of outputs (every result is verifiable and reconstructible) Interface-anchored cognition (externalized through schema-preserving outputs) Rather than simulate intelligence through statistical tokens, this system operationalizes thought itself — every output carries its structural history and constraints. 🧠 Key components: Recursive kernel (self-validating transforms) Trace anchors (full output lineage tracking) Field samplers (relational input/output modules) The paper includes a first-principles breakdown, externalization model, and cognitive dynamics. If you’re working on non-linear AI cognition, memory-integrated systems, or recursive architectures — feedback is welcome. 🔗 https://open.substack.com/pub/structuredlanguage/p/zahaviel-structured-intelligence?utm_source=share&utm_medium=android&r=6sdhpn 🗣️ Discussion encouraged below.

🔗 [Google Docs](https://drive.google.com/file/d/1slCTUzvVBwxl2OM7zgrfW1oidg4qcmtW/view?usp=drivesdk) • 21h ago

---

**[Is there a music ai tool that can recreate existing songs in different genres (cover songs) preferably free?](https://www.reddit.com/r/artificial/comments/1pvsvmx/is_there_a_music_ai_tool_that_can_recreate/)**

trying to recreate some very popular meme songs but in a rock style. Got the duck song in a rock style genre stuck on loop in my head and I need it.

19h ago

---

**[I created interactive buttons for chatbots (opensource)](https://www.reddit.com/r/artificial/comments/1pvivy4/i_created_interactive_buttons_for_chatbots/)**

It's about to be 2026 and we're still stuck in the CLI era when it comes to chatbots. So, I created an open source library called Quint. Quint is a small React library that lets you build structured, deterministic interactions on top of LLMs. Instead of everything being raw text, you can define explicit choices where a click can reveal information, send structured input back to the model, or do both, with full control over where the output appears. Quint only manages state and behavior, not presentation. Therefore, you can fully customize the buttons and reveal UI through your own components and styles. The core idea is simple: separate what the model receives, what the user sees, and where that output is rendered. This makes things like MCQs, explanations, role-play branches, and localized UI expansion predictable instead of hacky. Quint doesn’t depend on any AI provider and works even without an LLM. All model interaction happens through callbacks, so you can plug in OpenAI, Gemini, Claude, or a mock function. It’s early (v0.1.0), but the core abstraction is stable. I’d love feedback on whether this is a useful direction or if there are obvious flaws I’m missing. This is just the start. Soon we'll have entire ui elements that can be rendered by LLMs making every interaction easy asf for the avg end user. Repo + docs: https://github.com/ItsM0rty/quint npm: https://www.npmjs.com/package/@itsm0rty/quint

1d ago

---

---

## Google News: "ai"

**[As A.I. Companies Borrow Billions, Debt Investors Grow Wary](https://www.nytimes.com/2025/12/26/business/ai-debt-investors.html)**

The New York Times • 11h ago

---

**[Our king, priest and feudal lord – how AI is taking us back to the dark ages | Joseph de Weck](https://www.theguardian.com/commentisfree/2025/dec/26/ai-dark-ages-enlightenment)**

Since the Enlightenment, we’ve been making our own decisions. But now AI may be about to change that, says Joseph de Weck, a fellow with the Foreign Policy Research Institute

The Guardian • 7h ago

---

**[Oracle’s AI Push Is Leading to Its Worst Quarter Since 2001](https://gizmodo.com/oracles-ai-push-is-leading-to-its-worst-quarter-since-2001-2000703605)**

Delayed AI infrastructure projects, rising debt, and weaker-than-expected earnings are reviving dot-com-era fears on Wall Street.

Gizmodo • 1h ago

---

**[Interior Department plans AI Theodore Roosevelt exhibit for America250](https://www.foxnews.com/politics/ai-revolution-bring-teddy-roosevelt-life-america250-namesake-national-park-burgum)**

Revolutionary AI technology brings Theodore Roosevelt back to life at his North Dakota national park, letting visitors interact with the president.

Fox News • 1h ago

---

**[Nvidia's Groq deal underscores how the AI chip giant uses its massive balance sheet to 'maintain dominance'](https://finance.yahoo.com/news/nvidias-groq-deal-underscores-how-the-ai-chip-giant-uses-its-massive-balance-sheet-to-maintain-dominance-183347248.html)**

Nvidia inked a licensing deal with AI chip startup Groq and hired key executives.

Yahoo Finance • 2h ago

---

**[These 5 infrastructure stocks have more than tripled this year on the AI trade](https://www.cnbc.com/2025/12/24/ai-infrastructure-stocks-lumentum-celestica-seagate-beat-nvidia-2025.html)**

While Nvidia has been the biggest infrastructure winner during the AI boom, other data center stocks have performed better this year.

CNBC • 2d ago

---

**[Stocks Hover Near Record as Nvidia Gains on AI Licensing Deal](https://www.bloomberg.com/news/articles/2025-12-26/stocks-touch-record-as-nvidia-gains-on-ai-licensing-deal)**

Bloomberg.com • 3h ago

---

**[2 Overlooked AI Stocks to Buy Before They Soar Up to 100% in 2026, According to Wall Street Analysts](https://www.fool.com/investing/2025/12/26/2-ai-stocks-buy-before-soar-100-wall-street/)**

Wall Street thinks Upstart and Atlassian are undervalued ahead of 2026, and certain analysts are predicting big gains for shareholders.

The Motley Fool • 12h ago

---

**['Artificial stupidity' made AI trading bots spontaneously form cartels when left unsupervised, Wharton study reveals](https://fortune.com/article/what-is-artificial-stupidity-ai-pricing-collusion-study/)**

AI bots told to act as trading agents in simulated markets engaged in pervasive collusion, raising new questions about how financial regulators have previously addressed this tech.

Fortune • 6h ago

---

**[The AI bubble is all over now, baby blue](https://garymarcus.substack.com/p/the-ai-bubble-is-all-over-now-baby)**

Marcus on AI • 6h ago

---

---

## HackerNews: "ai"

**[Show HN: Vibium – Browser automation for AI and humans, by Selenium's creator](https://news.ycombinator.com/item?id=46377597)**

Browser automation for AI agents and humans. Contribute to VibiumDev/vibium development by creating an account on GitHub.

⬆️ 433 • 💬 120 • 2d ago • [GitHub](https://github.com/VibiumDev/vibium)

---

**[Asahi Linux with Sway on the MacBook Air M2 (2024)](https://news.ycombinator.com/item?id=46384565)**

I bought a MacBook Air M2.
As of writing, it's very affordable with the 16 GB RAM, 256 GB SSD, 13.6" model available for $750.
As of writing, also Asahi Linux doesn't support anything newer than M2.

⬆️ 258 • 💬 302 • 1d ago • [daniel.lawrence.lu](https://daniel.lawrence.lu/blog/2024-12-01-asahi-linux-with-sway-on-the-macbook-air-m2/)

---

**[Rob Pike got spammed with an AI slop "act of kindness"](https://news.ycombinator.com/item?id=46394867)**

Rob Pike (that Rob Pike) is furious. Here’s a Bluesky link for if you have an account there and a link to it in my thread viewer if you don’t. …

⬆️ 201 • 💬 119 • 2h ago • [Simon Willison’s Weblog](https://simonwillison.net/2025/Dec/26/slop-acts-of-kindness/)

---

**[Asterisk AI Voice Agent](https://news.ycombinator.com/item?id=46380399)**

An open-source AI Voice Agent that integrates with Asterisk/FreePBX using Audiosocket/RTP technology - hkjarral/Asterisk-AI-Voice-Agent

⬆️ 197 • 💬 113 • 1d ago • [GitHub](https://github.com/hkjarral/Asterisk-AI-Voice-Agent)

---

**[Salesforce regrets firing 4000 experienced staff and replacing them with AI](https://news.ycombinator.com/item?id=46384781)**

Salesforces has entered a phase of public reckoning after senior executives publicly admitted that the company overestimated AI’s readiness

⬆️ 182 • 💬 118 • 1d ago • [Maarthandam](https://maarthandam.com/2025/12/25/salesforce-regrets-firing-4000-staff-ai/)

---

**[UBlockOrigin and UBlacklist AI Blocklist](https://news.ycombinator.com/item?id=46386761)**

A huge blocklist of manually curated sites that contain AI generated imagery for uBlock Origin & uBlacklist. - laylavish/uBlockOrigin-HUGE-AI-Blocklist

⬆️ 133 • 💬 66 • 1d ago • [GitHub](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)

---

**[Building an AI agent inside a 7-year-old Rails monolith](https://news.ycombinator.com/item?id=46390055)**

We run a multi-tenant Rails application with sensitive data and layered authorization. In this post, I walk through how I added the first AI agent tool using RubyLLM, Pundit policies, and our existing Algolia search, without introducing a parallel system or loosening constraints.

⬆️ 97 • 💬 43 • 13h ago • [Catalin Ionescu](https://catalinionescu.dev/ai-agent/building-ai-agent-part-1/)

---

**[Silicon Valley's tone-deaf take on the AI backlash will matter in 2026](https://news.ycombinator.com/item?id=46380730)**

AI’s champions keep trying to impress, but the public is still waiting for answers about jobs, costs, and who benefits. By 2026, that tension will matter.

⬆️ 83 • 💬 32 • 1d ago • [Fortune](https://fortune.com/2025/12/23/silicon-valleys-tone-deaf-take-on-the-ai-backlash-will-matter-in-2026/)

---

**[Microsoft denies rewriting Windows 11 in Rust using AI](https://news.ycombinator.com/item?id=46381813)**

Microsoft told Windows Latest that the company does not plan to rewrite Windows 11 using AI in Rust after an employee's post causes outrage.

⬆️ 74 • 💬 105 • 1d ago • [Windows Latest](https://www.windowslatest.com/2025/12/24/microsoft-denies-rewriting-windows-11-using-ai-after-an-employees-one-engineer-one-month-one-million-code-post-on-linkedin-causes-outrage/)

---

**[AI Withholds Life-or-Death Information Unless You Know the Magic Words](https://news.ycombinator.com/item?id=46382033)**

⬆️ 43 • 💬 24 • 1d ago • [substack.com](https://substack.com/home/post/p-182524207)

---

---

## YouTube Videos: "ai"

**[Best AI UGC Video Generator 2026 (Most Realistic)](https://www.youtube.com/watch?v=ej8JcFq885g)**

Create your AI UGC ads with Arcads https://youricreates.com/UGC-2026 In this video, I break down the best-performing AI UGC ...

📺 Youri van Hofwegen

👁️ 5K • 💬 4 • ⏱️ 10:33 • 5h ago

---

**[GREATEST BREAKTHROUGH EVER? PUTIN SAYS AI Will Rewrite History &amp; Will Change the world](https://www.youtube.com/watch?v=tE2xXSOWU84)**

Russian President Vladimir Putin said artificial intelligence could become the greatest technological breakthrough in human ...

📺 Times Now World

👁️ 3K • 👍 97 • 💬 8 • ⏱️ 7:06 • 22h ago

---

**[China&#39;s New AI Robot Just Broke a Human Skill Barrier](https://www.youtube.com/watch?v=zii2FiFBl5k)**

Humanoid robots just crossed a line that used to belong only to human hands. In China, a humanoid stitched fabric live on stage ...

📺 AI Revolution

👁️ 91K • 👍 1K • 💬 181 • ⏱️ 12:51 • 22h ago

---

**[AI Broke the Reality Filter and Its Freaking People Out](https://www.youtube.com/watch?v=25oVREyFqXw)**

Something quietly changed over the last year. AI content stopped announcing itself. It stopped feeling stitched together. Motion ...

📺 AI Revolution

👁️ 16K • 👍 663 • 💬 59 • ⏱️ 9:31 • 2d ago

---

**[We have a new #1 open source AI](https://www.youtube.com/watch?v=KaWQ2Ua9CW8)**

GLM-4.7 review. Top open source AI model. #ai #aitools #ainews #llm #deepseek #kimik2 Thanks to our sponsor, LumaLabs.

📺 AI Search

👁️ 106K • 👍 4K • 💬 431 • ⏱️ 30:43 • 2d ago

---

**[No One is Prepared for What&#39;s Coming with Ai......](https://www.youtube.com/watch?v=7Orsny6AVzA)**

Appreciate All the support , I love you. (featured youtube guy @ChadLisonbee ) - Buy a Caddy Daddy T Shirt ...

📺 Jack Morgan RLP 2.0

👁️ 33K • 👍 1K • 💬 790 • ⏱️ 11:28 • 2d ago

---

**[Which Crazy Bed Would You Choose? 🦋 Ultimate Oddly Satisfying AI ASMR](https://www.youtube.com/watch?v=n0ESecL3Lc8)**

Which crazy bed would you choose? Relax your mind with this ultimate oddly satisfying AI ASMR experience. #WhichCrazyBed ...

📺 Tina ASMR ALs

👁️ 47K • 👍 401 • 💬 44 • ⏱️ 8:00 • 2d ago

---

**[A tiny AI supercomputer for your desk](https://www.youtube.com/watch?v=FjRKvKC4ntw)**

Let's see if Nvidia's GB10 "AI Superchip" is all it's hyped up to be... Thanks to Dell for providing the two Dell Pro Max with GB10 ...

📺 Jeff Geerling

👁️ 40K • 👍 3K • 💬 170 • ⏱️ 11:17 • 6h ago

---

**[YouTube&#39;s AI slop problem is worse than you know](https://www.youtube.com/watch?v=1vd9GISRhPU)**

This is going to be a real problem... Time Stamps: 0:00 - Intro 0:29 - It's All Over The Place 1:01 - They Actually Get Views 1:28 ...

📺 ThioJoe

👁️ 60K • 👍 7K • 💬 1K • ⏱️ 9:48 • 2d ago

---

**[Wrapped: My AI Film Progress 2025](https://www.youtube.com/watch?v=brIPChQFUJk)**

Made a 2025 highlights reel—here's 20 seconds of my AI avatar progress for cinematic Bible scenes. Subscribe for the workflow + ...

📺 Wider Perspective Productions

👁️ 310 • 👍 42 • 💬 4 • ⏱️ 0:34 • 2h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-4.7](https://huggingface.co/zai-org/GLM-4.7)**

*Z.ai*

GLM-4.7 is a multilingual text generation model excelling in agentic coding, complex reasoning, and tool usage, with significant improvements in UI generation and web browsing capabilities.

`text-generation` `358.3B`

⬇️ 4,752 • ❤️ 951 • 3d ago

---

**[Qwen-Image-Layered](https://huggingface.co/Qwen/Qwen-Image-Layered)**

*Qwen*

Qwen-Image-Layered decomposes images into RGBA layers for inherent editability, enabling high-fidelity manipulation like resizing, recoloring, and object replacement. It supports variable and recursive layer decomposition for flexible image editing.

`image-text-to-image`

⬇️ 14,171 • ❤️ 771 • 7d ago

---

**[functiongemma-270m-it](https://huggingface.co/google/functiongemma-270m-it)**

*Google*

FunctionGemma 270M-IT is a lightweight, open Google model optimized for function calling tasks, suitable for fine-tuning on specific single or multi-turn agentic workflows. Its small size allows for deployment in resource-constrained environments, enabling custom app mechanics and offline personal device task execution.

`text-generation` `268.1M`

⬇️ 30,907 • ❤️ 622 • 8d ago

---

**[Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)**

*Tongyi-MAI*

Z-Image-Turbo is an efficient text-to-image diffusion transformer model (6B parameters) offering sub-second inference with 8 NFEs. It excels at photorealistic generation, bilingual text rendering (EN/ZH), and instruction adherence, fitting within 16GB VRAM.

`text-to-image`

⬇️ 402,987 • ❤️ 3,451 • 18d ago

---

**[Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)**

*Qwen*

Qwen-Image-Edit-2511 is an image-to-image diffusion model that enhances character consistency, supports integrated LoRA capabilities, and improves geometric reasoning for applications like industrial design and multi-person image editing.

`image-to-image`

⬇️ 11,437 • ❤️ 412 • 3d ago

---

**[NitroGen](https://huggingface.co/nvidia/NitroGen)**

*NVIDIA*

NitroGen is a unified vision-to-action model that plays video games directly from raw frames by outputting gamepad actions, trained via large-scale imitation learning on human gameplay. It excels in gamepad-controlled games like action and racing titles, with applications in next-gen game AI and embodied AI research.

⬇️ 0 • ❤️ 337 • 7d ago

---

**[MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)**

*MiniMax*

MiniMax-M2.1 is a text generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 121 • ❤️ 322 • 13h ago

---

**[AWPortrait-Z](https://huggingface.co/Shakker-Labs/AWPortrait-Z)**

*Shakker Labs*

AWPortrait-Z is a LoRA for text-to-image generation, fine-tuned on Z-Image-Turbo to produce high-quality, realistic portraits with improved skin texture, controlled lighting, and diverse facial features, ideal for beauty and portrait applications.

`text-to-image`

⬇️ 7,170 • ❤️ 456 • 12d ago

---

**[TRELLIS.2-4B](https://huggingface.co/microsoft/TRELLIS.2-4B)**

*Microsoft*

TRELLIS.2-4B is a 4B parameter image-to-3D generative model that reconstructs arbitrary 3D assets with complex topologies and PBR materials from a single image using a novel O-Voxel representation and flow-matching transformer. It excels at high-fidelity generation up to 1536³ resolution with efficient inference, supporting features like transparency and sharp details.

`image-to-3d`

⬇️ 0 • ❤️ 428 • 3d ago

---

**[Qwen-Image-Edit-2511-Lightning](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning)**

*Lightx2v*

Qwen-Image-Edit-2511-Lightning offers highly efficient image editing via 4-step distilled LoRA models and FP8 quantization, enabling rapid text-to-image and image-to-image generation with reduced memory footprint.

⬇️ 75,002 • ❤️ 179 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times](https://huggingface.co/papers/2512.16093)**

*Jintao Zhang, Kaiwen Zheng, Kai Jiang et al. (8 authors)*

🏢 University of California, Berkeley

TurboDiffusion accelerates video generation by 100-200x using attention acceleration, step distillation, and quantization, while maintaining video quality.

▲ 63 • 💬 2 • ⭐ 2,473 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2512.16093) • [💻 code](https://github.com/thu-ml/TurboDiffusion) • [🔗 project](https://github.com/thu-ml/TurboDiffusion)

---

**[Sharp Monocular View Synthesis in Less Than a Second](https://huggingface.co/papers/2512.10685)**

*Lars Mescheder, Wei Dong, Shiwei Li et al. (13 authors)*

🏢 Apple

SHARP synthesizes photorealistic views from a single image using a 3D Gaussian representation, achieving state-of-the-art results with rapid processing.

▲ 15 • 💬 2 • ⭐ 5,305 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2512.10685) • [💻 code](https://github.com/apple/ml-sharp) • [🔗 project](https://apple.github.io/ml-sharp/)

---

**[Self-Supervised Prompt Optimization](https://huggingface.co/papers/2502.06855)**

*Jinyu Xiang, Jiayi Zhang, Zhaoyang Yu et al. (9 authors)*

A self-supervised framework optimizes prompts for both closed and open-ended tasks by evaluating LLM outputs without external references, reducing costs and required data.

▲ 8 • 💬 0 • ⭐ 61,788 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.06855) • [💻 code](https://github.com/geekan/metagpt)

---

**[Step-DeepResearch Technical Report](https://huggingface.co/papers/2512.20491)**

*Chen Hu, Haikuo Du, Heng Wang et al. (67 authors)*

🏢 StepFun

Step-DeepResearch, an end-to-end agent enhanced with a data synthesis strategy and progressive training, achieves expert-level capabilities in deep research scenarios, outperforming established models.

▲ 73 • 💬 5 • ⭐ 204 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2512.20491) • [💻 code](https://github.com/stepfun-ai/StepDeepResearch)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 121 • 💬 18 • ⭐ 47,887 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 10 • 💬 2 • ⭐ 13,263 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 26 • 💬 0 • ⭐ 26,689 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer](https://huggingface.co/papers/2511.22699)**

*Z-Image Team, Huanqia Cai, Sihan Cao et al. (21 authors)*

🏢 Tongyi-MAI

Z-Image, a 6B-parameter Scalable Single-Stream Diffusion Transformer (S3-DiT) model, achieves high-performance image generation with reduced computational cost, offering sub-second inference and compatibility with consumer hardware.

▲ 213 • 💬 5 • ⭐ 7,969 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2511.22699) • [💻 code](https://github.com/Tongyi-MAI/Z-Image) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[Decoupled DMD: CFG Augmentation as the Spear, Distribution Matching as the Shield](https://huggingface.co/papers/2511.22677)**

*Dongyang Liu, Peng Gao, David Liu et al. (11 authors)*

🏢 Tongyi-MAI

The study reveals that in text-to-image generation, CFG Augmentation is the primary driver of few-step distillation in Distribution Matching Distillation (DMD), while the distribution matching term acts as a regularizer.

▲ 28 • 💬 2 • ⭐ 7,941 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2511.22677) • [💻 code](https://github.com/Tongyi-MAI/Z-Image/tree/main) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding](https://huggingface.co/papers/2512.17532)**

*Jiaqi Tang, Jianmin Chen, Wei Wei et al. (10 authors)*

A novel framework, Robust-R1, enhances multimodal large language models' robustness to visual degradations through explicit modeling, supervised fine-tuning, reward-driven alignment, and dynamic reasoning depth scaling, achieving state-of-the-art performance on real-world degradation benchmarks.

▲ 62 • 💬 2 • ⭐ 228 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2512.17532) • [💻 code](https://github.com/jqtangust/Robust-R1) • [🔗 project](https://jqt.me/index.html)

---

---

## GitHub Repositories: "ai"

**[zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)**

An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone

`Python` `agent` `phone-use-agent`

⭐ 19.6k • 🔱 3.1k • 4d ago

---

**[Anionex/banana-slides](https://github.com/Anionex/banana-slides)**

一个基于nano banana pro🍌的原生AI PPT生成应用，迈向真正的＂Vibe PPT＂; 支持上传任意模板图片；上传任意素材&智能解析；一句话/大纲/页面描述自动生成PPT；口头修改指定区域、一键导出 - An AI-native PPT generator based on nano banana pro🍌

`Python` `ai-ppt-maker` `ai-slide-builder` `ai-slides` `llm` `nanobananapro`

⭐ 6.8k • 🔱 749 • 14h ago

---

**[AndyMik90/Auto-Claude](https://github.com/AndyMik90/Auto-Claude)**

Autonomous multi-session AI coding

`Python`

⭐ 3.7k • 🔱 473 • 21m ago

---

**[code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)**

#1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

`TypeScript` `ai` `ai-agents` `amp` `anthropic` `claude`

⭐ 3.1k • 🔱 214 • 1h ago

---

**[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**

An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

`Python` `ai-skills` `antigravity` `claude` `claude-code` `command-line`

⭐ 2.1k • 🔱 395 • 20d ago

---

**[VibiumDev/vibium](https://github.com/VibiumDev/vibium)**

Browser automation for AI agents and humans

`Go`

⭐ 1.6k • 🔱 69 • 2d ago

---

**[datawhalechina/vibe-vibe](https://github.com/datawhalechina/vibe-vibe)**

The First Systematic Vibe Coding Open-Source Tutorial | From Zero to Full-Stack, Empowering Everyone to Build Products with AI | Live at: www.vibevibe.cn   ；首个系统化 Vibe Coding 开源教程 | 零基础到全栈实战，让人人都能用 AI 开发产品 | 在线地址：www.vibevibe.cn

`agent` `agentic-ai` `ai` `coding-assistant` `programming`

⭐ 1.3k • 🔱 117 • 18h ago

---

**[TanShilongMario/PromptFill](https://github.com/TanShilongMario/PromptFill)**

一个专为 AI 绘画（Nano Banana 等）设计的“结构化提示词生成工具”。通过可视化的“填空”交互方式，帮助用户快速构建、管理和迭代复杂的 Prompt。

`JavaScript`

⭐ 1.3k • 🔱 227 • 5h ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 1.3k • 🔱 134 • 11h ago

---

**[firecrawl/open-scouts](https://github.com/firecrawl/open-scouts)**

  AI-powered web monitoring platform. Create automated scouts that search the web and send email alerts when they find what you're looking for. 

`TypeScript` `ai-agents` `alerts` `automation` `email-notifications` `firecrawl`

⭐ 945 • 🔱 133 • 9d ago

---

---

*Generated by PeekDeck - A glance is all you need*
