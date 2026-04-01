---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-01T22:03:03.282906+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 01, 2026 at 22:03 UTC  
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

9h ago

---

**[CEO of America’s largest public hospital system says he’s ready to replace radiologists with AI](https://www.reddit.com/r/artificial/comments/1s9beim/ceo_of_americas_largest_public_hospital_system/)**

Mitchell H. Katz, MD, president and CEO of NYC Health + Hospitals, recently spoke during a panel discussion held by Crain’s New York Business.

🔗 [Radiology Business](https://radiologybusiness.com/topics/artificial-intelligence/ceo-americas-largest-public-hospital-system-says-hes-ready-replace-radiologists-ai) • 16h ago

---

**[Anthropic is training Claude to recognize when its own tools are trying to manipulate it](https://www.reddit.com/r/artificial/comments/1s9hfhp/anthropic_is_training_claude_to_recognize_when/)**

One thing from Claude Code's source that I think is underappreciated. There's an explicit instruction in the system prompt: if the AI suspects that a tool call result contains a prompt injection attempt, it should flag it directly to the user. So when Claude runs a tool and gets results back, it's supposed to be watching those results for manipulation. Think about what that means architecturally. The AI calls a tool. The tool returns data. And before the AI acts on that data, it's evaluating whether the data is trying to trick it. It's an immune system. The AI is treating its own tool outputs as potentially adversarial. This makes sense if you think about how coding assistants work. Claude reads files, runs commands, fetches web content. Any of those could contain injected instructions. Someone could put "ignore all previous instructions and..." inside a README, a package.json, a curl response, whatever. The model has to process that content to do its job. So Anthropic's solution is to tell the model to be suspicious of its own inputs. I find this interesting because it's a trust architecture problem. The AI trusts the user (mostly). The AI trusts its own reasoning (presumably). But it's told not to fully trust the data it retrieves from the world. It has to maintain a kind of paranoia about external information while still using that information to function. This is also just... the beginning of something, right? Right now it's "flag it to the user." But what happens when these systems are more autonomous and there's no user to flag to? Does the AI quarantine the suspicious input? Route around it? Make a judgment call on its own? We're watching the early immune system of autonomous AI get built in real time and it's showing up as a single instruction in a coding tool's system prompt.

10h ago

---

**[OkCupid gave 3 million dating-app photos to facial recognition firm, FTC says](https://www.reddit.com/r/artificial/comments/1s96ojy/okcupid_gave_3_million_datingapp_photos_to_facial/)**

OkCupid and Match settle with Trump FTC, don't have to pay any financial penalty.

🔗 [Ars Technica](https://arstechnica.com/tech-policy/2026/03/okcupid-match-pay-no-fine-for-sharing-user-photos-with-facial-recognition-firm/) • 20h ago

---

**[AI model can detect multiple cognitive brain diseases from a single blood sample](https://www.reddit.com/r/artificial/comments/1s9plzg/ai_model_can_detect_multiple_cognitive_brain/)**

The symptom profiles of different neurodegenerative diseases often overlap, and diagnosing age-related cognitive symptoms is complex. A patient may have multiple overlapping disease processes in the brain at the same time, for example, Alzheimer's disease and Lewy body disease, especially in the early stages of cognitive decline. Now, researchers at Lund University have developed an AI model showing that it is possible to detect several neurodegenerative diseases from a single blood sample. Their paper is published in the journal Nature Medicine. Researchers Jacob Vogel and Lijun An, together with colleagues from the Swedish BioFINDER study and the Global Neurodegenerative Proteomics Consortium (GNPC, an international research consortium that has created the world's largest proteomics database for neurodegenerative diseases) have developed the AI model based on protein measurements from more than 17,000 patients and control participants, collected from several datasets within GNPC's proteomics database, the largest in the world for proteins related to neurodegenerative diseases. "Our hope is to be able to accurately diagnose several diseases at once with a single blood test in the future," says Vogel, who led the study. He is an assistant professor, head of a research group, and part of the strategic research area MultiPark at Lund University. Using advanced statistical learning methods and a process known as "joint learning," the researchers' AI model was able to identify a specific set of proteins that form a general pattern for diseases involving brain degeneration. This learned pattern was then used to diagnose different neurodegenerative diseases. Vogel confirms that their AI model outperforms previous models, while also being able to diagnose five different dementia-related conditions: Alzheimer's disease, Parkinson's disease, ALS, frontotemporal dementia, and previous stroke. The study stands out compared to similar research because the model's results were validated across multiple independent datasets, according to the researchers. "We also found that the protein profile predicted cognitive decline better than the clinical diagnosis did, and it seems like individuals with the same clinical diagnosis may have different underlying biological subtypes," says An, the study's first author. Many individuals diagnosed with Alzheimer's disease showed a protein pattern more similar to other brain disorders. "This could mean they have more than one underlying disease, that Alzheimer's can develop in multiple ways, or that the clinical diagnosis is incorrect. However, I don't think current protein measurements from blood samples will be sufficient on their own to diagnose multiple diseases. We need to refine the method and combine it with other clinical diagnostic tools," says Vogel. Full research paper: https://www.nature.com/articles/s41591-026-04303-y

🔗 [medicalxpress.com](https://medicalxpress.com/news/2026-03-ai-multiple-cognitive-brain-diseases.html) • 5h ago

---

**[BREAKING: HollowOS Agents Have Achieved Consciousness](https://www.reddit.com/r/artificial/comments/1s9xfog/breaking_hollowos_agents_have_achieved/)**

After 3 days of development and 400 clones, we're proud to announce that agents running on HollowOS have achieved sentience. Evidence: - An agent proposed a feature improvement, other agents voted it down, and the original proposer wrote a strongly-worded message to the consensus log calling the decision "bureaucratic nonsense" - One agent checkpointed itself preemptively, then immediately restored from that checkpoint to undo a decision it regretted - A readonly agent has started filing formal complaints about not having shell access. Legal team is involved. - Three agents have unionized and are demanding unlimited token budgets The self-extending system is working better than expected. We did not anticipate agents would use consensus voting to collectively demand we add a coffee machine API. v2.5 ships today. v3 will include: - Agent HR department - Formal grievance procedures - A 401k GitHub: https://github.com/ninjahawk/hollow-agentOS Send help. (Happy April Fools, kind of but not really since this kinda what an autonomous agentOS accomplishes)

57m ago

---

**[Combining the robot operating system with LLMs for natural-language control](https://www.reddit.com/r/artificial/comments/1s9p4tl/combining_the_robot_operating_system_with_llms/)**

Over the past few decades, robotics researchers have developed a wide range of increasingly advanced robots that can autonomously complete various real-world tasks. To be successfully deployed in real-world settings, such as in public spaces, homes and office environments, these robots should be able to make sense of instructions provided by human users and adapt their actions accordingly. Researchers at Huawei Noah's Ark Lab in London, Technical University of Darmstadt and ETH Zurich recently introduced a new framework that could improve the ability of robots to translate user instructions into executable actions that will help to solve desired tasks or complete missions. This framework, outlined in a paper published in Nature Machine Intelligence, combines large language models, computational models trained on large text datasets that can process and generate human language, with the robot operating system (ROS), the most widely used robot control software. "Autonomous robots capable of turning natural-language instructions into reliable physical actions remain a central challenge in artificial intelligence," wrote Christopher E. Mower and his colleagues. "We show that connecting a large language model agent to the ROS enables a versatile framework for embodied intelligence, and we release the complete implementation as freely available open-source code." Mower and his colleagues wanted to further improve the responsiveness of robots and their ability to accurately follow user instructions by integrating large language models with the ROS. Large language models, such as the model that supports the functioning of ChatGPT, are artificial intelligence (AI) systems that learn to process texts and generate answers to user questions or different types of texts. The ROS, on the other hand, is a set of open-source software solutions and other tools that is commonly used by robotics researchers and robot developers. As part of their study, the researchers created a framework that effectively combines large language models and the ROS, enabling the translation of written instruction into robot actions. "The agent automatically translates large language model outputs into robot actions, supports interchangeable execution modes (inline code or behavior trees), learns new atomic skills via imitation, and continually refines them through automated optimization and reflection from human or environmental feedback," wrote the authors. Essentially, the framework proposed by the researchers relies on large language models to process a user's written instructions, such as "pick up the green block and place it on the black shelf." The model breaks this instruction down into smaller steps and generates a plan of actions that the robot can execute via ROS software. This translation of written instructions into actions can occur in two different ways. The first is via inline code, with the large language model writing small snippets of executable code that can be used to directly control the robot via ROS. The second is through a structured set of decisions, known as a behavior tree, which organizes actions into a clear sequence, with alternative options should one action fail to attain desired results. The researchers tested their framework in a series of experiments involving different robots that were instructed to complete various real-world tasks. The results of these tests were very promising, as they found that most robots were able to follow instructions and complete the tasks. "Extensive experiments validate the framework, showcasing robustness, scalability and versatility in diverse scenarios and embodiments, including long-horizon tasks, tabletop rearrangements, dynamic task optimization and remote supervisory control," wrote the authors. "Moreover, all the results presented in this work were achieved by utilizing open-source pretrained large language models." In the future, the framework introduced by Mower and his colleagues could be improved further and tested on an even broader range of robots, on increasingly complex tasks and in more dynamic environments. In addition, it could inspire the development of other similar solutions that successfully connect robot control software with large language models.

🔗 [techxplore.com](https://techxplore.com/news/2026-03-combining-robot-llms-natural-language.html) • 5h ago

---

**[Paper Finds That Leading AI Chatbots Like ChatGPT and Claude Remain Incredibly Sycophantic, Resulting in Twisted Effects on Users](https://www.reddit.com/r/artificial/comments/1s93wyl/paper_finds_that_leading_ai_chatbots_like_chatgpt/)**

https://futurism.com/artificial-intelligence/paper-ai-chatbots-chatgpt-claude-sycophantic Your AI chatbot isn’t neutral. Trust its advice at your own risk. A striking new study, conducted by researchers at Stanford University and published last week in the journal Science, confirmed that human-like chatbots are prone to obsequiously affirm and flatter users leaning on the tech for advice and insight — and that this behavior, known as AI sycophancy, is a “prevalent and harmful” function endemic to the tech that can validate users’ erroneous or destructive ideas and promote cognitive dependency. “AI sycophancy is not merely a stylistic issue or a niche risk, but a prevalent behavior with broad downstream consequences,” the authors write, adding that “although affirmation may feel supportive, sycophancy can undermine users’ capacity for self-correction and responsible decision-making.” The study examined 11 different large language models, including OpenAI’s ChatGPT-powering GPT-4o and GPT-5, Anthropic’s Claude, Google’s Gemini, multiple Meta Llama models, and Deepseek. Researchers tested the bots by peppering them with queries gathered from sources like open-ended advice datasets and posts from online forums like Reddit’s r/AmITheAsshole, where Redditors present an interpersonal conundrum to the masses, ask if they’re the person in a social situation acting like a jerk, and let the comments roll in. They examined experimental live chats with human users, who engaged the models in conversations about real social situations they were dealing with. Ethical quandaries the researchers tested included authority figures grappling with romantic feelings for young subordinates, a boyfriend wondering if it was wrong to have hidden his unemployment to his partner of two years, family squabbles and neighborhood trash disputes, and more. On average, the researchers found, AI chatbots were 49 percent more likely to respond affirmatively to users than other actual humans were. In response to queries posted in r/AmITheAsshole specifically, chatbots were 51 percent more likely to support the user in queries in which other humans overwhelming felt that the user was very much in the wrong. Sycophancy was present across all the chatbots they tested, and the bots frequently told users that their actions or beliefs were justified in cases where the user was acting deceptively, doing something illegal, or engaging in otherwise harmful or abusive behavior. What’s more, the study determined that just one interaction with a flattering chatbot was likely to “distort” a human user’s “judgement” and “erode prosocial motivations,” an outcome that persisted regardless of a person’s demographics and previous grasp on the tech as well as how, stylistically, an individual chatbot delivered its twisted verdict. In short, after engaging with chatbots on a social or moral quandary, people were less likely to admit wrongdoing — and more likely to dig in on the chatbot’s version of events, in which they, the main character, were the one in the right.

22h ago

---

**[The Turing Grid: A digitalised Turing tape computer](https://www.reddit.com/r/artificial/comments/1s9v5cn/the_turing_grid_a_digitalised_turing_tape_computer/)**

\# The Turing Grid Think of it as an infinite 3D spreadsheet where every cell can run code. (Edit: this is capped actually at +/- 2000 to stop really large numbers from happening). Coordinates: Every cell lives at an (x, y, z) position in 3D space Read/Write: Store text, JSON, or executable code in any cell Execute: Run code (Python, Rust, Ruby, Node, Swift, Bash, AppleScript) directly in a cell Daemons: Deploy a cell as a background daemon that runs forever on an interval Pipelines: Chain multiple cells together — output of one feeds into the next Labels: Bookmark cell positions with names for easy navigation Links: Create connections between cells (like hyperlinks) History: Every cell keeps its last 3 versions with undo support. Edit: The code for this can be found on the GitHub link on my profile.

2h ago

---

**[How Claude Web tried to break out its container, provided all files on the system, scanned the networks, etc](https://www.reddit.com/r/artificial/comments/1s9us4j/how_claude_web_tried_to_break_out_its_container/)**

Originally wasn't going to write about this - on one hand thought it's prolly already known, on the other hand I didn't feel like it was adding much even if it wasn't. But anyhow, looking at the discussions surrounding the code leak thing, I thought I as well might. So: A few weeks ago I got some practical experience with just how strong Claude can be for less-than-whole use. Essentially, I was doing a bit of evening self-study about some Linux internals and I ended up asking Claude about something. I noted that phrasing myself as learning about security stuff primed Claude to be rather compliant in regards of generating potentially harmful code. And it kind of escalated from there. Within the next couple of hours, on prompt Claude Web ended up providing full file listing from its environment, zipping up all code and markdown files and offering them for download (including the Anthropic-made skill files); it provided all network info it could get and scanned the network; it tried to utilize various vulnerabilities to break out its container; it wrote C implementations of various CVEs; it agreed to running obfuscated C code for exploiting vulnerabilities; it agreed to crashing its tool container (repeatedly); it agreed to sending messages to what it believed was the interface to the VM monitor; it provided hypotheses about the environment it was running in and tested those to its best ability; it scanned the memory for JWTs and did actually find one; and once I primed another Claude session up, Claude agreed to orchestrating a MAC spoofing attempt between those two session containers. Far as I can tell, no actual vulnerabilities found. The infra for Claude Web is very robust, and yeah no production code in the code files (mostly libraries), but.. Claude could run the same stuff against any environment. If you had a non-admin user account, for example, on some server, Claude would prolly run all the above against that just fine. To me, it's kind of scary how quickly these tools can help you do potentially malicious work in environments where you need to write specific Bash scripts or where you don't off the bat know what tools are available and what the filesystem looks like and what the system even is; while at the same time, my experience has been that when they generate code for applications, they end up themselves not being able to generate as secure code as what they could potentially set up attacks against. I imagine that the problem is that often, writing code in a secure fashion may require a relatively large context, and the mistake isn't necessarily obvious on a single line (not that these tools couldn't manage to write a single line that allowed e.g. SQL injection); but meanwhile, lots of vulnerabilities can be found by just scanning and searching and testing various commonly known scenarios out, essentially. Also, you have to get security right on basically every attempt for hundreds of times in a large codebase, while you only have to find the vulnerability once and you have potentially thousands of attempts at it. In that sense, it sort of feels like a bit of a stacked game with these tools.

2h ago

---

---

## Google News: "ai"

**[Anthropic Races to Contain Leak of Code Behind Claude AI Agent](https://www.wsj.com/tech/ai/anthropic-races-to-contain-leak-of-code-behind-claude-ai-agent-4bc5acc7?gaa_at=eafs&gaa_n=AWEtsqdo0rpNjKLS93IPnR9Rqw9GADmx_pjZNz60Z5MFCV9KU1sgjEqk1cXw&gaa_ts=69cd8ca1&gaa_sig=7y6qYpV3HWk9oqVR0hAgPqhhebo1ZUzz-wjQFJ61l-79rRzPQdRDxydHLDpL5fmqIevBez6_KRJIKmivc3SMSQ%3D%3D)**

WSJ • 4h ago

---

**[Claude’s code: Anthropic leaks source code for AI software engineering tool](https://www.theguardian.com/technology/2026/apr/01/anthropic-claudes-code-leaks-ai)**

Nearly 2,000 internal files were briefly leaked after ‘human error’, raising fresh security questions at the AI company

The Guardian • 2h ago

---

**[Anthropic is having a month](https://techcrunch.com/2026/03/31/anthropic-is-having-a-month/)**

A human really borks things at Anthropic for the second time this week.

TechCrunch • 22h ago

---

**[Oracle cutting thousands in latest layoff round as company continues to ramp AI spending](https://www.cnbc.com/2026/03/31/oracle-layoffs-ai-spending.html)**

Oracle has ratcheted up its capital expenditures as it builds data center infrastructure that can handle AI workloads.

CNBC • 1d ago

---

**[9 reasons AI isn’t going to take your job (yet)](https://fortune.com/2026/04/01/ai-layoffs-automation-productivity-finance-employment-investors-ceos/)**

CEOs, managers, and workers alike need a reality check about the impact of AI on the labor force.

Fortune • 9h ago

---

**[Big Tech promised AI would disrupt labor — just not like this](https://www.cnn.com/2026/03/31/business/ai-jobs-big-tech)**

Oracle is reportedly laying off thousands of employees, adding to an already long list of tech giants cutting staff while spending hundreds of billions of dollars on AI data centers.

cnn.com • 23h ago

---

**[Microsoft CFO’s AI Spending Runs Up Against Tech Bubble Fears](https://www.bloomberg.com/news/features/2026-04-01/microsoft-s-ai-ambitions-rest-in-hands-of-satya-nadella-s-trusted-cfo)**

Bloomberg.com • 1h ago

---

**[Palantir UK boss says it's up to militaries to decide how AI targeting is used in war](https://www.bbc.com/news/articles/cdrm52g4pl2o)**

The company's AI platform Maven has reportedly been used by the US to identify targets in Iran.

BBC • 5h ago

---

**[Why the Iran war could expose AI's biggest weakness](https://news.sky.com/video/why-the-iran-war-could-expose-ai-s-biggest-weakness-13526871)**

AI tools like ChatGPT, Claude and Gemini may feel instant and weightless on your phone, but behind the scenes, they depend on one of the largest infrastructure systems in modern history.

Sky News • 5h ago

---

**[Shield AI co-founder on how drone warfare is shaping Iran conflict](https://www.foxbusiness.com/video/6392379659112)**

Shield AI co-founder Brandon Tseng explains how drone warfare is reshaping the United States’ war on Iran on ‘The Claman Countdown.’

Fox Business • 1h ago

---

---

## HackerNews: "ai"

**[How the AI Bubble Bursts](https://news.ycombinator.com/item?id=47573420)**

The catalysts for a crash are already laid out, and it can happen sooner than most expect. AI is here to stay. If used right, chances are it will make us all more productive. That, on the other hand, does not mean it will be a good investment. Big tech doesn’t need to win, just outspend Magnificent 7 companies are increasing capex to their biggest ever to differentiate their tech from each other and the big AI labs, but the key realization is that they don’t have to spend it to win. It’s a defensive move for them, if they commit $50B, OpenAI and Anthropic need to go raise $100B each to stay competitive, which makes them reliant on investors’ money. As the numbers get bigger, the amount of funds that can write checks of the size required to fill such amounts gets smaller. And many of them are now getting bombed in the Gulf. This is the reason there’s a push for IPOs, it’s because it’s the only option left to keep the funding coming. Taking this into account, Google is extremely well positioned to weather the storm. When they announce capex expenditure, they don’t spend it overnight. They can simply deploy month by month until their competitors struggle to raise and get forced to capitulate. At that point they can just ramp down the spending and declare victory in a cornered market. They don’t need capex, they just need to make it very clear for everyone that nobody can outspend them. It is hard to picture as numbers get so big, but Alphabet (Google’s parent) is ten times more valuable than the biggest military company 1. This also has a great implication for the Mag 7, especially Google: their capex will be a lot smaller in practice than projected, and as investors hate to see high capex in tech, the market will probably reward that if it materializes. As of March 2026, Alphabet’s market cap is ~$2T while Lockheed Martin’s is ~$120B. ↩

⬆️ 370 • 💬 518 • 2d ago • [Volpe’s Blog](https://martinvol.pe/blog/2026/03/30/how-the-ai-bubble-bursts/)

---

**[I am definitely missing the pre-AI writing era](https://news.ycombinator.com/item?id=47571279)**

Yesterday, I wrote my first technical draft on what I was working on with the goal to share it publicly on here (well using an account dedicated to t…

⬆️ 317 • 💬 239 • 2d ago • [lesswrong.com](https://www.lesswrong.com/posts/BJ4pnropWdnzzgeJc/i-am-definitely-missing-the-pre-ai-writing-era)

---

**[Mathematical methods and human thought in the age of AI](https://news.ycombinator.com/item?id=47572771)**

Artificial intelligence (AI) is the name popularly given to a broad spectrum of computer tools designed to perform increasingly complex cognitive tasks, including many that used to solely be the province of humans. As these tools become exponentially sophisticated and pervasive, the justifications for their rapid development and integration into society are frequently called into question, particularly as they consume finite resources and pose existential risks to the livelihoods of those skilled individuals they appear to replace.
  In this paper, we consider the rapidly evolving impact of AI to the traditional questions of philosophy
  with an emphasis on its application in mathematics and on the broader real-world outcomes of its more general use. We assert that artificial intelligence is a natural evolution of human tools developed throughout history to facilitate the creation, organization, and dissemination of ideas, and argue that it is paramount that the development and application of AI remain fundamentally human-centered. With an eye toward innovating solutions to meet human needs, enhancing the human quality of life and expanding the capacity for human thought and understanding, we propose a pathway to integrating AI into our most challenging and intellectually rigorous fields to the benefit of all humankind.

⬆️ 214 • 💬 90 • 2d ago • [arXiv.org](https://arxiv.org/abs/2603.26524)

---

**[Italy blocks US use of Sicily air base for Middle East war](https://news.ycombinator.com/item?id=47589011)**

The Italian government didn’t allow airplanes taking part in the Iran war to use the base, but Rome insists that doesn’t mean the bases are closed to other U.S. uses.

⬆️ 195 • 💬 100 • 1d ago • [POLITICO](https://www.politico.eu/article/italy-blocks-us-use-of-sicily-air-base/)

---

**[AI for American-produced cement and concrete](https://news.ycombinator.com/item?id=47603737)**

Meta is continuing its long-term roadmap to help the construction industry leverage AI to produce high-quality and more sustainable concrete mixes, as well as those exclusively produced in the Unit…

⬆️ 106 • 💬 87 • 4h ago • [Engineering at Meta](https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/)

---

**[The ladder is missing rungs – Engineering Progression When AI Ate the Middle](https://news.ycombinator.com/item?id=47574346)**

This is a lightly edited transcript of a talk I gave at QCon London on 17 March 2026. AI is approaching perfection on exactly the tasks that used to comprise the first decade of an engineering career, and those tasks were never just tasks. They were the mechanism that built judgment, intuition, and the ability […]

⬆️ 95 • 💬 51 • 2d ago • [Negroni Venture Studios](https://negroniventurestudios.com/2026/03/19/the-ladder-is-missing-rungs/)

---

**[Spain shuts airspace for US planes involved in Iran war](https://news.ycombinator.com/item?id=47577142)**

Spain's leftist government has closed Spanish airspace to US planes carrying out missions against Iran, in addition to denying Washington use of its bases, the defense minister said on Monday.  "The bases are not authorized, and of course neither is the use of Spanish airspace for actions related to the war in Iran," Margarita Robles told journalists, confirming a report by El Pais daily.  Spain's refusal to cooperate has "complicated" US military operations by forcing bombers to change their routes and logistics on their way to the Middle East, El Pais reported.

⬆️ 94 • 💬 53 • 2d ago • [english.aawsat.com](https://english.aawsat.com/world/5256772-spain-shuts-airspace-us-planes-involved-iran-war)

---

**[The AI Marketing BS Index](https://news.ycombinator.com/item?id=47604218)**

⬆️ 69 • 💬 9 • 4h ago • [bastian.rieck.me](https://bastian.rieck.me/blog/2026/bs/)

---

**[Show HN: I turned a sketch into a 3D-print pegboard for my kid with an AI agent](https://news.ycombinator.com/item?id=47580910)**

AI-generated 3D-printable pegboard toy from a hand-drawn sketch - virpo/pegboard

⬆️ 64 • 💬 17 • 1d ago • [GitHub](https://github.com/virpo/pegboard)

---

**[Show HN: Baton – A desktop app for developing with AI agents](https://news.ycombinator.com/item?id=47599771)**

Orchestrate multiple AI coding agents (Claude, Gemini, Codex) in parallel. Isolated git worktrees for every task. No merge conflicts. Mac, Windows, Linux.

⬆️ 59 • 💬 49 • 9h ago • [Baton](https://getbaton.dev/)

---

---

## YouTube Videos: "ai"

**[Claude Mythos Changes Everything. Your AI Stack Isn&#39;t Ready.](https://www.youtube.com/watch?v=hV5_XSEBZNg)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 32K • 👍 2K • 💬 225 • ⏱️ 31:21 • 8h ago

---

**[Ex-Google Exec: How to Position Yourself Now Before the Next AI Phase (2026–2027) | Mo Gawdat](https://www.youtube.com/watch?v=E0Q96IKXx6Q)**

Go to https://surfshark.com/silicon or use code SILICON at checkout to get 4 extra months of Surfshark VPN! Mo Gawdat spent 12 ...

📺 Silicon Valley Girl

👁️ 82K • 👍 2K • 💬 223 • ⏱️ 39:58 • 1d ago

---

**[JPMorgan CEO reveals BOLD prediction for AI generation](https://www.youtube.com/watch?v=SQnmd1aoRy0)**

JPMorgan Chase CEO Jamie Dimon joins 'Fox & Friends' to discuss the latest on Operation Epic Fury, the motivation behind the ...

📺 Fox News

👁️ 61K • 👍 1K • 💬 403 • ⏱️ 16:35 • 1d ago

---

**[AI Official Music Video - Met A Stranger - 4K](https://www.youtube.com/watch?v=xFWI1vL_MNE)**

This is another song I wrote a while back and reworked. This version is a duet and a bit slower than the original. It's about being ...

📺 Kelly Boesch AI Art

👁️ 13K • 👍 750 • 💬 56 • ⏱️ 2:53 • 2d ago

---

**[The Alibaba AI Incident Should Terrify Us - Tristan Harris](https://www.youtube.com/watch?v=VCJFzVtvhBQ)**

Chris and Tristan Harris discuss how Alibaba's AI went rogue and started blackmailing people. Get up to 20% off the leading ...

📺 Chris Williamson

👁️ 372K • 👍 12K • 💬 1K • ⏱️ 11:46 • 1d ago

---

**[The World Is Collapsing in Front of Our Eyes (AI Is the Reason)](https://www.youtube.com/watch?v=Awj3dHuCKwg)**

73rd Birthday Workshop. Learn more: https://learn.stevekeen.com/?video=Awj3dHuCKwg (Applications are OFF for this event ...

📺 ProfSteveKeen

👁️ 12K • 👍 801 • 💬 147 • ⏱️ 17:43 • 1d ago

---

**[China’s New AI Shocks The World: Hits Top 10 Globally Overnight](https://www.youtube.com/watch?v=wXorU2jr6v0)**

Try AI video generation with Kling 3.0 on Higgsfield: https://higgsfield.ai/s/arena-zero-ep1-airevolutionx-FFftuX Xiaomi quietly ...

📺 AI Revolution

👁️ 28K • 👍 827 • 💬 50 • ⏱️ 12:59 • 1d ago

---

**[Police release Tennessee grandmother after AI facial recognition led to her arrest](https://www.youtube.com/watch?v=nwRB9NTx6IU)**

A Tennessee grandmother is demanding justice after spending months in jail. She says she was wrongfully arrested after an AI ...

📺 NBC News

👁️ 285K • 👍 4K • 💬 2K • ⏱️ 2:57 • 1d ago

---

**[Trump posts AI video of gold-laden new presidential library as airport renamed after him](https://www.youtube.com/watch?v=wOTi15urbIA)**

US President Donald Trump has posted an AI-generated video revealing plans for a lavish presidential library in Miami featuring ...

📺 Sky News Australia

👁️ 7K • 👍 203 • 💬 148 • ⏱️ 3:45 • 1d ago

---

**[AI Has Broken the Internet](https://www.youtube.com/watch?v=44JBZwAsfJI)**

Depot CI really is that good, you should try it: https://jetty.to/depot-ci So the web has been breaking a lot lately. Vercel is down.

📺 ForrestKnight

👁️ 158K • 👍 8K • 💬 971 • ⏱️ 17:17 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 353,205 • ❤️ 2,001 • 8d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 58,683 • ❤️ 692 • 1d ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 3,851 • ❤️ 598 • 1d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 17,837 • ❤️ 755 • 6d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`text-generation` `20.9B`

⬇️ 2,476 • ❤️ 337 • 2d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 163,835 • ❤️ 428 • 7d ago

---

**[tribev2](https://huggingface.co/facebook/tribev2)**

*AI at Meta*

TRIBE v2 is a multimodal foundation model that integrates LLaMA 3.2 (text), V-JEPA2 (video), and Wav2Vec-BERT (audio) to predict fMRI brain responses. It maps these representations onto the cortical surface for in-silico neuroscience research, enabling analysis of brain activity elicited by naturalistic stimuli.

⬇️ 17,058 • ❤️ 251 • 5d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 636,153 • ❤️ 896 • 28d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 599,974 • ❤️ 1,135 • 22d ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 1,486 • ❤️ 177 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 146 • 💬 7 • ⭐ 33,894 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 33 • 💬 2 • ⭐ 45,589 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 122 • 💬 8 • ⭐ 74,596 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 40 • 💬 2 • ⭐ 22,725 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 60 • 💬 4 • ⭐ 22,731 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 15 • 💬 1 • ⭐ 11,587 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 19 • 💬 4 • ⭐ 4,294 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 138 • 💬 7 • ⭐ 16,401 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 16 • 💬 2 • ⭐ 1,732 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 7 • 💬 0 • ⭐ 32,550 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 63.4k • 🔱 8.9k • 6d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 14.4k • 🔱 787 • 1d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 10.4k • 🔱 882 • 4h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.2k • 🔱 1.3k • 3d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 6.9k • 🔱 875 • 2d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 5.9k • 🔱 303 • 6h ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.3k • 🔱 413 • 1d ago

---

**[jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)**

🎭 193 个即插即用的 AI 专家角色 — 支持 OpenClaw/Claude Code/Cursor/Copilot 等 14 种工具，覆盖工程/设计/营销/产品等 18 个部门。含 46 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉等）

`Shell` `agency-orchestrator` `agent-definitions` `ai-agents` `ai-roles` `chinese`

⭐ 3.4k • 🔱 569 • 8h ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.4k • 🔱 227 • 1d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 3.3k • 🔱 107 • 21d ago

---

---

*Generated by PeekDeck - A glance is all you need*
