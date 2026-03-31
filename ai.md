---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-31T08:09:11.627011+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 31, 2026 at 08:09 UTC  
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

11h ago

---

**[Iran War Chokes Off Helium Supply Critical for AI](https://www.reddit.com/r/artificial/comments/1s8ew65/iran_war_chokes_off_helium_supply_critical_for_ai/)**

🔗 [wsj.com](https://www.wsj.com/world/iran-war-chokes-off-helium-supply-critical-for-ai-bf020a3f?st=fWrBVq&reflink=article_copyURL_share) • 2h ago

---

**[If frontier AI labs have unlimited shovels, what's stopping them from building everything?](https://www.reddit.com/r/artificial/comments/1s8fw9n/if_frontier_ai_labs_have_unlimited_shovels_whats/)**

I found myself explaining AI tokens to my mom over the weekend. At first I related them to building bricks: blocks of data the model uses to understand and respond. Then I thought about it as we're all paying for tokens as units of work. Not just a shovel, but the work a shovel can do, like horses and horsepower. “Picks and shovels company” is the idea that a company sells the thing that is needed to do fundamental work. It comes from the California gold rush. Not everyone will find gold, but everyone looking for gold will buy picks and shovels. Thus, AI companies' LLMs are shovel factories and AI tokens are shovels. Smart shovels. These shovels do work across writing, coding, research, planning, support, analysis, and more. And everyone is using them to build new products, even better shovels. So if foundation model companies control the shovel factories, and they can use effectively unlimited shovels on their own ideas, what happens to everyone building on top of them? How can startups, who have to pay for tokens and rate limits, compete against the shovel factories? Medical, legal, compliance, education, finance. If a category gets big enough, what stops the model company from absorbing the best ideas directly into its own platform? The solution I came up with was creating products that were incredibly niche or too risky for a general LLM company to touch. But still, everything seems like it’s on a timeline before it gets integrated into LLM platforms. It’s already happening with the medical industry. Why would a hospital use dozens of different vendors if they can use one LLM to assist doctors with diagnosing patients, help patients navigate health plans, take care of scheduling, write contracts, and handle compliance. You could say speed, focus, and trust might help startups, but that moat disappears when the LLM can throw unlimited shovels at the problem. Now that a small team can run a startup that once took hundreds of people, the LLM company can become a multi headed hydra, with businesses in every industry. Are patents and proprietary data enough to protect yourself from platform risk? Can startups create a real moat for survival? Or is everything already on a clock?

1h ago

---

**[I tried building a memory-first AI… and ended up discovering smaller models can beat larger ones](https://www.reddit.com/r/artificial/comments/1s89wx9/i_tried_building_a_memoryfirst_ai_and_ended_up/)**

Dataset Model Acc F1 Δ vs Log Δ vs Static Avg Params Peak Params Steps Infer ms Size Banking77-20 Logistic TF-IDF 92.37% 0.9230 +0.00pp +0.76pp 64,940 64,940 0.00M 0.473 1.000x Static Seed 91.61% 0.9164 -0.76pp +0.00pp 52,052 52,052 94.56M 0.264 0.801x Dynamic Seed Distill 93.53% 0.9357 +1.17pp +1.92pp 12,648 16,881 70.46M 0.232 0.195x CLINC150 | Logistic TF-IDF | 97.00% | 0.9701 | +0.00pp | +1.78pp | 41,020 | 41,020 | 0.00M | 0.000 | 1.000x | Static Seed | 95.22% | 0.9521 | -1.78pp | +0.00pp | 52,052 | 52,052 | 66.80M | 0.302 | 1.269x | Dynamic Seed | 94.78% | 0.9485 | -2.22pp | -0.44pp | 10,092 | 10,136 | 28.41M | 0.324 | 0.246x | Dynamic Seed Distill | 95.44% | 0.9544 | -1.56pp | +0.22pp | 9,956 | 9,956 | 32.69M | 0.255 | 0.243x HWU64 | Logistic TF-IDF | 87.94% | 0.8725 | +0.00pp | +0.81pp | 42,260 | 42,260 | 0.00M | 0.000 | 1.000x | Static Seed | 87.13% | 0.8674 | -0.81pp | +0.00pp | 52,052 | 52,052 | 146.61M | 0.300 | 1.232x | Dynamic Seed | 86.63% | 0.8595 | -1.31pp | -0.50pp | 12,573 | 17,565 | 62.54M | 0.334 | 0.297x | Dynamic Seed Distill | 87.23% | 0.8686 | -0.71pp | +0.10pp | 13,117 | 17,575 | 62.86M | 0.340 | 0.310x MASSIVE-20 | Logistic TF-IDF | 86.06% | 0.7324 | +0.00pp | -1.92pp | 74,760 | 74,760 | 0.00M | 0.000 | 1.000x | Static Seed | 87.98% | 0.8411 | +1.92pp | +0.00pp | 52,052 | 52,052 | 129.26M | 0.247 | 0.696x | Dynamic Seed | 86.94% | 0.7364 | +0.88pp | -1.04pp | 11,595 | 17,565 | 47.62M | 0.257 | 0.155x | Dynamic Seed Distill | 86.45% | 0.7380 | +0.39pp | -1.53pp | 11,851 | 19,263 | 51.90M | 0.442 | 0.159x TL;DR: I built a system that finds much smaller models that stay competitive — and sometimes outperform larger baselines. Built a small experiment around Seed (architecture discovery). Instead of training bigger models, Seed: generates candidate architectures evaluates them keeps the smallest ones that still perform well Tested across 4 datasets: Banking77 CLINC150 HWU64 MASSIVE 🧠 Key result (Banking77) Logistic TF-IDF: 92.37% Dynamic Seed (distilled): 93.53% 👉 Higher accuracy + ~5x smaller (12.6k vs 64.9k params) 📊 Other results MASSIVE → quality + size wins CLINC150 / HWU64 → not always higher accuracy but ~4–5x smaller models with competitive performance 🔥 What actually matters (not just accuracy) If you only look at accuracy → mixed If you include: model size training compute inference latency 👉 this becomes a much stronger result 🧠 Takeaway Traditional ML: 👉 scale model size and hope Seed: 👉 search for better structure Smaller models can compete with larger ones if you find the right architecture Not AGI Not “we solved NLU” But a real signal that: 👉 structure > scale Smaller models can compete with larger ones — if you find the right structure

6h ago

---

**[Anyone else following the drama behind the TurboQuant paper?](https://www.reddit.com/r/artificial/comments/1s7xkm6/anyone_else_following_the_drama_behind_the/)**

A few hours ago, the first author of a paper that played a significant role in the TQ paper posted about some ongoing issues: In May 2025, our emails directly raised the theoretical and empirical issues; Majid wrote that he had informed his co-authors. During ICLR review, reviewers also asked for clarification about random rotation and the relation to RaBitQ. On March 26, 2026, we formally raised these concerns again to all authors and were told that corrections would wait until after the ICLR 2026 conference takes place; we were also told that they would not acknowledge the structural similarity regarding the Johnson-Lindenstrauss transformation. We do not consider that acceptable given the present level of public promotion and community confusion. We are posting this comment so that the community has an accurate public record. We request that the authors publicly and promptly clarify the method-level relationship between TurboQuant and RaBitQ, the theory comparison, and the exact experimental conditions underlying the reported RaBitQ baseline. Given that these concerns were known before ICLR submission and before the current round of public promotion of TurboQuant, we believe it is necessary to bring these issues into the public discussion.

14h ago

---

**[Newsom signs executive order requiring AI companies to have safety, privacy guardrails](https://www.reddit.com/r/artificial/comments/1s8ge2h/newsom_signs_executive_order_requiring_ai/)**

🔗 [ktla.com](https://ktla.com/news/california/newsom-signs-executive-order-requiring-ai-companies-to-have-safety-privacy-guardrails/) • 57m ago

---

**[The traditional "app" might be a transitional form. What actually replaces it when AI becomes the primary interface?](https://www.reddit.com/r/artificial/comments/1s888ix/the_traditional_app_might_be_a_transitional_form/)**

Something I keep coming back to after 30 years in engineering: if AI becomes a primary way we interact with our data, the "app" as an organizing concept starts to feel like a workaround. I think most of us still use AI as a peripheral. It helps us think, and then we manually move the output into whatever system of record we're using. I don't think that's where this lands. My intuition is that the app dissolves. Not overnight, but the idea that you need dedicated software to organize data around a specific workflow might not survive contact with good AI infrastructure. What remains is the data itself, organized so any AI can reach it, in open formats you own. That's the direction I've been building toward. Early stage, but it's running. Curious whether this resonates, or whether it sounds like I've been staring at the same problem too long. DM me if you'd want to follow the project (will release as open source).

7h ago

---

**[Built a training stability monitor that detects instability before your loss curve shows anything — open sourced the core today](https://www.reddit.com/r/artificial/comments/1s8cmqj/built_a_training_stability_monitor_that_detects/)**

Been working on a weight divergence trajectory curvature approach to detecting neural network training instability. Treats weight updates as geometric objects and measures when the trajectory starts bending wrong — catches problems well before loss diverges. Validated across 7 architectures including DistilBERT, GPT-2, ResNet-50. 100% detection rate, 0% false positives across a 30-seed benchmark. Open sourced the detection core today. Links in comments.

4h ago

---

**[Built an Event Kernel for Agent OSes that Coordinates Under Load: Real-Time Events, Replayable Logs, TTL subs, No Deadlocks](https://www.reddit.com/r/artificial/comments/1s8fzjg/built_an_event_kernel_for_agent_oses_that/)**

Agent systems are running on outdated infrastructure, manual state checks, endless polling, and fragile logs. Every workaround patches another inefficiency, and it breaks under real coordination. So I built the Event Kernel: Now, agent operating systems can be event-driven: • 27 real-time events like task.started, agent.terminated, and budget.warning. • Every event is logged for full transparency, a complete history, even across restarts. • TTL subscriptions stop stale listeners from bloating memory. • Deadlock-proof by design: Every safeguard is baked into the core. What Happened: I swapped from polling and logs to events, and the system just worked: • Workflows ran cleaner and 10x easier to debug. • Deadlocks are completely eliminated. • Scales without breaking. It’s simple: Events transform how agents react, scale, and coordinate. This acts like Android sitting on Linux, agents stay abstracted from the system completely. No shell calls or missed states. It gives real-time updates. Would love to know if anyone else has tried event-driven architecture for agents, it’s the cleanest system I’ve worked with yet. https://github.com/ninjahawk/hollow-agentOS

1h ago

---

**[Depth-first pruning seems to transfer from GPT-2 to Llama (unexpectedly well)](https://www.reddit.com/r/artificial/comments/1s8ft8d/depthfirst_pruning_seems_to_transfer_from_gpt2_to/)**

TL;DR: Removing the right transformer layers (instead of shrinking all layers) gives smaller, faster models with minimal quality loss — and this seems to transfer from GPT-2 to Llama. been experimenting with a simple idea: instead of shrinking model width, just remove entire layers based on sensitivity and then recover with distillation. Originally tested it on GPT-2 (124M) and it worked pretty well. Decided to try the exact same approach on TinyLlama 1.1B to see if it was just a fluke. but it wasn’t GPT-2 (12L → 10L / 9L) ~11–17% parameter reduction ~9–13% PPL degradation ~1.2x decode speedup TinyLlama 1.1B (22L → 20L / 19L) 20L: ~8% smaller, PPL ratio ~1.058 19L: ~12% smaller, PPL ratio ~1.081 20L gives a clean speedup, 19L is more mixed Also ran 3 seeds on the 20L setup: 9.72 / 9.72 / 9.70 PPL → basically no variance A couple things that stood out: early/mid layers are consistently easier to drop first/last layers are almost always critical the “best” layer pair changes after pruning + recovery (model rebalances) once the setup is fixed, recovery is surprisingly stable Takeaway (for me at least): Removing the right layers seems to preserve structure much better than shrinking everything uniformly. And more interestingly, the same basic recipe works across architectures — not just GPT-2. Not claiming anything groundbreaking here, just surprised how cleanly it transferred. Curious if others have seen similar behavior with depth pruning vs width reduction.

1h ago

---

---

## Google News: "ai"

**[States Plow Ahead With A.I. Regulation, Defying Trump](https://www.nytimes.com/2026/03/30/technology/trump-states-ai-gavin-newsom-california.html)**

The New York Times • 10h ago

---

**[A Game Plan for the AI Boom](https://www.theatlantic.com/technology/2026/03/alphago-ai-boom/686618/)**

Ten years ago, AlphaGo trounced human competitors—and its legacy is still present in today’s most advanced bots.

The Atlantic • 9h ago

---

**[Nebius unveils plans to build one of Europe's largest AI factories as region scrambles for compute](https://www.cnbc.com/2026/03/31/nebius-finland-ai-factory-europe-compute.html)**

Europe is racing to create the infrastructure needed to power the AI boom.

CNBC • 22m ago

---

**[Big Tech's $635 billion AI spending faces energy shock test, S&P Global says](https://www.reuters.com/world/china/big-techs-635-billion-ai-spending-faces-energy-shock-test-sp-global-says-2026-03-31/)**

reuters.com • 1h ago

---

**[Equinix Plans More South African Data Centers as Local AI Booms](https://www.bloomberg.com/news/articles/2026-03-31/equinix-plans-more-south-african-data-centers-as-local-ai-booms)**

Bloomberg • 1h ago

---

**[TV star’s AI porn allegations spark national debate in Germany](https://www.theguardian.com/world/2026/mar/30/collien-fernandes-deepfake-porn-allegations-digital-violence-against-women)**

Collien Fernandes accuses ex-husband Christian Ulmen of sharing sexually explicit deepfake images of her online

The Guardian • 12h ago

---

**[Israel targets Iran’s leaders with lethal expertise using new AI platform](https://www.washingtonpost.com/world/2026/03/30/iran-israel-war-killings/)**

The division of responsibility has left Israel to hunt and kill Iranian leaders ruthlessly, using an intelligence apparatus built up to assassinate with lethal proficiency.

The Washington Post • 16h ago

---

**[Trump helped build the Middle East’s AI ambitions. Could his war break them?](https://www.cnn.com/2026/03/30/tech/trump-iran-war-middle-east-ai-intl-hnk)**

President Donald Trump arrived in the Middle East last spring, making deals that would vault the Gulf into the global race for artificial intelligence.

CNN • 4h ago

---

**[Inside David Sacks' new role shaping Trump's AI agenda](https://www.axios.com/2026/03/30/david-sacks-trump-ai-agenda-plan)**

Axios • 5h ago

---

**[Kanye West Makes a Record for the A.I. Era](https://www.newyorker.com/magazine/2026/04/13/kanye-west-music-review-bully)**

Listeners can’t quite tell whether Kanye West’s new album, “Bully,” uses A.I. But the question of what the “real” Ye sounds like has never been simple.

The New Yorker • 9h ago

---

---

## HackerNews: "ai"

**[AI overly affirms users asking for personal advice](https://news.ycombinator.com/item?id=47554773)**

⬆️ 783 • 💬 609 • 2d ago • [news.stanford.edu](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)

---

**[Police used AI facial recognition to wrongly arrest TN woman for crimes in ND](https://news.ycombinator.com/item?id=47563384)**

A Tennessee grandmother spent more than five months in jail after police used an AI facial recognition tool to link her to crimes committed in North Dakota – a state she says she’d never been to before. Police in Fargo, North Dakota, have acknowledged “a few errors” in the case and pledged changes in their operations but stopped short of issuing a direct apology.

⬆️ 433 • 💬 198 • 1d ago • [CNN](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)

---

**[How the AI Bubble Bursts](https://news.ycombinator.com/item?id=47573420)**

The catalysts for a crash are already laid out, and it can happen sooner than most expect. AI is here to stay. If used right, chances are it will make us all more productive. That, on the other hand, does not mean it will be a good investment. Big tech doesn’t need to win, just outspend Magnificent 7 companies are increasing capex to their biggest ever to differentiate their tech from each other and the big AI labs, but the key realization is that they don’t have to spend it to win. It’s a defensive move for them, if they commit $50B, OpenAI and Anthropic need to go raise $100B each to stay competitive, which makes them reliant on investors’ money. As the numbers get bigger, the amount of funds that can write checks of the size required to fill such amounts gets smaller. And many of them are now getting bombed in the Gulf. This is the reason there’s a push for IPOs, it’s because it’s the only option left to keep the funding coming. Taking this into account, Google is extremely well positioned to weather the storm. When they announce capex expenditure, they don’t spend it overnight. They can simply deploy month by month until their competitors struggle to raise and get forced to capitulate. At that point they can just ramp down the spending and declare victory in a cornered market. They don’t need capex, they just need to make it very clear for everyone that nobody can outspend them. It is hard to picture as numbers get so big, but Alphabet (Google’s parent) is ten times more valuable than the biggest military company 1. This also has a great implication for the Mag 7, especially Google: their capex will be a lot smaller in practice than projected, and as investors hate to see high capex in tech, the market will probably reward that if it materializes. As of March 2026, Alphabet’s market cap is ~$2T while Lockheed Martin’s is ~$120B. ↩

⬆️ 360 • 💬 487 • 19h ago • [Volpe’s Blog](https://martinvol.pe/blog/2026/03/30/how-the-ai-bubble-bursts/)

---

**[Miasma: A tool to trap AI web scrapers in an endless poison pit](https://news.ycombinator.com/item?id=47561819)**

Trap AI web scrapers in an endless poison pit. Contribute to austin-weeks/miasma development by creating an account on GitHub.

⬆️ 340 • 💬 243 • 1d ago • [GitHub](https://github.com/austin-weeks/miasma)

---

**[I am definitely missing the pre-AI writing era](https://news.ycombinator.com/item?id=47571279)**

Yesterday, I wrote my first technical draft on what I was working on with the goal to share it publicly on here (well using an account dedicated to t…

⬆️ 305 • 💬 224 • 1d ago • [lesswrong.com](https://www.lesswrong.com/posts/BJ4pnropWdnzzgeJc/i-am-definitely-missing-the-pre-ai-writing-era)

---

**[Folk are getting dangerously attached to AI that always tells them they're right](https://news.ycombinator.com/item?id=47555090)**

: Sycophantic bots coach users into selfish, antisocial behavior, say researchers, and they love it

⬆️ 285 • 💬 224 • 2d ago • [theregister.com](https://www.theregister.com/2026/03/27/sycophantic_ai_risks/)

---

**[Further human + AI + proof assistant work on Knuth's "Claude Cycles" problem](https://news.ycombinator.com/item?id=47557166)**

⬆️ 258 • 💬 182 • 2d ago • [X (formerly Twitter)](https://twitter.com/BoWang87/status/2037648937453232504)

---

**[The first 40 months of the AI era](https://news.ycombinator.com/item?id=47557185)**

A personal blog, by a programmer and IT expert. Essays, Articles, Guides, and Recipes. As well as Code, Quotes, and Links.

⬆️ 214 • 💬 144 • 2d ago • [lzon.ca](https://lzon.ca/posts/other/thoughts-ai-era/)

---

**[Mathematical methods and human thought in the age of AI](https://news.ycombinator.com/item?id=47572771)**

Artificial intelligence (AI) is the name popularly given to a broad spectrum of computer tools designed to perform increasingly complex cognitive tasks, including many that used to solely be the province of humans. As these tools become exponentially sophisticated and pervasive, the justifications for their rapid development and integration into society are frequently called into question, particularly as they consume finite resources and pose existential risks to the livelihoods of those skilled individuals they appear to replace.
  In this paper, we consider the rapidly evolving impact of AI to the traditional questions of philosophy
  with an emphasis on its application in mathematics and on the broader real-world outcomes of its more general use. We assert that artificial intelligence is a natural evolution of human tools developed throughout history to facilitate the creation, organization, and dissemination of ideas, and argue that it is paramount that the development and application of AI remain fundamentally human-centered. With an eye toward innovating solutions to meet human needs, enhancing the human quality of life and expanding the capacity for human thought and understanding, we propose a pathway to integrating AI into our most challenging and intellectually rigorous fields to the benefit of all humankind.

⬆️ 202 • 💬 84 • 21h ago • [arXiv.org](https://arxiv.org/abs/2603.26524)

---

**[What if AI doesn't need more RAM but better math?](https://news.ycombinator.com/item?id=47561297)**

⬆️ 186 • 💬 99 • 1d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-what-if-ai-doesnt-need-more)

---

---

## YouTube Videos: "ai"

**[How to Use AI Agents Better than 99% of People](https://www.youtube.com/watch?v=u_B1p_9q2fw)**

Best AI Agent is Base44 https://base44.pxf.io/c/6440076/3820726/25619?trafcat=agent&sharedid=agent2 ✓ FREE Masterclass: ...

📺 Mikey No Code

👁️ 13K • 💬 6 • ⏱️ 26:48 • 18h ago

---

**[AI is Destroying The Internet](https://www.youtube.com/watch?v=NWQ1CFIj8zo)**

Is the AI bubble finally starting to burst, or is it taking the entire tech industry down with it? In this video, we'll cover how Generative ...

📺 CyberCPU Tech

👁️ 18K • 👍 2K • 💬 654 • ⏱️ 19:23 • 18h ago

---

**[The AI Endgame (12 Scenarios)](https://www.youtube.com/watch?v=FLcrvMfHUJM)**

Detailed sources: https://docs.google.com/document/d/1P1X9xEmmgSYH0g1FSizgV2rDVomb_Wi0TcX-E-0np_Q/edit?tab=t.0 ...

📺 Species | Documenting AGI

👁️ 101K • 👍 6K • 💬 1K • ⏱️ 35:45 • 1d ago

---

**[AI Has Broken the Internet](https://www.youtube.com/watch?v=44JBZwAsfJI)**

Depot CI really is that good, you should try it: https://jetty.to/depot-ci So the web has been breaking a lot lately. Vercel is down.

📺 ForrestKnight

👁️ 58K • 👍 3K • 💬 406 • ⏱️ 17:17 • 12h ago

---

**[China’s New AI Shocks The World: Hits Top 10 Globally Overnight](https://www.youtube.com/watch?v=wXorU2jr6v0)**

Try AI video generation with Kling 3.0 on Higgsfield: https://higgsfield.ai/s/arena-zero-ep1-airevolutionx-FFftuX Xiaomi quietly ...

📺 AI Revolution

👁️ 14K • 👍 468 • 💬 32 • ⏱️ 12:59 • 8h ago

---

**[Anthropic’s New Claude MYTHOS Is The Most Powerful AI Ever!](https://www.youtube.com/watch?v=M6yRREy_5CM)**

Anthropic accidentally exposed Claude MYTHOS, its most powerful AI yet, Meta unveiled a model that predicts brain activity from ...

📺 AI Revolution

👁️ 39K • 👍 1K • 💬 61 • ⏱️ 12:51 • 1d ago

---

**[Things You Should Never Ask AI...](https://www.youtube.com/watch?v=4qYkY4LR2yU)**

i really hope we aren't cooked in a few years. BECOME A MEMBER AND GET PERKS: ...

📺 John Casterline

👁️ 55K • 👍 5K • 💬 512 • ⏱️ 12:44 • 10h ago

---

**[Tristan Harris on ‘The AI Doc,’ Elon Musk, and the Promise and Peril of Tech | Talk Easy](https://www.youtube.com/watch?v=jCvBdmJb45s)**

I got calls from people inside of some of the AI labs,” says technology ethicist Tristan Harris. “And it felt like getting a call from ...

📺 Talk Easy with Sam Fragoso

👁️ 5K • 👍 124 • 💬 50 • ⏱️ 1:25:03 • 1d ago

---

**[48 Days. That&#39;s How Long Before the Helium Runs Out for AI Chips.](https://www.youtube.com/watch?v=sTkqCREdMXo)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 60K • 👍 2K • 💬 429 • ⏱️ 22:21 • 1d ago

---

**[Which Dream Staircase Would You Take? ☁️✨ | Ultimate Oddly Satisfying AI ASMR Vol. 3](https://www.youtube.com/watch?v=YN1r1Xs6Q2M)**

Which Dream Staircase Would You Take? ☁️✨ | Ultimate Oddly Satisfying AI ASMR Vol. 3 https://youtu.be/YN1r1Xs6Q2M Step ...

📺 JellyBed ASMR

👁️ 22K • 👍 687 • 💬 46 • ⏱️ 2:02:39 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 337,432 • ❤️ 1,781 • 7d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 50,497 • ❤️ 583 • 23h ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 3,721 • ❤️ 536 • 3d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 17,643 • ❤️ 688 • 4d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`text-generation` `20.9B`

⬇️ 2,387 • ❤️ 301 • 1d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 155,487 • ❤️ 332 • 6d ago

---

**[daVinci-MagiHuman](https://huggingface.co/GAIR/daVinci-MagiHuman)**

*SII - GAIR*

daVinci-MagiHuman is a fast, single-stream Transformer model for generating high-quality, human-centric audio-video from text or images. It excels at expressive facial performance, natural speech-expression coordination, and accurate audio-video synchronization across multiple languages, with inference speeds of 2 seconds for 256p and 38 seconds for 1080p.

`image-to-video`

⬇️ 605 • ❤️ 268 • 5d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 592,823 • ❤️ 1,093 • 20d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 623,469 • ❤️ 839 • 27d ago

---

**[tribev2](https://huggingface.co/facebook/tribev2)**

*AI at Meta*

TRIBE v2 is a multimodal foundation model that integrates LLaMA 3.2 (text), V-JEPA2 (video), and Wav2Vec-BERT (audio) to predict fMRI brain responses. It maps these representations onto the cortical surface for in-silico neuroscience research, enabling analysis of brain activity elicited by naturalistic stimuli.

⬇️ 14,264 • ❤️ 203 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 144 • 💬 7 • ⭐ 31,077 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 33 • 💬 2 • ⭐ 44,771 • 15mo ago

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

▲ 17 • 💬 4 • ⭐ 4,082 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 15 • 💬 1 • ⭐ 10,986 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 38 • 💬 5 • ⭐ 1,954 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 11 • 💬 2 • ⭐ 1,548 • 17d ago

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

⭐ 62.1k • 🔱 8.7k • 5d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 23.3k • 🔱 1.1k • 4d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 14.0k • 🔱 764 • 1h ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 9.5k • 🔱 794 • 12m ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 7.9k • 🔱 1.2k • 2d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 6.4k • 🔱 757 • 1d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 5.1k • 🔱 244 • 20m ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.1k • 🔱 393 • 2d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.4k • 🔱 222 • 17d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 3.3k • 🔱 107 • 19d ago

---

---

*Generated by PeekDeck - A glance is all you need*
