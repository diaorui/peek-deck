---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-02T18:08:10.767610+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 02, 2026 at 18:08 UTC  
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

**[List up Fav Multi AI AI Open Source Projects](https://www.reddit.com/r/artificial/comments/1sabr5t/list_up_fav_multi_ai_ai_open_source_projects/)**

As the toual says and why. So many out there whats ur go to.

9h ago

---

**[The Claude Code leak accidentally published the first complete blueprint for production AI agents. Here's what it tells us about where this is all going.](https://www.reddit.com/r/artificial/comments/1s9jprb/the_claude_code_leak_accidentally_published_the/)**

Most coverage of the Claude Code leak focuses on the drama or the hidden features. But the bigger story is that this is the first time we've seen the complete architecture of a production-grade AI agent system running at scale ($2.5B ARR, 80% enterprise adoption). And the patterns it reveals tell us where autonomous AI agents are actually heading. What the architecture confirms: AI agents aren't getting smarter just from better models. The real progress is in the orchestration layer around the model. Claude Code's leaked source shows six systems working together: Skeptical memory. Three-layer system where the agent treats its own memory as a hint, not a fact. It verifies against the real world before acting. This is how you prevent an agent from confidently doing the wrong thing based on outdated information. Background consolidation. A system called autoDream runs during idle time to merge observations, remove contradictions, and keep memory bounded. Without this, agents degrade over weeks as their memory fills with noise and conflicting notes. Multi-agent coordination. One lead agent spawns parallel workers. They share a prompt cache so the cost doesn't multiply linearly. Each worker gets isolated context and restricted tool access. Risk classification. Every action gets labeled LOW, MEDIUM, or HIGH risk. Low-risk actions auto-approve. High-risk ones require human approval. The agent knows which actions are safe to take alone. CLAUDE.md reinsertion. The config file isn't a one-time primer. It gets reinserted on every turn. The agent is constantly reminded of its instructions. KAIROS daemon mode. The biggest unreleased feature (150+ references in the source). An always-on background agent that acts proactively, maintains daily logs, and has a 15-second blocking budget so it doesn't overwhelm the user. What this tells us about the future: AI tools are moving from "you ask, it responds" to "it works when you're not looking." KAIROS isn't a gimmick. It's the natural next step: agents that plan, act, verify, and consolidate their own memory autonomously. With human gates on dangerous actions and rate limits on proactive behavior. The patterns are convergent. I've been building my own AI agent independently for months. Scheduled autonomous work, memory consolidation, multi-agent delegation, risk tiers. I arrived at the same architecture without seeing Anthropic's code. Multiple independent builders keep converging on the same design because the constraints demand it. The part people are overlooking: Claude Code itself isn't even a good tool by benchmark standards. It ranks 39th on terminal bench. The harness adds nothing to the model's performance. The value is in the architecture patterns, not the implementation. This leak is basically a free textbook on production AI agent design from a $60B company. The drama fades. The patterns are permanent. Full technical breakdown with what I built from it: https://thoughts.jock.pl/p/claude-code-source-leak-what-to-learn-ai-agents-2026

1d ago

---

**[Building an AI agent that finds repos and content relevant to my work](https://www.reddit.com/r/artificial/comments/1sa8xt3/building_an_ai_agent_that_finds_repos_and_content/)**

I kept missing interesting stuff on HuggingFace, arXiv, Substack etc., so I made an agent that sends a weekly summary of only what’s relevant, for free Any thoughts on the idea?

12h ago

---

**[Google has published its new open-weight model Gemma 4. And made it commercially available under Apache 2.0 License](https://www.reddit.com/r/artificial/comments/1sann00/google_has_published_its_new_openweight_model/)**

The model is also available here: 🤗 HuggingFace: https://huggingface.co/collections/google/gemma-4 🦙 Ollama: https://ollama.com/library/gemma4

🔗 [Google](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) • 47m ago

---

**[AI Tools That Can’t Prove What They Did Will Hit a Wall](https://www.reddit.com/r/artificial/comments/1sakjzg/ai_tools_that_cant_prove_what_they_did_will_hit_a/)**

Most AI products are still judged like answer machines. People ask whether the model is smart, fast, creative, cheap, or good at sounding human. Teams compare outputs, benchmark quality, and argue about hallucinations. That makes sense when the product is mainly being used for writing, search, summarisation, or brainstorming. It breaks down once AI starts doing real operational work. The question stops being what the system output. The real question becomes whether you can trust what it did, why it did it, whether it stayed inside the rules, and whether you can prove any of that after the fact. That shift matters more than people think. I do not think it stays a feature. I think it creates a new product category. A lot of current AI products still hide the middle layer. You give them a prompt and they give you a result, but the actual execution path is mostly opaque. You do not get much visibility into what tools were used, what actions were taken, what data was touched, what permissions were active, what failed, or what had to be retried. You just get the polished surface. For low-stakes use, people tolerate that. For internal operations, customer-facing automation, regulated work, multi-step agents, and systems that can actually act on the world, it becomes a trust problem very quickly. At that point output quality is still important, but it is no longer enough. A system can produce a good result and still be operationally unsafe, uninspectable, or impossible to govern. That is why I think trustworthiness has to become a product surface, not a marketing claim. Right now a lot of products try to borrow trust from brand, model prestige, policy language, or vague “enterprise-ready” positioning. But trust is not created by a PDF, a security page, or a model name. Trust becomes real when it is embedded into the product itself. You can see it in approvals. You can see it in audit trails. You can see it in run history, incident handling, permission boundaries, failure visibility, and execution evidence. If those surfaces do not exist, then the product is still mostly asking the operator to believe it. That is not the same thing as earning trust. The missing concept here is the control layer. A control layer sits between model capability and real-world action. It decides what the system is allowed to do, what requires approval, what gets logged, how failures surface, how policy is enforced, and what evidence is collected. It is the layer that turns raw model capability into something operationally governable. Without that layer, you mostly have intelligence with a nice interface. With it, you start getting something much closer to a trustworthy system. That is also why proof-driven systems matter. An output-driven system tells you something happened. A proof-driven system shows you that it happened, how it happened, and whether it happened correctly. It can show what task ran, what tools were used, what data was touched, what approvals happened, what got blocked, what failed, what recovered, and what proof supports the final result. That difference sounds subtle until you are the one accountable for the outcome. If you are using AI for anything serious, “it said it did the work” is not the same thing as “the work can be verified.” Output is presentation. Proof is operational trust. I think this changes buying criteria in a big way. The next wave of buyers will increasingly care about questions like these: can operators see what is going on, can actions be reviewed, can failures be surfaced and remediated, can the system be governed, can execution be proven to internal teams, customers, or regulators, and can someone supervise the system without reading code or guessing from outputs. Once those questions become central, the product is no longer being judged like a chatbot or assistant. It is being judged like a trust system. That is why I think this becomes a category, not just a feature request. One side of the market will stay output-first. Fast, impressive, consumer-friendly, and mostly opaque. The other side will become trust-first. Controlled, inspectable, evidence-backed, and usable in real operations. That second side is where the new category forms. You can already see the pressure building in agent frameworks and orchestration-heavy systems. The more capable these systems become, the less acceptable it is for them to operate as black boxes. Once a system can actually do things instead of just suggest things, people start asking for control, evidence, and runtime truth. That is why I think the winners in this space will not just be the companies that build more capable models. They will be the ones that build AI systems people can actually trust to operate. The next wave of AI products will not be defined by who can generate the most. It will be defined by who can make AI trustworthy enough to supervise, govern, and prove in the real world. Once AI moves from assistant to actor, trust stops being optional. It becomes the product.

2h ago

---

**[Chatgpt vs purpose built ai for cre underwriting: which one can finish the job?](https://www.reddit.com/r/artificial/comments/1sacme5/chatgpt_vs_purpose_built_ai_for_cre_underwriting/)**

I keep seeing people recommend chatgpt for financial modeling and I need to push back because I spent a month testing it for multifamily underwriting and the results were not close to usable. Pasting rent rolls, T12s, operating statements and asking it to build models, you get fragments. A few formulas, a cash flow table, maybe a cap rate calculation. Nothing ties together into a workbook you could hand to an investment committee. Fifteen rounds of prompting later and you've spent the same time you would have just building it in excel, except now you also have to debug whatever chatgpt hallucinated in cell D47. Problem with chatgpt is that it doesn't maintain state across a complex multi-step task. It treats each prompt like a fresh conversation even in the same thread. An underwriting model where assumptions feed cash flows which feed returns which feed sensitivities requires coherence across all those layers and it fragments. Purpose-built tools are architecturally different. They decompose the task, run autonomously for 15 to 30 minutes, check intermediate outputs, return a complete workbook with actual excel formulas. That's not a model quality difference, that's a design philosophy difference. Chatgpt for quick questions and brainstorming, yes. For anything where the output IS the deliverable, no. Different architecture for different jobs.

8h ago

---

**[Is there something I can do about my prompts? [Long read, I’m sorry]](https://www.reddit.com/r/artificial/comments/1sakiaa/is_there_something_i_can_do_about_my_prompts_long/)**

Hello everyone, this will be a bit of a long read, i have a lot of context to provide so i can paint the full picture of what I’m asking, but i’ll be as concise as possible. i want to start this off by saying that I’m not an AI coder or engineer, or technician, whatever you call yourselves, point is I’m don’t use AI for work or coding or pretty much anything I’ve seen in the couple of subreddits I’ve been scrolling through so far today. Idk anything about LLMs or any of the other technical terms and jargon that i seen get thrown around a lot, but i feel like i could get insight from asking you all about this. So i use DeepSeek primarily, and i use all the other apps (ChatGPT, Gemini, Grok, CoPilot, Claude, Perplexity) for prompt enhancement, and just to see what other results i could get for my prompts. Okay so pretty much the rest here is the extensive context part until i get to my question. So i have this Marvel OC superhero i created. It’s all just 3 documents (i have all 3 saved as both a .pdf and a .txt file). A Profile Doc (about 56 KB-gives names, powers, weaknesses, teams and more), A Comics Doc (about 130 KB-details his 21 comics that I’ve written for him with info like their plots as well as main cover and variant cover concepts. 18 issue series, and 3 separate “one-shot” comics), and a Timeline Document (about 20 KB-Timline starting from the time his powers awakens, establishes the release year of his comics and what other comic runs he’s in [like Avengers, X-Men, other character solo series he appears in], and it maps out information like when his powers develop, when he meets this person, join this team, etc.). Everything in all 3 docs are perfect laid out. Literally everything is organized and numbered or bulleted in some way, so it’s all easy to read. It’s not like these are big run on sentences just slapped together. So i use these 3 documents for 2 prompts. Well, i say 2 but…let me explain. There are 2, but they’re more like, the foundation to a series of prompts. So the first prompt, the whole reason i even made this hero in the first place mind you, is that i upload the 3 docs, and i ask “How would the events of Avengers Vol. 5 #1-3 or Uncanny X-Men #450 play out with this person in the story?” For a little further clarity, the timeline lists issues, some individually and some grouped together, so I’m not literally asking “_ comic or _ comic”, anyways that starting question is the main question, the overarching task if you will. The prompt breaks down into 3 sections. The first section is an intro basically. It’s a 15-30 sentence long breakdown of my hero at the start of the story, “as of the opening page of x” as i put it. It goes over his age, powers, teams, relationships, stage of development, and a couple other things. The point of doing this is so the AI basically states the corrects facts to itself initially, and not mess things up during the second section. For Section 2, i send the AI’s a summary that I’ve written of the comics. It’s to repeat that verbatim, then give me the integration. Section 3 is kind of a recap. It’s just a breakdown of the differences between the 616 (Main Marvel continuity for those who don’t know) story and the integration. It also goes over how the events of the story affects his relationships. Now for the “foundations” part. So, the way the hero’s story is set up, his first 18 issues happen, and after those is when he joins other teams and is in other people comics. So basically, the first of these prompts starts with the first X-Men issue he joins in 2003, then i have a list of these that go though the timeline. It’s the same prompt, just different comic names and plot details, so I’m feeding the AIs these prompts back to back. Now the problem I’m having is really only in Section 1. It’ll get things wrong like his age, what powers he has at different points, what teams is he on. Stuff like that, when it all it has to do is read the timeline doc up the given comic, because everything needed for Section 1 is provided in that one document. Now the second prompt is the bigger one. So i still use the 3 docs, but here’s a differentiator. For this prompt, i use a different Comics Doc. It has all the same info, but also adds a lot more. So i created this fictional backstory about how and why Marvel created the character and a whole bunch of release logistics because i have it set up to where Issue #1 releases as a surprise release. And to be consistent (idek if this info is important or not), this version of the Comics Doc comes out to about 163 KB vs the originals 130. So im asking the AIs “What would it be like if on Saturday, June 1st, 2001 [Comic Name Here] Vol. 1 #1 was released as a real 616 comic?” And it goes through a whopping 6 sections. Section 1 is a reception of the issue and seasonal and cultural context breakdown, Section 2 goes over the comic plot page by page and give real time fan reactions as they’re reading it for the first time. Section 3 goes over sales numbers, Section 4 goes over Mavrel’s post release actions, their internal and creative adjustments, and their mood following the release. Section 5 goes over fan discourse basically. Section 6 is basically the DC version of Section 4, but in addition to what was listed it also goes over how they’re generally sizing up and assessing the release. My problem here is essentially the same thing. Messing up information. Now here it’s a bit more intricate. Both prompts have directives as far as sentence count, making sure to answer the question completely, and stuff like that. But this prompt, each section is 2-5 questions. On top of that, these prompts have way, way more additional directives because it the release is a surprise release. And there more factors that play in. Pricing, the fact of his suit and logo not being revealed until issue #18, the fact that the 18 issues are completed beforehand, and few more stuff. Like, this comic and the series as whole is set to be released a very particular type of way and the AIs don’t account for that properly, so all these like Meta-level directives and things like that. But it’ll still get information wrong, gives “the audience” insight and knowledge about the comics they shouldn’t have and things like that. So basically i want to know what can i do to fix these problems, if i can. Like, are my documents too big? Are my prompts (specifically the second one) asking too much? For the second, I can’t break the prompts down and send them broken up because that messes up the flow as when I’m going through all the way to 18, asking these same questions, they build on each other. These questions ask specifically how decisions from previous issues panned out, how have past releases affected this factor, that factor, so yeah breaking up the same prompt and sending it in multiple messages messes all that up. It’s pretty much the same concept for the first but it’s not as intricate and interconnected to each other. That aside, i don’t think breaking down 1 message of 3 sections into 3 messages would work well with the flow I’m building there either way. So yeah, any tips would be GREATLY appreciated. I have tried the “ask me questions before you start” hack, that smoothes things a bit. Doing the “you’re a….” Doesn’t really help too much, and pretty much everything else I’ve seen i can’t really apply here. So i apologize for the long read, and i also apologize if this post shouldn’t be here and doesn’t fit for some reason. I just want some help

2h ago

---

**[Microsoft’s new ‘superintelligence’ game plan is all about business](https://www.reddit.com/r/artificial/comments/1sajhlk/microsofts_new_superintelligence_game_plan_is_all/)**

Its new transcription model is a step toward those goals, says Microsoft AI’s Mustafa Suleyman.

🔗 [The Verge](https://www.theverge.com/report/905791/mustafa-suleyman-microsoft-ai-transcription-model) • 3h ago

---

**[I am doing a multi-model graph database in pure Rust with Cypher, SQL, Gremlin, and native GNN looking for extreme speed and performance](https://www.reddit.com/r/artificial/comments/1sae4r1/i_am_doing_a_multimodel_graph_database_in_pure/)**

Hi guys, I'm a PhD student in Applied AI and I've been building an embeddable graph database engine from scratch in Rust. I'd love feedback from people who actually work with graph databases daily. I got frustrated with the tradeoffs: Neo4j is mature but JVM-heavy and single-model. ArcadeDB is multi-model but slow on graph algorithms. Vector databases like Milvus handle embeddings but have zero graph awareness. I wanted one engine that does all three natively. So I would like if someone could give me feedback or points to improve it, I am very open mind for whatever opinion I was working several months with my university professors and I decided to publish the code yesterday night because I guessed its more or less reddit to try it. The repo is: https://github.com/DioCrafts/BikoDB Guys, as I told you, whatever feedback is more than welcome. PD: Obviously is open source project. Cheers!

7h ago

---

**[Automate IOS devices through XCUITest with droidrun.](https://www.reddit.com/r/artificial/comments/1saipox/automate_ios_devices_through_xcuitest_with/)**

Automate iOS apps with XCUITest and Droidrun using just natural language. You send the command to Droidrun, and the agent starts the task and executes it autonomously. GitHub repo: https://github.com/droidrun/droidrun

3h ago

---

---

## Google News: "ai"

**[How A.I. Helped One Man (and His Brother) Build a $1.8 Billion Company](https://www.nytimes.com/2026/04/02/technology/ai-billion-dollar-company-medvi.html)**

The New York Times • 9h ago

---

**[Twin cybersecurity incidents leave AI industry shaken](https://finance.yahoo.com/sectors/technology/article/twin-cybersecurity-incidents-leave-ai-industry-shaken-141850823.html)**

The AI industry is dealing with the fallout from two security incidents this week that exposed customer data at Mercor and source code at Anthropic.

Yahoo Finance • 3h ago

---

**[India AI Startup Sarvam Raises Funds at $1.5 Billion Valuation](https://www.bloomberg.com/news/articles/2026-04-02/india-ai-startup-sarvam-raises-funds-at-1-5-billion-valuation?srnd=homepage-americas)**

Bloomberg.com • 55m ago

---

**[Microsoft building its own high-powered AI models as it looks to slash dependence on OpenAI](https://finance.yahoo.com/sectors/technology/article/microsoft-building-its-own-high-powered-ai-models-as-it-looks-to-slash-dependence-on-openai-160053651.html)**

Microsoft says it's on a path to developing high-powered frontier models, an acknowledgment that it is looking to wean itself off of its dependence on partner models from OpenAI.

Yahoo Finance • 2h ago

---

**[Microsoft takes on AI rivals with three new foundational models](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)**

MAI released models that can transcribe voice into text as well as generate audio and images after the group's formation six months ago.

TechCrunch • 1h ago

---

**[Microsoft launches 3 new AI models in direct shot at OpenAI and Google](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)**

Microsoft launches three in-house AI models for transcription, voice, and image generation, challenging OpenAI and Google with lower-cost systems.

VentureBeat • 7h ago

---

**[Jack Dorsey and Roelof Botha think AI can make middle management obsolete](https://fortune.com/2026/04/02/jack-dorsey-roelof-botha-ai-middle-management/)**

The Silicon Valley execs want companies to function as a "mini-artificial general intelligence,” and leave traditional corporate hierarchy behind.

Fortune • 1h ago

---

**[Young People Are Falling Behind, but Not Because of AI](https://www.theatlantic.com/economy/2026/04/job-market-artificial-intelligence/686659/)**

The case that AI is already stealing young people’s jobs is based on a statistical mirage.

The Atlantic • 7h ago

---

**[Oracle cutting thousands in latest layoff round as company continues to ramp AI spending](https://www.cnbc.com/2026/03/31/oracle-layoffs-ai-spending.html)**

Oracle has ratcheted up its capital expenditures as it builds data center infrastructure that can handle AI workloads.

CNBC • 2d ago

---

**[Layoff plans ticked up last month, with employers citing AI](https://finance.yahoo.com/economy/article/layoff-plans-ticked-up-last-month-with-employers-citing-ai-115205398.html)**

Layoff plans rose in March from a month earlier as employers leaned on AI, according to a new report from the global outplacement firm Challenger, Gray & Christmas.

Yahoo Finance • 5h ago

---

---

## HackerNews: "ai"

**[AI for American-produced cement and concrete](https://news.ycombinator.com/item?id=47603737)**

Meta is continuing its long-term roadmap to help the construction industry leverage AI to produce high-quality and more sustainable concrete mixes, as well as those exclusively produced in the Unit…

⬆️ 214 • 💬 115 • 1d ago • [Engineering at Meta](https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/)

---

**[Italy blocks US use of Sicily air base for Middle East war](https://news.ycombinator.com/item?id=47589011)**

The Italian government didn’t allow airplanes taking part in the Iran war to use the base, but Rome insists that doesn’t mean the bases are closed to other U.S. uses.

⬆️ 198 • 💬 104 • 2d ago • [POLITICO](https://www.politico.eu/article/italy-blocks-us-use-of-sicily-air-base/)

---

**[The AI Marketing BS Index](https://news.ycombinator.com/item?id=47604218)**

⬆️ 103 • 💬 22 • 1d ago • [bastian.rieck.me](https://bastian.rieck.me/blog/2026/bs/)

---

**[ZomboCom stolen by a hacker, sold, now replaced with AI-generated makeover](https://news.ycombinator.com/item?id=47608155)**

⬆️ 72 • 💬 34 • 18h ago • [old.reddit.com](https://old.reddit.com/r/oldinternet/comments/1raiz8v/zombocom_was_stolen_by_hacker_put_up_for_sale_and/)

---

**[Show HN: I turned a sketch into a 3D-print pegboard for my kid with an AI agent](https://news.ycombinator.com/item?id=47580910)**

AI-generated 3D-printable pegboard toy from a hand-drawn sketch - virpo/pegboard

⬆️ 64 • 💬 17 • 2d ago • [GitHub](https://github.com/virpo/pegboard)

---

**[Show HN: Baton – A desktop app for developing with AI agents](https://news.ycombinator.com/item?id=47599771)**

Orchestrate multiple AI coding agents (Claude, Gemini, Codex) in parallel. Isolated git worktrees for every task. No merge conflicts. Mac, Windows, Linux.

⬆️ 61 • 💬 52 • 1d ago • [Baton](https://getbaton.dev/)

---

**[AI has suddenly become more useful to open-source developers](https://news.ycombinator.com/item?id=47601107)**

More open-source developers are finding that, when used properly, AI can actually help current and long-neglected programs. However, legal and quality issues loom.

⬆️ 53 • 💬 46 • 1d ago • [ZDNET](https://www.zdnet.com/article/maybe-open-source-needs-ai/)

---

**[CEO of largest public hospital says he's ready to replace radiologists with AI](https://news.ycombinator.com/item?id=47600244)**

Mitchell H. Katz, MD, president and CEO of NYC Health + Hospitals, recently spoke during a panel discussion held by Crain’s New York Business.

⬆️ 44 • 💬 110 • 1d ago • [Radiology Business](https://radiologybusiness.com/topics/artificial-intelligence/ceo-americas-largest-public-hospital-system-says-hes-ready-replace-radiologists-ai)

---

**[I built a 516-panel financial terminal in 3 weeks using AI](https://news.ycombinator.com/item?id=47596654)**

Professional-grade financial terminal with AI-powered news analysis and real-time market data.

⬆️ 44 • 💬 41 • 1d ago • [neuberg.ai](https://neuberg.ai/)

---

**[Men are ditching TV for YouTube as AI usage and social media fatigue grow](https://news.ycombinator.com/item?id=47612127)**

⬆️ 42 • 💬 110 • 8h ago • [ofcom.org.uk](https://www.ofcom.org.uk/media-use-and-attitudes/media-habits-adults/passive-social-media-use-ai-companionship-and-online-side-hustles-uk-adults-media-and-online-lives-revealed)

---

---

## YouTube Videos: "ai"

**[The Alibaba AI Incident Should Terrify Us - Tristan Harris](https://www.youtube.com/watch?v=VCJFzVtvhBQ)**

Chris and Tristan Harris discuss how Alibaba's AI went rogue and started blackmailing people. Get up to 20% off the leading ...

📺 Chris Williamson

👁️ 432K • 👍 13K • 💬 2K • ⏱️ 11:46 • 2d ago

---

**[Ex-Google Exec: How to Position Yourself Now Before the Next AI Phase (2026–2027) | Mo Gawdat](https://www.youtube.com/watch?v=E0Q96IKXx6Q)**

Go to https://surfshark.com/silicon or use code SILICON at checkout to get 4 extra months of Surfshark VPN! Mo Gawdat spent 12 ...

📺 Silicon Valley Girl

👁️ 120K • 👍 3K • 💬 274 • ⏱️ 39:58 • 2d ago

---

**[JPMorgan CEO reveals BOLD prediction for AI generation](https://www.youtube.com/watch?v=SQnmd1aoRy0)**

JPMorgan Chase CEO Jamie Dimon joins 'Fox & Friends' to discuss the latest on Operation Epic Fury, the motivation behind the ...

📺 Fox News

👁️ 68K • 👍 1K • 💬 422 • ⏱️ 16:35 • 1d ago

---

**[Oracle Begins 30,000 Layoffs to Fund AI Buildout - Investors Fleeing Sinking Ship](https://www.youtube.com/watch?v=25vjF_ljLns)**

RSVP for In Person Classes at -- https://www.SiliconDojo.com Support Content at - https://donorbox.org/etcg LinkedIn at ...

📺 Eli the Computer Guy

👁️ 7K • 👍 423 • 💬 118 • ⏱️ 14:04 • 21h ago

---

**[AI Blamed Heavily For March Layoffs, Report Says](https://www.youtube.com/watch?v=6LRbOk5n1KI)**

A singular reason has been blamed more than any other for companies cutting 60000 jobs in March of this year, career services ...

📺 Forbes Breaking News

👁️ 841 • 👍 11 • 💬 5 • ⏱️ 2:24 • 3h ago

---

**[Claude Mythos Changes Everything. Your AI Stack Isn&#39;t Ready.](https://www.youtube.com/watch?v=hV5_XSEBZNg)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 90K • 👍 3K • 💬 362 • ⏱️ 31:21 • 1d ago

---

**[Google’s New AI Just Broke My Brain](https://www.youtube.com/watch?v=7YVrb3-ABYE)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The TurboQuant paper is available here: ...

📺 Two Minute Papers

👁️ 108K • 👍 8K • 💬 823 • ⏱️ 8:34 • 1d ago

---

**[The AI Insider Giving Humanity 50/50 Odds (And What Tips the Scale) | Emad Mostaque](https://www.youtube.com/watch?v=tMBXbN6ZiKc)**

Emad Mostaque joins me to explore one of the most confronting questions of our time: what happens when human intelligence is ...

📺 André Duqum

👁️ 45K • 👍 1K • 💬 274 • ⏱️ 2:26:43 • 2d ago

---

**[Your iPhone Is About to Control Every AI App You Use. Here&#39;s What This Means For You.](https://www.youtube.com/watch?v=BhXNtvZvziY)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 64K • 👍 2K • 💬 271 • ⏱️ 22:12 • 2d ago

---

**[AI BUSINESS SUMMIT 2026 - DAY 2](https://www.youtube.com/watch?v=41sJkyS8Vtc)**

TODAY. IS. THE. DAY. Our Most Awaited Ai Business Summit starts TODAY at 12pm EST! I know you've been counting ...

📺 Alicia Lyttle

👁️ 5K • 👍 348 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 428,791 • ❤️ 2,113 • 9d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 71,028 • ❤️ 724 • 1h ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 4,316 • ❤️ 624 • 2d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 19,085 • ❤️ 808 • 7d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`text-generation` `20.9B`

⬇️ 2,820 • ❤️ 352 • 3d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 202,605 • ❤️ 462 • 8d ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 13,844 • ❤️ 292 • 2d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 674,007 • ❤️ 914 • 29d ago

---

**[tribev2](https://huggingface.co/facebook/tribev2)**

*AI at Meta*

TRIBE v2 is a multimodal foundation model that integrates LLaMA 3.2 (text), V-JEPA2 (video), and Wav2Vec-BERT (audio) to predict fMRI brain responses. It maps these representations onto the cortical surface for in-silico neuroscience research, enabling analysis of brain activity elicited by naturalistic stimuli.

⬇️ 25,665 • ❤️ 259 • 6d ago

---

**[LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M)**

*Liquid AI*

LFM2.5-350M is a 350M parameter text generation model optimized for on-device deployment, offering fast edge inference and competitive performance. It excels at data extraction, structured outputs, and tool use, supporting multiple languages and a context length of 32,768 tokens.

`text-generation` `354.5M`

⬇️ 7,703 • ❤️ 195 • 22h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 148 • 💬 7 • ⭐ 34,837 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 34 • 💬 2 • ⭐ 45,990 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 17 • 💬 1 • ⭐ 12,658 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 123 • 💬 8 • ⭐ 74,718 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 41 • 💬 2 • ⭐ 22,817 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 61 • 💬 4 • ⭐ 22,821 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 20 • 💬 4 • ⭐ 4,431 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 139 • 💬 7 • ⭐ 16,463 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 18 • 💬 2 • ⭐ 1,812 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild](https://huggingface.co/papers/2603.17187)**

*Peng Xia, Jianwen Chen, Xinyu Yang et al. (13 authors)*

🏢 University of North Carolina at Chapel Hill

A continual meta-learning framework for large language model agents that jointly evolves policies and reusable behavioral skills while minimizing downtime through opportunistic updates and skill-driven adaptation.

▲ 135 • 💬 4 • ⭐ 3,429 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2603.17187) • [💻 code](https://github.com/aiming-lab/MetaClaw)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 64.2k • 🔱 9.1k • 7d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 14.7k • 🔱 805 • 2d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 11.4k • 🔱 979 • 18m ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.3k • 🔱 1.3k • 4d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 7.1k • 🔱 923 • 3d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 6.2k • 🔱 335 • 2h ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.4k • 🔱 421 • 2d ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 4.3k • 🔱 1.4k • 7h ago

---

**[jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)**

🎭 193 个即插即用的 AI 专家角色 — 支持 OpenClaw/Claude Code/Cursor/Copilot 等 14 种工具，覆盖工程/设计/营销/产品等 18 个部门。含 46 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉等）

`Shell` `agency-orchestrator` `agent-definitions` `ai-agents` `ai-roles` `chinese`

⭐ 3.5k • 🔱 589 • 3h ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.4k • 🔱 228 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
