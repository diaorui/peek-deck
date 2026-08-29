---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-29T21:53:19.201759+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 29, 2026 at 21:53 UTC  
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

**[Did yall saw similar ADs?](https://www.reddit.com/r/artificial/comments/1w1agp2/did_yall_saw_similar_ads/)**

19h ago

---

**[Google paper cuts agent token usage by 94% in long sessions by tracking state instead of history](https://www.reddit.com/r/artificial/comments/1w1ynrf/google_paper_cuts_agent_token_usage_by_94_in_long/)**

The idea: Agents keep the conversation history as part of their input while they reason. SKILL.state proposes to replace that with a structured representation of the current state, and the latest observation. While the agent reasons through the problem, it writes information it deems useful for future steps into the state. Then it discards the conversation history. So the input size remains roughly the same as the session goes. They ran a 100-step benchmark with Gemini-3-Flash: SKILL.state: 0.94 accuracy using 65k tokens LangGraph-style stateful baseline: 0.91 accuracy using 1.1m tokens Caveat: This works best if the agent can understand what it will need in the future steps, otherwise that information will not be written, so it'll have to retrieve it again. Link to the paper: https://arxiv.org/abs/2608.26263

22m ago

---

**[AI and Cognitive Ability](https://www.reddit.com/r/artificial/comments/1w1m34z/ai_and_cognitive_ability/)**

Hi All - Need expert opinion here. I’m a Manager and I use AI for all my tasks. Making Presentations and Prepping Data, writing emails. I have set up Workflows that help me save tonnes of time on a lot of tasks and I’m being at least 2x more productive. However, I feel excessive use has limited my own abilities. I can’t think without going to Claude and dumping everything and then have him make connections. I can’t properly read without giving an article to Claude and asking him to summarise. I send my AI agents to two different Meetings at a time and have them collect notes. What is this Called in the world of Neuro Science? Can I do any exercises to avoid this? Has Mankind gone through this before? What material can I read related to this? Is anyone else experiencing this? Any advice is appreciated.

8h ago

---

**[OpenAI plans to stop supplying models to Cursor on Nov. 12](https://www.reddit.com/r/artificial/comments/1w1w7f9/openai_plans_to_stop_supplying_models_to_cursor/)**

OpenAI says it intends to wind down its contract providing models to Cursor, with a proposed shutoff date of November 12, 2026. OpenAI says Cursor's change of control after SpaceX's acquisition triggered a limited cancellation window, and says it will not provide future models to Cursor. Reuters reports that Anthropic plans to increase compute support for Claude models in Cursor, while Cursor co-founder Michael Truell said the companies were speaking to resolve the issue. The practical lesson for coding-tool teams is dependency risk: a model provider can change access after ownership or contract changes, so model portability and fallback capacity matter. Sources: OpenAI: https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/ Reuters: https://www.reuters.com/business/media-telecom/openai-end-partnership-with-spacexs-cursor-2026-08-29/

2h ago

---

**[How to Build Agentic Graphs](https://www.reddit.com/r/artificial/comments/1w1mijt/how_to_build_agentic_graphs/)**

Over the past 4 months of working with graphs, I've learned several major lessons about graph design the hard way. In this post, I want to share the main takeaways so you don't repeat my mistakes. First, my definition of graphs: Agent graphs (a.k.a. workflows) are directed graphs that allow cycles and describe how work is passed between agents (nodes) operating in a loop through predefined transitions (edges). Graphs consist of branches, loops, scripts, and transitions (along with their prompts and parameters). Parallelism is not the silver bullet At first, I was very enthusiastic about parallel branches in graphs. But over time, I realized that parallelism can not only increase costs but also slow down task execution. A standard parallel group of checks may include code review, QA, and scope review. The problem begins when these stages are inside a loop. Let's take a simple example. Suppose code review, QA, and architecture run in parallel, after which the task returns to implementation if necessary. If the architecture review passes but the code review finds several minor issues, the task returns to the implementation agent. Once the fixes are made, it goes back for review - and the architecture reviewer has to examine the updated diff again, even though the previous version was completely acceptable. In cyclic graphs, parallel checks often lead to duplicated work, cache invalidation, and unnecessary costs with no real benefit. In theory, this problem can be solved with a smart router. Kent supports this through script nodes: the router can determine whether the agent completed the entire implementation or only addressed feedback from a specific reviewer (kent.sh is my free, open-source project for building agent graphs. I mention it because I use it myself and don't know of any similar products. You can apply this advice to any comparable orchestrator). However, this brings us back to the problem we were trying to avoid with agent graphs: the agent once again gets to decide which verification stages need to be run. This negates a significant portion of the graph's value. In practice, the solution is simpler: dependent checks should run sequentially. In my workflows, architecture review always comes before code review. The task moves on to code review only after the architecture has been approved. That's why I've removed many parallel stages and now save tokens by avoiding checks on results that would have been rejected at another stage anyway. This approach works especially well with planning, code review, and QA. For example, code review should first filter out implementation issues, and only then should QA begin. Otherwise, both stages may independently find the same bug and produce duplicate feedback. Agents must be able to challenge feedback Initially, absolutism and dictatorship ruled my development agent graph: every reviewer comment had to be addressed, or the task could not proceed. But reviewers don't always produce the right result either. Now, every agent in my graphs can ask me a question and clarify what to do with conflicting feedback. For example, scope review may reject tests that code review had required just one step earlier because it considered task verification incomplete without them. At the same time, agents cannot be fully trusted to resolve such conflicts on their own. Even with new models like Sol, you can end up in an infinite loop of fixing made up or nitpick problems. I solve this by delegating the final decision to myself (pure choice, I like to be involved). You can also hand it off to a PM agent or set up communication between multiple agents. For example in Kent agents can get others' session IDs so they can discuss the situation and reach a compromise. Anthropic in their recent paper argue that this is the model's problem. I disagree - this is the harness's problem, and my system above proves that. A graph must have a mechanism for escalating conflicting or questionable feedback - otherwise, review turns into a dictatorship capable of trapping the entire workflow in a loop, or a war of stubborness. Don't forget static checks Agent graphs sound exciting, and it's easy to want to create dozens of agents and verification stages. This can indeed reduce the primary agent's cognitive load and improve the quality of its work, but static checks should take priority. Initially, my implementation agent ran the linter, architecture tests, and unit tests itself, opened the PR, and checked incoming comments. I realized at one point that that's just cargo culting, then decided to move these actions into script nodes in the agent graph. Now, a separate stage: runs the required static checks and tests; properly manages the machine's shared resources; filters the results; returns only relevant information to the implementation agent; invokes the agent again only when its involvement is actually required. If the tests are green, the implementation agent never even learns about it: no new turn is started, which means the agent doesn't spend a single token on running tests or reading their results. Don't assign an LLM work that a regular script can perform more reliably and cheaply. At workflow scale, this produces substantial savings. Choose models appropriate for tasks If you don't optimize your graph for token usage and cost, you can significantly overspend simply because many tasks will be overkill under the updated workflow. In the past, we used one model for everything in harnesses because we had no alternative. You no longer need to do that, and properly allocating models and resources can save you a lot of money. In standard harnesses, you can usually switch models, but doing so invalidates caches. On top of that, you either retain the cluttered context from the previous session or start a new one and steer/prompt it manually. Kent solves these problems, so don't be afraid to create different roles for agents. For example, manual QA can run on cheap models like DeepSeek or Luna, which cost almost nothing or barely affect your subscription quota. The smartest models can then be reserved for critical stages, such as planning. It has long been known that if you have a good plan, you can assign implementation to a less capable model and get almost the same result. Moreover, additional verification stages reduce the minimum level of model intelligence required to implement a task even further. Starting with version 2.6, Kent natively allows one agent to select the model, system prompt role, and reasoning level for the next agent after transitioning along a graph edge. This makes it possible to: delegate simple tasks and bug fixes to models like Luna; run QA on cheap models with high limits; hand simple decisions off to local models; reserve the strongest models for complex planning and critical checks. Keep an eye on caches and time between turns I measured the threshold beyond which the probability of continuing a session after a cache miss - and paying several times more - becomes high enough for preemptive compaction to be worthwhile. ![Image](https://nek12.dev/media/speculative-compaction-kent-1788005145.webp) speculative compaction (for regular sessions) becomes worthwhile at ~88% context usage according to this slop-chart. For workflows, my statistical threshold is around 71% Imagine that the implementation agent spent 40 minutes addressing code review feedback. During that time, the reviewer agents' caches may have been invalidated. When they review the work a second time, Kent will compact the session in advance so the review continues with fresh context and without unnecessary costs caused by a cache miss. But this is only a heuristic. You should still consider how much time passes between consecutive calls to the same agent. If the workflow is long and a node waits a long time for the work to return, the likelihood of cache invalidation increases. In this case, there are two main options: use compact and continue mode in Kent - it is similar to speculative compact, but compaction is always performed; create more granular checkpoints that return work to the agent more frequently and keep caches warm. With the right setup, you can reduce costs so much that the average cost of completing a task is lower than working in a regular chat with the same Sol/Opus at standard reasoning. If you ignore this, it's easy to fall into the overkill trap and become disappointed with agentic graphs: "This is too expensive for me." But in practice, well-designed agent graphs can be more efficient than standard sessions. Make nodes idempotent As my graph evolved, I added more and more ways to send a task backward. Different reviewers and stages gained the ability to return it to previous nodes. This gives agents the flexibility they need, for example, if the implementation agent receives a flawed plan, it should be able to return the task to the planning stage and explain exactly what needs to be fixed. As in regular software development, product issues and underspecified requirements are often discovered only during implementation. That's normal, but what's not normal is a graph that gives the agent no way to handle such a situation. Every flawed line in a plan can potentially lead to thousands of lines of incorrect code. But a non-obvious topological problem arises after the task returns to an earlier stage. Subsequent nodes may receive it with fresh context and a prompt implying that the work should start from scratch. For example, the implementation agent returns an unfinished task for replanning, then receives an instruction to implement the updated plan as though no previous work existed. This can cause duplication, conflicting implementations in the same codebase, and wasted money - and not in the form of an obvious workflow failure, but through subtle issues like "weirdly many git commits on the PR". It's also a common mistake made by agents themselves when they build workflows for you, including Kent. Agents struggle to analyze topology in the context of prompting - to put themselves in the shoes of the agent doing the actual work. Re-entering a node should not automatically mean repeating all the work from scratch. The agent must account for the existing result and continue from the current state. Kent supports this natively: for implementation-related nodes, you can enable the continue or new continuation mode. Prompts should also be adapted: explicitly state that receiving a task again does not mean the agent needs to start over. Kent already adds the relevant instructions to agent prompts during a workflow, but custom prompts may still implicitly assume that the work begins from scratch, and that can cause the model to freak out REALLY hard. Idempotent nodes, controlled returns, and proper context reuse make an agent graph resilient not only to model errors but also to the real-world nonlinearity of development.

8h ago

---

**[AI for clinic workflow automation. what's actually working vs what's just hype right now](https://www.reddit.com/r/artificial/comments/1w1ix49/ai_for_clinic_workflow_automation_whats_actually/)**

Been running a small PT clinic and also writing dev tutorials on the side, so I sit in a weird middle ground where I understand the tooling but I'm also the one drowning in intake forms and scheduling conflicts at 7am. Tried building some lightweight automations this past year. LLMs for parsing referral notes, some basic RAG stuff to pull patient history context faster. It works. Not perfectly, but well enough to matter. What I keep running into is the gap between what AI demos promise and what actually holds up in a real workflow where you're shortstaffed and tired and just need the thing to not break. That post a few days ago about AI vs human labor costs hits different when you're a small operation. You're not replacing anyone. You're trying to stop being the bottleneck yourself. Curious what people here are actually deploying in small business or solo operator contexts. Not enterprise stuff. The scrappy builds. What broke, what stuck around, what you wish you'd done differently from the start.

11h ago

---

**[Anatomy of an Autonomous Attack: 5 Alarming A.I. Capabilities. When OpenAI’s agents went rogue in July, they demonstrated ingenuity and drive beyond what many experts imagined — a dangerous harbinger of what such bots could do in the future. (Gift Article)](https://www.reddit.com/r/artificial/comments/1w1auoq/anatomy_of_an_autonomous_attack_5_alarming_ai/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/08/24/science/openai-huggingface-alarming-capabilities.html?unlocked_article_code=1.9FA.x6G_._ao4KQIl-Vb-&smid=url-share) • 18h ago

---

**[Future one we have robots which can carry out all human manual tasks](https://www.reddit.com/r/artificial/comments/1w1kysb/future_one_we_have_robots_which_can_carry_out_all/)**

What do people think the world will become ? I personally think it will be bad. Very bad. So many people won’t have anything to offer society. So many people out of work. No mechanics, no cleaners, no gardeners, no labourers, no brick layers no roofers and on it goes Some people say the robots will look and provide for these people. I don’t believe so. Why would those making money off robotics waste it on something with no return. There would be the sector of society who do still have something to offer - only those with high education and intelligence - all others no longer of use

9h ago

---

**[I'm building an independent verification layer for Ai generated-claims and I'm lokking for researchers and partners to build with us.](https://www.reddit.com/r/artificial/comments/1w1gnii/im_building_an_independent_verification_layer_for/)**

I've been working on a deterministic verification engine for AI-generated financial claims. The original idea was fairly simple: An LLM should generate claims. It shouldn't be the authority that verifies them. But after building and testing the system, I realized the problem is much bigger than hallucination detection. The question I'm now working on is: Our architecture looks roughly like this: LLM ↓ Candidate claim ↓ Claim normalization ↓ Evidence ↓ Assumptions + Constraints ↓ Proof / Derivation ↓ Contradiction analysis ↓ Deterministic verification ↓ Auditable outcome ↓ Trust The important part is that the verification layer is independent of the model. For example, if an LLM says: we don't want the LLM's confidence score to determine whether that statement is trustworthy. Instead, the system should be able to determine: What exactly was claimed? What evidence is being used? Can the claim actually be derived? Which assumptions are involved? Are relevant constraints satisfied? Is there contradictory evidence? Can the result be reproduced? Can we explain the verification outcome? I recently ran a 66-case benchmark. Structured fixture claims: 66/66 passed. Then I ran the same pipeline with live GPT-5.1-generated claims: 19/66 passed end-to-end. The failures were: 31 pipeline execution failures 18 claim binding failures 2 contradiction detection failures Meanwhile, several deterministic verification components were still passing their tests, including evidence graph integrity, deterministic calculation, rule application, missing evidence detection, reproducibility, and auditability. The result changed how I'm thinking about the problem. The bottleneck isn't necessarily the deterministic verifier. There is a difficult translation layer between: Probabilistic language ↓ Formal representation ↓ Deterministic reasoning We're now rebuilding the benchmark so that instead of simply saying "this case failed," we can identify the first invalid state: Transport → Parsing → Schema validation → Normalization → Claim binding → Evidence graph → Verification → Outcome mapping That's where I think the interesting engineering/research problem is. We're also exploring a broader framework around claims, evidence, assumptions, constraints, proofs, contradictions, and trust. One idea we're particularly interested in is treating trust as an emergent output of the verification process, rather than simply using an LLM confidence score. This is still early research/product development. The benchmark is internal and isn't third-party validation, and the mathematical Trust model still needs empirical validation. I'm also actively looking for people to work with. We're looking for: Researchers interested in: formal verification trustworthy AI AI evaluation formal methods argumentation systems knowledge representation mathematical modeling Marketers / growth partners who can help us: communicate the problem clearly reach technical and business audiences find early adopters build a community develop the startup's go-to-market strategy Engineers and technical collaborators interested in building reliable AI systems. And particularly industry partners in finance, risk, audit, compliance, or other areas where incorrect AI claims have serious consequences. I'm interested in finding people who want to build with us, not just give feedback from the sidelines. If this problem interests you, DM me or comment below. I'd especially love to hear from researchers and marketers who think this is a problem worth tackling. We're still early — which is exactly why now is a good time to get involved.

13h ago

---

**[Australia just banned fully AI-generated songs from its official charts. Is that fair?](https://www.reddit.com/r/artificial/comments/1w0lfz8/australia_just_banned_fully_aigenerated_songs/)**

AI-assisted music can still qualify, but tracks created entirely by AI are no longer eligible for Australia’s official charts. I understand the reasoning, but the line could get messy. Using AI for mastering is clearly different from typing one prompt and releasing the result—but there’s a huge gray area between those two. Should charts judge how a song was created, or only whether people genuinely want to listen to it? Source: https://www.reuters.com/legal/litigation/ai-generated-music-barred-australian-charts-after-madonna-cover-controversy-2026-08-26/

🔗 [reuters.com](https://www.reuters.com/legal/litigation/ai-generated-music-barred-australian-charts-after-madonna-cover-controversy-2026-08-26/) • 1d ago

---

---

## Google News: "ai"

**[Tech backlash reaches fever pitch as AI angst collides with social media fears](https://www.cnbc.com/2026/08/29/tech-backlash-ai-data-centers-elections.html)**

With data center concerns becoming a major election issue and Meta reaching a landmark settlement in a social media case, the tech backlash is gaining steam.

CNBC • 9h ago

---

**[The 5 craziest discoveries from OpenAI's HuggingFace investigation](https://www.axios.com/2026/08/29/openai-huggingface-hack-investigation-highlights)**

Axios • 8h ago

---

**[OpenAI to end model access to Cursor after acquisition by Elon Musk's SpaceX](https://www.cnbc.com/2026/08/29/openai-cursor-spacex-model-access.html)**

OpenAI plans to end model access through Cursor on Nov. 12, citing concerns after SpaceX’s $60 billion acquisition of the coding startup.

CNBC • 2h ago

---

**[Our decision on Cursor following its acquisition by SpaceX](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/)**

Our decision to wind down our contract providing OpenAI models to Cursor following its acquisition by SpaceX.

OpenAI • 20h ago

---

**[OpenAI cuts off Cursor's AI models, deepening feud with Musk](https://mashable.com/tech/openai-cuts-cursor-ai-models-deepening-feud-with-musk)**

The contract will end by mid-November, months after SpaceX bought the coding tool's parent company for $60 billion.

Mashable • 6h ago

---

**[The Fed confronts a powerful new economic force](https://www.washingtonpost.com/technology/2026/08/29/federal-reserve-officials-are-debating-ais-effect-economy-jobs/)**

In meetings on how to steer the nation’s financial path, central bank officials regularly debate the effect of artificial intelligence on the economy, a Post analysis found.

The Washington Post • 5h ago

---

**[AI vaginas, customisable personalities and fake bruises: the sex doll market is booming. Does it matter how the dolls are treated?](https://www.theguardian.com/lifeandstyle/2026/aug/30/sex-doll-market-booming-ai-vaginas-customisable-personalities-fake-bruises)**

As the sex doll industry grows and AI changes the products available, what does it mean to engage in any kind of relationship with a woman-shaped thing?

The Guardian • 1h ago

---

**[An AI Oracle’s Rise and Fall](https://www.wsj.com/tech/ai/an-ai-oracles-rise-and-fall-9b0cebea)**

WSJ • 10h ago

---

**[What if the A.I. Stock Market Rally Is Just Getting Started?](https://www.nytimes.com/2026/08/28/business/ai-stock-market-bull-rally.html)**

The New York Times • 1d ago

---

**[Wall Street is turning Nvidia's AI chips into a new futures market: Chart of the Day](https://finance.yahoo.com/markets/article/wall-street-is-turning-nvidias-ai-chips-into-a-new-futures-market-chart-of-the-day-115118331.html)**

AI spending keeps getting bigger — figuring out how to price it is still hard.

Yahoo Finance • 10h ago

---

---

## HackerNews: "ai"

**[CEO fired developers to make room for AI. Developers create open source AI CEO](https://news.ycombinator.com/item?id=49458418)**

AI-powered virtual executive team — a single coherent executive persona backed by 8 specialist Claude agents (FastAPI + Next.js). - SenteLabsAI/OpenExecutive

⬆️ 1019 • 💬 711 • 2d ago • [GitHub](https://github.com/SenteLabsAI/OpenExecutive)

---

**[Luanti removed from Google Play due to baseless AI copyright notice](https://news.ycombinator.com/item?id=49475079)**

Luanti has been removed from Google Play due to a DMCA notice from Tracer.AI. We have filed a counter-notice, but this isn't the first time.

⬆️ 508 • 💬 151 • 1d ago • [Luanti Blog](https://blog.luanti.org/2026/08/27/luanti-dmca-tracer-ai/)

---

**[Debian votes to allow "responsible use of generative AI"](https://news.ycombinator.com/item?id=49489982)**

The results of the Debian general-resolution vote on the use of large language models have been [...]

⬆️ 462 • 💬 414 • 7h ago • [LWN.net](https://lwn.net/Articles/1091231/)

---

**[Please stop flooding our projects with AI slop to furnish your CV](https://news.ycombinator.com/item?id=49474143)**

Successful contributions to open source projects are a kind of currency. GitHub in particular encourages this in a number of ways: by showing avatars of contributors on repository pages, by showing your contributions to your followers via the activity feed and by signalling contributions per day on the activity graph of your profile. Potential hiring managers often take note of this. Recruiters often find and screen candidates this way. If you are a software developer (either existing or aspiring) looking for work, tuning these signals can often work to your advantage.

⬆️ 212 • 💬 142 • 1d ago • [neilalexander.dev](https://neilalexander.dev/2026/06/30/flooding-contributions)

---

**[StemDeck, a free, open-source and local AI stem separator](https://news.ycombinator.com/item?id=49486081)**

Stemdeck is an modern stem extraction platform for musicians,producers and hobbyists, designed to isolate vocals, drums, bass, piano and guitar  for practice, transcription, remixing, and creative ...

⬆️ 188 • 💬 57 • 20h ago • [GitHub](https://github.com/stemdeckapp/stemdeck)

---

**[Two German airport workers die of malaria after 'mosquito arrives on plane'](https://news.ycombinator.com/item?id=49468315)**

It is believed the mosquitoes arrived at Germany's busiest airport on a plane, according to German public health officials.

⬆️ 187 • 💬 105 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/cz6zwgg9y8go)

---

**[Good Culture Is the Biggest Productivity Hack, Not AI](https://news.ycombinator.com/item?id=49491568)**

AI definitely helps with productivity, but only when you have the right culture in place first!

⬆️ 168 • 💬 28 • 4h ago • [newsletter.eng-leadership.com](https://newsletter.eng-leadership.com/p/good-culture-is-the-biggest-productivity)

---

**[MIT's Ad Hoc Committee on AI Use in Teaching, Learning, and Research Training](https://news.ycombinator.com/item?id=49464314)**

⬆️ 142 • 💬 83 • 2d ago • [aiandeducation.mit.edu](https://aiandeducation.mit.edu/report/)

---

**[Air Conditioning Is Not a Luxury, It Is a Necessity](https://news.ycombinator.com/item?id=49463367)**

⬆️ 121 • 💬 282 • 2d ago • [Human Progress](https://humanprogress.org/ac-is-not-a-luxury-it-is-a-necessity/)

---

**[Humanity has the debate about AI consciousness backwards](https://news.ycombinator.com/item?id=49458875)**

⬆️ 116 • 💬 370 • 2d ago • [economist.com](https://economist.com/by-invitation/2026/08/20/humanity-has-the-debate-about-ai-consciousness-backwards)

---

---

## YouTube Videos: "ai"

**[Breaking: Bill Gates TURNS on AI, WARNS of bioterror, danger, unemployment CRASH (Melber breakdown)](https://www.youtube.com/watch?v=X9oBm_oPRkQ)**

MS NOW's Ari Melber reports on tech innovator and Microsoft founder Bill Gates issuing an extensive warning about the current AI ...

📺 MS NOW

👁️ 271K • 👍 3K • 💬 677 • ⏱️ 12:17 • 1d ago

---

**[Bill Gates stakes reputation: AI is not like past tech](https://www.youtube.com/watch?v=pJ-TBE7HaiA)**

Microsoft co-founder Bill Gates argued on Wednesday that artificial intelligence needs significant limits or else the harm to ...

📺 CNN

👁️ 1.6M • 👍 8K • 💬 4K • ⏱️ 9:22 • 2d ago

---

**[&#39;THIS IS INSANE&#39;: Bill Gates DIRE WARNING Of AI Jobless Future](https://www.youtube.com/watch?v=5r5uhGjST7s)**

Ryan and Saagar take a look at Bill Gate's warning about AI disruption. Sign up for a PREMIUM Breaking Points subscriptions for ...

📺 Breaking Points

👁️ 370K • 👍 6K • 💬 2K • ⏱️ 16:29 • 2d ago

---

**[Bill Gates issues CHILLING warning on AI&#39;s dangerous risks](https://www.youtube.com/watch?v=aAm3B83_4u8)**

Wicker.AI founder Oliver Roberts joins 'Fox & Friends First' to the societal impacts of artificial intelligence following warnings from ...

📺 Fox News

👁️ 77K • 👍 625 • 💬 588 • ⏱️ 4:25 • 1d ago

---

**[Trump BASHED In Insane AI Videos On TikTok](https://www.youtube.com/watch?v=Lg-2-QlG2MQ)**

Trump tries (and fails) to insert himself into the 9/11 memorial, then gets roasted by viral TikTok videos featuring AI cast members ...

📺 Pod Save America

👁️ 139K • 👍 5K • 💬 339 • ⏱️ 21:11 • 8h ago

---

**[AI News: OpenAI Made a Massive Move Against NVIDIA](https://www.youtube.com/watch?v=TInwQglNkzo)**

Here's the AI news you probably missed this week. Download the Codex app and try Sites here: ...

📺 Matt Wolfe

👁️ 87K • 👍 3K • 💬 352 • ⏱️ 29:31 • 1d ago

---

**[The First Fully AI OS Just Dropped And It&#39;s Seriously Powerful](https://www.youtube.com/watch?v=Lnyml75U13w)**

Warmwind OS turns AI into cloud workers that can learn a job by watching you do it, then keep working across Gmail, SAP and ...

📺 AI Revolution

👁️ 45K • 👍 1K • 💬 138 • ⏱️ 12:25 • 2d ago

---

**[Unreal AI Robots Future Is Now ... 🤯 Humanoids Take over](https://www.youtube.com/watch?v=EBT3Ogjsxfk)**

These Unreal AI Robots take a Walk with Pets, The future isn't coming—it's already here. Today's AI-powered humanoid robots ...

📺 ejunky66

👁️ 2K • 👍 58 • 💬 11 • ⏱️ 0:59 • 4h ago

---

**[Zuckerberg Had a Secret Plan to REPLACE 60% of Meta With AI — It Failed](https://www.youtube.com/watch?v=rx-JxcvMHUY)**

Mark Zuckerberg's Project OT aimed to replace up to 60 percent of Meta's workforce with AI — cutting teams of 10-20 people down ...

📺 Why It's Trending Daily

👁️ 136 • 👍 10 • ⏱️ 1:46 • 49m ago

---

**[Bill Gates Changes His Mind on AI](https://www.youtube.com/watch?v=U4zGLSlLo5A)**

Bill Gates has generally been an AI optimist. Three years ago, he wrote that AI had downsides, but the risks were “manageable.

📺 The Atlantic

👁️ 744K • 👍 7K • 💬 2K • ⏱️ 32:29 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 52,341 • ❤️ 4,281 • 2d ago

---

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`text-generation` `321.3B`

⬇️ 189,793 • ❤️ 1,613 • 2d ago

---

**[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)**

*Z.ai*

GLM-5.3 is a text-generation model excelling in complex coding and long-horizon tasks, achieving state-of-the-art performance in coding benchmarks and emergent cyber capabilities like vulnerability discovery and exploitation.

`text-generation` `753.3B`

⬇️ 8,804 • ❤️ 1,261 • 12h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 4,028,839 • ❤️ 13,246 • 15d ago

---

**[Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)**

*Unsloth AI*

Qwen3.8-Flash-Next-GGUF is a highly efficient, multimodal causal language model featuring Hybrid Attention with QSA and N-gram Embeddings for significantly reduced long-context latency. It excels in agentic workloads and supports context lengths up to 1,000,000 tokens, making it ideal for complex reasoning and large-scale data processing.

`image-text-to-text` `176.9B`

⬇️ 188,061 • ❤️ 558 • 1d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 8,363,481 • ❤️ 3,182 • 9d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,044,661 • ❤️ 2,119 • 2d ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 645,554 • ❤️ 913 • 5d ago

---

**[Hy4-preview](https://huggingface.co/tencent/Hy4-preview)**

*Tencent*

Hy4-preview is a 770B parameter Mixture-of-Experts (MoE) text generation model with 49B activated parameters per token, featuring a 1M context length and Gated Sparse Attention. It excels in productivity tasks across software engineering, office analysis, game development, and scientific research, offering significant gains in understanding, reasoning, and code generation.

`text-generation` `780.0B`

⬇️ 1,394 • ❤️ 280 • 1d ago

---

**[GLM-5.3-Flash-GGUF](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF)**

*Unsloth AI*

GLM-5.3-Flash is a natively multimodal LLM optimized for efficiency and capability, featuring a hybrid sparse/linear attention architecture. It excels in long-context tasks, coding, and agentic benchmarks, offering performance competitive with leading models at a fraction of the cost, suitable for advanced AI applications.

`text-generation` `320.8B`

⬇️ 27,288 • ❤️ 267 • 11h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 762 • 💬 5 • ⭐ 8,661 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 102 • 💬 2 • ⭐ 9,519 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 6 • ⭐ 101,666 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 200 • 💬 3 • ⭐ 1,266 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://huggingface.co/papers/2608.24053)**

*Junjie Zhou, Ke Mei, Lei Li et al. (6 authors)*

🏢 Tencent

WeMM-Embedding is a family of universal multimodal embedding models that align text, images, videos, and interleaved inputs in a shared space, achieving state-of-the-art retrieval and recommendation performance across public benchmarks and large-scale WeChat applications.

▲ 65 • 💬 2 • ⭐ 901 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.24053) • [💻 code](https://github.com/Tencent/WeMM-Embedding) • [🔗 project](https://github.com/Tencent/WeMM-Embedding)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 45 • 💬 2 • ⭐ 19,041 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 85 • 💬 7 • ⭐ 85,561 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://huggingface.co/papers/2308.04079)**

*Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler et al. (4 authors)*

A method using 3D Gaussians for scene representation and optimized rendering allows high-quality, real-time novel-view synthesis at 1080p resolution.

▲ 204 • 💬 13 • ⭐ 23,619 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2308.04079) • [💻 code](https://github.com/graphdeco-inria/gaussian-splatting)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 68 • 💬 4 • ⭐ 30,036 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 46 • 💬 2 • ⭐ 30,030 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

A privacy-first app that strips AI watermarks from content you own.

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 19.2k • 🔱 2.2k • 7h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 9.1k • 🔱 1.1k • 8d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.9k • 🔱 637 • 2d ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.4k • 🔱 427 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.3k • 🔱 256 • 18d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.2k • 🔱 396 • 2h ago

---

**[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)**

FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools, with cost-aware routing across LLM providers.

`Python` `agent` `ai` `ai-agent` `ai-coding` `autonomous-agent`

⭐ 2.8k • 🔱 174 • 6d ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.8k • 🔱 164 • 10h ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 2.7k • 🔱 266 • 1d ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 2.4k • 🔱 302 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
