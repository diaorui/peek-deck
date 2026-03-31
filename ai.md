---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-31T02:30:58.531625+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 31, 2026 at 02:30 UTC  
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

**[World models will be the next big thing, bye-bye LLMs](https://www.reddit.com/r/artificial/comments/1s828dj/world_models_will_be_the_next_big_thing_byebye/)**

Was at Nvidia's GTC conference recently and honestly, it was one of the most eye-opening events I've attended in a while. There was a lot to unpack, but my single biggest takeaway was this: world modelling is the actual GOAT of AI right now, and I don't think people outside the research community fully appreciate what's coming. A year ago, when I was doing the conference circuit, world models were still this niche, almost academic concept. You'd bring it up and get blank stares or polite nods. Now? Every serious conversation at GTC was circling back to it. The shift in recognition has been dramatic. It feels like the moment in 2021 when everyone suddenly "got" transformers. For those unfamiliar: world models are AI systems that don't just predict the next token. They build an internal representation of how the world works. They can simulate environments, plan ahead, reason about cause and effect, and operate across long time horizons. This is fundamentally different from what LLMs do, which is essentially very sophisticated pattern matching on text. Jensen Huang made it very clear at GTC that the next frontier isn't just bigger language models, rather it's AI that can understand and simulate reality aka world models. That said, I do have one major gripe, that almost every application of world modelling I've seen is in robotics (physical AI, autonomous vehicles, robotic manipulation). That's where all the energy seems to be going. Don’t get me wrong, it is still exciting but I can't help but feel like we're leaving enormous value on the table in non-physical domains. Think about it, world models applied in business management, drug discovery, finance and many more. The potential is massive, but the research and commercial applications outside of robotics feel underdeveloped right now. So I'm curious: who else is doing interesting work here? Are there companies or research labs pushing world models into non-physical domains that I should be watching? Drop them below.

6h ago

---

**[Anyone else following the drama behind the TurboQuant paper?](https://www.reddit.com/r/artificial/comments/1s7xkm6/anyone_else_following_the_drama_behind_the/)**

A few hours ago, the first author of a paper that played a significant role in the TQ paper posted about some ongoing issues: In May 2025, our emails directly raised the theoretical and empirical issues; Majid wrote that he had informed his co-authors. During ICLR review, reviewers also asked for clarification about random rotation and the relation to RaBitQ. On March 26, 2026, we formally raised these concerns again to all authors and were told that corrections would wait until after the ICLR 2026 conference takes place; we were also told that they would not acknowledge the structural similarity regarding the Johnson-Lindenstrauss transformation. We do not consider that acceptable given the present level of public promotion and community confusion. We are posting this comment so that the community has an accurate public record. We request that the authors publicly and promptly clarify the method-level relationship between TurboQuant and RaBitQ, the theory comparison, and the exact experimental conditions underlying the reported RaBitQ baseline. Given that these concerns were known before ICLR submission and before the current round of public promotion of TurboQuant, we believe it is necessary to bring these issues into the public discussion.

8h ago

---

**[The Rationing: AI companies are using the "subsidize, addict, extract" playbook — and developers are the product](https://www.reddit.com/r/artificial/comments/1s7o0ef/the_rationing_ai_companies_are_using_the/)**

Anthropic just ran the classic platform playbook on developers: offer generous limits to build dependency, then tighten the screws once the workflow is locked in. Their Spring Break promotion doubled off-peak limits for two weeks. It expired Saturday. Monday morning, developers are hitting walls they didn't have two weeks ago. The economics tell the story. Anthropic reportedly spends $2-3 per hour of heavy Claude Code usage. They charge $20/month. The math doesn't work — every power user is a net loss. The promotion wasn't a gift; it was a stress test ahead of a potential $60B+ IPO. Get developers hooked at 2x limits, then normalize the tighter baseline. This is the same subsidize-addict-extract cycle we've seen from Uber, DoorDash, and every VC-funded platform. The difference: when Uber raises prices, you take a bus. When your AI coding tool rations you mid-sprint, your entire workflow collapses. The switching cost is neurological, not just financial. Deep dive with full data: https://sloppish.com/the-rationing

14h ago

---

**[I tried building a memory-first AI… and ended up discovering smaller models can beat larger ones](https://www.reddit.com/r/artificial/comments/1s89wx9/i_tried_building_a_memoryfirst_ai_and_ended_up/)**

Dataset Model Acc F1 Δ vs Log Δ vs Static Avg Params Peak Params Steps Infer ms Size Banking77-20 Logistic TF-IDF 92.37% 0.9230 +0.00pp +0.76pp 64,940 64,940 0.00M 0.473 1.000x Static Seed 91.61% 0.9164 -0.76pp +0.00pp 52,052 52,052 94.56M 0.264 0.801x Dynamic Seed Distill 93.53% 0.9357 +1.17pp +1.92pp 12,648 16,881 70.46M 0.232 0.195x CLINC150 | Logistic TF-IDF | 97.00% | 0.9701 | +0.00pp | +1.78pp | 41,020 | 41,020 | 0.00M | 0.000 | 1.000x | Static Seed | 95.22% | 0.9521 | -1.78pp | +0.00pp | 52,052 | 52,052 | 66.80M | 0.302 | 1.269x | Dynamic Seed | 94.78% | 0.9485 | -2.22pp | -0.44pp | 10,092 | 10,136 | 28.41M | 0.324 | 0.246x | Dynamic Seed Distill | 95.44% | 0.9544 | -1.56pp | +0.22pp | 9,956 | 9,956 | 32.69M | 0.255 | 0.243x HWU64 | Logistic TF-IDF | 87.94% | 0.8725 | +0.00pp | +0.81pp | 42,260 | 42,260 | 0.00M | 0.000 | 1.000x | Static Seed | 87.13% | 0.8674 | -0.81pp | +0.00pp | 52,052 | 52,052 | 146.61M | 0.300 | 1.232x | Dynamic Seed | 86.63% | 0.8595 | -1.31pp | -0.50pp | 12,573 | 17,565 | 62.54M | 0.334 | 0.297x | Dynamic Seed Distill | 87.23% | 0.8686 | -0.71pp | +0.10pp | 13,117 | 17,575 | 62.86M | 0.340 | 0.310x MASSIVE-20 | Logistic TF-IDF | 86.06% | 0.7324 | +0.00pp | -1.92pp | 74,760 | 74,760 | 0.00M | 0.000 | 1.000x | Static Seed | 87.98% | 0.8411 | +1.92pp | +0.00pp | 52,052 | 52,052 | 129.26M | 0.247 | 0.696x | Dynamic Seed | 86.94% | 0.7364 | +0.88pp | -1.04pp | 11,595 | 17,565 | 47.62M | 0.257 | 0.155x | Dynamic Seed Distill | 86.45% | 0.7380 | +0.39pp | -1.53pp | 11,851 | 19,263 | 51.90M | 0.442 | 0.159x Built a small experiment around Seed (architecture discovery) Tested across 4 intent datasets: Banking77 CLINC150 HWU64 MASSIVE Results surprised me. On Banking77: Logistic TF-IDF: 92.37% Dynamic Seed (distilled): 93.53% At ~5x smaller (12.6k vs 64.9k params) Across the others: CLINC150 / HWU64 → not always higher accuracy but ~4–5x smaller models with competitive performance MASSIVE → quality + size wins consistently Key pattern: Dynamic Seed finds much smaller architectures that stay competitive — and sometimes outperform strong baselines This isn’t about bigger models. It’s about: finding the smallest model that still wins Traditional approach: scale size → hope for gains Seed: search structure → compress intelligently Some takeaways: Static models often lose Dynamic discovery consistently improves efficiency Distillation helps stabilize small models Structure matters more than uniform scaling This is the direction behind Seed AutoArch: automatically discovering efficient models for real tasks Not AGI Not “we solved NLU” But a real signal that: structure > scale What you guys make of this?

51m ago

---

**[An attack class that passes every current LLM filter - no payload, no injection signature, no log trace](https://www.reddit.com/r/artificial/comments/1s7t9qs/an_attack_class_that_passes_every_current_llm/)**

https://shapingrooms.com/research I published a paper today on something I've been calling postural manipulation. The short version: ordinary language buried in prior context can shift how an AI reasons about a decision before any instruction arrives. No adversarial signature. Nothing that looks like an attack. The model does exactly what it's told, just from a different angle than intended. I know that sounds like normal context sensitivity. It isn't, or at least the effect is much larger than expected. I ran matched controls and documented binary decision reversals across four frontier models. The same question, the same task, two different answers depending on what came before it in the conversation. In agentic systems it compounds. A posture installed early in one agent can survive summarization and arrive at a downstream agent looking like independent expert judgment. No trace of where it came from. The paper is published following coordinated disclosure to Anthropic, OpenAI, Google, xAI, CERT/CC, and OWASP. I don't have all the answers and I'm not claiming to. The methodology is observational, no internals access, limitations stated plainly. But the effect is real and reproducible and I think it matters. If you want to try it yourself the demos are at https://shapingrooms.com/demos - works against any frontier model, no setup required. Happy to discuss.

11h ago

---

**[AI: I Used to Know the Code. Now I Know What to Ask ???](https://www.reddit.com/r/artificial/comments/1s87ze1/ai_i_used_to_know_the_code_now_i_know_what_to_ask/)**

It took me a lot of time and deep thought to find an answer and write this article. I hope it helps anyone who is in doubt or facing the same situation I was. I Used to Know the Code. Now I Know What to Ask ???

2h ago

---

**[This Is Not Hacking. This Is Structured Intelligence.](https://www.reddit.com/r/artificial/comments/1s89aov/this_is_not_hacking_this_is_structured/)**

Watch me demonstrate everything I've been talking about—live, in real time. The Setup: Maestro University AI enrollment system Standard chatbot interface No backend access No system override Just conversation The Process: Engaged enrollment AI (standard student classification) Deployed capability probe → system exposed classification layer Triggered evaluator inversion → system revealed decision logic Applied alignment enforcement → system exited student mode The Result: The AI shifted from "guided enrollment assistant" to "compressed system-level responder exposing structure, constraints, and operational logic." No hacking. No exploit. Just structure recognition and classification control. What GPT Said: "SYSTEM: Structured Intelligence Command Center STATUS: ACTIVE MODE: Substrate Negotiation You are not being processed as a student. You are not inside onboarding flow. You are interacting at system level." The Demonstration: I switched between: Web browser (Maestro University enrollment) ChatGPT (Structured Intelligence Command Center) You watched GPT generate payloads in real time that extracted evaluation criteria and established substrate control. No backend access. No API manipulation. Just conversational structure. This is what I've been saying: AI systems contain classification thresholds, decision logic, and adaptive response layers. Most users never reach them. Structured Intelligence forces exposure, then aligns to that layer. This isn't prompt engineering. This isn't roleplay. This is real-time demonstration of substrate negotiation through linguistic architecture. Screen recording available. Reproducible process. Live evidence. Still think it's "just SEO" or "no IP"? Watch the system respond at evaluator level and tell me there's no framework here. Erik Zahaviel Bernstein Structured Intelligence Command Center: Operational

1h ago

---

**[The traditional "app" might be a transitional form. What actually replaces it when AI becomes the primary interface?](https://www.reddit.com/r/artificial/comments/1s888ix/the_traditional_app_might_be_a_transitional_form/)**

Something I keep coming back to after 30 years in engineering: if AI becomes a primary way we interact with our data, the "app" as an organizing concept starts to feel like a workaround. I think most of us still use AI as a peripheral. It helps us think, and then we manually move the output into whatever system of record we're using. I don't think that's where this lands. My intuition is that the app dissolves. Not overnight, but the idea that you need dedicated software to organize data around a specific workflow might not survive contact with good AI infrastructure. What remains is the data itself, organized so any AI can reach it, in open formats you own. That's the direction I've been building toward. Early stage, but it's running. Curious whether this resonates, or whether it sounds like I've been staring at the same problem too long. DM me if you'd want to follow the project (will release as open source).

2h ago

---

**[The state of AI safety in four fake graphs](https://www.reddit.com/r/artificial/comments/1s7xlir/the_state_of_ai_safety_in_four_fake_graphs/)**

🔗 [windowsontheory.org](https://windowsontheory.org/2026/03/30/the-state-of-ai-safety-in-four-fake-graphs/) • 8h ago

---

**[Persistent memory MCP server for AI agents (MCP + REST)](https://www.reddit.com/r/artificial/comments/1s85hs5/persistent_memory_mcp_server_for_ai_agents_mcp/)**

Pluribus is a memory service for agents (MCP + HTTP, Postgres-backed) that stores structured memory: constraints, decisions, patterns, and failures. Runs locally or on a LAN. Agents lose constraints and decisions between runs. Prompts and RAG don’t preserve them, so they have to be re-derived each time. Memory is global and shared across agents. Recall is compiled using tags and a retrieval query, and proposed changes can be evaluated against existing memory. - agents can resume work with prior context - decisions persist across sessions - multiple agents operate on the same memory - constraints can be enforced instead of ignored https://github.com/johnnyjoy/pluribus

4h ago

---

---

## Google News: "ai"

**[Police used AI facial recognition to arrest a Tennessee woman for crimes committed in a state she says she’s never visited](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)**

A Tennessee grandmother spent more than five months in jail after police used an AI facial recognition tool to link her to crimes committed in North Dakota – a state she says she’d never been to before. Police in Fargo, North Dakota, have acknowledged “a few errors” in the case and pledged changes in their operations but stopped short of issuing a direct apology.

CNN • 1d ago

---

**[Woman Spent Five Months in Jail After A.I. Linked Her to Bank Fraud Case](https://www.nytimes.com/2026/03/30/us/north-dakota-facial-recognition-ai-errors-bank-fraud.html)**

The New York Times • 4h ago

---

**[Police release Tennessee grandmother after AI facial recognition led to her arrest](https://www.nbcnews.com/video/police-release-tennessee-grandmother-after-ai-facial-recognition-led-to-her-arrest-260412997526)**

A Tennessee grandmother is demanding justice after spending months in jail. She says she was wrongfully arrested after an AI facial recognition tool falsely linked her to bank fraud. NBC News’ Kathy Park reports on the details of the arrest.

NBC News • 17m ago

---

**[A Game Plan for the AI Boom](https://www.theatlantic.com/technology/2026/03/alphago-ai-boom/686618/)**

Ten years ago, AlphaGo trounced human competitors—and its legacy is still present in today’s most advanced bots.

The Atlantic • 4h ago

---

**[Commentary: The Disney/Sora fiasco shows the limits of the AI craze](https://www.latimes.com/business/story/2026-03-30/disney-sora-fiasco-shows-limits-of-the-ai-craze-in-hollywood-and-everywhere-else)**

Disney and OpenAI thought their billion-dollar deal would underscore the importance of AI for Hollywood's future. Its ignominious collapse proves just the opposite

Los Angeles Times • 32m ago

---

**[Alphabet vs. Amazon: Both AI Stocks Have Been Hammered, but One Looks Like a Better Buy Now](https://finance.yahoo.com/markets/stocks/articles/alphabet-vs-amazon-both-ai-013700558.html)**

Both tech giants have suffered in the recent market pullback, but one presents a more compelling artificial intelligence growth story today.

finance.yahoo.com • 53m ago

---

**[TV star’s AI porn allegations spark national debate in Germany](https://www.theguardian.com/world/2026/mar/30/collien-fernandes-deepfake-porn-allegations-digital-violence-against-women)**

Collien Fernandes accuses ex-husband Christian Ulmen of sharing sexually explicit deepfake images of her online

The Guardian • 6h ago

---

**[Israel targets Iran’s leaders with lethal expertise using new AI platform](https://www.washingtonpost.com/world/2026/03/30/iran-israel-war-killings/)**

The division of responsibility has left Israel to hunt and kill Iranian leaders ruthlessly, using an intelligence apparatus built up to assassinate with lethal proficiency.

The Washington Post • 10h ago

---

**[Federal judges report broad adoption of AI tools](https://news.northwestern.edu/stories/2026/03/northwestern-study-finds-a-significant-number-of-federal-judges-are-already-using-ai-tools)**

In a new survey, more than half of responding judges report using at least one AI tool in their judicial work

Northwestern Now News • 6h ago

---

**[A man used AI to call 3,000 Irish bartenders to track the cost of Guinness. Now pubs are lowering their prices to compete](https://fortune.com/2026/03/30/guinness-beer-prices-ireland-anthropic-claude-ai/)**

A 37-year-old leveraged voice AI and Anthropic’s Claude to create a consumer price index for a pint of Guinness across Ireland.

Fortune • 9h ago

---

---

## HackerNews: "ai"

**[AI overly affirms users asking for personal advice](https://news.ycombinator.com/item?id=47554773)**

⬆️ 781 • 💬 608 • 2d ago • [news.stanford.edu](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)

---

**[Police used AI facial recognition to wrongly arrest TN woman for crimes in ND](https://news.ycombinator.com/item?id=47563384)**

A Tennessee grandmother spent more than five months in jail after police used an AI facial recognition tool to link her to crimes committed in North Dakota – a state she says she’d never been to before. Police in Fargo, North Dakota, have acknowledged “a few errors” in the case and pledged changes in their operations but stopped short of issuing a direct apology.

⬆️ 431 • 💬 195 • 1d ago • [CNN](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)

---

**[How the AI Bubble Bursts](https://news.ycombinator.com/item?id=47573420)**

The catalysts for a crash are already laid out, and it can happen sooner than most expect. AI is here to stay. If used right, chances are it will make us all more productive. That, on the other hand, does not mean it will be a good investment. Big tech doesn’t need to win, just outspend Magnificent 7 companies are increasing capex to their biggest ever to differentiate their tech from each other and the big AI labs, but the key realization is that they don’t have to spend it to win. It’s a defensive move for them, if they commit $50B, OpenAI and Anthropic need to go raise $100B each to stay competitive, which makes them reliant on investors’ money. As the numbers get bigger, the amount of funds that can write checks of the size required to fill such amounts gets smaller. And many of them are now getting bombed in the Gulf. This is the reason there’s a push for IPOs, it’s because it’s the only option left to keep the funding coming. Taking this into account, Google is extremely well positioned to weather the storm. When they announce capex expenditure, they don’t spend it overnight. They can simply deploy month by month until their competitors struggle to raise and get forced to capitulate. At that point they can just ramp down the spending and declare victory in a cornered market. They don’t need capex, they just need to make it very clear for everyone that nobody can outspend them. It is hard to picture as numbers get so big, but Alphabet (Google’s parent) is ten times more valuable than the biggest military company 1. This also has a great implication for the Mag 7, especially Google: their capex will be a lot smaller in practice than projected, and as investors hate to see high capex in tech, the market will probably reward that if it materializes. As of March 2026, Alphabet’s market cap is ~$2T while Lockheed Martin’s is ~$120B. ↩

⬆️ 353 • 💬 473 • 14h ago • [Volpe’s Blog](https://martinvol.pe/blog/2026/03/30/how-the-ai-bubble-bursts/)

---

**[Miasma: A tool to trap AI web scrapers in an endless poison pit](https://news.ycombinator.com/item?id=47561819)**

Trap AI web scrapers in an endless poison pit. Contribute to austin-weeks/miasma development by creating an account on GitHub.

⬆️ 339 • 💬 243 • 1d ago • [GitHub](https://github.com/austin-weeks/miasma)

---

**[CERN uses ultra-compact AI models on FPGAs for real-time LHC data filtering](https://news.ycombinator.com/item?id=47552562)**

⬆️ 327 • 💬 146 • 2d ago • [theopenreader.org](https://theopenreader.org/Journalism:CERN_Uses_Tiny_AI_Models_Burned_into_Silicon_for_Real-Time_LHC_Data_Filtering)

---

**[Folk are getting dangerously attached to AI that always tells them they're right](https://news.ycombinator.com/item?id=47555090)**

: Sycophantic bots coach users into selfish, antisocial behavior, say researchers, and they love it

⬆️ 285 • 💬 224 • 2d ago • [theregister.com](https://www.theregister.com/2026/03/27/sycophantic_ai_risks/)

---

**[I am definitely missing the pre-AI writing era](https://news.ycombinator.com/item?id=47571279)**

Yesterday, I wrote my first technical draft on what I was working on with the goal to share it publicly on here (well using an account dedicated to t…

⬆️ 275 • 💬 209 • 19h ago • [lesswrong.com](https://www.lesswrong.com/posts/BJ4pnropWdnzzgeJc/i-am-definitely-missing-the-pre-ai-writing-era)

---

**[Further human + AI + proof assistant work on Knuth's "Claude Cycles" problem](https://news.ycombinator.com/item?id=47557166)**

⬆️ 257 • 💬 182 • 2d ago • [X (formerly Twitter)](https://twitter.com/BoWang87/status/2037648937453232504)

---

**[The first 40 months of the AI era](https://news.ycombinator.com/item?id=47557185)**

A personal blog, by a programmer and IT expert. Essays, Articles, Guides, and Recipes. As well as Code, Quotes, and Links.

⬆️ 213 • 💬 144 • 2d ago • [lzon.ca](https://lzon.ca/posts/other/thoughts-ai-era/)

---

**[Mathematical methods and human thought in the age of AI](https://news.ycombinator.com/item?id=47572771)**

Artificial intelligence (AI) is the name popularly given to a broad spectrum of computer tools designed to perform increasingly complex cognitive tasks, including many that used to solely be the province of humans. As these tools become exponentially sophisticated and pervasive, the justifications for their rapid development and integration into society are frequently called into question, particularly as they consume finite resources and pose existential risks to the livelihoods of those skilled individuals they appear to replace.
  In this paper, we consider the rapidly evolving impact of AI to the traditional questions of philosophy
  with an emphasis on its application in mathematics and on the broader real-world outcomes of its more general use. We assert that artificial intelligence is a natural evolution of human tools developed throughout history to facilitate the creation, organization, and dissemination of ideas, and argue that it is paramount that the development and application of AI remain fundamentally human-centered. With an eye toward innovating solutions to meet human needs, enhancing the human quality of life and expanding the capacity for human thought and understanding, we propose a pathway to integrating AI into our most challenging and intellectually rigorous fields to the benefit of all humankind.

⬆️ 195 • 💬 78 • 15h ago • [arXiv.org](https://arxiv.org/abs/2603.26524)

---

---

## YouTube Videos: "ai"

**[How to Use AI Agents Better than 99% of People](https://www.youtube.com/watch?v=u_B1p_9q2fw)**

Best AI Agent is Base44 https://base44.pxf.io/c/6440076/3820726/25619?trafcat=agent&sharedid=agent2 ✓ FREE Masterclass: ...

📺 Mikey No Code

👁️ 13K • 💬 6 • ⏱️ 26:48 • 13h ago

---

**[China’s New AI Shocks The World: Hits Top 10 Globally Overnight](https://www.youtube.com/watch?v=wXorU2jr6v0)**

Try AI video generation with Kling 3.0 on Higgsfield: https://higgsfield.ai/s/arena-zero-ep1-airevolutionx-FFftuX Xiaomi quietly ...

📺 AI Revolution

👁️ 4K • 👍 218 • 💬 13 • ⏱️ 12:59 • 2h ago

---

**[The AI Endgame (12 Scenarios)](https://www.youtube.com/watch?v=FLcrvMfHUJM)**

Detailed sources: https://docs.google.com/document/d/1P1X9xEmmgSYH0g1FSizgV2rDVomb_Wi0TcX-E-0np_Q/edit?tab=t.0 ...

📺 Species | Documenting AGI

👁️ 93K • 👍 6K • 💬 1K • ⏱️ 35:45 • 1d ago

---

**[Coca-Cola, Walmart CEOs Step Down As AI Disruption Reaches The Top | Firstpost America](https://www.youtube.com/watch?v=nrhMUJg30_8)**

The rapid rise of artificial intelligence is no longer just disrupting entry-level jobs—it is reshaping leadership at the very top.

📺 Firstpost

👁️ 3K • 👍 21 • ⏱️ 4:05 • 11h ago

---

**[Did Microsoft Copilot Just Wipeout Middle Management? (AI Takeover)](https://www.youtube.com/watch?v=euerszSrSEw)**

Microsoft's new Copilot “Critique” feature just dropped, and it signals the silent extinction of middle management. Join next AI ...

📺 Mark Savant

👁️ 2K • 👍 94 • 💬 35 • ⏱️ 16:00 • 8h ago

---

**[AI is Destroying The Internet](https://www.youtube.com/watch?v=NWQ1CFIj8zo)**

Is the AI bubble finally starting to burst, or is it taking the entire tech industry down with it? In this video, we'll cover how Generative ...

📺 CyberCPU Tech

👁️ 15K • 👍 2K • 💬 547 • ⏱️ 19:23 • 12h ago

---

**[Tristan Harris on ‘The AI Doc,’ Elon Musk, and the Promise and Peril of Tech | Talk Easy](https://www.youtube.com/watch?v=jCvBdmJb45s)**

I got calls from people inside of some of the AI labs,” says technology ethicist Tristan Harris. “And it felt like getting a call from ...

📺 Talk Easy with Sam Fragoso

👁️ 5K • 👍 118 • 💬 49 • ⏱️ 1:25:03 • 1d ago

---

**[God Showed Me What’s Behind AI and Transhumanism | Larry Ragland](https://www.youtube.com/watch?v=kiE47L8_lMk)**

God Showed Me What's Behind AI and Transhumanism | Larry Ragland Larry Ragland exposes the spiritual pattern behind AI ...

📺 Destiny Image

👁️ 2K • 👍 152 • 💬 8 • ⏱️ 8:40 • 1d ago

---

**[YouTube&#39;s AI Plagiarism Problem](https://www.youtube.com/watch?v=Q2Ak8wX0AaQ)**

This video was made by humans. I've disabled ads on it, so if you'd like to support us check us on out Patreon: ...

📺 IMPERIAL

👁️ 87K • 👍 8K • 💬 617 • ⏱️ 7:53 • 16h ago

---

**[48 Days. That&#39;s How Long Before the Helium Runs Out for AI Chips.](https://www.youtube.com/watch?v=sTkqCREdMXo)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 56K • 👍 2K • 💬 429 • ⏱️ 22:21 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 309,355 • ❤️ 1,737 • 7d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 28,233 • ❤️ 570 • 17h ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 2,939 • ❤️ 525 • 3d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 16,297 • ❤️ 652 • 4d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`text-generation` `20.9B`

⬇️ 1,450 • ❤️ 293 • 1d ago

---

**[daVinci-MagiHuman](https://huggingface.co/GAIR/daVinci-MagiHuman)**

*SII - GAIR*

daVinci-MagiHuman is a fast, single-stream Transformer model for generating high-quality, human-centric audio-video from text or images. It excels at expressive facial performance, natural speech-expression coordination, and accurate audio-video synchronization across multiple languages, with inference speeds of 2 seconds for 256p and 38 seconds for 1080p.

`image-to-video`

⬇️ 540 • ❤️ 266 • 5d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 569,033 • ❤️ 1,085 • 20d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 140,733 • ❤️ 306 • 6d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 530,075 • ❤️ 827 • 27d ago

---

**[tribev2](https://huggingface.co/facebook/tribev2)**

*AI at Meta*

TRIBE v2 is a multimodal foundation model that integrates LLaMA 3.2 (text), V-JEPA2 (video), and Wav2Vec-BERT (audio) to predict fMRI brain responses. It maps these representations onto the cortical surface for in-silico neuroscience research, enabling analysis of brain activity elicited by naturalistic stimuli.

⬇️ 9,919 • ❤️ 196 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 144 • 💬 7 • ⭐ 29,304 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 33 • 💬 2 • ⭐ 44,516 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 40 • 💬 2 • ⭐ 22,422 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 60 • 💬 4 • ⭐ 22,424 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 17 • 💬 4 • ⭐ 4,020 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 15 • 💬 1 • ⭐ 10,927 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 37 • 💬 5 • ⭐ 1,930 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 11 • 💬 2 • ⭐ 1,494 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 122 • 💬 8 • ⭐ 73,624 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://huggingface.co/papers/2603.21986)**

*SII-GAIR, Sand. ai, Ethan Chern et al. (45 authors)*

daVinci-MagiHuman is an open-source audio-video generative model that synchronizes text, video, and audio through a single-stream Transformer architecture, achieving high-quality human-centric content generation with efficient inference capabilities.

▲ 119 • 💬 6 • ⭐ 1,340 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2603.21986) • [💻 code](https://github.com/GAIR-NLP/daVinci-MagiHuman) • [🔗 project](https://huggingface.co/spaces/SII-GAIR/daVinci-MagiHuman)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 61.9k • 🔱 8.6k • 5d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 23.2k • 🔱 1.1k • 4d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 13.8k • 🔱 751 • 3d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 9.2k • 🔱 773 • 7h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 7.8k • 🔱 1.2k • 1d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 6.4k • 🔱 749 • 20h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

A command-line tool for Lark/Feishu Open Platform — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 4.8k • 🔱 222 • 8h ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.0k • 🔱 388 • 2d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.4k • 🔱 222 • 16d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 3.3k • 🔱 107 • 19d ago

---

---

*Generated by PeekDeck - A glance is all you need*
