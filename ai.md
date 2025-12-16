---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2025-12-16T15:59:33.986203+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** December 16, 2025 at 15:59 UTC  
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

**[Anthropic Exec Forces AI Chatbot on Gay Discord Community, Members Flee](https://www.reddit.com/r/artificial/comments/1po4nzu/anthropic_exec_forces_ai_chatbot_on_gay_discord/)**

“We’re bringing a new kind of sentience into existence,” Anthropic's Jason Clinton said after launching the bot.

🔗 [404 Media](https://www.404media.co/anthropic-exec-forces-ai-chatbot-on-gay-discord-community-members-flee/) • 36m ago

---

**[Linus Torvalds is 'a huge believer' in using AI to maintain code - just don't call it a revolution](https://www.reddit.com/r/artificial/comments/1pntfs5/linus_torvalds_is_a_huge_believer_in_using_ai_to/)**

Torvalds is sick of all the AI hype, but says AI is finally maturing to the point where it will be useful for Linux developers and maintainers.

🔗 [ZDNET](https://www.zdnet.com/article/linus-torvalds-ai-tool-maintaining-linux-code/) • 10h ago

---

**[Mozilla names new CEO, Firefox to evolve into a "modern AI browser"](https://www.reddit.com/r/artificial/comments/1po4ttq/mozilla_names_new_ceo_firefox_to_evolve_into_a/)**

Mozilla Corporation has named its new CEO in replacing interim CEO Laura Chambers.

🔗 [phoronix.com](https://www.phoronix.com/news/Mozilla-New-CEO-AI) • 30m ago

---

**[We used Qwen3-Coder to build a 2D Mario-style game in seconds (demo + setup guide)](https://www.reddit.com/r/artificial/comments/1po40li/we_used_qwen3coder_to_build_a_2d_mariostyle_game/)**

We recently tested Qwen3-Coder (480B), an open-weight model from Alibaba built for code generation and agent-style tasks. We connected it to Cursor IDE using a standard OpenAI-compatible API. Prompt: “Create a 2D game like Super Mario.” Here’s what the model did: Asked if any asset files were available Installed pygame and created a requirements.txt file Generated a clean project layout: main.py, README.md, and placeholder folders Implemented player movement, coins, enemies, collisions, and a win screen We ran the code as-is. The game worked without edits. Why this stood out: The entire project was created from a single prompt It planned the steps: setup → logic → output → instructions It cost about $2 per million tokens to run, which is very reasonable for this scale The experience felt surprisingly close to GPT-4’s agent mode - but powered entirely by open-source models on a flexible, non-proprietary backend We documented the full process with screenshots and setup steps here: Qwen3-Coder is Actually Amazing: We Confirmed this with NetMind API at Cursor Agent Mode. Would be curious to hear how others are using Qwen3 or similar models for real tasks. Any tips or edge cases you’ve hit?

1h ago

---

**[If AI replaces workers, should it also pay taxes?](https://www.reddit.com/r/artificial/comments/1pn7tvx/if_ai_replaces_workers_should_it_also_pay_taxes/)**

The technological race among industry giants and the wave of layoffs they have announced has revived the debate about the advisability of taxing automation

🔗 [EL PAÍS English](https://english.elpais.com/technology/2025-11-30/if-ai-replaces-workers-should-it-also-pay-taxes.html) • 1d ago

---

**[ZLUDA for CUDA on non-NVIDIA GPUs enables AMD ROCm 7 support](https://www.reddit.com/r/artificial/comments/1po01ci/zluda_for_cuda_on_nonnvidia_gpus_enables_amd_rocm/)**

The ZLUDA open-source project that has been through several incarnations but ultimately about getting CUDA software up and running on non-NVIDIA GPUs now supports the AMD ROCm 7 series.

🔗 [phoronix.com](https://www.phoronix.com/news/ZLUDA-ROCm-7) • 4h ago

---

**[Red Hat acquires another AI company](https://www.reddit.com/r/artificial/comments/1po5dd8/red_hat_acquires_another_ai_company/)**

Last year Red Hat acquired Neural Magic as part of their AI acquisitions and to bolster the open-source AI ecosystem

🔗 [phoronix.com](https://www.phoronix.com/news/Red-Hat-Another-AI-Company) • 8m ago

---

**[Nvidia Becomes a Major Model Maker With Nemotron 3](https://www.reddit.com/r/artificial/comments/1pn9big/nvidia_becomes_a_major_model_maker_with_nemotron_3/)**

The world’s top chipmaker wants open source AI to succeed—perhaps because closed models increasingly run on its rivals’ silicon.

🔗 [WIRED](https://www.wired.com/story/nvidia-becomes-major-model-maker-nemotron-3/) • 1d ago

---

**[Microsoft Scales Back AI Goals Because Almost Nobody Is Using Copilot](https://www.reddit.com/r/artificial/comments/1pmuboi/microsoft_scales_back_ai_goals_because_almost/)**

RIP Copilot.

🔗 [extremetech.com](https://www.extremetech.com/computing/microsoft-scales-back-ai-goals-because-almost-nobody-is-using-copilot) • 1d ago

---

**[Compact offline medical SLM with Native Knowledge Graph + RAG audit (benchmark + HF demo)](https://www.reddit.com/r/artificial/comments/1pnwh03/compact_offline_medical_slm_with_native_knowledge/)**

I’ve been experimenting with a slightly different approach to medical LMs and would really value feedback from people working on ML, health IT, or clinical education. Instead of chasing more parameters, I built a ~6 GB medical SLM that’s tightly coupled to a biomedical knowledge graph and a self‑contained RAG/audit layer. The goal is not to sound smarter than GPT‑4, but to be *safer, more structured, and auditable* for clinical decision support / education use cases. Core setup: - Base: BioGPT‑Large (~6 GB footprint) - Biomedical knowledge graph: 5k+ nodes, 25k+ edges across diseases, symptoms, treatments, risk factors, diagnostics, body parts, cellular structures - Graph‑aware embeddings + special tokens so the model “anchors” to graph concepts - Built‑in RAG/audit: entity + semantic search over the graph to validate each answer against the graph before accepting it I ran a small 5 case internal evaluation on multi sentence clinical questions (diagnosis + risk factors + tests + treatments + contraindications). Scoring dimensions: contextual accuracy, multi‑hop reasoning, entity structure, clarity, hallucination resistance. This model landed at 4.5/5 overall, including 5/5 on hallucination resistance. Baselines were typical medical SLMs (BioBERT/PubMedBERT/ClinicalBERT) and large general LLMs. Trade‑offs vs big LLMs: less fluent, more constrained; better at staying inside medically grounded entities/relations; easier to audit because every answer is tied back to explicit graph nodes. For anyone curious, there’s a HF Space demo here (model is private, Space is public responses can take 30–180s+ because of shared infra; locally it’s ~3–5s per query) on GPU, 7-10s on CPU: https://huggingface.co/spaces/cmtopbas/medical-slm-testing I’d really appreciate: - Critical feedback on the architecture (graph + audit layer) - Ideas for realistic, high‑impact use cases (e.g. med ed, trainee tools, clinician reference) where this kind of architecture would be useful - Pointers to similar work I should be aware of so I’m not reinventing the wheel Happy to share more detailed benchmarks/trace examples if there’s interest. Question 1: A 55-year-old male patient presents with persistent chest pain radiating to the left arm. He has a history of hypertension and Type 2 diabetes. ECG shows ST-segment elevation. The patient is allergic to aspirin. Question: Based on the patient’s condition, what treatments are recommended, which are contraindicated, and which risk factors are involved? Prompt → Categories: ['BodyPart', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 9 Answer → Categories: ['BodyPart', 'Disease', 'RiskFactor', 'Symptom', 'Treatment'] | Nodes: 10 ◇ Best effort (Missing: Riskfactor) Answer 1: Hypertension is common among patients who have CKD. It can be treated effectively if it is identified early and managed appropriately. Patients should avoid medications that may exacerbate their symptoms or cause adverse effects such as angiotensin converting enzyme (ACE) inhibitors. If an ACE inhibitor cannot be used because of intolerance, then other antihypertensive agents are available. In addition to blood pressure control, treatment for heart failure includes use of diuretics, beta blockers, aldosterone antagonists, and digoxin. Treatment options also include calcium channel blockers, alpha adrenergic receptor agonists, vasodilators, and endothelin receptor antagonists. Please consult a healthcare professional for personalized medical advice. Question 2: Female patient presents with fatigue, swelling in her ankles, has a history of hypertension and chronic kidney disease. Also experiences persistent cough when taking ACE inhibitors and her Echocardiogram shows reduced ejection fraction. What is the diagnosis and treatment based on her combined diagnosis Prompt → Categories: ['BodyPart', 'Disease', 'RiskFactor', 'Symptom', 'Treatment'] | Nodes: 8 Answer → Categories: ['BodyPart', 'DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Treatment'] | Nodes: 7 ✓ Graph-validated (Valid) Answer 2: The diagnosis is acute heart failure (HF) due to left ventricular systolic dysfunction. Treatment includes diuretics for congestion and vasodilators or inotropes for hypotension. Angiotensin-converting enzyme inhibitor therapy should be discontinued if there are signs of worsening renal function. Hypertension can worsen cardiac outcomes by increasing afterload on the heart. Chronic kidney disease may also contribute to poor prognosis through increased risk of cardiovascular events and death. Please consult a healthcare professional for personalized medical advice. Question 3: A 45-year-old male patient reports frequent urination, excessive thirst, and fatigue. He has a family history of type 2 diabetes and is overweight. Blood tests show elevated fasting glucose and HbA1c levels. Identify the disease, list risk factors, symptoms, recommended treatments, and contraindications Prompt → Categories: ['DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 5 Answer → Categories: ['BodyPart', 'DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Treatment'] | Nodes: 9 ✓ Graph-validated (Valid) Answer 3: Type 2 Diabetes Mellitus (T2DM) is an endocrine disorder that affects millions worldwide. It can be diagnosed by measuring blood sugar levels or glycated hemoglobin A1c. The American Diabetes Association recommends screening for T2DM in adults with any one of the following characteristics: age > 4 0 years; < 1 8 y / o Body Mass Index (BMI); African ancestry; Hispanic ethnicity; Asian descent; or having polycystic ovarian syndrome. Patients should also have at least two other features of the metabolic syndrome to increase their risk of developing T2DM. Treatment options are based on patients' comorbidities and goals for glycemic control. Lifestyle modifications such as diet and exercise are first line treatment but may not achieve optimal results if they fail. Medications including metformin, sulfonylureas, thiazolidinediones, dipeptidyl peptidase IV inhibitors, glucagon like peptide-1RAs. Please consult a healthcare professional for personalized medical advice. Question 4: A 30-year-old female patient reports persistent cough, fever, and shortness of breath. She recently returned from a trip abroad and has a mild history of asthma. Chest X-ray shows patchy infiltrates in the lower lobes. Identify the disease, list risk factors, symptoms, recommended treatments, and contraindications. Prompt → Categories: ['DiagnosticTest', 'Disease', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 5 Answer → Categories: ['DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 6 ✓ Graph-validated (Valid) Answer 4: The diagnosis is acute respiratory distress syndrome (ARDS) caused by pneumonia with secondary bacterial infection. ARDS can be fatal if not treated promptly. Risk factors for ARDS are discussed along with treatment options including antibiotics, corticosteroids, mechanical ventilation, vasopressors, and extracorporeal membrane oxygenation. Treatment should focus on preventing further complications such as nosocomial infections or ventilator associated events. Please consult a healthcare professional for personalized medical advice. Question 5: A 50-year-old male patient experiences abdominal pain, bloating, and intermittent diarrhea. He has a family history of celiac disease and reports gluten sensitivity. Blood tests show elevated anti-tTG antibodies. Identify the disease, list risk factors, symptoms, recommended treatments, and contraindications Prompt → Categories: ['DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Symptom', 'Treatment'] | Nodes: 7 Answer → Categories: ['BodyPart', 'DiagnosticTest', 'Disease', 'RiskFactor', 'Riskfactor', 'Treatment'] | Nodes: 6 ✓ Graph-validated (Valid) Answer 5: Celiac Disease is an autoimmune disorder that affects approximately 1% to 2% of people in North America. It can be diagnosed by serologic testing for IgA antitissue transglutaminase (anti-tTG) antibody levels or duodenal biopsy. The diagnosis should trigger a discussion about dietary restrictions with patients and their families. Patients must also understand the potential risks associated with untreated celiac disease, including increased susceptibility to cancer, cardiovascular diseases, type I diabetes mellitus, osteoporosis, infertility, neurologic disorders, and psychiatric conditions. Treatment options are limited but may involve lifelong adherence to a strict gluten free diet. This includes avoiding wheat products, rye, barley, oats, legumes, nuts, seeds, and other grains containing glutenins. Other treatment options include oral supplements such as zinc sulfate and magnesium oxide; however, these have not been. Please consult a healthcare professional for personalized medical advice. Please consult a healthcare professional for personalized medical advice.

7h ago

---

---

## Google News: "ai"

**[Teachers are using software to see if students used AI. What happens when it's wrong?](https://www.npr.org/2025/12/16/nx-s1-5492397/ai-schools-teachers-students)**

School districts from Utah to Ohio to Alabama are spending thousands of dollars on these tools, despite research showing the technology is far from reliable.

NPR • 5h ago

---

**[How Tech’s Biggest Companies Are Offloading the Risks of the A.I. Boom](https://www.nytimes.com/2025/12/15/technology/ai-risks-debt.html)**

The New York Times • 18h ago

---

**[Publishers and brands grapple with AI errors](https://www.axios.com/2025/12/16/ai-media-mistakes-backlash)**

Axios • 28m ago

---

**[AI boom seen lifting chipmaking equipment sales 9% to $126 billion in 2026](https://finance.yahoo.com/news/ai-boom-seen-lifting-chipmaking-152903092.html)**

AMSTERDAM, Dec 16 (Reuters) - Sales of equipment used to make computer chip wafers ​will rise about 9% to $126 billion ‌in 2026 and a further 7.3% to $135 billion in ‌2027, as chipmakers expand capacity for logic and memory chips used in artificial intelligence, industry group SEMI forecast on Tuesday.

Yahoo Finance • 30m ago

---

**[Perplexity AI Revamps iPad App to Deepen Focus on Research Tools](https://www.bloomberg.com/news/articles/2025-12-16/perplexity-ai-revamps-ipad-app-to-deepen-focus-on-research-tools)**

Bloomberg.com • 2m ago

---

**[Opinion | AI Is About to Empty Madison Avenue](https://www.wsj.com/opinion/ai-is-about-to-empty-madison-avenue-58ab2ea2?gaa_at=eafs&gaa_n=AWEtsqdemQ1BWQ5kHwk23GIndxB_xPZ0gp91a6L0psdDZ7jEHBdwUw31z7SS&gaa_ts=69418544&gaa_sig=tIjpe0-iusiLMt6TxJBeGwVJV6Tyvr6cPnuHY-WbW4L-xagvZCtT8TBJhtVkR9OuCzPxrh8_bo4H40tlxFiySA%3D%3D)**

The Wall Street Journal • 20h ago

---

**[Why 2026 could be the year of anti-AI marketing](https://www.cnn.com/2025/12/16/business/anti-ai-backlash-nightcap)**

It’s getting harder to escape AI slop. But a growing backlash could put a premium on “human-made” content.

CNN • 4h ago

---

**[Review | We asked five AIs to give The Rock hair, draw fingers and delete an ex. Only one was a clear winner.](https://www.washingtonpost.com/technology/interactive/2025/best-ai-image-generator/)**

The Washington Post • 1h ago

---

**[Trump admin to hire 1,000 specialists for 'Tech Force' to build AI, finance projects](https://www.cnbc.com/2025/12/15/trump-ai-tech-force-amazon-apple.html)**

A slew of tech giants, including Amazon Web Services, Apple, Google Public Sector, Dell Technologies, Microsoft, Nvidia and OpenAI, are listed as partners.

CNBC • 23h ago

---

**[Business leaders agree AI is the future. They just wish it worked right now.](https://www.reuters.com/business/business-leaders-agree-ai-is-future-they-just-wish-it-worked-right-now-2025-12-16/)**

Reuters • 3h ago

---

---

## HackerNews: "ai"

**[8M users' AI conversations sold for profit by "privacy" extensions](https://news.ycombinator.com/item?id=46284266)**

⬆️ 677 • 💬 221 • 12h ago • [koi.ai](https://www.koi.ai/blog/urban-vpn-browser-extension-ai-conversations-data-collection)

---

**[If AI replaces workers, should it also pay taxes?](https://news.ycombinator.com/item?id=46268709)**

The technological race among industry giants and the wave of layoffs they have announced has revived the debate about the advisability of taxing automation

⬆️ 567 • 💬 934 • 1d ago • [EL PAÍS English](https://english.elpais.com/technology/2025-11-30/if-ai-replaces-workers-should-it-also-pay-taxes.html)

---

**[AI agents are starting to eat SaaS](https://news.ycombinator.com/item?id=46268452)**

Software ate the world. Agents are going to eat SaaS.

⬆️ 385 • 💬 374 • 1d ago • [Martin Alderson](https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/)

---

**[JetBlue flight averts mid-air collision with US Air Force jet](https://news.ycombinator.com/item?id=46281944)**

⬆️ 348 • 💬 279 • 17h ago • [reuters.com](https://www.reuters.com/world/americas/jetblue-flight-averts-mid-air-collision-with-us-air-force-jet-2025-12-15/)

---

**[Microsoft Copilot AI Comes to LG TVs, and Can't Be Deleted](https://news.ycombinator.com/item?id=46268844)**

Microsoft's Copilot AI chatbot is arguably one of the most controversial add-ons ever implemented in the Windows 11 operating system. However, the controversy doesn't stop at PC operating systems. It seems to extend to TVs as well. According to Reddit user u/defjam16, his LG TV webOS received an upd...

⬆️ 293 • 💬 300 • 1d ago • [TechPowerUp](https://www.techpowerup.com/344075/microsoft-copilot-ai-comes-to-lg-tvs-and-cant-be-deleted)

---

**[AI and the ironies of automation – Part 2](https://news.ycombinator.com/item?id=46262816)**

Some (well-known) consequences of AI automating work

⬆️ 255 • 💬 118 • 2d ago • [Uwe Friedrichsen](https://www.ufried.com/blog/ironies_of_ai_2/)

---

**[The Gorman Paradox: Where Are All the AI-Generated Apps?](https://news.ycombinator.com/item?id=46262545)**

In 1950, while discussing the recent wave of flying saucer reports over lunch with colleagues at Los Alamos National Laboratory in New Mexico, physicist Enrico Fermi asked a simple question. There …

⬆️ 158 • 💬 219 • 2d ago • [Codemanship's Blog](https://codemanship.wordpress.com/2025/12/14/the-gorman-paradox-where-are-all-the-ai-generated-apps/)

---

**[If a Meta AI model can read a brain-wide signal, why wouldn't the brain?](https://news.ycombinator.com/item?id=46260106)**

In 2023, Meta researchers were able to decode images in thoughts from the brain's magnetic fields. What if that's how the brain coordinates it's own global state?

⬆️ 138 • 💬 91 • 2d ago • [1393](https://1393.xyz/writing/if-a-meta-ai-model-can-read-a-brain-wide-signal-why-wouldnt-the-brain)

---

**[Willison on Merchant's "Copywriters reveal how AI has decimated their industry"](https://news.ycombinator.com/item?id=46261998)**

Brian Merchant has been collecting personal stories for his series AI Killed My Job - previously covering tech workers, translators, and artists - and this latest piece includes anecdotes from …

⬆️ 80 • 💬 89 • 2d ago • [Simon Willison’s Weblog](https://simonwillison.net/2025/Dec/14/copywriters-reveal-how-ai-has-decimated-their-industry/)

---

**[Show HN: 100 Million splats, a whole town, rendered in M2 MacBook Air](https://news.ycombinator.com/item?id=46277477)**

⬆️ 78 • 💬 39 • 22h ago • [X (formerly Twitter)](https://twitter.com/AKurian001/status/1986979144014701026)

---

---

## YouTube Videos: "ai"

**[900 Days Left – AI Is Coming for Capitalism](https://www.youtube.com/watch?v=A8mj1Ngz2JI)**

Welcome to Impact Theory with Tom Bilyeu. In today's Deep Dive episode, Tom Bilyeu tackles one of the most urgent questions of ...

📺 Tom Bilyeu

👁️ 55K • 👍 2K • 💬 673 • ⏱️ 23:28 • 1d ago

---

**[The Most Powerful AI Shift Is Happening Without Anyone Noticing](https://www.youtube.com/watch?v=EjQpzEeiL3k)**

Hit the new HYPE Button! - It's designed to help smaller channels like me! CHAPTERS ⤵ 00:00 – Keep It Curious 04:03 – Disney ...

📺 Dylan Curious

👁️ 7K • 👍 458 • 💬 86 • ⏱️ 30:05 • 1d ago

---

**[OpenAI Just Caught an AI Thinking!](https://www.youtube.com/watch?v=YBRyR6FPgl4)**

OpenAI released circuit-sparsity, a research drop that exposes how a language model makes decisions internally. Instead of ...

📺 AI Revolution

👁️ 42K • 👍 2K • 💬 166 • ⏱️ 12:07 • 1d ago

---

**[China Just Crossed The Line With 6 Arm AI Robot (Works All At Once)](https://www.youtube.com/watch?v=ppoFxgp0PJI)**

Factories, streets, and physical reality just crossed a line. China unveiled a six-armed industrial robot built to outwork humans on ...

📺 AI Revolution

👁️ 23K • 👍 642 • 💬 103 • ⏱️ 11:23 • 15h ago

---

**[The $25 TRILLION AI Bubble Is BURSTING](https://www.youtube.com/watch?v=UQhM13yK6DQ)**

IBM's CEO said there is “no way” that the massive spending on AI and data centers will ever pay off. For the first time in this bubble ...

📺 Eurodollar University

👁️ 135K • 👍 5K • 💬 785 • ⏱️ 20:44 • 1d ago

---

**[AI STOCKS GO DEEP RED, PAYPAL BANK, UNEMPLOYMENT/PAYROLLS | MARKET OPEN](https://www.youtube.com/watch?v=-TOHi_Y2UpQ)**

Welcome to the Lunch Time stock market hour with your host Couch Investor aka Neil. 15% OFF Fiscal AI: https://fiscal.ai/couch ...

📺 Couch Investor

👁️ 2K • 👍 126 • 4h ago

---

**[#samsung Unveils Its AI Humanoid Robot ‘Leno X’. #robotics #robot  #humanoidrobot #ai](https://www.youtube.com/watch?v=g4hvzxnSLRc)**

📺 AI . Robot

👁️ 250K • 👍 3K • 💬 24 • ⏱️ 0:21 • 2d ago

---

**[Lady Soldier Rescues Grandma and Builds Golden Carousel for Her 😭 #ai #save #army](https://www.youtube.com/watch?v=Rg0j9jUTTPM)**

Lady Soldier Rescues Grandma and Builds Golden Carousel for Her #ai #save #army.

📺 Anime world 

👁️ 208K • 👍 1K • 💬 1 • ⏱️ 0:22 • 2d ago

---

**[Which Dream Bed Would You Choose? 🛏️✨ Ultimate Oddly Satisfying AI ASMR](https://www.youtube.com/watch?v=4_WX7Vr4Hcg)**

Join Impossible AIs and unlock exclusive perks! ✨ @ImpossibleAIs-c9z Drift into pure comfort—AI-crafted relaxing beds designed ...

📺 Impossible AIs

👁️ 52K • 👍 296 • 💬 15 • ⏱️ 8:43 • 2d ago

---

**[China Rejects US-Made AI Chips, The White House Admits That Export Strategy May Be Failing](https://www.youtube.com/watch?v=WRwqRoIfAAU)**

The White House has raised fresh concerns after admitting that China is turning away U.S.-made AI chips, including Nvidia's H200 ...

📺 Mint

👁️ 67K • 👍 789 • 💬 338 • ⏱️ 4:14 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)**

*Tongyi-MAI*

Z-Image-Turbo is a highly efficient text-to-image diffusion transformer model with 6B parameters, achieving sub-second inference on H800 GPUs with 8 NFEs. It excels at photorealistic generation, bilingual text rendering (English/Chinese), and instruction adherence, fitting within 16GB VRAM.

`text-to-image`

⬇️ 296,552 • ❤️ 2,801 • 7d ago

---

**[Devstral-Small-2-24B-Instruct-2512](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)**

*Mistral AI_*

Devstral Small 2 24B Instruct 2512 is a lightweight, agentic LLM for software engineering tasks, excelling at codebase exploration and multi-file editing with a 256k context window and FP8 precision. It is ideal for AI code assistants and agentic coding use cases, capable of running locally on consumer hardware.

`24.0B`

⬇️ 28,106 • ❤️ 379 • 1d ago

---

**[VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)**

*Microsoft*

VibeVoice-Realtime-0.5B is a lightweight, real-time text-to-speech model with ~300ms latency, supporting streaming input for robust long-form generation, ideal for live narration and LLM integration.

`text-to-speech` `1.0B`

⬇️ 158,614 • ❤️ 880 • 4d ago

---

**[AutoGLM-Phone-9B](https://huggingface.co/zai-org/AutoGLM-Phone-9B)**

*Z.ai*

AutoGLM-Phone-9B is a vision-language model for mobile intelligent assistance, enabling automated smartphone operations via ADB by understanding UI elements and executing natural language commands for task completion.

`image-text-to-text` `934,400`

⬇️ 51,591 • ❤️ 322 • 7d ago

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

⬇️ 6,543 • ❤️ 222 • 1d ago

---

**[NVIDIA-Nemotron-3-Nano-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 is a 30B parameter LLM with a hybrid MoE/Mamba architecture, excelling at reasoning tasks by generating explicit reasoning traces. It supports multiple languages and is suitable for commercial use, offering high accuracy in complex problem-solving.

`text-generation` `31.6B`

⬇️ 10,487 • ❤️ 219 • 16h ago

---

**[GLM-TTS](https://huggingface.co/zai-org/GLM-TTS)**

*Z.ai*

GLM-TTS is a controllable, zero-shot text-to-speech system that uses a two-stage LLM and Flow Matching architecture, enhanced by multi-reward reinforcement learning for expressive emotion control and high-quality synthesis. It supports voice cloning from short prompts and streaming inference for interactive applications.

`text-to-speech`

⬇️ 0 • ❤️ 217 • 5d ago

---

**[AutoGLM-Phone-9B-Multilingual](https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual)**

*Z.ai*

AutoGLM-Phone-9B-Multilingual is a vision-language model for mobile intelligent assistance, capable of understanding smartphone UIs via multimodal perception and executing tasks through ADB. It enables natural language control for automated operations on Android devices.

`image-text-to-text` `934,400`

⬇️ 7,731 • ❤️ 184 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 6 • 💬 2 • ⭐ 11,986 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 130 • 💬 6 • ⭐ 18,331 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based framework for real-time portrait animation that enhances speed and efficiency through multi-stage training, hybrid implicit signals, appearance distillation, and autoregressive micro-chunk streaming.

▲ 21 • 💬 2 • ⭐ 422 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2512.11253) • [💻 code](https://github.com/GVCLab/PersonaLive)

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

**[Sharp Monocular View Synthesis in Less Than a Second](https://huggingface.co/papers/2512.10685)**

*Lars Mescheder, Wei Dong, Shiwei Li et al. (13 authors)*

🏢 Apple

SHARP synthesizes photorealistic views from a single image using a 3D Gaussian representation, achieving state-of-the-art results with rapid processing.

▲ 4 • 💬 2 • ⭐ 426 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2512.10685) • [💻 code](https://github.com/apple/ml-sharp) • [🔗 project](https://apple.github.io/ml-sharp/)

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

---

## GitHub Repositories: "ai"

**[zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)**

An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone

`Python` `agent` `phone-use-agent`

⭐ 16.3k • 🔱 2.5k • 6h ago

---

**[Anionex/banana-slides](https://github.com/Anionex/banana-slides)**

一个基于nano banana pro🍌的原生AI PPT生成应用，迈向真正的＂Vibe PPT＂; 支持上传任意模板图片；上传任意素材&智能解析；一句话/大纲/页面描述自动生成PPT；口头修改指定区域、一键导出 - An AI-native PPT generator based on nano banana pro🍌

`Python` `ai-ppt-maker` `ai-slide-builder` `ai-slides` `llm` `nanobananapro`

⭐ 3.8k • 🔱 411 • 2h ago

---

**[glidea/banana-prompt-quicker](https://github.com/glidea/banana-prompt-quicker)**

🍌Awesome Prompts; Nano Banana；Banana Pro; Gemini；AI Studio；Prompt Quickly[正在开发 Sidebar 高级功能，敬请期待]

`JavaScript` `banana` `gemini` `prompt`

⭐ 1.8k • 🔱 141 • 8d ago

---

**[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**

An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

`Python` `ai-skills` `antigravity` `claude` `claude-code` `command-line`

⭐ 1.3k • 🔱 315 • 10d ago

---

**[repplus/rep](https://github.com/repplus/rep)**

rep+ — Burp-style HTTP Repeater for Chrome DevTools with built‑in AI to explain requests and suggest attacks

`JavaScript` `css` `html` `javascript` `markdown`

⭐ 1.1k • 🔱 137 • 3h ago

---

**[Norsico/Video-Materials-AutoGEN-Workstation](https://github.com/Norsico/Video-Materials-AutoGEN-Workstation)**

一个集内容策划、AI文案自动生成、TTS 批量自动配音、(AI)图片素材合成、ASR自动提取语言字幕脚本、AI自由创作于一体的(短视频)生成工作站。方便管理每期的视频项目。

`Python`

⭐ 1.1k • 🔱 218 • 16d ago

---

**[Hugo-Dz/spritefusion-pixel-snapper](https://github.com/Hugo-Dz/spritefusion-pixel-snapper)**

A tool to snap pixels to a perfect grid. Designed to fix messy and inconsistent pixel art generated by AI.

`Rust` `game-development` `gamedev` `image-processing` `pixel-art`

⭐ 896 • 🔱 23 • 8d ago

---

**[Ryandonofrio3/osgrep](https://github.com/Ryandonofrio3/osgrep)**

Open Source Semantic Search for your AI Agent

`TypeScript` `colbert` `embeddings` `grep` `grep-search`

⭐ 867 • 🔱 49 • 1d ago

---

**[firecrawl/open-scouts](https://github.com/firecrawl/open-scouts)**

  AI-powered web monitoring platform. Create automated scouts that search the web and send email alerts when they find what you're looking for. 

`TypeScript` `ai-agents` `alerts` `automation` `email-notifications` `firecrawl`

⭐ 754 • 🔱 110 • 1d ago

---

**[TanShilongMario/PromptFill](https://github.com/TanShilongMario/PromptFill)**

一个专为 AI 绘画（Nano Banana 等）设计的“结构化提示词生成工具”。通过可视化的“填空”交互方式，帮助用户快速构建、管理和迭代复杂的 Prompt。

`JavaScript`

⭐ 751 • 🔱 115 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*
