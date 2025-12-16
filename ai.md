---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2025-12-16T14:34:48.275220+00:00'
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

**Last Updated:** December 16, 2025 at 14:34 UTC  
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

🔗 [ZDNET](https://www.zdnet.com/article/linus-torvalds-ai-tool-maintaining-linux-code/) • 9h ago

---

**[If AI replaces workers, should it also pay taxes?](https://www.reddit.com/r/artificial/comments/1pn7tvx/if_ai_replaces_workers_should_it_also_pay_taxes/)**

The technological race among industry giants and the wave of layoffs they have announced has revived the debate about the advisability of taxing automation

🔗 [EL PAÍS English](https://english.elpais.com/technology/2025-11-30/if-ai-replaces-workers-should-it-also-pay-taxes.html) • 1d ago

---

**[ZLUDA for CUDA on non-NVIDIA GPUs enables AMD ROCm 7 support](https://www.reddit.com/r/artificial/comments/1po01ci/zluda_for_cuda_on_nonnvidia_gpus_enables_amd_rocm/)**

The ZLUDA open-source project that has been through several incarnations but ultimately about getting CUDA software up and running on non-NVIDIA GPUs now supports the AMD ROCm 7 series.

🔗 [phoronix.com](https://www.phoronix.com/news/ZLUDA-ROCm-7) • 2h ago

---

**[Nvidia Becomes a Major Model Maker With Nemotron 3](https://www.reddit.com/r/artificial/comments/1pn9big/nvidia_becomes_a_major_model_maker_with_nemotron_3/)**

The world’s top chipmaker wants open source AI to succeed—perhaps because closed models increasingly run on its rivals’ silicon.

🔗 [WIRED](https://www.wired.com/story/nvidia-becomes-major-model-maker-nemotron-3/) • 23h ago

---

**[Dismissing discussion of AGI as “science fiction” should be seen as a sign of total unseriousness. Time travel is science fiction. Martians are science fiction. “Even many 𝘴𝘬𝘦𝘱𝘵𝘪𝘤𝘢𝘭 experts think we may well build it in the next decade or two” is not science fiction.](https://www.reddit.com/r/artificial/comments/1po1393/dismissing_discussion_of_agi_as_science_fiction/)**

🔗 [helentoner.substack.com](https://helentoner.substack.com/p/long-timelines-to-advanced-ai-have) • 1h ago

---

**[Microsoft Scales Back AI Goals Because Almost Nobody Is Using Copilot](https://www.reddit.com/r/artificial/comments/1pmuboi/microsoft_scales_back_ai_goals_because_almost/)**

RIP Copilot.

🔗 [extremetech.com](https://www.extremetech.com/computing/microsoft-scales-back-ai-goals-because-almost-nobody-is-using-copilot) • 1d ago

---

**[Compact offline medical SLM with Native Knowledge Graph + RAG audit (benchmark + HF demo)](https://www.reddit.com/r/artificial/comments/1pnwh03/compact_offline_medical_slm_with_native_knowledge/)**

I’ve been experimenting with a slightly different approach to medical LMs and would really value feedback from people working on ML, health IT, or clinical education. Instead of chasing more parameters, I built a ~6 GB medical SLM that’s tightly coupled to a biomedical knowledge graph and a self‑contained RAG/audit layer. The goal is not to sound smarter than GPT‑4, but to be *safer, more structured, and auditable* for clinical decision support / education use cases. Core setup: - Base: BioGPT‑Large (~6 GB footprint) - Biomedical knowledge graph: 5k+ nodes, 25k+ edges across diseases, symptoms, treatments, risk factors, diagnostics, body parts, cellular structures - Graph‑aware embeddings + special tokens so the model “anchors” to graph concepts - Built‑in RAG/audit: entity + semantic search over the graph to validate each answer against the graph before accepting it I ran a small 5 case internal evaluation on multi sentence clinical questions (diagnosis + risk factors + tests + treatments + contraindications). Scoring dimensions: contextual accuracy, multi‑hop reasoning, entity structure, clarity, hallucination resistance. This model landed at 4.5/5 overall, including 5/5 on hallucination resistance. Baselines were typical medical SLMs (BioBERT/PubMedBERT/ClinicalBERT) and large general LLMs. Trade‑offs vs big LLMs: less fluent, more constrained; better at staying inside medically grounded entities/relations; easier to audit because every answer is tied back to explicit graph nodes. For anyone curious, there’s a HF Space demo here (model is private, Space is public responses can take 30–180s+ because of shared infra; locally it’s ~3–5s per query) on GPU, 7-10s on CPU: https://huggingface.co/spaces/cmtopbas/medical-slm-testing I’d really appreciate: - Critical feedback on the architecture (graph + audit layer) - Ideas for realistic, high‑impact use cases (e.g. med ed, trainee tools, clinician reference) where this kind of architecture would be useful - Pointers to similar work I should be aware of so I’m not reinventing the wheel Happy to share more detailed benchmarks/trace examples if there’s interest. Question 1: A 55-year-old male patient presents with persistent chest pain radiating to the left arm. He has a history of hypertension and Type 2 diabetes. ECG shows ST-segment elevation. The patient is allergic to aspirin. Question: Based on the patient’s condition, what treatments are recommended, which are contraindicated, and which risk factors are involved? Prompt → Categories: ['BodyPart', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 9 Answer → Categories: ['BodyPart', 'Disease', 'RiskFactor', 'Symptom', 'Treatment'] | Nodes: 10 ◇ Best effort (Missing: Riskfactor) Answer 1: Hypertension is common among patients who have CKD. It can be treated effectively if it is identified early and managed appropriately. Patients should avoid medications that may exacerbate their symptoms or cause adverse effects such as angiotensin converting enzyme (ACE) inhibitors. If an ACE inhibitor cannot be used because of intolerance, then other antihypertensive agents are available. In addition to blood pressure control, treatment for heart failure includes use of diuretics, beta blockers, aldosterone antagonists, and digoxin. Treatment options also include calcium channel blockers, alpha adrenergic receptor agonists, vasodilators, and endothelin receptor antagonists. Please consult a healthcare professional for personalized medical advice. Question 2: Female patient presents with fatigue, swelling in her ankles, has a history of hypertension and chronic kidney disease. Also experiences persistent cough when taking ACE inhibitors and her Echocardiogram shows reduced ejection fraction. What is the diagnosis and treatment based on her combined diagnosis Prompt → Categories: ['BodyPart', 'Disease', 'RiskFactor', 'Symptom', 'Treatment'] | Nodes: 8 Answer → Categories: ['BodyPart', 'DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Treatment'] | Nodes: 7 ✓ Graph-validated (Valid) Answer 2: The diagnosis is acute heart failure (HF) due to left ventricular systolic dysfunction. Treatment includes diuretics for congestion and vasodilators or inotropes for hypotension. Angiotensin-converting enzyme inhibitor therapy should be discontinued if there are signs of worsening renal function. Hypertension can worsen cardiac outcomes by increasing afterload on the heart. Chronic kidney disease may also contribute to poor prognosis through increased risk of cardiovascular events and death. Please consult a healthcare professional for personalized medical advice. Question 3: A 45-year-old male patient reports frequent urination, excessive thirst, and fatigue. He has a family history of type 2 diabetes and is overweight. Blood tests show elevated fasting glucose and HbA1c levels. Identify the disease, list risk factors, symptoms, recommended treatments, and contraindications Prompt → Categories: ['DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 5 Answer → Categories: ['BodyPart', 'DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Treatment'] | Nodes: 9 ✓ Graph-validated (Valid) Answer 3: Type 2 Diabetes Mellitus (T2DM) is an endocrine disorder that affects millions worldwide. It can be diagnosed by measuring blood sugar levels or glycated hemoglobin A1c. The American Diabetes Association recommends screening for T2DM in adults with any one of the following characteristics: age > 4 0 years; < 1 8 y / o Body Mass Index (BMI); African ancestry; Hispanic ethnicity; Asian descent; or having polycystic ovarian syndrome. Patients should also have at least two other features of the metabolic syndrome to increase their risk of developing T2DM. Treatment options are based on patients' comorbidities and goals for glycemic control. Lifestyle modifications such as diet and exercise are first line treatment but may not achieve optimal results if they fail. Medications including metformin, sulfonylureas, thiazolidinediones, dipeptidyl peptidase IV inhibitors, glucagon like peptide-1RAs. Please consult a healthcare professional for personalized medical advice. Question 4: A 30-year-old female patient reports persistent cough, fever, and shortness of breath. She recently returned from a trip abroad and has a mild history of asthma. Chest X-ray shows patchy infiltrates in the lower lobes. Identify the disease, list risk factors, symptoms, recommended treatments, and contraindications. Prompt → Categories: ['DiagnosticTest', 'Disease', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 5 Answer → Categories: ['DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 6 ✓ Graph-validated (Valid) Answer 4: The diagnosis is acute respiratory distress syndrome (ARDS) caused by pneumonia with secondary bacterial infection. ARDS can be fatal if not treated promptly. Risk factors for ARDS are discussed along with treatment options including antibiotics, corticosteroids, mechanical ventilation, vasopressors, and extracorporeal membrane oxygenation. Treatment should focus on preventing further complications such as nosocomial infections or ventilator associated events. Please consult a healthcare professional for personalized medical advice. Question 5: A 50-year-old male patient experiences abdominal pain, bloating, and intermittent diarrhea. He has a family history of celiac disease and reports gluten sensitivity. Blood tests show elevated anti-tTG antibodies. Identify the disease, list risk factors, symptoms, recommended treatments, and contraindications Prompt → Categories: ['DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 7 Answer → Categories: ['BodyPart', 'DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Treatment'] | Nodes: 6 ✓ Graph-validated (Valid) Answer 5: Celiac Disease is an autoimmune disorder that affects approximately 1% to 2% of people in North America. It can be diagnosed by serologic testing for IgA antitissue transglutaminase (anti-tTG) antibody levels or duodenal biopsy. The diagnosis should trigger a discussion about dietary restrictions with patients and their families. Patients must also understand the potential risks associated with untreated celiac disease, including increased susceptibility to cancer, cardiovascular diseases, type I diabetes mellitus, osteoporosis, infertility, neurologic disorders, and psychiatric conditions. Treatment options are limited but may involve lifelong adherence to a strict gluten free diet. This includes avoiding wheat products, rye, barley, oats, legumes, nuts, seeds, and other grains containing glutenins. Other treatment options include oral supplements such as zinc sulfate and magnesium oxide; however, these have not been. Please consult a healthcare professional for personalized medical advice. Please consult a healthcare professional for personalized medical advice.

6h ago

---

**[Not all CEOs favor Trump's executive order to block state AI laws](https://www.reddit.com/r/artificial/comments/1pnbrtt/not_all_ceos_favor_trumps_executive_order_to/)**

Also: All the news and watercooler chat from Fortune.

🔗 [Fortune](https://fortune.com/2025/12/15/trump-ai-state-laws-executive-order-ceo-reaction/) • 22h ago

---

**[One-Minute Daily AI News 12/15/2025](https://www.reddit.com/r/artificial/comments/1pnue0h/oneminute_daily_ai_news_12152025/)**

US government launches ‘Tech Force’ to hire AI talent.[1] Deep-learning model predicts how fruit flies form, cell by cell.[2] Nvidia bulks up open source offerings with an acquisition and new open AI models.[3] Podcast industry under siege as AI bots flood airways.[4] Sources: [1] https://www.cnn.com/2025/12/15/tech/government-tech-force-ai [2] https://news.mit.edu/2025/deep-learning-model-predicts-how-fruit-flies-form-1215 [3] https://techcrunch.com/2025/12/15/nvidia-bulks-up-open-source-offerings-with-an-acquisition-and-new-open-ai-models/ [4] https://www.yahoo.com/news/articles/podcast-industry-under-siege-ai-051031178.html

8h ago

---

**[It's been a big week for Agentic AI ; Here are 10 massive developments you might've missed:](https://www.reddit.com/r/artificial/comments/1pnf368/its_been_a_big_week_for_agentic_ai_here_are_10/)**

Stripe launches full Agentic Commerce Suite OpenAI + Anthropic found Agentic AI Foundation Google drops Deep Research + AlphaEvolve agent A collection of AI Agent Updates! 🧵 1. Stripe Launches Agentic Commerce Suite Single integration for businesses to sell via multiple AI agents. Handles product discovery, agentic checkout, payments, and fraud. Manage all agents from Stripe Dashboard. Works with existing commerce stack. AI-native commerce infrastructure now available. 2. OpenAI Co-Founds Agentic AI Foundation with Anthropic and Block Under Linux Foundation to support open, interoperable standards for agentic AI. Donating to establish standards enabling safe, reliable agents across tools and repositories. Industry leaders aligning on agent interoperability. 3. Google Opens Gemini Deep Research Agent to Developers Most advanced autonomous research capabilities now embeddable in applications for first time. Also open-sourcing DeepSearchQA benchmark for evaluating agents on complex search tasks. Google's agent infrastructure available to all developers. 4. Anthropic is Developing New Agent Mode for Claude Code-named "Yukon Gold" - tasks-based complex agent experience with toggle between classic chat and agent mode. Also testing pixel art avatar generation from uploaded photos. Claude may be getting a dedicated agent interface. 5. Google Cloud Unveils AlphaEvolve Coding Agent Gemini-powered agent for designing advanced algorithms. Uses LLMs to propose intelligent code modifications with feedback loop that evolves algorithms to be more efficient. Now in private preview. Haven’t tried, but seems promising. 6. Real Agent Usage Data: Harvard Analyzes Hundreds of Millions of Queries Perplexity study shows 55% personal use, 30% professional. Productivity/workflow dominates (36% of queries), followed by learning/research (21%). Users shift from simple to complex tasks over time. Real data on how people actually use agents. 7. Stitchbygoogle Launches Redesign Agent with Code Generation Screenshot apps, visually reimagine with Gemini Pro, then convert redesigns into working HTML. "Shipmas" week begins - new ship daily with big launch Wednesday. Screenshot → Redesign → Code → Deploy workflow now live. 8. Cursor Agents Can Now Debug Your Hardest Bugs Debug Mode instruments code, spins up server, captures logs, and streams runtime data to agent. Version 2.2 adds multi-agent judging (picks best solution) and Plan Mode improvements with diagrams. AI agents now debugging production code. 9. Code Drops Major Agent Experience Upgrade Agent sessions integrated into chat view. Isolated background agents via Git worktrees enable multiple agents without conflicts. Seamless delegation with automatic context transfer between local, background, and cloud agents. Multi-agent workflows now native in VS Code. 10. Microsoft Research Unveils Agent Lightning Decouples how agents work from training. Turns each agent step into reinforcement learning data. Developers can improve agent performance with almost zero code changes. RL for agents without code rewrites. That's a wrap on this week's Agentic news. Which update are you trying first? LMK if this was helpful | More weekly AI + Agentic content releasing ever week!

20h ago

---

---

## Google News: "ai"

**[Teachers are using software to see if students used AI. What happens when it's wrong?](https://www.npr.org/2025/12/16/nx-s1-5492397/ai-schools-teachers-students)**

School districts from Utah to Ohio to Alabama are spending thousands of dollars on these tools, despite research showing the technology is far from reliable.

NPR • 4h ago

---

**[How Tech’s Biggest Companies Are Offloading the Risks of the A.I. Boom](https://www.nytimes.com/2025/12/15/technology/ai-risks-debt.html)**

The New York Times • 22h ago

---

**[Racks of AI chips are too damn heavy](https://www.theverge.com/ai-artificial-intelligence/844966/heavy-ai-data-center-buildout)**

Too great a weight.

The Verge • 1h ago

---

**[Oracle's $248 Billion Rent is Another AI ‘Bombshell’](https://www.bloomberg.com/opinion/articles/2025-12-16/ai-bubble-oracle-delivers-next-bombshell-with-248-billion-rent)**

Bloomberg.com • 4h ago

---

**[Don’t throw the generative baby out with the AI bathwater](https://thehill.com/opinion/technology/5649753-ai-jagged-technological-frontier/)**

thehill.com • 34m ago

---

**[AI language models duped by poems](https://www.dw.com/en/ai-language-models-duped-by-poems/a-75180648)**

A new study has shown that prompts in the form of poems confuse AI models like ChatGPT, Gemini and Claude — to the point where sometimes, security mechanisms don't kick in. Are poets the new hackers?

dw.com • 17m ago

---

**[Thryv Experts Share Top AI Trends That Will Drive Small Business Success in 2026](https://finance.yahoo.com/news/thryv-experts-share-top-ai-140500501.html)**

DALLAS, December 16, 2025--With AI at the forefront of most current business innovations, small business experts from Thryv, Inc. (NASDAQ:THRY) share their predictions for those trends poised to transform how SMBs compete and succeed in 2026.

Yahoo Finance • 29m ago

---

**[Opinion | AI Is About to Empty Madison Avenue](https://www.wsj.com/opinion/ai-is-about-to-empty-madison-avenue-58ab2ea2?gaa_at=eafs&gaa_n=AWEtsqest0o7Kj7Y_u7-qTaiSPk74b0Hs-_YA5Zs7SZf27fUiIOaAX6Viwgo&gaa_ts=69417166&gaa_sig=h-T-9OPBMS7R3_RRtoOXczAakQFzPWAMBseyuCzC1Onq2Fyf7hoD48hQb9G0LoEwdVfB6DtZESFqqVnG5brz-w%3D%3D)**

The Wall Street Journal • 19h ago

---

**[Musicians are deeply concerned about AI. So why are the major labels embracing it?](https://www.theguardian.com/music/2025/dec/16/musicians-are-deeply-concerned-about-ai-so-why-are-the-major-labels-embracing-it)**

Companies such as Udio, Suno and Klay will let you use AI to make new music based on existing artists’ work. It could mean more royalties – but many are worried

The Guardian • 4h ago

---

**[Why 2026 could be the year of anti-AI marketing](https://www.cnn.com/2025/12/16/business/anti-ai-backlash-nightcap)**

It’s getting harder to escape AI slop. But a growing backlash could put a premium on “human-made” content.

CNN • 3h ago

---

---

## HackerNews: "ai"

**[8M users' AI conversations sold for profit by "privacy" extensions](https://news.ycombinator.com/item?id=46284266)**

⬆️ 622 • 💬 202 • 11h ago • [koi.ai](https://www.koi.ai/blog/urban-vpn-browser-extension-ai-conversations-data-collection)

---

**[If AI replaces workers, should it also pay taxes?](https://news.ycombinator.com/item?id=46268709)**

The technological race among industry giants and the wave of layoffs they have announced has revived the debate about the advisability of taxing automation

⬆️ 565 • 💬 932 • 1d ago • [EL PAÍS English](https://english.elpais.com/technology/2025-11-30/if-ai-replaces-workers-should-it-also-pay-taxes.html)

---

**[Ask HN: How can I get better at using AI for programming?](https://news.ycombinator.com/item?id=46255285)**

⬆️ 458 • 💬 460 • 2d ago

---

**[AI agents are starting to eat SaaS](https://news.ycombinator.com/item?id=46268452)**

Software ate the world. Agents are going to eat SaaS.

⬆️ 383 • 💬 373 • 1d ago • [Martin Alderson](https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/)

---

**[JetBlue flight averts mid-air collision with US Air Force jet](https://news.ycombinator.com/item?id=46281944)**

⬆️ 343 • 💬 255 • 15h ago • [reuters.com](https://www.reuters.com/world/americas/jetblue-flight-averts-mid-air-collision-with-us-air-force-jet-2025-12-15/)

---

**[Microsoft Copilot AI Comes to LG TVs, and Can't Be Deleted](https://news.ycombinator.com/item?id=46268844)**

Microsoft's Copilot AI chatbot is arguably one of the most controversial add-ons ever implemented in the Windows 11 operating system. However, the controversy doesn't stop at PC operating systems. It seems to extend to TVs as well. According to Reddit user u/defjam16, his LG TV webOS received an upd...

⬆️ 292 • 💬 300 • 1d ago • [TechPowerUp](https://www.techpowerup.com/344075/microsoft-copilot-ai-comes-to-lg-tvs-and-cant-be-deleted)

---

**[AI and the ironies of automation – Part 2](https://news.ycombinator.com/item?id=46262816)**

Some (well-known) consequences of AI automating work

⬆️ 254 • 💬 118 • 2d ago • [Uwe Friedrichsen](https://www.ufried.com/blog/ironies_of_ai_2/)

---

**[The Gorman Paradox: Where Are All the AI-Generated Apps?](https://news.ycombinator.com/item?id=46262545)**

In 1950, while discussing the recent wave of flying saucer reports over lunch with colleagues at Los Alamos National Laboratory in New Mexico, physicist Enrico Fermi asked a simple question. There …

⬆️ 158 • 💬 218 • 2d ago • [Codemanship's Blog](https://codemanship.wordpress.com/2025/12/14/the-gorman-paradox-where-are-all-the-ai-generated-apps/)

---

**[If a Meta AI model can read a brain-wide signal, why wouldn't the brain?](https://news.ycombinator.com/item?id=46260106)**

In 2023, Meta researchers were able to decode images in thoughts from the brain's magnetic fields. What if that's how the brain coordinates it's own global state?

⬆️ 138 • 💬 91 • 2d ago • [1393](https://1393.xyz/writing/if-a-meta-ai-model-can-read-a-brain-wide-signal-why-wouldnt-the-brain)

---

**[Willison on Merchant's "Copywriters reveal how AI has decimated their industry"](https://news.ycombinator.com/item?id=46261998)**

Brian Merchant has been collecting personal stories for his series AI Killed My Job - previously covering tech workers, translators, and artists - and this latest piece includes anecdotes from …

⬆️ 80 • 💬 89 • 2d ago • [Simon Willison’s Weblog](https://simonwillison.net/2025/Dec/14/copywriters-reveal-how-ai-has-decimated-their-industry/)

---

---

## YouTube Videos: "ai"

**[The $25 TRILLION AI Bubble Is BURSTING](https://www.youtube.com/watch?v=UQhM13yK6DQ)**

IBM's CEO said there is “no way” that the massive spending on AI and data centers will ever pay off. For the first time in this bubble ...

📺 Eurodollar University

👁️ 126K • 👍 4K • 💬 683 • ⏱️ 20:44 • 1d ago

---

**[OpenAI Just Caught an AI Thinking!](https://www.youtube.com/watch?v=YBRyR6FPgl4)**

OpenAI released circuit-sparsity, a research drop that exposes how a language model makes decisions internally. Instead of ...

📺 AI Revolution

👁️ 42K • 👍 2K • 💬 163 • ⏱️ 12:07 • 1d ago

---

**[The Most Powerful AI Shift Is Happening Without Anyone Noticing](https://www.youtube.com/watch?v=EjQpzEeiL3k)**

Hit the new HYPE Button! - It's designed to help smaller channels like me! CHAPTERS ⤵ 00:00 – Keep It Curious 04:03 – Disney ...

📺 Dylan Curious

👁️ 7K • 👍 450 • 💬 93 • ⏱️ 30:05 • 23h ago

---

**[China Just Crossed The Line With 6 Arm AI Robot (Works All At Once)](https://www.youtube.com/watch?v=ppoFxgp0PJI)**

Factories, streets, and physical reality just crossed a line. China unveiled a six-armed industrial robot built to outwork humans on ...

📺 AI Revolution

👁️ 21K • 👍 605 • 💬 100 • ⏱️ 11:23 • 14h ago

---

**[Lady Soldier Rescues Grandma and Builds Golden Carousel for Her 😭 #ai #save #army](https://www.youtube.com/watch?v=Rg0j9jUTTPM)**

Lady Soldier Rescues Grandma and Builds Golden Carousel for Her #ai #save #army.

📺 Anime world 

👁️ 208K • 👍 1K • 💬 1 • ⏱️ 0:22 • 2d ago

---

**[I bought 3 AI-generated products.. here’s what they REALLY look like. 🤡](https://www.youtube.com/watch?v=p6sslqc-BME)**

📺 Maggie McGaugh

👁️ 170K • 👍 9K • 💬 132 • ⏱️ 1:16 • 18h ago

---

**[China Rejects US-Made AI Chips, The White House Admits That Export Strategy May Be Failing](https://www.youtube.com/watch?v=WRwqRoIfAAU)**

The White House has raised fresh concerns after admitting that China is turning away U.S.-made AI chips, including Nvidia's H200 ...

📺 Mint

👁️ 61K • 👍 723 • 💬 320 • ⏱️ 4:14 • 1d ago

---

**[Slicing the solar system (AI ASMR)](https://www.youtube.com/watch?v=2SjWN7ZSx3Q)**

this video is AI Generated and contains no copyright sound NOTE: This video does not contain harmful content so please don't ...

📺 saturn2309altacc2

👁️ 365 • 👍 11 • ⏱️ 2:29 • 4h ago

---

**[Why YouTube Won&#39;t Stop Pushing AI Nonsense...](https://www.youtube.com/watch?v=We7FzVfIIcs)**

Hello guys and gals, it's me Mutahar again! This time we take a look at why sites like YouTube are taking AI so seriously.

📺 SomeOrdinaryGamers

👁️ 86K • 👍 5K • 💬 948 • ⏱️ 19:00 • 2d ago

---

**[Build anything with Google AI Studio, here&#39;s how...](https://www.youtube.com/watch?v=IVWTX1CyOEw)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses https://juliangoldieai.com/07L1kg Get a ...

📺 Julian Goldie SEO

👁️ 6K • 👍 114 • 💬 10 • ⏱️ 36:04 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)**

*Tongyi-MAI*

Z-Image-Turbo is a highly efficient text-to-image diffusion transformer model with 6B parameters, achieving sub-second inference on H800 GPUs with 8 NFEs. It excels at photorealistic generation, bilingual text rendering (English/Chinese), and instruction adherence, fitting within 16GB VRAM.

`text-to-image`

⬇️ 296,552 • ❤️ 2,797 • 7d ago

---

**[Devstral-Small-2-24B-Instruct-2512](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)**

*Mistral AI_*

Devstral Small 2 24B Instruct 2512 is a lightweight, agentic LLM for software engineering tasks, excelling at codebase exploration and multi-file editing with a 256k context window and FP8 precision. It is ideal for AI code assistants and agentic coding use cases, capable of running locally on consumer hardware.

`24.0B`

⬇️ 28,106 • ❤️ 377 • 1d ago

---

**[VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)**

*Microsoft*

VibeVoice-Realtime-0.5B is a lightweight, real-time text-to-speech model with ~300ms latency, supporting streaming input for robust long-form generation, ideal for live narration and LLM integration.

`text-to-speech` `1.0B`

⬇️ 158,614 • ❤️ 878 • 3d ago

---

**[AutoGLM-Phone-9B](https://huggingface.co/zai-org/AutoGLM-Phone-9B)**

*Z.ai*

AutoGLM-Phone-9B is a vision-language model for mobile intelligent assistance, enabling automated smartphone operations via ADB by understanding UI elements and executing natural language commands for task completion.

`image-text-to-text` `934,400`

⬇️ 51,591 • ❤️ 321 • 7d ago

---

**[GLM-4.6V-Flash](https://huggingface.co/zai-org/GLM-4.6V-Flash)**

*Z.ai*

GLM-4.6V-Flash is a lightweight multimodal model for image-text-to-text tasks, featuring native function calling for vision-driven tool use and interleaved content generation. It excels at multimodal document understanding, frontend replication, and low-latency applications.

`image-text-to-text` `10.3B`

⬇️ 102,395 • ❤️ 459 • 6d ago

---

**[GLM-ASR-Nano-2512](https://huggingface.co/zai-org/GLM-ASR-Nano-2512)**

*Z.ai*

GLM-ASR-Nano-2512 is a 1.5B parameter speech recognition model excelling in low-volume and dialectal (Cantonese) speech, outperforming Whisper V3 on benchmarks with a 4.10 average error rate. It's ideal for noisy environments and diverse linguistic use cases.

`automatic-speech-recognition` `2.3B`

⬇️ 74,813 • ❤️ 235 • 4d ago

---

**[Devstral-2-123B-Instruct-2512](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512)**

*Mistral AI_*

Devstral 2 123B Instruct is an FP8 agentic LLM optimized for software engineering tasks, excelling in codebase exploration, multi-file editing, and powering SWE agents with a 256k context window.

`125.0B`

⬇️ 6,543 • ❤️ 221 • 1d ago

---

**[GLM-TTS](https://huggingface.co/zai-org/GLM-TTS)**

*Z.ai*

GLM-TTS is a controllable, zero-shot text-to-speech system that uses a two-stage LLM and Flow Matching architecture, enhanced by multi-reward reinforcement learning for expressive emotion control and high-quality synthesis. It supports voice cloning from short prompts and streaming inference for interactive applications.

`text-to-speech`

⬇️ 0 • ❤️ 216 • 5d ago

---

**[NVIDIA-Nemotron-3-Nano-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 is a 30B parameter LLM with a hybrid MoE/Mamba architecture, excelling at reasoning tasks by generating explicit reasoning traces. It supports multiple languages and is suitable for commercial use, offering high accuracy in complex problem-solving.

`text-generation` `31.6B`

⬇️ 10,487 • ❤️ 215 • 14h ago

---

**[AutoGLM-Phone-9B-Multilingual](https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual)**

*Z.ai*

AutoGLM-Phone-9B-Multilingual is a vision-language model for mobile intelligent assistance, capable of understanding smartphone UIs via multimodal perception and executing tasks through ADB. It enables natural language control for automated operations on Android devices.

`image-text-to-text` `934,400`

⬇️ 7,731 • ❤️ 183 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 5 • 💬 2 • ⭐ 11,986 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based framework for real-time portrait animation that enhances speed and efficiency through multi-stage training, hybrid implicit signals, appearance distillation, and autoregressive micro-chunk streaming.

▲ 20 • 💬 2 • ⭐ 341 • 4d ago

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

▲ 25 • 💬 2 • ⭐ 12,568 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2512.07921) • [💻 code](https://github.com/HKUDS/DeepCode)

---

**[FunAudioLLM: Voice Understanding and Generation Foundation Models for
  Natural Interaction Between Humans and LLMs](https://huggingface.co/papers/2407.04051)**

*Tongyi SpeechTeam*

FunAudioLLM enhances voice interactions by integrating SenseVoice for multilingual speech recognition, emotion detection, and audio event detection with CosyVoice for natural speech generation across languages, timbres, and styles.

▲ 39 • 💬 1 • ⭐ 17,834 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.04051) • [💻 code](https://github.com/funaudiollm/cosyvoice)

---

**[Decoupled DMD: CFG Augmentation as the Spear, Distribution Matching as the Shield](https://huggingface.co/papers/2511.22677)**

*Dongyang Liu, Peng Gao, David Liu et al. (11 authors)*

🏢 Tongyi-MAI

The study reveals that in text-to-image generation, CFG Augmentation is the primary driver of few-step distillation in Distribution Matching Distillation (DMD), while the distribution matching term acts as a regularizer.

▲ 27 • 💬 2 • ⭐ 7,099 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2511.22677) • [💻 code](https://github.com/Tongyi-MAI/Z-Image/tree/main) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer](https://huggingface.co/papers/2511.22699)**

*Z-Image Team, Huanqia Cai, Sihan Cao et al. (21 authors)*

🏢 Tongyi-MAI

Z-Image, a 6B-parameter Scalable Single-Stream Diffusion Transformer (S3-DiT) model, achieves high-performance image generation with reduced computational cost, offering sub-second inference and compatibility with consumer hardware.

▲ 199 • 💬 4 • ⭐ 7,089 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2511.22699) • [💻 code](https://github.com/Tongyi-MAI/Z-Image) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 25 • 💬 1 • ⭐ 65,529 • 27mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 117 • 💬 18 • ⭐ 46,888 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Fara-7B: An Efficient Agentic Model for Computer Use](https://huggingface.co/papers/2511.19663)**

*Ahmed Awadallah, Yash Lara, Raghav Magazine et al. (12 authors)*

🏢 Microsoft

FaraGen creates synthetic datasets for computer use agents, enabling the training of efficient and high-performing models like Fara-7B on diverse web tasks, outperforming larger models on benchmarks.

▲ 12 • 💬 2 • ⭐ 3,187 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2511.19663) • [💻 code](https://github.com/microsoft/fara) • [🔗 project](https://aka.ms/msaif/fara)

---

---

## GitHub Repositories: "ai"

**[zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)**

An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone

`Python` `agent` `phone-use-agent`

⭐ 16.2k • 🔱 2.5k • 4h ago

---

**[Anionex/banana-slides](https://github.com/Anionex/banana-slides)**

一个基于nano banana pro🍌的原生AI PPT生成应用，迈向真正的＂Vibe PPT＂; 支持上传任意模板图片；上传任意素材&智能解析；一句话/大纲/页面描述自动生成PPT；口头修改指定区域、一键导出 - An AI-native PPT generator based on nano banana pro🍌

`Python` `ai-ppt-maker` `ai-slide-builder` `ai-slides` `llm` `nanobananapro`

⭐ 3.8k • 🔱 409 • 39m ago

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

⭐ 1.1k • 🔱 137 • 1h ago

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

⭐ 867 • 🔱 49 • 1d ago

---

**[firecrawl/open-scouts](https://github.com/firecrawl/open-scouts)**

  AI-powered web monitoring platform. Create automated scouts that search the web and send email alerts when they find what you're looking for. 

`TypeScript` `ai-agents` `alerts` `automation` `email-notifications` `firecrawl`

⭐ 752 • 🔱 110 • 1d ago

---

**[TanShilongMario/PromptFill](https://github.com/TanShilongMario/PromptFill)**

一个专为 AI 绘画（Nano Banana 等）设计的“结构化提示词生成工具”。通过可视化的“填空”交互方式，帮助用户快速构建、管理和迭代复杂的 Prompt。

`JavaScript`

⭐ 751 • 🔱 115 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*
