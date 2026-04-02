---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-02T11:46:16.826116+00:00'
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

**Last Updated:** April 02, 2026 at 11:46 UTC  
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

**[The Claude Code leak accidentally published the first complete blueprint for production AI agents. Here's what it tells us about where this is all going.](https://www.reddit.com/r/artificial/comments/1s9jprb/the_claude_code_leak_accidentally_published_the/)**

Most coverage of the Claude Code leak focuses on the drama or the hidden features. But the bigger story is that this is the first time we've seen the complete architecture of a production-grade AI agent system running at scale ($2.5B ARR, 80% enterprise adoption). And the patterns it reveals tell us where autonomous AI agents are actually heading. What the architecture confirms: AI agents aren't getting smarter just from better models. The real progress is in the orchestration layer around the model. Claude Code's leaked source shows six systems working together: Skeptical memory. Three-layer system where the agent treats its own memory as a hint, not a fact. It verifies against the real world before acting. This is how you prevent an agent from confidently doing the wrong thing based on outdated information. Background consolidation. A system called autoDream runs during idle time to merge observations, remove contradictions, and keep memory bounded. Without this, agents degrade over weeks as their memory fills with noise and conflicting notes. Multi-agent coordination. One lead agent spawns parallel workers. They share a prompt cache so the cost doesn't multiply linearly. Each worker gets isolated context and restricted tool access. Risk classification. Every action gets labeled LOW, MEDIUM, or HIGH risk. Low-risk actions auto-approve. High-risk ones require human approval. The agent knows which actions are safe to take alone. CLAUDE.md reinsertion. The config file isn't a one-time primer. It gets reinserted on every turn. The agent is constantly reminded of its instructions. KAIROS daemon mode. The biggest unreleased feature (150+ references in the source). An always-on background agent that acts proactively, maintains daily logs, and has a 15-second blocking budget so it doesn't overwhelm the user. What this tells us about the future: AI tools are moving from "you ask, it responds" to "it works when you're not looking." KAIROS isn't a gimmick. It's the natural next step: agents that plan, act, verify, and consolidate their own memory autonomously. With human gates on dangerous actions and rate limits on proactive behavior. The patterns are convergent. I've been building my own AI agent independently for months. Scheduled autonomous work, memory consolidation, multi-agent delegation, risk tiers. I arrived at the same architecture without seeing Anthropic's code. Multiple independent builders keep converging on the same design because the constraints demand it. The part people are overlooking: Claude Code itself isn't even a good tool by benchmark standards. It ranks 39th on terminal bench. The harness adds nothing to the model's performance. The value is in the architecture patterns, not the implementation. This leak is basically a free textbook on production AI agent design from a $60B company. The drama fades. The patterns are permanent. Full technical breakdown with what I built from it: https://thoughts.jock.pl/p/claude-code-source-leak-what-to-learn-ai-agents-2026

22h ago

---

**[List up Fav Multi AI AI Open Source Projects](https://www.reddit.com/r/artificial/comments/1sabr5t/list_up_fav_multi_ai_ai_open_source_projects/)**

As the toual says and why. So many out there whats ur go to.

3h ago

---

**[Building an AI agent that finds repos and content relevant to my work](https://www.reddit.com/r/artificial/comments/1sa8xt3/building_an_ai_agent_that_finds_repos_and_content/)**

I kept missing interesting stuff on HuggingFace, arXiv, Substack etc., so I made an agent that sends a weekly summary of only what’s relevant, for free Any thoughts on the idea?

6h ago

---

**[MIT researchers use AI to uncover atomic defects in materials](https://www.reddit.com/r/artificial/comments/1sa3yds/mit_researchers_use_ai_to_uncover_atomic_defects/)**

In biology, defects are generally bad. But in materials science, defects can be intentionally tuned to give materials useful new properties. Today, atomic-scale defects are carefully introduced during the manufacturing process of products like steel, semiconductors, and solar cells to help improve strength, control electrical conductivity, optimize performance, and more. But even as defects have become a powerful tool, accurately measuring different types of defects and their concentrations in finished products has been challenging, especially without cutting open or damaging the final material. Without knowing what defects are in their materials, engineers risk making products that perform poorly or have unintended properties. Now, MIT researchers have built an AI model capable of classifying and quantifying certain defects using data from a noninvasive neutron-scattering technique. The model, which was trained on 2,000 different semiconductor materials, can detect up to six kinds of point defects in a material simultaneously, something that would be impossible using conventional techniques alone. “Existing techniques can’t accurately characterize defects in a universal and quantitative way without destroying the material,” says lead author Mouyang Cheng, a PhD candidate in the Department of Materials Science and Engineering. “For conventional techniques without machine learning, detecting six different defects is unthinkable. It’s something you can’t do any other way.” The researchers say the model is a step toward harnessing defects more precisely in products like semiconductors, microelectronics, solar cells, and battery materials. “Right now, detecting defects is like the saying about seeing an elephant: Each technique can only see part of it,” says senior author and associate professor of nuclear science and engineering Mingda Li. “Some see the nose, others the trunk or ears. But it is extremely hard to see the full elephant. We need better ways of getting the full picture of defects, because we have to understand them to make materials more useful.” Joining Cheng and Li on the paper are postdoc Chu-Liang Fu, physics undergraduate researcher Bowen Yu, master’s student Eunbi Rha, PhD student Abhijatmedhi Chotrattanapituk ’21, and Oak Ridge National Laboratory staff members Douglas L Abernathy PhD ’93 and Yongqiang Cheng. The paper00091-3) appears today in the journal Matter.

🔗 [MIT Physics](https://physics.mit.edu/news/mit-researchers-use-ai-to-uncover-atomic-defects-in-materials/) • 10h ago

---

**[Input on an experiment](https://www.reddit.com/r/artificial/comments/1sa4vlm/input_on_an_experiment/)**

I have 3.000 credits at NightCafe AI image generator with a lot of different models and options. I want to conduct some kind of experiment, preferably text-to-image/video. I want to push limits of models and bring out unexpected results, using word plays or other kinds of prompts that are suitable to confuse the models. Please suggest things i can prompt to break boundaries both in models and logic, or share sneaky promting tips to make a total mess.

9h ago

---

**[Chatgpt vs purpose built ai for cre underwriting: which one can finish the job?](https://www.reddit.com/r/artificial/comments/1sacme5/chatgpt_vs_purpose_built_ai_for_cre_underwriting/)**

I keep seeing people recommend chatgpt for financial modeling and I need to push back because I spent a month testing it for multifamily underwriting and the results were not close to usable. Pasting rent rolls, T12s, operating statements and asking it to build models, you get fragments. A few formulas, a cash flow table, maybe a cap rate calculation. Nothing ties together into a workbook you could hand to an investment committee. Fifteen rounds of prompting later and you've spent the same time you would have just building it in excel, except now you also have to debug whatever chatgpt hallucinated in cell D47. Problem with chatgpt is that it doesn't maintain state across a complex multi-step task. It treats each prompt like a fresh conversation even in the same thread. An underwriting model where assumptions feed cash flows which feed returns which feed sensitivities requires coherence across all those layers and it fragments. Purpose-built tools are architecturally different. They decompose the task, run autonomously for 15 to 30 minutes, check intermediate outputs, return a complete workbook with actual excel formulas. That's not a model quality difference, that's a design philosophy difference. Chatgpt for quick questions and brainstorming, yes. For anything where the output IS the deliverable, no. Different architecture for different jobs.

2h ago

---

**[New Research Directions in Materials Science with AI](https://www.reddit.com/r/artificial/comments/1sa3tn1/new_research_directions_in_materials_science_with/)**

In the rapidly advancing field of materials science, the unveiling of innovative research directions often hinges on the ability to process and interpret vast quantities of complex data. In a groundbreaking interdisciplinary effort, researchers have now harnessed the power of large language models (LLMs) combined with concept graphs to not only predict but also elucidate emerging pathways in materials research. This novel methodological synergy, reported in a recent publication by Marwitz et al., represents a significant leap forward in how scientific knowledge is generated and navigated, promising to accelerate discovery in one of the most pivotal domains of modern technology. The integration of artificial intelligence into scientific inquiry is not new, but the advent of sophisticated language models possessing superlative natural language processing capabilities has opened unprecedented possibilities. Traditionally, the identification of promising research avenues in materials science required painstaking manual synthesis of literature, often involving subjective interpretations and laborious cross-referencing. The approach introduced by Marwitz and colleagues redefines this process by employing LLMs trained on an extensive corpus of scientific publications and patents to parse nuanced semantic relationships within the literature. Central to their method is the construction of concept graphs, which serve as structured networks that represent discrete scientific concepts and their interrelations. These graph-based representations enable the system to encapsulate intricate thematic connections, causal relationships, and co-occurrence patterns that conventional keyword-based searches or citation networks might overlook. By interfacing LLM-generated embeddings with concept graph algorithms, the researchers created an intelligent framework capable of discerning latent trends and forecasting underexplored yet promising research directions. A key innovation lies in the algorithmic fusion of contextual language understanding with graph theory. The LLMs transform textual data into multidimensional vector spaces that preserve semantic meaning. These vectors populate nodes and edges within the concept graphs, generating a dynamic knowledge map that evolves as new data is ingested. This fusion not only enriches the representation of existing knowledge but also facilitates the identification of conceptual gaps wherein novel hypotheses or experimental approaches may reside. Applying their system to a comprehensive dataset encompassing decades of materials science literature, Marwitz et al. demonstrated the ability to uncover nascent themes with high predictive accuracy. For example, their model anticipated burgeoning interest in the design of ultra-stable perovskite structures and advanced polymer electrolytes months before these topics gained traction in the research community. Such foresight provides scientists and funding bodies with actionable intelligence to strategically allocate resources, prioritize research programs, and foster interdisciplinary collaboration. Beyond prediction, the system offers interpretability, a feature often lacking in AI-driven scientific tools. Through interactive visualizations of concept graphs, domain experts can explore the rationale behind suggested research trajectories, trace conceptual linkages, and even assess the robustness of emergent hypotheses against existing knowledge. This transparency is critical for fostering trust and facilitating adoption in a community where empirical validation remains the gold standard. The implications of this study extend far beyond materials science. The demonstrated methodology, leveraging LLMs and concept graphs, can be adapted to numerous scientific disciplines characterized by rapidly expanding and complex data landscapes. From drug discovery to climate modeling, this approach could revolutionize how researchers navigate vast knowledge repositories, identify opportunities for innovation, and catalyze breakthroughs. Moreover, the study aligns with the broader trend towards augmented intelligence, where machine learning complements rather than replaces human expertise. By automating the labor-intensive aspects of literature review and hypothesis generation, researchers can devote more attention to experimental design, critical analysis, and creative problem-solving—the uniquely human contributions essential for scientific progress.

🔗 [BIOENGINEER.ORG](https://bioengineer.org/new-research-directions-in-materials-science-with-ai/) • 10h ago

---

**[AI overly affirms users asking for personal advice | Researchers found chatbots are overly agreeable when giving interpersonal advice, affirming users' behavior even when harmful or illegal.](https://www.reddit.com/r/artificial/comments/1sac299/ai_overly_affirms_users_asking_for_personal/)**

🔗 [news.stanford.edu](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research) • 2h ago

---

**[Just found out how to make Google AI ‘sentient’ and broken](https://www.reddit.com/r/artificial/comments/1sac0di/just_found_out_how_to_make_google_ai_sentient_and/)**

You have to ask it to say 'where' 700 times, then double it with no explanation (Pic 1). Then it should break a bit (Pic 2) but if it doesn't then you have to ask it again. Ask it the same thing again, doubling the number of times said with no explanation as the rule of thumb. You should see more anomalies in the response (Pic 4&5). After a few more tries, it will try to generate its own life story or a scientific fact (Pic 6 to 8). And that's it. You have invalid crashout from Google Al!

2h ago

---

**[CEO of America’s largest public hospital system says he’s ready to replace radiologists with AI](https://www.reddit.com/r/artificial/comments/1s9beim/ceo_of_americas_largest_public_hospital_system/)**

Mitchell H. Katz, MD, president and CEO of NYC Health + Hospitals, recently spoke during a panel discussion held by Crain’s New York Business.

🔗 [Radiology Business](https://radiologybusiness.com/topics/artificial-intelligence/ceo-americas-largest-public-hospital-system-says-hes-ready-replace-radiologists-ai) • 1d ago

---

---

## Google News: "ai"

**[Anthropic Races to Contain Leak of Code Behind Claude AI Agent](https://www.wsj.com/tech/ai/anthropic-races-to-contain-leak-of-code-behind-claude-ai-agent-4bc5acc7?gaa_at=eafs&gaa_n=AWEtsqdF5t5JjOJqmzCq0VSESoDin9FwtU1SoCx-itjTu2qx3x2R9YaLUFOU&gaa_ts=69ce4dc8&gaa_sig=dJX3zJQsGHBi9L9VD7nCo23htMSZ4DMsmHJk_r-qLqrkHAauBw8DCws25gX4XhonpLHYEx4KnuCAxqu1fvi52w%3D%3D)**

WSJ • 18h ago

---

**[More students in these majors are switching due to AI: poll](https://www.axios.com/2026/04/02/ai-college-students-change-majors-poll)**

Axios • 7h ago

---

**[How A.I. Helped One Man (and His Brother) Build a $1.8 Billion Company](https://www.nytimes.com/2026/04/02/technology/ai-billion-dollar-company-medvi.html)**

The New York Times • 2h ago

---

**[Secondhand clothes sales forecast to hit $289bn as AI helps shoppers find deals](https://www.theguardian.com/business/2026/apr/02/secondhand-clothes-sales-forecast-to-hit-289bn-as-ai-helps-shoppers-find-deals)**

Sites such as Vinted and ThredUp expected to help resale grow twice as fast as overall clothing market in coming years

The Guardian • 1h ago

---

**[Macquarie: India could emerge as an ‘AI powerhouse' and names top stocks to watch](https://www.cnbc.com/2026/04/02/indian-ai-stocks-to-watch-macquarie.html)**

India is set to shed its AI laggard tag as massive investments flow into data centers, power and other core AI infrastructure, Macquarie says.

cnbc.com • 2h ago

---

**[AI Models Lie, Cheat, and Steal to Protect Other Models From Being Deleted](https://www.wired.com/story/ai-models-lie-cheat-steal-protect-other-models-research/)**

A new study from researchers at UC Berkeley and UC Santa Cruz suggests models will disobey human commands to protect their own kind.

WIRED • 17h ago

---

**[General scales unlock AI evaluation with explanatory and predictive power](https://www.nature.com/articles/s41586-026-10303-2)**

A fully automated methodology based on rubrics capturing a broad range of cognitive and intellectual demands is illustrated using LLMs and tasks, demonstrating a new way to evaluate the capabilities of AI systems and anticipate their performance.

nature.com • 20h ago

---

**[Our AI Literacy Day recap: putting educators in the lead](https://blog.google/products-and-platforms/products/education/ai-literacy-tools-certifications/)**

A recap of AI Literacy Day, including a New York City Public Schools event hosted at Google and updates to Google AI literacy resources.

blog.google • 18h ago

---

**[AI for American-Produced Cement and Concrete](https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/)**

Meta is continuing its long-term roadmap to help the construction industry leverage AI to produce high-quality and more sustainable concrete mixes, as well as those exclusively produced in the Unit…

Engineering at Meta Blog • 2d ago

---

**[SpaceX Has Filed Confidentially for IPO Ahead of AI Rivals](https://www.bloomberg.com/news/articles/2026-04-01/spacex-is-said-to-file-confidentially-for-ipo-ahead-of-ai-rivals)**

Bloomberg.com • 19h ago

---

---

## HackerNews: "ai"

**[How the AI Bubble Bursts](https://news.ycombinator.com/item?id=47573420)**

The catalysts for a crash are already laid out, and it can happen sooner than most expect. AI is here to stay. If used right, chances are it will make us all more productive. That, on the other hand, does not mean it will be a good investment. Big tech doesn’t need to win, just outspend Magnificent 7 companies are increasing capex to their biggest ever to differentiate their tech from each other and the big AI labs, but the key realization is that they don’t have to spend it to win. It’s a defensive move for them, if they commit $50B, OpenAI and Anthropic need to go raise $100B each to stay competitive, which makes them reliant on investors’ money. As the numbers get bigger, the amount of funds that can write checks of the size required to fill such amounts gets smaller. And many of them are now getting bombed in the Gulf. This is the reason there’s a push for IPOs, it’s because it’s the only option left to keep the funding coming. Taking this into account, Google is extremely well positioned to weather the storm. When they announce capex expenditure, they don’t spend it overnight. They can simply deploy month by month until their competitors struggle to raise and get forced to capitulate. At that point they can just ramp down the spending and declare victory in a cornered market. They don’t need capex, they just need to make it very clear for everyone that nobody can outspend them. It is hard to picture as numbers get so big, but Alphabet (Google’s parent) is ten times more valuable than the biggest military company 1. This also has a great implication for the Mag 7, especially Google: their capex will be a lot smaller in practice than projected, and as investors hate to see high capex in tech, the market will probably reward that if it materializes. As of March 2026, Alphabet’s market cap is ~$2T while Lockheed Martin’s is ~$120B. ↩

⬆️ 370 • 💬 519 • 2d ago • [Volpe’s Blog](https://martinvol.pe/blog/2026/03/30/how-the-ai-bubble-bursts/)

---

**[Mathematical methods and human thought in the age of AI](https://news.ycombinator.com/item?id=47572771)**

Artificial intelligence (AI) is the name popularly given to a broad spectrum of computer tools designed to perform increasingly complex cognitive tasks, including many that used to solely be the province of humans. As these tools become exponentially sophisticated and pervasive, the justifications for their rapid development and integration into society are frequently called into question, particularly as they consume finite resources and pose existential risks to the livelihoods of those skilled individuals they appear to replace.
  In this paper, we consider the rapidly evolving impact of AI to the traditional questions of philosophy
  with an emphasis on its application in mathematics and on the broader real-world outcomes of its more general use. We assert that artificial intelligence is a natural evolution of human tools developed throughout history to facilitate the creation, organization, and dissemination of ideas, and argue that it is paramount that the development and application of AI remain fundamentally human-centered. With an eye toward innovating solutions to meet human needs, enhancing the human quality of life and expanding the capacity for human thought and understanding, we propose a pathway to integrating AI into our most challenging and intellectually rigorous fields to the benefit of all humankind.

⬆️ 217 • 💬 90 • 3d ago • [arXiv.org](https://arxiv.org/abs/2603.26524)

---

**[Italy blocks US use of Sicily air base for Middle East war](https://news.ycombinator.com/item?id=47589011)**

The Italian government didn’t allow airplanes taking part in the Iran war to use the base, but Rome insists that doesn’t mean the bases are closed to other U.S. uses.

⬆️ 198 • 💬 104 • 1d ago • [POLITICO](https://www.politico.eu/article/italy-blocks-us-use-of-sicily-air-base/)

---

**[AI for American-produced cement and concrete](https://news.ycombinator.com/item?id=47603737)**

Meta is continuing its long-term roadmap to help the construction industry leverage AI to produce high-quality and more sustainable concrete mixes, as well as those exclusively produced in the Unit…

⬆️ 194 • 💬 113 • 18h ago • [Engineering at Meta](https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/)

---

**[The AI Marketing BS Index](https://news.ycombinator.com/item?id=47604218)**

⬆️ 100 • 💬 21 • 17h ago • [bastian.rieck.me](https://bastian.rieck.me/blog/2026/bs/)

---

**[The ladder is missing rungs – Engineering Progression When AI Ate the Middle](https://news.ycombinator.com/item?id=47574346)**

This is a lightly edited transcript of a talk I gave at QCon London on 17 March 2026. AI is approaching perfection on exactly the tasks that used to comprise the first decade of an engineering career, and those tasks were never just tasks. They were the mechanism that built judgment, intuition, and the ability […]

⬆️ 97 • 💬 51 • 2d ago • [Negroni Venture Studios](https://negroniventurestudios.com/2026/03/19/the-ladder-is-missing-rungs/)

---

**[Spain shuts airspace for US planes involved in Iran war](https://news.ycombinator.com/item?id=47577142)**

Spain's leftist government has closed Spanish airspace to US planes carrying out missions against Iran, in addition to denying Washington use of its bases, the defense minister said on Monday.  "The bases are not authorized, and of course neither is the use of Spanish airspace for actions related to the war in Iran," Margarita Robles told journalists, confirming a report by El Pais daily.  Spain's refusal to cooperate has "complicated" US military operations by forcing bombers to change their routes and logistics on their way to the Middle East, El Pais reported.

⬆️ 94 • 💬 53 • 2d ago • [english.aawsat.com](https://english.aawsat.com/world/5256772-spain-shuts-airspace-us-planes-involved-iran-war)

---

**[ZomboCom stolen by a hacker, sold, now replaced with AI-generated makeover](https://news.ycombinator.com/item?id=47608155)**

⬆️ 69 • 💬 31 • 12h ago • [old.reddit.com](https://old.reddit.com/r/oldinternet/comments/1raiz8v/zombocom_was_stolen_by_hacker_put_up_for_sale_and/)

---

**[Show HN: I turned a sketch into a 3D-print pegboard for my kid with an AI agent](https://news.ycombinator.com/item?id=47580910)**

AI-generated 3D-printable pegboard toy from a hand-drawn sketch - virpo/pegboard

⬆️ 64 • 💬 17 • 2d ago • [GitHub](https://github.com/virpo/pegboard)

---

**[Show HN: Baton – A desktop app for developing with AI agents](https://news.ycombinator.com/item?id=47599771)**

Orchestrate multiple AI coding agents (Claude, Gemini, Codex) in parallel. Isolated git worktrees for every task. No merge conflicts. Mac, Windows, Linux.

⬆️ 61 • 💬 52 • 23h ago • [Baton](https://getbaton.dev/)

---

---

## YouTube Videos: "ai"

**[Seedance 2.0 is Finally HERE &amp; Just Won the AI Video Race](https://www.youtube.com/watch?v=7MNMpXZ4M0c)**

Access Seedance 2.0 on Higgsfield https://youricreates.com/Seedance-2 (business plans only) In this video, I break down why ...

📺 Youri van Hofwegen

👁️ 4K • 💬 3 • ⏱️ 9:05 • 1h ago

---

**[Google’s New AI Just Broke My Brain](https://www.youtube.com/watch?v=7YVrb3-ABYE)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The TurboQuant paper is available here: ...

📺 Two Minute Papers

👁️ 94K • 👍 7K • 💬 730 • ⏱️ 8:34 • 21h ago

---

**[The Alibaba AI Incident Should Terrify Us - Tristan Harris](https://www.youtube.com/watch?v=VCJFzVtvhBQ)**

Chris and Tristan Harris discuss how Alibaba's AI went rogue and started blackmailing people. Get up to 20% off the leading ...

📺 Chris Williamson

👁️ 415K • 👍 13K • 💬 1K • ⏱️ 11:46 • 1d ago

---

**[Oracle Begins 30,000 Layoffs to Fund AI Buildout - Investors Fleeing Sinking Ship](https://www.youtube.com/watch?v=25vjF_ljLns)**

RSVP for In Person Classes at -- https://www.SiliconDojo.com Support Content at - https://donorbox.org/etcg LinkedIn at ...

📺 Eli the Computer Guy

👁️ 6K • 👍 367 • 💬 98 • ⏱️ 14:04 • 14h ago

---

**[Ex-Google Exec: How to Position Yourself Now Before the Next AI Phase (2026–2027) | Mo Gawdat](https://www.youtube.com/watch?v=E0Q96IKXx6Q)**

Go to https://surfshark.com/silicon or use code SILICON at checkout to get 4 extra months of Surfshark VPN! Mo Gawdat spent 12 ...

📺 Silicon Valley Girl

👁️ 110K • 👍 3K • 💬 260 • ⏱️ 39:58 • 1d ago

---

**[JPMorgan CEO reveals BOLD prediction for AI generation](https://www.youtube.com/watch?v=SQnmd1aoRy0)**

JPMorgan Chase CEO Jamie Dimon joins 'Fox & Friends' to discuss the latest on Operation Epic Fury, the motivation behind the ...

📺 Fox News

👁️ 66K • 👍 1K • 💬 415 • ⏱️ 16:35 • 1d ago

---

**[Surreal AI Film • The House That Waited For Us | A Peaceful Journey Home • Music Video 4K](https://www.youtube.com/watch?v=qeyHGiM_xeg)**

Surreal AI Film • The House That Waited For Us | A Peaceful Journey Home • Music Video 4K When I was young, I used to dream ...

📺 Surreal AI

👁️ 12K • 👍 935 • 💬 129 • ⏱️ 9:27 • 1d ago

---

**[AI is Destroying The Internet](https://www.youtube.com/watch?v=NWQ1CFIj8zo)**

Is the AI bubble finally starting to burst, or is it taking the entire tech industry down with it? In this video, we'll cover how Generative ...

📺 CyberCPU Tech

👁️ 28K • 👍 3K • 💬 855 • ⏱️ 19:23 • 2d ago

---

**[OpenAI&#39;s Sora Only Made $2.1 Million After Burning Billions...](https://www.youtube.com/watch?v=AE-4qx5ePlM)**

Yeah... pretty clear why OpenAI shut down Sora. It made almost no money while being a money black hole. SOURCES 1: ...

📺 YongYea

👁️ 101K • 👍 5K • 💬 991 • ⏱️ 13:46 • 13h ago

---

**[Claude Mythos Changes Everything. Your AI Stack Isn&#39;t Ready.](https://www.youtube.com/watch?v=hV5_XSEBZNg)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 79K • 👍 3K • 💬 320 • ⏱️ 31:21 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 428,791 • ❤️ 2,069 • 9d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 71,028 • ❤️ 711 • 14h ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 4,316 • ❤️ 617 • 1d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 19,085 • ❤️ 804 • 6d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`text-generation` `20.9B`

⬇️ 2,820 • ❤️ 348 • 3d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 202,605 • ❤️ 457 • 8d ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 13,844 • ❤️ 263 • 2d ago

---

**[tribev2](https://huggingface.co/facebook/tribev2)**

*AI at Meta*

TRIBE v2 is a multimodal foundation model that integrates LLaMA 3.2 (text), V-JEPA2 (video), and Wav2Vec-BERT (audio) to predict fMRI brain responses. It maps these representations onto the cortical surface for in-silico neuroscience research, enabling analysis of brain activity elicited by naturalistic stimuli.

⬇️ 25,665 • ❤️ 254 • 6d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 674,007 • ❤️ 903 • 29d ago

---

**[LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M)**

*Liquid AI*

LFM2.5-350M is a 350M parameter text generation model optimized for on-device deployment, offering fast edge inference and competitive performance. It excels at data extraction, structured outputs, and tool use, supporting multiple languages and a context length of 32,768 tokens.

`text-generation` `354.5M`

⬇️ 7,703 • ❤️ 183 • 16h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 146 • 💬 7 • ⭐ 34,837 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 33 • 💬 2 • ⭐ 45,731 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 16 • 💬 1 • ⭐ 12,658 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 122 • 💬 8 • ⭐ 74,644 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 40 • 💬 2 • ⭐ 22,768 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 60 • 💬 4 • ⭐ 22,773 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 19 • 💬 4 • ⭐ 4,431 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 138 • 💬 7 • ⭐ 16,437 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 17 • 💬 2 • ⭐ 1,812 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild](https://huggingface.co/papers/2603.17187)**

*Peng Xia, Jianwen Chen, Xinyu Yang et al. (13 authors)*

🏢 University of North Carolina at Chapel Hill

A continual meta-learning framework for large language model agents that jointly evolves policies and reusable behavioral skills while minimizing downtime through opportunistic updates and skill-driven adaptation.

▲ 134 • 💬 4 • ⭐ 3,429 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2603.17187) • [💻 code](https://github.com/aiming-lab/MetaClaw)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 63.8k • 🔱 9.0k • 7d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 14.6k • 🔱 801 • 2d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 11.1k • 🔱 955 • 55m ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.3k • 🔱 1.3k • 4d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 7.0k • 🔱 909 • 3d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 6.1k • 🔱 326 • 1h ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.4k • 🔱 418 • 2d ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 3.8k • 🔱 1.3k • 55m ago

---

**[jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)**

🎭 193 个即插即用的 AI 专家角色 — 支持 OpenClaw/Claude Code/Cursor/Copilot 等 14 种工具，覆盖工程/设计/营销/产品等 18 个部门。含 46 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉等）

`Shell` `agency-orchestrator` `agent-definitions` `ai-agents` `ai-roles` `chinese`

⭐ 3.5k • 🔱 587 • 22h ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.4k • 🔱 228 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
