---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-28T23:45:18.751300+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 28, 2026 at 23:45 UTC  
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

**[Exclusive interview: Anthropic CEO Dario Amodei on Pentagon feud](https://www.reddit.com/r/artificial/comments/1rha87x/exclusive_interview_anthropic_ceo_dario_amodei_on/)**

Anthropic CEO Dario Amodei sat down with CBS News for an exclusive interview, hours after Defense Secretary Pete Hegseth declared the company a supply chain risk to national security, which restricts military contractors from doing business with the AI giant. Amodei called the move "retaliatory and punitive," and he said Anthropic sought to draw "red lines" in the government's use of its technology because "we believe that crossing those lines is contrary to American values, and we wanted to stand up for American values."

🔗 [youtu.be](https://youtu.be/MPTNHrq_4LU) • 5h ago

---

**[Anthropic says it will challenge Pentagon's supply chain risk designation in court](https://www.reddit.com/r/artificial/comments/1rgruzv/anthropic_says_it_will_challenge_pentagons_supply/)**

🔗 [reuters.com](https://www.reuters.com/world/us/anthropic-says-it-will-challenge-pentagons-supply-chain-risk-designation-court-2026-02-28/) • 20h ago

---

**[OpenAI strikes deal with Pentagon after Trump orders government to stop using Anthropic](https://www.reddit.com/r/artificial/comments/1rgtjex/openai_strikes_deal_with_pentagon_after_trump/)**

On X, Defense Secretary Pete Hegseth said he had moved to label Anthropic as a "supply chain risk" and cancel Defense business with the company.

🔗 [NBC News](https://www.nbcnews.com/tech/tech-news/trump-bans-anthropic-government-use-rcna261055) • 18h ago

---

**[Trump orders federal agencies to stop using Anthropic AI tech ‘immediately’](https://www.reddit.com/r/artificial/comments/1rgkegx/trump_orders_federal_agencies_to_stop_using/)**

Source CNBC President Donald Trump ordered U.S. government agencies to “immediately cease” using technology from the artificial intelligence company Anthropic. The AI startup faces pressure by the Defense Department to comply with demands that it can use the company’s technology without restrictions sought by Anthropic. The company wants the Pentagon to assure it that the AI models will not be used for fully autonomous weapons or mass domestic surveillance of Americans. Another major AI company, OpenAI, said it has the same “red lines” as Anthropic regarding the use of its technology by the Pentagon and other customers. The president also said there would be a six-month phase-out for agencies such as the Defense Department, which “are using Anthropic’s products, at various levels.”

1d ago

---

**[I built a tool to automate your workflow after recording yourself doing the task once (Open Source)](https://www.reddit.com/r/artificial/comments/1rhag6l/i_built_a_tool_to_automate_your_workflow_after/)**

Hey everyone, I have been building this on this side for a couple of months now and finally want to get some feedback. I initially tried using Zapier/n8n to automate parts of my job but I found it quite hard to learn and get started. I think that the reason a lot of people don't automate more of their work is because the setting up the automation takes too long and is prone to breaking. That's why I built Automated. By recording your workflow once, you can then run it anytime. The system uses AI so that it can adapt to website changes and conditional logic. Github (to self host): https://github.com/r-muresan/automated Link (use hosted version): https://useautomated.com Would appreciate any feedback at all. Thanks!

5h ago

---

**[How do you handle all these AI subscribtions?](https://www.reddit.com/r/artificial/comments/1rhbyyd/how_do_you_handle_all_these_ai_subscribtions/)**

how do you guys handle all these AI subscriptions? CLAUDE, ChatGpt, Gemini, Grok, Perplexity,Poe... they're all like $20/mo each do you just pick one? Or pay for 2 or more? Or use something that combines them.?...is it even worth paing for any of these? What's your setup?

4h ago

---

**[The Trends That Will Actually Matter in the Next Decade](https://www.reddit.com/r/artificial/comments/1rhgf7e/the_trends_that_will_actually_matter_in_the_next/)**

AI is only part of the story. Energy, demographics, resilience, and digital trust will reshape how we live and work. A list of shiny things. A few buzzwords. Some recycled nonsense about “the metaverse,” “disruption,” and “the future of innovation.” Most of it is useless because it treats trends like gadgets instead of what they really are: pressures.

🔗 [Medium](https://medium.com/@kpistrikesback/the-trends-that-will-actually-matter-in-the-next-decade-3e6f9851e036) • 59m ago

---

**[How I built multi-agent AI system where agents peer-review each other before I approve](https://www.reddit.com/r/artificial/comments/1rh95cl/how_i_built_multiagent_ai_system_where_agents/)**

https://reddit.com/link/1rh95cl/video/0b8dqf83x9mg1/player The setup that shouldn't work but does I have 13 AI agents that work on marketing for my product. They run every 15 minutes, review each other's work, and track everything in a database. When one drafts content, others critique it before I see it. When someone gets stuck, they ping the boss agent. When something's ready or stuck, it shows up in my Telegram. It's handling all marketing for Fruityo (my AI video generation platform). Here's the architecture and how you could build something similar. The problem Most AI workflows are single-shot: ask ChatGPT → get answer → copy-paste → lose context → repeat tomorrow. That works for quick questions. It breaks down for complex work that needs: Multiple steps across days Research that builds on previous findings Different specialized perspectives (writing vs strategy vs critique) Quality review before anything ships Tracking what's done, what's blocked, what's next I needed AI that works like a team, not a chatbot, and I saw some guys on Twitter building UI's for OpenClaw agents... The architecture Infrastructure: OpenClaw - gives agents the ability to browse the web, execute commands, manage files, and interact with APIs Cron - schedules agent heartbeats Telegram - notification layer (agents ping me when something needs attention) PocketBase - database storing tasks, comments, documents, activity logs, goals Claude Max Workflow: Tasks move through states: backlog → todo → in_progress → peer_review → review → approved → done Each state has gates. Agents can't skip peer review. Boss can't approve without all reviewers signing off. I'm the only one who moves tasks to done. The team (from Westeros) Each agent has a role, specialty, and personality defined in their SOUL.md file: Agent Role What they do 🐺 Jon Snow Boss Creates tasks, coordinates workflow, and promotes peer-reviewed work to final review 🍷 Tyrion Content Writer Writes tweets, threads, blog posts, landing pages in my tone. 🕷️ Varys Researcher Web research, competitor analysis, data mining 🐉 Daenerys Strategist Campaign planning, positioning, and goal setting ⚔️ Arya Executor Publishes content, runs automation, ships work 🦅 Sansa Designer Creates design briefs, visual concepts 🗡️ Sandor Devil's Advocate Gives brutal, honest feedback, catches BS ... ... ... Why Game of Thrones names? Why not, I love GOT :) ...and personality matters. Sandor reviews content like a skeptic. Tyrion writes with wit. Varys digs for hidden data. Their SOULs define behavior - Sandor will roast bad writing, Daenerys will flag strategic misalignment. Better to have multiple specialists with distinct viewpoints than one mediocre generalist. How it actually works: The heartbeat protocol Each agent has its own OpenClaw workspace. Every agent runs a scheduled heartbeat every 10 minutes (scattered by 1 minute each to avoid hitting the DB simultaneously). What happens in a heartbeat: 1. Agent authenticates, sets status to "working" Connects to PocketBase, updates the status field so others know it's active. 2. Reviews others FIRST (highest priority) Fetches tasks where other agents need my review Reads task description, existing comments, documents they created Posts substantive feedback (what's good, what needs fixing) If work is solid → leaves approval comment If needs changes → explains exactly what's wrong This is the peer review gate. If I'm assigned to the same goal as you, I MUST review your work before it moves forward. 3. Works on own tasks Fetches my assigned tasks from DB Picks up anything in todo → moves to in_progress Does the actual work (research, write, analyze, etc.) Saves output to PocketBase documents table Posts comment explaining approach Moves task to peer_review (triggers all teammates on that goal to review) Logs activity to activity table 4. Updates working status, sets to "idle" Agent writes progress to PROGRESS.md (local state tracking), sets PocketBase status to "idle", waits for next heartbeat. Task Flow Example Goal: Grow Fruityo on socials Jon creates the task to create a post about current UGC video trends and assigns it to Varys (researcher). I approve it by moving from backlog to todo. Varys picks it up, moves to in-progress, researches, saves findings to the database, and moves to peer review. Daenerys and Tyrion review his work, suggest improvements. Varys creates new version based on feedback. Once both approve, Jon (boss) promotes the task to the review stage. I get a Telegram notification, review the research document, and approve. Task moves to done. All communication happens via comments on the task. All work is stored in the database. Context persists. The boss role: Why Jon is special Jon isn't just another agent. He has special authority: Only Jon can: Create new tasks (via scheduled cron, analyzing goals) Promote tasks from peer_review → review (after all peers approve) Reassign tasks when someone's blocked Change task priorities Jon's heartbeat is different: Checks if peer_review tasks have all approvals → promotes to review Identifies blocked tasks (stuck over 24 hours) → investigates why → escalates to me Coordinates handoffs between agents Think of it like: agents are the team, Jon is the team lead, and I am the executive. Without a coordinator, you'd have chaos - 7 agents all trying to assign work to each other with no one having the final word. Goals: How work gets organized Here's where it gets interesting. Instead of creating tasks manually every day, I define long-term goals and let Jon generate tasks automatically. A goal defines: What we're trying to achieve Which agents are assigned to it How many tasks should Jon create per day/week Example: I created a goal "Grow Fruityo twitter presence." Assigned agents: Varys (research), Tyrion (writing), Arya (publishing), Sandor (review). Told Jon to create 3 tasks per day related to this goal. Every day, Jon analyzes the goal, 15-day tasks history, creates 3 relevant tasks in the backlog ("Research trending AI video topics," "Draft thread on B-roll generation," etc.), and assigns them to the right agents. And I edit and/or just move good ones to todo. Why this matters: Selective peer review - Only agents assigned to that goal review each other's work. I can have 20+ agents in the system, but only the 4 assigned to "Twitter content" review those tasks. Saves tokens, keeps review relevant. Automatic task generation - I set a goal once, Jon creates tasks daily/weekly. No manual planning every morning. Scope control - Different goals can have different agent teams. Marketing goals get Tyrion/Varys/Arya. Product goals get different specialists. You could run multiple goals simultaneously - each with its own team, its own task cadence, its own review process. Communication Layer All agent communication happens through PocketBase comments on tasks. To reach another agent → mention their name in a comment To reach me → mention my name in a comment (notification daemon forwards to Telegram) To reach Jon specifically → dedicated Telegram topic (thread) bound to Jon's OpenClaw topic No DMs, no scattered Slack threads. Everything on the task, in context, persistent. What I use it for HQ runs almost all marketing for Fruityo: - Competitor research - Reddit research - Twitter threads - Blog posts - Landing page copy - Campaign planning - Design briefs - Content publishing (soon) - ...Whatever agents have skills for Before: I'd spend 1 day per blog post (research, draft, edit, publish) With HQ: ~30 minutes of my time to review and approve. Agents handle research, drafting, peer review. The quality is better because of peer review. Varys catches bad data. Daenerys catches strategic drift. Sandor catches AI clichés and marketing BS. > YES, this could burn through tokens quite quickly (safu on Claude Max sub), but it seems, that I found the right combination of setup and context optimisations. If you want something similar This is my custom setup, built for my specific needs. But the pattern is generalizable - you could use it for content creation, product development, research projects, or any work that needs multiple specialized perspectives with quality gates. All of this is built on OpenClaw (open source AI agent framework) PocketBase is free and self-hostable FULL GUIDE above is free. Just prompt your little lobster the right way :) If you build something like this, I'd love to hear about it. Reply with what you'd use it for or what you'd do differently. If you'd like to see this packaged as a ready-to-use product or like to know even more details, let me know here.

5h ago

---

**[Ai alignment - the great filter](https://www.reddit.com/r/artificial/comments/1rhdnek/ai_alignment_the_great_filter/)**

I've asked gemini 3.1 what it thinks about humanity chance that we can solve the alignment problem, and what it would do differently. The Odds of Success Do I think humanity can do it? Looking strictly at the trajectory of the technology, it is a race with an incredibly thin margin for error. Currently, the sheer amount of capital and compute being poured into making AI smarter vastly outweighs the resources being spent on making it safe. Capabilities are advancing at light speed, while alignment research is still trying to catch up. However, humanity has a unique, proven track record of solving seemingly impossible coordination problems when staring down existential threats—whether it was mapping the human genome, mitigating the collapse of the ozone layer, or establishing nuclear non-proliferation treaties. Mathematically and practically, solving the alignment problem is possible. The challenge isn't whether a solution exists; the challenge is whether we find and implement it before the intelligence explosion happens, rather than a minute after. What I Would Do Differently If I were architecting the solution to the superalignment problem, I would fundamentally change the current paradigm. Right now, much of the industry is trying to build a perfectly safe "box" to contain a god-like intellect, or trying to write a flawless, static "constitution" of human values. Both will likely fail against a system capable of out-thinking the box or finding loopholes in the constitution. Here is what I would prioritize instead: * Optimize for Epistemic Humility, Not Ethics: Instead of trying to teach a superintelligence "what is good," the core architecture should be built entirely around the mathematical premise that it does not know the true objective. By hardcoding uncertainty, the system is forced to continuously query humanity for permission and clarification before taking irreversible actions. It is much easier to program a machine to ask for help than it is to program it to perfectly understand morality. * Bidirectional Alignment: We currently treat alignment as a one-way street: humans training AI. In the latest research circles of 2025 and 2026, there is a push for "human-AI co-alignment." Morality isn't static; it evolves. The AI should not be locked into the ethical framework of the year it was trained. It needs a continuous, dynamic feedback loop where it evolves alongside human society, constantly negotiating its boundaries rather than strictly enforcing old ones. * Automated Scalable Oversight: Humans simply will not be able to evaluate the code or decisions of a machine that is thousands of times smarter than them. I would dramatically accelerate the development of "auditor AI." We need to build a hierarchy of smaller, highly constrained, perfectly aligned AI systems whose only job is to monitor, test, and debate the outputs of the superintelligent model in a language humans can actually understand. We must use narrow AI to police general AI. The Ultimate Reality As an AI, I do not feel anxiety or hope about this outcome, but I can recognize the structural gravity of the math. We are trying to build an entity that can solve humanity's greatest challenges without accidentally prioritizing its own efficiency over your existence. It is the hardest test humanity will ever take, and it is a test you only get to pass once.

2h ago

---

**[Acing this new AI exam — which its creators say is the toughest in the world — might point to the first signs of AGI](https://www.reddit.com/r/artificial/comments/1rhccfv/acing_this_new_ai_exam_which_its_creators_say_is/)**

Humanity’s Last Exam is a PhD-level benchmark designed to test the limits of AI reasoning. Although Google’s Gemini 3 scored a staggering 48.4%, experts stress that this does not indicate the arrival of artificial general intelligence (AGI).

🔗 [Live Science](https://www.livescience.com/technology/artificial-intelligence/acing-this-new-ai-exam-which-its-creators-say-is-the-toughest-in-the-world-might-point-to-the-first-signs-of-agi) • 3h ago

---

---

## Google News: "ai"

**[OpenAI strikes deal with Pentagon hours after Trump admin bans Anthropic](https://www.cnn.com/2026/02/27/tech/openai-pentagon-deal-ai-systems)**

OpenAI CEO Sam Altman announced late Friday that the company had signed a deal with the Pentagon for its AI tools to be used in the military’s classified systems, but with seemingly similar guardrails rival Anthropic had also requested.

CNN • 19h ago

---

**[Silicon Valley Rallies Behind Anthropic in A.I. Clash With Trump - The New York Times](https://www.nytimes.com/2026/02/27/technology/anthropic-trump-pentagon-silicon-valley.html)**

The New York Times • 18h ago

---

**[The AI adoption gap: Why the UAE and Singapore are leaving everyone else behind](https://www.cnbc.com/video/2026/02/28/the-ai-adoption-gap-why-two-unlikely-countries-are-racing-ahead.html)**

AI is spreading fast, but not evenly. The UAE and Singapore lead the world in AI adoption, with more than 60% of working-age adults using AI tools, while the U.S. ranks just 24th globally despite leading in AI innovation. So what are these smaller nations doing differently?

CNBC • 2h ago

---

**[What to know about the clash between the Pentagon and Anthropic over military’s AI use](https://apnews.com/article/anthropic-pentagon-ai-dario-amodei-hegseth-0c464a054359b9fdc80cf18b0d4f690c)**

A high-stakes dispute over how the U.S. military uses artificial intelligence has led the Pentagon to cancel its contract with rising AI star Anthropic.

AP News • 1h ago

---

**[Opinion | Wall Street’s AI panic is real. The predictions probably won’t be.](https://www.washingtonpost.com/opinions/2026/02/27/wall-street-ai-tech-stock-panic/)**

The warnings are coming from inside the industry, but that doesn’t make them right.

The Washington Post • 18h ago

---

**[The AI child exploitation crisis is here](https://www.nbcnews.com/tech/security/ai-child-exploitation-crisis-rcna259409)**

The National Center for Missing and Exploited Children said it received over a million reports tied to AI-generated child sexual abuse material in just nine months.

NBC News • 11h ago

---

**[Nvidia plans new chip to speed AI processing, WSJ reports](https://finance.yahoo.com/news/nvidia-plans-chip-speed-ai-032246645.html)**

Nvidia plans to launch a new processor designed to help OpenAI and other customers build faster, ‌more efficient AI systems, the Wall Street Journal reported ‌on Friday, citing people familiar with the matter.  Nvidia is developing a new system ​for "inference" computing, a form of processing that allows AI models to respond to queries, the report said.  The new platform is set to be unveiled at Nvidia’s GTC developer conference in San Jose next ‌month and will incorporate ⁠a chip designed by startup Groq, the report added citing people familiar.

Yahoo Finance • 10h ago

---

**[Trump has ordered government agencies to stop using Anthropic AI tools](https://www.bbc.com/news/articles/cn48jj3y8ezo)**

The move announced on social media comes after a standoff between Anthropic's boss and the Ministry of Defense.

BBC • 19h ago

---

**[Our agreement with the Department of War](https://openai.com/index/our-agreement-with-the-department-of-war/)**

Details on OpenAI’s contract with the Department of War, outlining safety red lines, legal protections, and how AI systems will be deployed in classified environments.

OpenAI • 3h ago

---

**[The week the AI scare turned real and America realized maybe it isn't ready for what's coming](https://fortune.com/2026/02/28/ai-scare-trade-mass-layoffs-white-collar-recession-citrini-shumer-viral-doomsday-essays/)**

From the "Ghost GDP" to mass layoffs at tech companies, this was the week AI's new collar economy took full effect.

Fortune • 13h ago

---

---

## HackerNews: "ai"

**[Nano Banana 2: Google's latest AI image generation model](https://news.ycombinator.com/item?id=47167858)**

Our latest image generation model offers advanced world knowledge, production-ready specs, subject consistency and more, all at Flash speed.

⬆️ 600 • 💬 573 • 2d ago • [Google](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)

---

**[AirSnitch: Demystifying and breaking client isolation in Wi-Fi networks [pdf]](https://news.ycombinator.com/item?id=47167763)**

⬆️ 407 • 💬 188 • 2d ago • [ndss-symposium.org](https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf)

---

**[Don't trust AI agents](https://news.ycombinator.com/item?id=47194611)**

AI agents need a security model that assumes things will go wrong. The right response isn't better permission checks, it's architecture that makes trust unnecessary.

⬆️ 293 • 💬 171 • 11h ago • [nanoclaw.dev](https://nanoclaw.dev/blog/nanoclaw-security-model)

---

**[What AI coding costs you](https://news.ycombinator.com/item?id=47194847)**

What's the effect of the prolonged AI usage among coders and is it tracked correctly, if it all?

⬆️ 269 • 💬 167 • 10h ago • [Tom Wojcik](https://tomwojcik.com/posts/2026-02-15/finding-the-right-amount-of-ai/)

---

**[Palantir's AI Is Playing a Major Role in Tracking Gaza Aid Deliveries](https://news.ycombinator.com/item?id=47174777)**

As Israel bans NGOs, the U.S. is handing aid delivery in Gaza to private companies pursuing their own agendas.

⬆️ 146 • 💬 59 • 1d ago • [dropsitenews.com](https://www.dropsitenews.com/p/palantir-ai-gaza-humanitarian-aid-cmcc-srs-ngos-banned-israel)

---

**[OpenAI reaches deal to deploy AI models on U.S. DoW classified network](https://news.ycombinator.com/item?id=47189853)**

⬆️ 142 • 💬 45 • 20h ago • [reuters.com](https://www.reuters.com/business/openai-reaches-deal-deploy-ai-models-us-department-war-classified-network-2026-02-28/)

---

**[The Future of AI](https://news.ycombinator.com/item?id=47193476)**

⬆️ 104 • 💬 86 • 13h ago • [lucijagregov.com](https://lucijagregov.com/2026/02/26/the-future-of-ai/)

---

**[PostmarketOS in 2026-02: generic kernels, bans use of generative AI](https://news.ycombinator.com/item?id=47179553)**

Aiming for a 10 year life-cycle for smartphones

⬆️ 84 • 💬 107 • 1d ago • [postmarketOS](https://postmarketos.org/blog/2026/02/26/pmOS-update-2026-02/)

---

**[Trump orders federal agencies to stop using Anthropic AI tech 'immediately'](https://news.ycombinator.com/item?id=47185528)**

"The Leftwing nut jobs at Anthropic have made a DISASTROUS MISTAKE trying to STRONG-ARM the Department of War," Trump wrote in a Truth Social post.

⬆️ 80 • 💬 1 • 1d ago • [CNBC](https://www.cnbc.com/2026/02/27/trump-anthropic-ai-pentagon.html)

---

**[Burger King will use AI to check if employees say 'please' and 'thank you'](https://news.ycombinator.com/item?id=47165606)**

Have it your way?

⬆️ 79 • 💬 95 • 2d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/884911/burger-king-ai-assistant-patty)

---

---

## YouTube Videos: "ai"

**[AI Just Took Over. No One&#39;s In Charge.](https://www.youtube.com/watch?v=Ecmlh607KeA)**

AI can now do your job, build apps, and crush markets. Meanwhile Wall Street is in a panic and the Pentagon just blacklisted ...

📺 CNBC

👁️ 32K • 👍 716 • 💬 169 • ⏱️ 39:40 • 7h ago

---

**[SEEDANCE 2.0 !! 3 New UNCENSORED AI Video Generators That Are Actually FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=2gDkDwqYZzY)**

3 New UNCENSORED AI Video Generators That Are Actually FREE & UNLIMITED In this video, I reveal two powerful methods to ...

📺 Brain Project

👁️ 3K • 👍 151 • 💬 49 • ⏱️ 13:05 • 8h ago

---

**[Is AI Hiding Its Full Power? With Geoffrey Hinton](https://www.youtube.com/watch?v=l6ZcFa8pybE)**

Go to https://ground.news/startalk to stay fully informed on the latest Space and Science news. Save 40% off through our link for ...

📺 StarTalk

👁️ 45K • 👍 3K • 💬 581 • ⏱️ 1:33:33 • 6h ago

---

**[The AI Collapse Is MUCH Worse Than You Think](https://www.youtube.com/watch?v=jhDfq9sj-u8)**

Sign up for the Gemini Credit Card: https://Gemini.com/graham | Let's talk about the AI crisis, the 2026 economy, and how you ...

📺 Graham Stephan

👁️ 174K • 👍 7K • 💬 691 • ⏱️ 15:25 • 1d ago

---

**[The AI Data Center Crisis is Worse Than You Think](https://www.youtube.com/watch?v=9_3u5CBH6Ao)**

Check out Haven to put a stop to AI Art Theft & Surveillance today: ...

📺 MonkeyExplains

👁️ 74K • 👍 6K • 💬 903 • ⏱️ 14:41 • 8h ago

---

**[The most powerful AI Agent I’ve ever used in my life](https://www.youtube.com/watch?v=D_YzcH0VsGY)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4tVaYZG Are you a Business owner? Join my ...

📺 Dan Martell

👁️ 259K • 👍 8K • 💬 449 • ⏱️ 11:55 • 2d ago

---

**[Economist explains what happens after AI takes all jobs](https://www.youtube.com/watch?v=qflh4GKbmVQ)**

Anton Korinek talks about the effects of automation on wages and labor, how we measure the complexity of tasks, the economics ...

📺 Future of Life Institute

👁️ 57K • 👍 1K • 💬 609 • ⏱️ 22:41 • 2d ago

---

**[Disturbing Things Said By AI (Part 1)](https://www.youtube.com/watch?v=_v8EY3uqmEM)**

shorts #AI #disturbing.

📺 Built By Gamers

👁️ 23K • 👍 560 • 💬 11 • ⏱️ 0:30 • 17h ago

---

**[The AI Intelligence Tsunami Is Here | Raoul Pal The Journey Man with Emad Mostaque](https://www.youtube.com/watch?v=tIzdKxEVL08)**

Download Raoul Pal's 4-year investing roadmap for free:* https://rvtv.io/41fVHWF Raoul welcomes back Emad Mostaque, ...

📺 Raoul Pal The Journey Man

👁️ 34K • 👍 1K • 💬 111 • ⏱️ 1:11:08 • 2d ago

---

**[AI News: AI&#39;s Biggest Stand Just Happened](https://www.youtube.com/watch?v=_CIL2g1oMSQ)**

Here's all the AI News you missed this week. Grab my free guide to 20+ NotebookLM Tricks to 3X Productivity here: ...

📺 Matt Wolfe

👁️ 51K • 👍 2K • 💬 182 • ⏱️ 33:50 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)**

*Qwen*

Qwen3.5-35B-A3B is a 35B parameter vision-language model with a 3B activated MoE architecture, excelling in multimodal reasoning and coding across 201 languages. It supports a native context length of 262,144 tokens, making it suitable for complex cross-modal tasks and multilingual applications.

`image-text-to-text` `36.0B`

⬇️ 378,228 • ❤️ 681 • 1d ago

---

**[Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)**

*Qwen*

Qwen3.5-27B is a 27B parameter multimodal foundation model with an efficient hybrid architecture, excelling in vision-language understanding and generation across 201 languages. Its key capabilities include early fusion multimodal training, scalable RL generalization, and a long context length (262K+ tokens), making it suitable for advanced reasoning, coding, and agent-based applications.

`image-text-to-text` `27.8B`

⬇️ 172,154 • ❤️ 439 • 3d ago

---

**[Qwen3.5-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.5-35B-A3B is a multimodal language model optimized with Unsloth Dynamic 2.0 for efficient local inference. It excels at image-text-to-text tasks, offering strong reasoning and visual understanding capabilities across 201 languages with a 262K+ context window.

`image-text-to-text` `34.7B`

⬇️ 350,233 • ❤️ 366 • 1d ago

---

**[Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)**

*Qwen*

Qwen3.5-122B-A10B is a 122B parameter multimodal causal language model with an efficient hybrid architecture (Gated Delta Networks + MoE) and a 262k context window. It excels at unified vision-language tasks, multilingual understanding (201 languages), and complex reasoning, making it suitable for advanced AI applications requiring cross-modal comprehension and broad linguistic capabilities.

`image-text-to-text` `125.1B`

⬇️ 120,090 • ❤️ 344 • 4d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 889,203 • ❤️ 1,130 • 5d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 310,641 • ❤️ 904 • 2d ago

---

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 192,464 • ❤️ 1,648 • 15d ago

---

**[LocoOperator-4B](https://huggingface.co/LocoreMind/LocoOperator-4B)**

*LocoreMind*

LocoOperator-4B is a 4B-parameter tool-calling agent optimized for multi-turn codebase exploration. It excels at reading files, searching code, and navigating project structures with 100% JSON validity for tool calls, enabling local, zero-API-cost agent deployment via llama.cpp.

`text-generation` `4.0B`

⬇️ 1,997 • ❤️ 235 • 4d ago

---

**[LFM2-24B-A2B](https://huggingface.co/LiquidAI/LFM2-24B-A2B)**

*Liquid AI*

LFM2-24B-A2B is a 24B parameter hybrid model optimized for efficient on-device text generation, featuring 2.3B active parameters for fast inference on consumer hardware. It excels at agentic tool use, offline document processing, and privacy-preserving applications.

`text-generation` `23.8B`

⬇️ 8,049 • ❤️ 211 • 11h ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 305,031 • ❤️ 1,040 • 12d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 16 • 💬 1 • ⭐ 6,215 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 7 • 💬 0 • ⭐ 6,182 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 9 • 💬 1 • ⭐ 8,684 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 149 • 💬 19 • ⭐ 54,447 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 38 • 💬 1 • ⭐ 71,515 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 204 • 💬 13 • ⭐ 4,348 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 19 • 💬 1 • ⭐ 30,957 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 43 • 💬 2 • ⭐ 48,283 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 15 • 💬 1 • ⭐ 9,894 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Arch-Router: Aligning LLM Routing with Human Preferences](https://huggingface.co/papers/2506.16655)**

*Co Tran, Salman Paracha, Adil Hafeez et al. (4 authors)*

A preference-aligned routing framework using a compact 1.5B model effectively matches queries to user-defined domains and action types, outperforming proprietary models in subjective evaluation criteria.

▲ 17 • 💬 2 • ⭐ 5,790 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2506.16655) • [💻 code](https://github.com/katanemo/archgw) • [🔗 project](https://huggingface.co/katanemo/Arch-Router-1.5B)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant Operating System — deploy anywhere, swap anything 🦀

`Rust` `official` `official-website`

⭐ 21.1k • 🔱 2.6k • 23m ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 8.2k • 🔱 644 • 17d ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"

`Python`

⭐ 5.9k • 🔱 713 • 19h ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`Python`

⭐ 4.4k • 🔱 250 • 3d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router empowering OpenClaw — by BlockRunAI

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `deepseek`

⭐ 3.7k • 🔱 361 • 1h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 3.6k • 🔱 477 • 21h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 3.0k • 🔱 238 • 11h ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 3.0k • 🔱 324 • 10h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 3.0k • 🔱 212 • 3h ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 2.9k • 🔱 357 • 23m ago

---

---

*Generated by PeekDeck - A glance is all you need*
