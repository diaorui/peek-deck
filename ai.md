---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2025-12-16T10:23:25.491109+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** December 16, 2025 at 10:23 UTC  
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

**[Linus Torvalds is 'a huge believer' in using AI to maintain code - just don't call it a revolution](https://www.reddit.com/r/artificial/comments/1pntfs5/linus_torvalds_is_a_huge_believer_in_using_ai_to/)**

Torvalds is sick of all the AI hype, but says AI is finally maturing to the point where it will be useful for Linux developers and maintainers.

🔗 [ZDNET](https://www.zdnet.com/article/linus-torvalds-ai-tool-maintaining-linux-code/) • 5h ago

---

**[If AI replaces workers, should it also pay taxes?](https://www.reddit.com/r/artificial/comments/1pn7tvx/if_ai_replaces_workers_should_it_also_pay_taxes/)**

The technological race among industry giants and the wave of layoffs they have announced has revived the debate about the advisability of taxing automation

🔗 [EL PAÍS English](https://english.elpais.com/technology/2025-11-30/if-ai-replaces-workers-should-it-also-pay-taxes.html) • 20h ago

---

**[Nvidia Becomes a Major Model Maker With Nemotron 3](https://www.reddit.com/r/artificial/comments/1pn9big/nvidia_becomes_a_major_model_maker_with_nemotron_3/)**

The world’s top chipmaker wants open source AI to succeed—perhaps because closed models increasingly run on its rivals’ silicon.

🔗 [WIRED](https://www.wired.com/story/nvidia-becomes-major-model-maker-nemotron-3/) • 19h ago

---

**[Compact offline medical SLM with Native Knowledge Graph + RAG audit (benchmark + HF demo)](https://www.reddit.com/r/artificial/comments/1pnwh03/compact_offline_medical_slm_with_native_knowledge/)**

I’ve been experimenting with a slightly different approach to medical LMs and would really value feedback from people working on ML, health IT, or clinical education. Instead of chasing more parameters, I built a ~6 GB medical SLM that’s tightly coupled to a biomedical knowledge graph and a self‑contained RAG/audit layer. The goal is not to sound smarter than GPT‑4, but to be *safer, more structured, and auditable* for clinical decision support / education use cases. Core setup: - Base: BioGPT‑Large (~6 GB footprint) - Biomedical knowledge graph: 5k+ nodes, 25k+ edges across diseases, symptoms, treatments, risk factors, diagnostics, body parts, cellular structures - Graph‑aware embeddings + special tokens so the model “anchors” to graph concepts - Built‑in RAG/audit: entity + semantic search over the graph to validate each answer against the graph before accepting it I ran a small 5 case internal evaluation on multi sentence clinical questions (diagnosis + risk factors + tests + treatments + contraindications). Scoring dimensions: contextual accuracy, multi‑hop reasoning, entity structure, clarity, hallucination resistance. This model landed at 4.5/5 overall, including 5/5 on hallucination resistance. Baselines were typical medical SLMs (BioBERT/PubMedBERT/ClinicalBERT) and large general LLMs. Trade‑offs vs big LLMs: less fluent, more constrained; better at staying inside medically grounded entities/relations; easier to audit because every answer is tied back to explicit graph nodes. For anyone curious, there’s a HF Space demo here (model is private, Space is public responses can take 30–180s+ because of shared infra; locally it’s ~3–5s per query) on GPU, 7-10s on CPU: https://huggingface.co/spaces/cmtopbas/medical-slm-testing I’d really appreciate: - Critical feedback on the architecture (graph + audit layer) - Ideas for realistic, high‑impact use cases (e.g. med ed, trainee tools, clinician reference) where this kind of architecture would be useful - Pointers to similar work I should be aware of so I’m not reinventing the wheel Happy to share more detailed benchmarks/trace examples if there’s interest. Question 1: A 55-year-old male patient presents with persistent chest pain radiating to the left arm. He has a history of hypertension and Type 2 diabetes. ECG shows ST-segment elevation. The patient is allergic to aspirin. Question: Based on the patient’s condition, what treatments are recommended, which are contraindicated, and which risk factors are involved? Prompt → Categories: ['BodyPart', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 9 Answer → Categories: ['BodyPart', 'Disease', 'RiskFactor', 'Symptom', 'Treatment'] | Nodes: 10 ◇ Best effort (Missing: Riskfactor) Answer 1: Hypertension is common among patients who have CKD. It can be treated effectively if it is identified early and managed appropriately. Patients should avoid medications that may exacerbate their symptoms or cause adverse effects such as angiotensin converting enzyme (ACE) inhibitors. If an ACE inhibitor cannot be used because of intolerance, then other antihypertensive agents are available. In addition to blood pressure control, treatment for heart failure includes use of diuretics, beta blockers, aldosterone antagonists, and digoxin. Treatment options also include calcium channel blockers, alpha adrenergic receptor agonists, vasodilators, and endothelin receptor antagonists. Please consult a healthcare professional for personalized medical advice. Question 2: Female patient presents with fatigue, swelling in her ankles, has a history of hypertension and chronic kidney disease. Also experiences persistent cough when taking ACE inhibitors and her Echocardiogram shows reduced ejection fraction. What is the diagnosis and treatment based on her combined diagnosis Prompt → Categories: ['BodyPart', 'Disease', 'RiskFactor', 'Symptom', 'Treatment'] | Nodes: 8 Answer → Categories: ['BodyPart', 'DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Treatment'] | Nodes: 7 ✓ Graph-validated (Valid) Answer 2: The diagnosis is acute heart failure (HF) due to left ventricular systolic dysfunction. Treatment includes diuretics for congestion and vasodilators or inotropes for hypotension. Angiotensin-converting enzyme inhibitor therapy should be discontinued if there are signs of worsening renal function. Hypertension can worsen cardiac outcomes by increasing afterload on the heart. Chronic kidney disease may also contribute to poor prognosis through increased risk of cardiovascular events and death. Please consult a healthcare professional for personalized medical advice. Question 3: A 45-year-old male patient reports frequent urination, excessive thirst, and fatigue. He has a family history of type 2 diabetes and is overweight. Blood tests show elevated fasting glucose and HbA1c levels. Identify the disease, list risk factors, symptoms, recommended treatments, and contraindications Prompt → Categories: ['DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 5 Answer → Categories: ['BodyPart', 'DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Treatment'] | Nodes: 9 ✓ Graph-validated (Valid) Answer 3: Type 2 Diabetes Mellitus (T2DM) is an endocrine disorder that affects millions worldwide. It can be diagnosed by measuring blood sugar levels or glycated hemoglobin A1c. The American Diabetes Association recommends screening for T2DM in adults with any one of the following characteristics: age > 4 0 years; < 1 8 y / o Body Mass Index (BMI); African ancestry; Hispanic ethnicity; Asian descent; or having polycystic ovarian syndrome. Patients should also have at least two other features of the metabolic syndrome to increase their risk of developing T2DM. Treatment options are based on patients' comorbidities and goals for glycemic control. Lifestyle modifications such as diet and exercise are first line treatment but may not achieve optimal results if they fail. Medications including metformin, sulfonylureas, thiazolidinediones, dipeptidyl peptidase IV inhibitors, glucagon like peptide-1RAs. Please consult a healthcare professional for personalized medical advice. Question 4: A 30-year-old female patient reports persistent cough, fever, and shortness of breath. She recently returned from a trip abroad and has a mild history of asthma. Chest X-ray shows patchy infiltrates in the lower lobes. Identify the disease, list risk factors, symptoms, recommended treatments, and contraindications. Prompt → Categories: ['DiagnosticTest', 'Disease', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 5 Answer → Categories: ['DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 6 ✓ Graph-validated (Valid) Answer 4: The diagnosis is acute respiratory distress syndrome (ARDS) caused by pneumonia with secondary bacterial infection. ARDS can be fatal if not treated promptly. Risk factors for ARDS are discussed along with treatment options including antibiotics, corticosteroids, mechanical ventilation, vasopressors, and extracorporeal membrane oxygenation. Treatment should focus on preventing further complications such as nosocomial infections or ventilator associated events. Please consult a healthcare professional for personalized medical advice. Question 5: A 50-year-old male patient experiences abdominal pain, bloating, and intermittent diarrhea. He has a family history of celiac disease and reports gluten sensitivity. Blood tests show elevated anti-tTG antibodies. Identify the disease, list risk factors, symptoms, recommended treatments, and contraindications Prompt → Categories: ['DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 7 Answer → Categories: ['BodyPart', 'DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Treatment'] | Nodes: 6 ✓ Graph-validated (Valid) Answer 5: Celiac Disease is an autoimmune disorder that affects approximately 1% to 2% of people in North America. It can be diagnosed by serologic testing for IgA antitissue transglutaminase (anti-tTG) antibody levels or duodenal biopsy. The diagnosis should trigger a discussion about dietary restrictions with patients and their families. Patients must also understand the potential risks associated with untreated celiac disease, including increased susceptibility to cancer, cardiovascular diseases, type I diabetes mellitus, osteoporosis, infertility, neurologic disorders, and psychiatric conditions. Treatment options are limited but may involve lifelong adherence to a strict gluten free diet. This includes avoiding wheat products, rye, barley, oats, legumes, nuts, seeds, and other grains containing glutenins. Other treatment options include oral supplements such as zinc sulfate and magnesium oxide; however, these have not been. Please consult a healthcare professional for personalized medical advice. Please consult a healthcare professional for personalized medical advice.

2h ago

---

**[Microsoft Scales Back AI Goals Because Almost Nobody Is Using Copilot](https://www.reddit.com/r/artificial/comments/1pmuboi/microsoft_scales_back_ai_goals_because_almost/)**

RIP Copilot.

🔗 [extremetech.com](https://www.extremetech.com/computing/microsoft-scales-back-ai-goals-because-almost-nobody-is-using-copilot) • 1d ago

---

**[Not all CEOs favor Trump's executive order to block state AI laws](https://www.reddit.com/r/artificial/comments/1pnbrtt/not_all_ceos_favor_trumps_executive_order_to/)**

Also: All the news and watercooler chat from Fortune.

🔗 [Fortune](https://fortune.com/2025/12/15/trump-ai-state-laws-executive-order-ceo-reaction/) • 17h ago

---

**[How Claude & ChatGPT's Memory System Works](https://www.reddit.com/r/artificial/comments/1pnv4u8/how_claude_chatgpts_memory_system_works/)**

When I reverse-engineered ChatGPT’s memory system, I found it uses pre-computed summaries injected into every prompt. But Claude’s approach is different. Through extensive experimentation, I discovered Claude uses on-demand tools and selective retrieval, a fundamentally different architecture. But how does this actually work? And how does it compare to ChatGPT’s approach?
This is the second post in a series where I reverse-engineer the memory systems of popular AI assistants. The first post focused on ChatGPT’s memory system.

🔗 [manthanguptaa.in](https://manthanguptaa.in/posts/claude_memory) • 3h ago

---

**[It's been a big week for Agentic AI ; Here are 10 massive developments you might've missed:](https://www.reddit.com/r/artificial/comments/1pnf368/its_been_a_big_week_for_agentic_ai_here_are_10/)**

Stripe launches full Agentic Commerce Suite OpenAI + Anthropic found Agentic AI Foundation Google drops Deep Research + AlphaEvolve agent A collection of AI Agent Updates! 🧵 1. Stripe Launches Agentic Commerce Suite Single integration for businesses to sell via multiple AI agents. Handles product discovery, agentic checkout, payments, and fraud. Manage all agents from Stripe Dashboard. Works with existing commerce stack. AI-native commerce infrastructure now available. 2. OpenAI Co-Founds Agentic AI Foundation with Anthropic and Block Under Linux Foundation to support open, interoperable standards for agentic AI. Donating to establish standards enabling safe, reliable agents across tools and repositories. Industry leaders aligning on agent interoperability. 3. Google Opens Gemini Deep Research Agent to Developers Most advanced autonomous research capabilities now embeddable in applications for first time. Also open-sourcing DeepSearchQA benchmark for evaluating agents on complex search tasks. Google's agent infrastructure available to all developers. 4. Anthropic is Developing New Agent Mode for Claude Code-named "Yukon Gold" - tasks-based complex agent experience with toggle between classic chat and agent mode. Also testing pixel art avatar generation from uploaded photos. Claude may be getting a dedicated agent interface. 5. Google Cloud Unveils AlphaEvolve Coding Agent Gemini-powered agent for designing advanced algorithms. Uses LLMs to propose intelligent code modifications with feedback loop that evolves algorithms to be more efficient. Now in private preview. Haven’t tried, but seems promising. 6. Real Agent Usage Data: Harvard Analyzes Hundreds of Millions of Queries Perplexity study shows 55% personal use, 30% professional. Productivity/workflow dominates (36% of queries), followed by learning/research (21%). Users shift from simple to complex tasks over time. Real data on how people actually use agents. 7. Stitchbygoogle Launches Redesign Agent with Code Generation Screenshot apps, visually reimagine with Gemini Pro, then convert redesigns into working HTML. "Shipmas" week begins - new ship daily with big launch Wednesday. Screenshot → Redesign → Code → Deploy workflow now live. 8. Cursor Agents Can Now Debug Your Hardest Bugs Debug Mode instruments code, spins up server, captures logs, and streams runtime data to agent. Version 2.2 adds multi-agent judging (picks best solution) and Plan Mode improvements with diagrams. AI agents now debugging production code. 9. Code Drops Major Agent Experience Upgrade Agent sessions integrated into chat view. Isolated background agents via Git worktrees enable multiple agents without conflicts. Seamless delegation with automatic context transfer between local, background, and cloud agents. Multi-agent workflows now native in VS Code. 10. Microsoft Research Unveils Agent Lightning Decouples how agents work from training. Turns each agent step into reinforcement learning data. Developers can improve agent performance with almost zero code changes. RL for agents without code rewrites. That's a wrap on this week's Agentic news. Which update are you trying first? LMK if this was helpful | More weekly AI + Agentic content releasing ever week!

15h ago

---

**[One-Minute Daily AI News 12/15/2025](https://www.reddit.com/r/artificial/comments/1pnue0h/oneminute_daily_ai_news_12152025/)**

US government launches ‘Tech Force’ to hire AI talent.[1] Deep-learning model predicts how fruit flies form, cell by cell.[2] Nvidia bulks up open source offerings with an acquisition and new open AI models.[3] Podcast industry under siege as AI bots flood airways.[4] Sources: [1] https://www.cnn.com/2025/12/15/tech/government-tech-force-ai [2] https://news.mit.edu/2025/deep-learning-model-predicts-how-fruit-flies-form-1215 [3] https://techcrunch.com/2025/12/15/nvidia-bulks-up-open-source-offerings-with-an-acquisition-and-new-open-ai-models/ [4] https://www.yahoo.com/news/articles/podcast-industry-under-siege-ai-051031178.html

4h ago

---

**[The best Chinese open-weight models — and the strongest US rivals](https://www.reddit.com/r/artificial/comments/1pneiei/the_best_chinese_openweight_models_and_the/)**

The Understanding AI guide to open-weight models.

🔗 [understandingai.org](https://www.understandingai.org/p/the-best-chinese-open-weight-models) • 16h ago

---

---

## Google News: "ai"

**[How Tech’s Biggest Companies Are Offloading the Risks of the A.I. Boom](https://www.nytimes.com/2025/12/15/technology/ai-risks-debt.html)**

The New York Times • 13h ago

---

**[‘We have a right to do this’: DeSantis wants Florida to move ahead with AI policies](https://www.politico.com/news/2025/12/15/we-have-a-right-to-do-this-desantis-wants-florida-to-move-ahead-with-ai-policies-00690680)**

Politico • 16h ago

---

**[Trump admin to hire 1,000 specialists for 'Tech Force' to build AI, finance projects](https://www.cnbc.com/2025/12/15/trump-ai-tech-force-amazon-apple.html)**

A slew of tech giants, including Amazon Web Services, Apple, Google Public Sector, Dell Technologies, Microsoft, Nvidia and OpenAI, are listed as partners.

CNBC • 17h ago

---

**[Trump Signs Executive Order to Neuter State A.I. Laws](https://www.nytimes.com/2025/12/11/technology/ai-trump-executive-order.html)**

The New York Times • 4d ago

---

**[Teachers are using software to see if students used AI. What happens when it's wrong?](https://www.npr.org/2025/12/16/nx-s1-5492397/ai-schools-teachers-students)**

School districts from Utah to Ohio to Alabama are spending thousands of dollars on these tools, despite research showing the technology is far from reliable.

NPR • 23m ago

---

**[Here's how AI is helping holiday shoppers](https://www.usatoday.com/story/money/2025/12/16/holiday-shoppers-ai-gift-giving/87718158007/)**

More than half or 53% of shoppers surveyed by CouponFollow said they have or plan to use AI for holiday shopping.

USA Today • 17m ago

---

**[CEOs Want to Keep Pouring Money Into AI, Despite Weak Returns: Survey](https://gizmodo.com/ceos-want-to-keep-pouring-money-into-ai-despite-weak-returns-survey-2000700007)**

Most executives say their AI projects arenât delivering returns, but nearly 70% still plan to spend more next year.

Gizmodo • 22m ago

---

**[Google AI summaries are ruining the livelihoods of recipe writers: ‘It’s an extinction event’](https://www.theguardian.com/technology/2025/dec/15/google-ai-recipes-food-bloggers)**

AI Mode is mangling recipes by merging instructions from multiple creators – and causing them huge dips in ad traffic

The Guardian • 11h ago

---

**[The great AI hype correction of 2025](https://www.technologyreview.com/2025/12/15/1129174/the-great-ai-hype-correction-of-2025/)**

Four ways to think about this year's reckoning

MIT Technology Review • 1d ago

---

**[Opinion | AI Is About to Empty Madison Avenue](https://www.wsj.com/opinion/ai-is-about-to-empty-madison-avenue-58ab2ea2?gaa_at=eafs&gaa_n=AWEtsqd0jLjzAf4gD7dKalAECg5WAPd5CwfzafcZCKodVKUVYufBJws9JIhK&gaa_ts=69413689&gaa_sig=DSOmMjDAc4KRYHUdy8nFTuAFsDgSRmfAMu-vuLSkpyUkSLOa_At98Xxatyuo1BM1QgmsAYixBt9yRBodCjzR8g%3D%3D)**

The Wall Street Journal • 15h ago

---

---

## HackerNews: "ai"

**[If AI replaces workers, should it also pay taxes?](https://news.ycombinator.com/item?id=46268709)**

The technological race among industry giants and the wave of layoffs they have announced has revived the debate about the advisability of taxing automation

⬆️ 553 • 💬 922 • 1d ago • [EL PAÍS English](https://english.elpais.com/technology/2025-11-30/if-ai-replaces-workers-should-it-also-pay-taxes.html)

---

**[8M users' AI conversations sold for profit by "privacy" extensions](https://news.ycombinator.com/item?id=46284266)**

⬆️ 483 • 💬 154 • 7h ago • [koi.ai](https://www.koi.ai/blog/urban-vpn-browser-extension-ai-conversations-data-collection)

---

**[Ask HN: How can I get better at using AI for programming?](https://news.ycombinator.com/item?id=46255285)**

⬆️ 456 • 💬 459 • 2d ago

---

**[AI agents are starting to eat SaaS](https://news.ycombinator.com/item?id=46268452)**

Software ate the world. Agents are going to eat SaaS.

⬆️ 373 • 💬 367 • 1d ago • [Martin Alderson](https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/)

---

**[Microsoft Copilot AI Comes to LG TVs, and Can't Be Deleted](https://news.ycombinator.com/item?id=46268844)**

Microsoft's Copilot AI chatbot is arguably one of the most controversial add-ons ever implemented in the Windows 11 operating system. However, the controversy doesn't stop at PC operating systems. It seems to extend to TVs as well. According to Reddit user u/defjam16, his LG TV webOS received an upd...

⬆️ 280 • 💬 296 • 1d ago • [TechPowerUp](https://www.techpowerup.com/344075/microsoft-copilot-ai-comes-to-lg-tvs-and-cant-be-deleted)

---

**[JetBlue flight averts mid-air collision with US Air Force jet](https://news.ycombinator.com/item?id=46281944)**

⬆️ 273 • 💬 161 • 11h ago • [reuters.com](https://www.reuters.com/world/americas/jetblue-flight-averts-mid-air-collision-with-us-air-force-jet-2025-12-15/)

---

**[AI and the ironies of automation – Part 2](https://news.ycombinator.com/item?id=46262816)**

Some (well-known) consequences of AI automating work

⬆️ 253 • 💬 118 • 1d ago • [Uwe Friedrichsen](https://www.ufried.com/blog/ironies_of_ai_2/)

---

**[The Gorman Paradox: Where Are All the AI-Generated Apps?](https://news.ycombinator.com/item?id=46262545)**

In 1950, while discussing the recent wave of flying saucer reports over lunch with colleagues at Los Alamos National Laboratory in New Mexico, physicist Enrico Fermi asked a simple question. There …

⬆️ 158 • 💬 218 • 1d ago • [Codemanship's Blog](https://codemanship.wordpress.com/2025/12/14/the-gorman-paradox-where-are-all-the-ai-generated-apps/)

---

**[If a Meta AI model can read a brain-wide signal, why wouldn't the brain?](https://news.ycombinator.com/item?id=46260106)**

In 2023, Meta researchers were able to decode images in thoughts from the brain's magnetic fields. What if that's how the brain coordinates it's own global state?

⬆️ 136 • 💬 91 • 2d ago • [1393](https://1393.xyz/writing/if-a-meta-ai-model-can-read-a-brain-wide-signal-why-wouldnt-the-brain)

---

**[Willison on Merchant's "Copywriters reveal how AI has decimated their industry"](https://news.ycombinator.com/item?id=46261998)**

Brian Merchant has been collecting personal stories for his series AI Killed My Job - previously covering tech workers, translators, and artists - and this latest piece includes anecdotes from …

⬆️ 80 • 💬 89 • 2d ago • [Simon Willison’s Weblog](https://simonwillison.net/2025/Dec/14/copywriters-reveal-how-ai-has-decimated-their-industry/)

---

---

## YouTube Videos: "ai"

**[Artificial Intelligence in 2025 | 60 Minutes Full Episodes](https://www.youtube.com/watch?v=KpOcUrPdx-4)**

From November, Anderson Cooper's report on why Anthropic's CEO spends so much time warning of AI's potential dangers.

📺 60 Minutes

👁️ 530K • 👍 8K • 💬 1K • ⏱️ 1:21:07 • 2d ago

---

**[OpenAI Just Caught an AI Thinking!](https://www.youtube.com/watch?v=YBRyR6FPgl4)**

OpenAI released circuit-sparsity, a research drop that exposes how a language model makes decisions internally. Instead of ...

📺 AI Revolution

👁️ 41K • 👍 2K • 💬 162 • ⏱️ 12:07 • 1d ago

---

**[900 Days Left – AI Is Coming for Capitalism](https://www.youtube.com/watch?v=A8mj1Ngz2JI)**

Welcome to Impact Theory with Tom Bilyeu. In today's Deep Dive episode, Tom Bilyeu tackles one of the most urgent questions of ...

📺 Tom Bilyeu

👁️ 51K • 👍 2K • 💬 628 • ⏱️ 23:28 • 21h ago

---

**[The $25 TRILLION AI Bubble Is BURSTING](https://www.youtube.com/watch?v=UQhM13yK6DQ)**

IBM's CEO said there is “no way” that the massive spending on AI and data centers will ever pay off. For the first time in this bubble ...

📺 Eurodollar University

👁️ 111K • 👍 4K • 💬 600 • ⏱️ 20:44 • 1d ago

---

**[Lady Soldier Rescues Grandma and Builds Golden Carousel for Her 😭 #ai #save #army](https://www.youtube.com/watch?v=Rg0j9jUTTPM)**

Lady Soldier Rescues Grandma and Builds Golden Carousel for Her #ai #save #army.

📺 Anime world 

👁️ 207K • 👍 1K • 💬 1 • ⏱️ 0:22 • 1d ago

---

**[China Rejects US-Made AI Chips, The White House Admits That Export Strategy May Be Failing](https://www.youtube.com/watch?v=WRwqRoIfAAU)**

The White House has raised fresh concerns after admitting that China is turning away U.S.-made AI chips, including Nvidia's H200 ...

📺 Mint

👁️ 45K • 👍 567 • 💬 231 • ⏱️ 4:14 • 1d ago

---

**[#samsung Unveils Its AI Humanoid Robot ‘Leno X’. #robotics #robot  #humanoidrobot #ai](https://www.youtube.com/watch?v=g4hvzxnSLRc)**

📺 AI . Robot

👁️ 190K • 👍 2K • 💬 18 • ⏱️ 0:21 • 1d ago

---

**[Josh Johnson shares why he thinks that ultimately, AI can&#39;t win when it comes to comedy #AfterTheCut](https://www.youtube.com/watch?v=whpGVeJidS8)**

📺 The Daily Show

👁️ 210K • 👍 16K • 💬 407 • ⏱️ 2:38 • 19h ago

---

**[Why YouTube Won&#39;t Stop Pushing AI Nonsense...](https://www.youtube.com/watch?v=We7FzVfIIcs)**

Hello guys and gals, it's me Mutahar again! This time we take a look at why sites like YouTube are taking AI so seriously.

📺 SomeOrdinaryGamers

👁️ 85K • 👍 5K • 💬 941 • ⏱️ 19:00 • 2d ago

---

**[Build anything with Google AI Studio, here&#39;s how...](https://www.youtube.com/watch?v=IVWTX1CyOEw)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses https://juliangoldieai.com/07L1kg Get a ...

📺 Julian Goldie SEO

👁️ 6K • 👍 113 • 💬 10 • ⏱️ 36:04 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)**

*Tongyi-MAI*

Z-Image-Turbo is a highly efficient text-to-image diffusion transformer model with 6B parameters, achieving sub-second inference on H800 GPUs with 8 NFEs. It excels at photorealistic generation, bilingual text rendering (English/Chinese), and instruction adherence, fitting within 16GB VRAM.

`text-to-image`

⬇️ 296,552 • ❤️ 2,781 • 7d ago

---

**[Devstral-Small-2-24B-Instruct-2512](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)**

*Mistral AI_*

Devstral Small 2 24B Instruct 2512 is a lightweight, agentic LLM for software engineering tasks, excelling at codebase exploration and multi-file editing with a 256k context window and FP8 precision. It is ideal for AI code assistants and agentic coding use cases, capable of running locally on consumer hardware.

`24.0B`

⬇️ 28,106 • ❤️ 368 • 1d ago

---

**[VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)**

*Microsoft*

VibeVoice-Realtime-0.5B is a lightweight, real-time text-to-speech model with ~300ms latency, supporting streaming input for robust long-form generation, ideal for live narration and LLM integration.

`text-to-speech` `1.0B`

⬇️ 158,614 • ❤️ 871 • 3d ago

---

**[GLM-4.6V-Flash](https://huggingface.co/zai-org/GLM-4.6V-Flash)**

*Z.ai*

GLM-4.6V-Flash is a lightweight multimodal model for image-text-to-text tasks, featuring native function calling for vision-driven tool use and interleaved content generation. It excels at multimodal document understanding, frontend replication, and low-latency applications.

`image-text-to-text` `10.3B`

⬇️ 102,395 • ❤️ 455 • 6d ago

---

**[AutoGLM-Phone-9B](https://huggingface.co/zai-org/AutoGLM-Phone-9B)**

*Z.ai*

AutoGLM-Phone-9B is a vision-language model for mobile intelligent assistance, enabling automated smartphone operations via ADB by understanding UI elements and executing natural language commands for task completion.

`image-text-to-text` `934,400`

⬇️ 51,591 • ❤️ 312 • 7d ago

---

**[GLM-ASR-Nano-2512](https://huggingface.co/zai-org/GLM-ASR-Nano-2512)**

*Z.ai*

GLM-ASR-Nano-2512 is a 1.5B parameter speech recognition model excelling in low-volume and dialectal (Cantonese) speech, outperforming Whisper V3 on benchmarks with a 4.10 average error rate. It's ideal for noisy environments and diverse linguistic use cases.

`automatic-speech-recognition` `2.3B`

⬇️ 74,813 • ❤️ 233 • 4d ago

---

**[Devstral-2-123B-Instruct-2512](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512)**

*Mistral AI_*

Devstral 2 123B Instruct is an FP8 agentic LLM optimized for software engineering tasks, excelling in codebase exploration, multi-file editing, and powering SWE agents with a 256k context window.

`125.0B`

⬇️ 6,543 • ❤️ 215 • 1d ago

---

**[GLM-TTS](https://huggingface.co/zai-org/GLM-TTS)**

*Z.ai*

GLM-TTS is a controllable, zero-shot text-to-speech system that uses a two-stage LLM and Flow Matching architecture, enhanced by multi-reward reinforcement learning for expressive emotion control and high-quality synthesis. It supports voice cloning from short prompts and streaming inference for interactive applications.

`text-to-speech`

⬇️ 0 • ❤️ 212 • 5d ago

---

**[NVIDIA-Nemotron-3-Nano-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 is a 30B parameter LLM with a hybrid MoE/Mamba architecture, excelling at reasoning tasks by generating explicit reasoning traces. It supports multiple languages and is suitable for commercial use, offering high accuracy in complex problem-solving.

`text-generation` `31.6B`

⬇️ 10,487 • ❤️ 185 • 10h ago

---

**[AutoGLM-Phone-9B-Multilingual](https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual)**

*Z.ai*

AutoGLM-Phone-9B-Multilingual is a vision-language model for mobile intelligent assistance, capable of understanding smartphone UIs via multimodal perception and executing tasks through ADB. It enables natural language control for automated operations on Android devices.

`image-text-to-text` `934,400`

⬇️ 7,731 • ❤️ 181 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based framework for real-time portrait animation that enhances speed and efficiency through multi-stage training, hybrid implicit signals, appearance distillation, and autoregressive micro-chunk streaming.

▲ 19 • 💬 2 • ⭐ 341 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2512.11253) • [💻 code](https://github.com/GVCLab/PersonaLive)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 130 • 💬 6 • ⭐ 18,200 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[DeepCode: Open Agentic Coding](https://huggingface.co/papers/2512.07921)**

*Zongwei Li, Zhonghang Li, Zirui Guo et al. (5 authors)*

DeepCode, a fully autonomous framework, addresses the challenges of document-to-codebase synthesis by optimizing information flow through source compression, structured indexing, knowledge injection, and error correction, achieving state-of-the-art performance and surpassing human experts.

▲ 25 • 💬 2 • ⭐ 12,434 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2512.07921) • [💻 code](https://github.com/HKUDS/DeepCode)

---

**[Decoupled DMD: CFG Augmentation as the Spear, Distribution Matching as the Shield](https://huggingface.co/papers/2511.22677)**

*Dongyang Liu, Peng Gao, David Liu et al. (11 authors)*

🏢 Tongyi-MAI

The study reveals that in text-to-image generation, CFG Augmentation is the primary driver of few-step distillation in Distribution Matching Distillation (DMD), while the distribution matching term acts as a regularizer.

▲ 27 • 💬 2 • ⭐ 7,026 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2511.22677) • [💻 code](https://github.com/Tongyi-MAI/Z-Image/tree/main) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer](https://huggingface.co/papers/2511.22699)**

*Z-Image Team, Huanqia Cai, Sihan Cao et al. (21 authors)*

🏢 Tongyi-MAI

Z-Image, a 6B-parameter Scalable Single-Stream Diffusion Transformer (S3-DiT) model, achieves high-performance image generation with reduced computational cost, offering sub-second inference and compatibility with consumer hardware.

▲ 198 • 💬 4 • ⭐ 7,017 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2511.22699) • [💻 code](https://github.com/Tongyi-MAI/Z-Image) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[V-RGBX: Video Editing with Accurate Controls over Intrinsic Properties](https://huggingface.co/papers/2512.11799)**

*Ye Fang, Tong Wu, Valentin Deschaintre et al. (9 authors)*

🏢 Adobe

V-RGBX is an end-to-end framework for intrinsic-aware video editing that combines video inverse rendering, photorealistic synthesis, and keyframe-based editing to produce consistent and physically plausible edits.

▲ 27 • 💬 2 • ⭐ 45 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2512.11799) • [💻 code](https://github.com/Aleafy/V-RGBX) • [🔗 project](https://aleafy.github.io/vrgbx/)

---

**[Promptomatix: An Automatic Prompt Optimization Framework for Large
  Language Models](https://huggingface.co/papers/2507.14241)**

*Rithesh Murthy, Ming Zhu, Liangwei Yang et al. (9 authors)*

Promptomatix automates prompt optimization for Large Language Models, improving performance and efficiency across various tasks.

▲ 17 • 💬 2 • ⭐ 430 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.14241) • [💻 code](https://github.com/SalesforceAIResearch/promptomatix)

---

**[The Well: a Large-Scale Collection of Diverse Physics Simulations for
  Machine Learning](https://huggingface.co/papers/2412.00568)**

*Ruben Ohana, Michael McCabe, Lucas Meyer et al. (26 authors)*

A large-scale dataset collection, The Well, provides diverse numerical simulations for benchmarking machine learning models in physical systems simulation.

▲ 23 • 💬 2 • ⭐ 1,596 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.00568) • [💻 code](https://github.com/PolymathicAI/the_well)

---

**[Wan-Move: Motion-controllable Video Generation via Latent Trajectory Guidance](https://huggingface.co/papers/2512.08765)**

*Ruihang Chu, Yefei He, Zhekai Chen et al. (13 authors)*

🏢 TongyiLab

Wan-Move enhances motion control in video generative models by integrating motion-aware features into latent space, enabling high-quality and scalable video synthesis.

▲ 121 • 💬 3 • ⭐ 400 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2512.08765) • [💻 code](https://github.com/ali-vilab/Wan-Move) • [🔗 project](https://wan-move.github.io/)

---

**[Sharp Monocular View Synthesis in Less Than a Second](https://huggingface.co/papers/2512.10685)**

*Lars Mescheder, Wei Dong, Shiwei Li et al. (13 authors)*

🏢 Apple

SHARP synthesizes photorealistic views from a single image using a 3D Gaussian representation, achieving state-of-the-art results with rapid processing.

▲ 2 • 💬 2 • ⭐ 163 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2512.10685) • [💻 code](https://github.com/apple/ml-sharp) • [🔗 project](https://apple.github.io/ml-sharp/)

---

---

## GitHub Repositories: "ai"

**[zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)**

An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone

`Python` `agent` `phone-use-agent`

⭐ 16.1k • 🔱 2.5k • 46m ago

---

**[Anionex/banana-slides](https://github.com/Anionex/banana-slides)**

一个基于nano banana pro🍌的原生AI PPT生成应用，迈向真正的＂Vibe PPT＂; 支持上传任意模板图片；上传任意素材&智能解析；一句话/大纲/页面描述自动生成PPT；口头修改指定区域、一键导出 - An AI-native PPT generator based on nano banana pro🍌

`Python` `ai-ppt-maker` `ai-slide-builder` `ai-slides` `llm` `nanobananapro`

⭐ 3.7k • 🔱 404 • 5h ago

---

**[glidea/banana-prompt-quicker](https://github.com/glidea/banana-prompt-quicker)**

🍌Awesome Prompts; Nano Banana；Banana Pro; Gemini；AI Studio；Prompt Quickly[正在开发 Sidebar 高级功能，敬请期待]

`JavaScript` `banana` `gemini` `prompt`

⭐ 1.8k • 🔱 140 • 7d ago

---

**[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**

An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

`Python` `ai-skills` `antigravity` `claude` `claude-code` `command-line`

⭐ 1.3k • 🔱 315 • 10d ago

---

**[repplus/rep](https://github.com/repplus/rep)**

rep+ — Burp-style HTTP Repeater for Chrome DevTools with built‑in AI to explain requests and suggest attacks

`JavaScript` `css` `html` `javascript` `markdown`

⭐ 1.1k • 🔱 137 • 33m ago

---

**[Norsico/Video-Materials-AutoGEN-Workstation](https://github.com/Norsico/Video-Materials-AutoGEN-Workstation)**

一个集内容策划、AI文案自动生成、TTS 批量自动配音、(AI)图片素材合成、ASR自动提取语言字幕脚本、AI自由创作于一体的(短视频)生成工作站。方便管理每期的视频项目。

`Python`

⭐ 1.1k • 🔱 218 • 16d ago

---

**[Hugo-Dz/spritefusion-pixel-snapper](https://github.com/Hugo-Dz/spritefusion-pixel-snapper)**

A tool to snap pixels to a perfect grid. Designed to fix messy and inconsistent pixel art generated by AI.

`Rust` `game-development` `gamedev` `image-processing` `pixel-art`

⭐ 895 • 🔱 23 • 8d ago

---

**[Ryandonofrio3/osgrep](https://github.com/Ryandonofrio3/osgrep)**

Open Source Semantic Search for your AI Agent

`TypeScript` `colbert` `embeddings` `grep` `grep-search`

⭐ 867 • 🔱 49 • 21h ago

---

**[firecrawl/open-scouts](https://github.com/firecrawl/open-scouts)**

  AI-powered web monitoring platform. Create automated scouts that search the web and send email alerts when they find what you're looking for. 

`TypeScript` `ai-agents` `alerts` `automation` `email-notifications` `firecrawl`

⭐ 750 • 🔱 107 • 1d ago

---

**[TanShilongMario/PromptFill](https://github.com/TanShilongMario/PromptFill)**

一个专为 AI 绘画（Nano Banana 等）设计的“结构化提示词生成工具”。通过可视化的“填空”交互方式，帮助用户快速构建、管理和迭代复杂的 Prompt。

`JavaScript`

⭐ 744 • 🔱 114 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
