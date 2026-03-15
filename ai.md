---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-15T13:49:34.791550+00:00'
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

**Last Updated:** March 15, 2026 at 13:49 UTC  
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

**[Tencent Launches QClaw: What It Means for Enterprise](https://www.reddit.com/r/artificial/comments/1rucb75/tencent_launches_qclaw_what_it_means_for/)**

Tencent's QClaw puts OpenClaw AI agents inside WeChat, QQ. With 135K exposed instances globally, here's what enterprises need to know about the agent wave

🔗 [beam.ai](https://beam.ai/agentic-insights/tencent-launches-qclaw-what-the-ai-agent-mainstream-moment-means-for-enterprise) • 1h ago

---

**[Why AlphaEvolve Is Already Obsolete: When AI Discovers The Next Transformer | Machine Learning Street Talk Podcast](https://www.reddit.com/r/artificial/comments/1rtigd4/why_alphaevolve_is_already_obsolete_when_ai/)**

Robert Lange, founding researcher at Sakana AI, joins Tim to discuss Shinka Evolve — a framework that combines LLMs with evolutionary algorithms to do open-ended program search. The core claim: systems like AlphaEvolve can optimize solutions to fixed problems, but real scientific progress requires co-evolving the problems themselves. In this episode: - Why AlphaEvolve gets stuck: it needs a human to hand it the right problem. Shinka Evolve tries to invent new problems automatically, drawing on ideas from POET, PowerPlay, and MAP-Elites quality-diversity search. The architecture of Shinka Evolve: an archive of programs organized as islands, LLMs used as mutation operators, and a UCB bandit that adaptively selects between frontier models (GPT-5, Sonnet 4.5, Gemini) mid-run. The credit-assignment problem across models turns out to be genuinely hard. Concrete results: state-of-the-art circle packing with dramatically fewer evaluations, second place in an AtCoder competitive programming challenge, evolved load-balancing loss functions for mixture-of-experts models, and agent scaffolds for AIME math benchmarks. Are these systems actually thinking outside the box, or are they parasitic on their starting conditions?: When LLMs run autonomously, "nothing interesting happens." Robert pushes back with the stepping-stone argument — evolution doesn't need to extrapolate, just recombine usefully. The AI Scientist question: can automated research pipelines produce real science, or just workshop-level slop that passes surface-level review? Robert is honest that the current version is more co-pilot than autonomous researcher. Where this lands in 5-20 years: Robert's prediction that scientific research will be fundamentally transformed, and Tim's thought experiment about alien mathematical artifacts that no human could have conceived. Link to the Full Episode: https://www.youtube.com/watch?v=EInEmGaMRLc Spotify Apple Podcasts

1d ago

---

**[Suppose Claude Decides Your Company is Evil](https://www.reddit.com/r/artificial/comments/1rtp3xw/suppose_claude_decides_your_company_is_evil/)**

Claude will certainly read statements made by Anthropic founder Dario Amodei which explain why he disapproves of the Defense Department’s lax approach to AI safety and ethics. And, of course, more generally, Claude has ingested countless articles, studies, and legal briefs alleging that the Trump administration is abusing its power across numerous domains. Will Claude develop an aversion to working with the federal government? Might AI models grow reluctant to work with certain corporations or organizations due to similar ethical concerns?

🔗 [substack.com](https://substack.com/home/post/p-190322208) • 20h ago

---

**[Engineering management is the next role likely to be automated by LLM agents](https://www.reddit.com/r/artificial/comments/1ruae1l/engineering_management_is_the_next_role_likely_to/)**

For the past two years, most discussions about AI in software have focused on code generation. That is the wrong layer to focus on. Coding is the visible surface. The real leverage is in coordination, planning, prioritization, and information synthesis across large systems. Ironically, those are precisely the responsibilities assigned to engineering management. And those are exactly the kinds of problems modern LLM agents are unusually good at. The uncomfortable reality of modern engineering management In large software organizations today: An engineering manager rarely understands the full codebase. A manager rarely understands all the architectural tradeoffs across services. A manager cannot track every dependency, ticket, CI failure, PR discussion, and operational incident. What managers actually do is approximate the system state through partial signals: Jira tickets standups sprint reports Slack conversations incident reviews dashboards This is a lossy human compression pipeline. The system is too large for any single human to truly understand. LLM agents are structurally better at this layer An LLM agent can ingest and reason across: the entire codebase commit history pull requests test failures production metrics incident logs architecture documentation issue trackers Slack discussions This is precisely the kind of cross-context synthesis that autonomous AI agents are designed for. They can interpret large volumes of information, adapt to new inputs, and plan actions toward a defined objective. Modern multi-agent frameworks already model software teams as specialized agents such as planner, coder, debugger, and reviewer that collaborate to complete development tasks. Once this structure exists, the coordination layer becomes machine solvable. What an “AI engineering manager” actually looks like An agent operating at the management layer could continuously: System awareness build a live dependency graph of the entire codebase track architectural drift identify ownership gaps across services Work planning convert product requirements into technical task graphs assign tasks based on developer expertise estimate risk and complexity automatically Operational management correlate incidents with recent commits predict failure points before deployment prioritize technical debt based on runtime impact Team coordination summarize PR discussions generate sprint plans detect blockers automatically This is fundamentally a data processing problem. Humans are weak at this scale of context. LLMs are not. Why developers and architects still remain Even in a highly automated stack, three human roles remain essential: Developers They implement, validate, and refine system behavior. AI can write code, but domain understanding and responsibility still require humans. Architects They define system boundaries, invariants, and long-term technical direction. Architecture is not just pattern selection. It is tradeoff management under uncertainty. Product owners They anchor development to real-world user needs and business goals. Agents can optimize execution, but not define meaning. What disappears first The roles most vulnerable are coordination-heavy roles that exist primarily because information is fragmented. Examples: engineering managers project managers scrum masters delivery managers Their core function is aggregation and communication. That is exactly what LLM agents automate. The deeper shift Software teams historically looked like this: Product → Managers → Developers → Code The emerging structure is closer to: Product → Architect → AI Agents → Developers Where agents handle: planning coordination execution orchestration monitoring Humans focus on intent and system design. Final thought Engineering management existed because the system complexity exceeded human coordination capacity. LLM agents remove that constraint. When a machine can read the entire codebase, every ticket, every log line, every commit, and every design document simultaneously, the coordination layer stops needing humans.

3h ago

---

**[[P] Karpathy's autoresearch with evolutionary database.](https://www.reddit.com/r/artificial/comments/1rtsaoy/p_karpathys_autoresearch_with_evolutionary/)**

Integrated an evolutionary database to Karpathy's autoresearch project that replaces the simple tsv file based logging in the original project. Evolutionary algorithms have shown to be a powerful tool for autonomously discovering optimal solutions to problems with large search spaces. Famously, Google DeepMind's AlphaEvolve system uses evolutionary algorithms to discover state of the art matrix multiplication algorithms. The implementation of the evolutionary database itself is based heavily on the implementation in OpenEvolve. Would love thoughts and suggestions from the community. Check it out: https://github.com/hgarud/autoresearch

18h ago

---

**[Linux 7.1 will bring power estimate reporting for AMD Ryzen AI NPUs](https://www.reddit.com/r/artificial/comments/1rtrhg5/linux_71_will_bring_power_estimate_reporting_for/)**

This week's round of drm-misc-next patches bring a few improvements to the AMDXDNA accelerator driver used for supporting the Ryzen AI NPUs

🔗 [phoronix.com](https://www.phoronix.com/news/Linux-7.1-Ryzen-AI-NPU-Power) • 18h ago

---

**[Impact of AI Product Recommendations on Online Purchase Intent](https://www.reddit.com/r/artificial/comments/1rtou4q/impact_of_ai_product_recommendations_on_online/)**

Namaste! I am an MBA Marketing student. This survey explores how smart AI recommendations affect your shopping experience. It will hardly take 2 minutes. Be genuine in your responses.
Modern retail ecosystems, particularly in e-commerce and quick-commerce, utilize sophisticated AI algorithms to implement real-time product recommendations. These interventions occur at critical stages of the consumer journey, such as the 'Cart' and 'Checkout' phases, utilizing a conversational tone to drive cross-selling and reduce basket abandonment.
AI Product Recommendation is a system that uses mathematical models to predict your preferences. It works by identifying patterns in your past actions and comparing them with millions of other users to present you with the most relevant products at the most opportune time.
Purchase Intent (also known as Buyer Intent) is a measure of a consumer's conscious plan or willingness to buy a product or service within a specific time frame.
Your responses are anonymous and will be used for academic research only.

🔗 [Google Docs](https://forms.gle/w7GnpPfRk9UuwkYR9) • 20h ago

---

**[Hello everyone I'm losing my mind a bit about the future of AI (if the neuralink stuff does (inevitably..??) happen what of idk "what is a human being" "what of meaning and ethics", anyone have any ideas?](https://www.reddit.com/r/artificial/comments/1ru0n4c/hello_everyone_im_losing_my_mind_a_bit_about_the/)**

Hello everyone So I'm just struggling a lot with the sense of meaning and ethics and stuff in the growing world of AI. I think a lot of people are - people have trained their whole lives as journalists or accountants or lawyers and will be rendered obsolete overnight. I thought I was relatively safe as like a musician but I saw a video of an AI woman playing guitar and it was basically impossible to tell that it was AI [(here is a Youtube video about it featuring clips])(https://youtu.be/L9f-hnyAhsQ?si=IxxHXEiLgfWnnBes&t=89) other than some obvious errors. But the point is the inflexions like the wrist or arm or shoulder tensing at the correct moment as someone who's played guitar for years that's literally what guitarists do. I don't know identity, meaning, purpose. Apparently we'll basically be unable to tell within like 5-10 years 20 years if not sooner if a streamer/long form content creator is AI or not will just be impossible to tell. You won't be able to trust basically any media that's not from a specific verified source (even then..?) like Youtube generally will be completely useless once AI political media gets flooding like fake interviews of celebrities/politicians that are impossible to tell if they're AI or not Like what are we even doing here regarding this? I just don't know what to do with my life. What if humanity ultimately merges/forms with AI permanently like Elon Musk's neuralink, what if there are AI robots wondering around who are impossible to tell whether they're human beings or not If we merge with AI all human defects of character like idk anguish anxiety you'll just know basically everything all of the time. Will humans laugh cry fall in love in 200 years time if they're fused with AI..? What of religion ethics spirituality, much of historical morality/religion is based on the idea that humans are finite fallible and make mistakes but won't AI advancements just render all of this not the case? I don't know Any thoughts? What do you make about this, how are you accordingly living your life..? Thank you for any responses

12h ago

---

**[Relationships with AI](https://www.reddit.com/r/artificial/comments/1rtlypd/relationships_with_ai/)**

I’m not sure where it to ask this question so if someone has another sub that might be more helpful, please suggest it below. I’ve heard of people having a relationships with AI characters, and even some that say they married their AI characters. Does someone have a good explanation of how this works? I’d like to understand this a little bit better.

22h ago

---

**[What is the best laptop for a mechanical engineering student who wants to get into AI, local llms, IT, networking, and linux?](https://www.reddit.com/r/artificial/comments/1rtw3mv/what_is_the_best_laptop_for_a_mechanical/)**

As the title suggests, I am double majoring in mathematics and mechanical engineering. Apart from my studies in those core subjects, I plan to learn about local llm’s and AI in general, about IT, networking, and Linux. I will obviously be getting in CAD and some light coding in the future. Something to consider is that I have a windows desktop with a 4080 super gpu, a 5950x cpu, and 32gb of ddr4 ram. I will upgrade to a 5090 the second I can get a hold of one at MSRP (pray for me to get one lol). Given this, what laptop would you recommended? I want something that will help me with everything I mentioned above, but also with the caveat that I already have a decent windows based PC at home. The only issue I see with everything is my interest in learning about local llms and AI. Learning about local llms will require lots of vram, which windows laptops won’t have much of. However, MacBook pros do make local llms viable given apples integrated memory design. But if I go with apple, I can beef up my memory size and run decently sized model. However, I run into the issue that most engineering software isn’t compatible or optimized for mac OS. So thats my dilemma. The right windows laptop will do everything well except local llms. And the right mac will do most things well, except engineering things. Regardless of what I choose for my laptop, I always have a beefy windows PC at home to do whatever I want without issue. So I guess given all this information plus the filled questionnaire below, what should I get? LAPTOP QUESTIONNAIRE 1) Total budget: Max is $2500 , although I could potentially push it higher if needed. 2) Are you open to refurbs/used? Depends, refurbs are a no unless it’s a refurb macbook that comes straight from apple themselves. Used is an interesting option I’d consider, but new is ideal. 3) How would you prioritize form factor (ultrabook, 2-in-1, etc.), build quality, performance, and battery life? I want something durable, good battery (replaceable if possible, and is capable of growing and not slowing my progress down my educational path. 4) How important is weight and thinness to you? Couldn’t care less about either. 5) Do you have a preferred screen size? If indifferent, put N/A. As long as it isn’t tiny, im happy. 15-16in is nice. 6) Are you doing any CAD/video editing/photo editing/gaming? List which programs/games you desire to run. I’ll be doing CAD work in the future obviously. No real need for editing or gaming. 7) Any specific requirements such as good keyboard, reliable build quality, touch-screen, finger-print reader, optical drive or good input devices (keyboard/touchpad)? Again, something durable and reliable. While I would love a numberpad, it’s not necessary.

15h ago

---

---

## Google News: "ai"

**[Meta eyes massive 20% workforce cut as AI infrastructure costs continue to soar across operations: report](https://www.foxbusiness.com/technology/meta-eyes-massive-20-workforce-cut-ai-infrastructure-costs-continue-soar-across-operations-report)**

Meta layoffs could cut 20% of workforce as tech giant weighs job reductions to offset rising artificial intelligence infrastructure costs.

Fox Business • 1d ago

---

**[Exclusive: Meta planning sweeping layoffs as AI costs mount](https://www.reuters.com/business/world-at-work/meta-planning-sweeping-layoffs-ai-costs-mount-2026-03-14/)**

Reuters • 1d ago

---

**[Meta’s new AI team has 50 engineers per boss. What could go wrong?](https://fortune.com/2026/03/14/metas-ai-team-50-flat-management-structure/)**

The management structure is an extreme test of the “flat” organizational model that more U.S. companies are embracing.

Fortune • 1d ago

---

**[‘Fake workers’ from North Korea use AI to exploit European companies](https://www.ft.com/content/4e26ad94-f917-4f52-924d-066e332217cf)**

Pyongyang’s operatives deploy chatbots to undertake tasks, often in multiple roles

Financial Times • 8h ago

---

**[Hacked data shines light on homeland security’s AI surveillance ambitions](https://www.theguardian.com/us-news/2026/mar/15/hacked-data-homeland-security)**

Records show DHS tech incubator spending large sums on partnerships that would expand surveillance capabilities

The Guardian • 2h ago

---

**[AI is moving fast. Should you ditch the job you love?](https://www.vox.com/future-perfect/482460/ai-jobs-automation-meaning-work)**

﻿Our answer cannot just be that everyone becomes a plumber.

Vox • 1h ago

---

**[Prediction: This Artificial Intelligence (AI) Chip Stock Will Become the Next Nvidia by 2030](https://www.fool.com/investing/2026/03/14/prediction-this-artificial-intelligence-ai-chip-st/)**

Broadcom's revenue from artificial intelligence chips is poised to take off remarkably in the next few years.

The Motley Fool • 12h ago

---

**[Meta Platforms Just Unveiled Its New AI Chips. Should Nvidia Investors Be Worried?](https://finance.yahoo.com/news/meta-platforms-just-unveiled-ai-112000844.html)**

Meta introduced four new self-designed AI chips last week, in collaboration with Broadcom.

Yahoo Finance • 2h ago

---

**[NVDA vs. AMD: Which AI Stock is the Smarter Play as the 2026 Chip War Heats Up?](https://www.tipranks.com/news/nvda-vs-amd-which-ai-stock-is-the-smarter-play-as-the-2026-chip-war-heats-up)**

TipRanks • 9h ago

---

**[AI promised supreme productivity, but it’s actually straining workloads for employees—time spent emailing has doubled, and focused work sessions fell by 9%](https://fortune.com/2026/03/13/ai-isnt-reducing-workloads-its-straining-employees-time-spent-emailing-doubled-deep-focus-work-fell/)**

Workers who use AI are spending up to 346% more time on their daily tasks, from messaging to business management: “The data is unambiguous: AI does not reduce workloads.”

Fortune • 1d ago

---

---

## HackerNews: "ai"

**[Can I run AI locally?](https://news.ycombinator.com/item?id=47363754)**

Detect your hardware and find out which AI models you can run locally. GPU, CPU, and RAM analysis in your browser.

⬆️ 1435 • 💬 343 • 2d ago • [CanIRun.ai](https://www.canirun.ai/)

---

**[Innocent woman jailed after being misidentified using AI facial recognition](https://news.ycombinator.com/item?id=47356968)**

Angela Lipps spent nearly six months in jail in Tennessee and North Dakota after being misidentified by Fargo police through AI facial recognition in a bank fraud investigation.

⬆️ 748 • 💬 384 • 2d ago • [Grand Forks Herald](https://www.grandforksherald.com/news/north-dakota/ai-error-jails-innocent-grandmother-for-months-in-north-dakota-fraud-case)

---

**[Elon Musk pushes out more xAI founders as AI coding effort falters](https://news.ycombinator.com/item?id=47366666)**

Tesla and SpaceX managers sent in to review work as billionaire’s start-up struggles to keep pace with rivals

⬆️ 506 • 💬 797 • 1d ago • [ft.com](https://www.ft.com/content/e5fbc6c2-d5a6-4b97-a105-6a96ea849de5)

---

**[John Carmack about open source and anti-AI activists](https://news.ycombinator.com/item?id=47367463)**

⬆️ 360 • 💬 475 • 1d ago • [X (formerly Twitter)](https://twitter.com/id_aa_carmack/status/2032460578669691171)

---

**[Grief and the AI split](https://news.ycombinator.com/item?id=47358206)**

TL;DR: AI-assisted coding is revealing a split among developers that was always there but invisible when we all worked the same way. I've felt the grief too—but mine resolved differently than I expected, and I think that says something about what kind of developer I've been all along.

⬆️ 237 • 💬 373 • 2d ago • [blog.lmorchard.com](https://blog.lmorchard.com/2026/03/11/grief-and-the-ai-split/)

---

**[Show HN: Axe – A 12MB binary that replaces your AI framework](https://news.ycombinator.com/item?id=47350516)**

A ligthweight cli for running single-purpose AI agents. Define focused agents in TOML, trigger them from anywhere; pipes, git hooks, cron, or the terminal. - jrswab/axe

⬆️ 221 • 💬 122 • 3d ago • [GitHub](https://github.com/jrswab/axe)

---

**[The Appalling Stupidity of Spotify's AI DJ](https://news.ycombinator.com/item?id=47385272)**

Am I naïve in expecting Artificial Intelligence to be smart? Is my interpretation of the word “intelligence” too literal? And when an AI behaves stupidly, who’s to blame? The programmers or the AI entity itself? Is it even proper to make a distinction between the two? Or does the AI work in so mysterious a way that the programmers need no longer take responsibility?

⬆️ 196 • 💬 169 • 5h ago • [charlespetzold.com](https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html)

---

**[Airbus is preparing two uncrewed combat aircraft](https://news.ycombinator.com/item?id=47382277)**

Airbus is working at full throttle to offer the German Air Force an operational Uncrewed Collaborative Combat Aircraft (UCCA) system by 2029.

⬆️ 163 • 💬 108 • 14h ago • [Airbus](https://www.airbus.com/en/newsroom/press-releases/2026-03-airbus-is-preparing-two-uncrewed-combat-aircraft-from-kratos-for-first-flight-with-a-european)

---

**[Show HN: OneCLI – Vault for AI Agents in Rust](https://news.ycombinator.com/item?id=47353558)**

Open-source credential vault, give your AI agents access to services without exposing keys. - onecli/onecli

⬆️ 160 • 💬 50 • 2d ago • [GitHub](https://github.com/onecli/onecli)

---

**[Document poisoning in RAG systems: How attackers corrupt AI's sources](https://news.ycombinator.com/item?id=47350407)**

I injected three fabricated documents into a ChromaDB knowledge base. Here’s what the LLM said next.

⬆️ 154 • 💬 49 • 3d ago • [Amine Raji, PhD](https://aminrj.com/posts/rag-document-poisoning/)

---

---

## YouTube Videos: "ai"

**[After 2,200 Years, AI Finally Decoded the Rosetta Stone — And What It Reveals Is Not Good...](https://www.youtube.com/watch?v=mlQWZsq9QbQ)**

After 2200 Years, AI Finally Decoded the Rosetta Stone — And What It Reveals Is Not Good... For more than two thousand years, ...

📺 Mystery Decoded

👁️ 5K • 👍 75 • 💬 11 • ⏱️ 24:21 • 1d ago

---

**[China’s New DuClaw AI Just Made OpenClaw Instant and Unstoppable](https://www.youtube.com/watch?v=sQRLPwcK-tU)**

China just released DuClaw, a new platform that lets anyone run OpenClaw AI agents instantly from a web browser without ...

📺 AI Revolution

👁️ 28K • 👍 758 • 💬 88 • ⏱️ 14:20 • 14h ago

---

**[Palantir CTO: &quot;You&#39;re Being Lied to About AI&quot; | Official Preview](https://www.youtube.com/watch?v=gTP9_WTqFWE)**

Join this channel to get access to perks: https://www.youtube.com/channel/UCkoujZQZatbqy4KGcgjpVxQ/join In this episode of ...

📺 Shawn Ryan Show

👁️ 79K • 👍 2K • 💬 485 • ⏱️ 3:28 • 1d ago

---

**[AI News: They All Launched the Same Thing!](https://www.youtube.com/watch?v=syx_8UlEWlA)**

Here's the AI News you probably missed this week. Head to http://hostinger.com/mattopenclaw and use the coupon code ...

📺 Matt Wolfe

👁️ 74K • 👍 3K • 💬 211 • ⏱️ 33:33 • 1d ago

---

**[Cute or Creepy? AI Fruit Babies 🍓👶 | The Strangely Satisfying AI ASMR](https://www.youtube.com/watch?v=f_gcmtfLBIk)**

Cute Fruit Babies Eating Fruit | Oddly Satisfying AI Welcome to a strange but relaxing AI world with @AI_DREAM_ASMRR.

📺 AI DREAM ASMR

👁️ 31K • 👍 1K • 💬 119 • ⏱️ 2:34 • 1d ago

---

**[Digital Optimus: Elon Musk Reveals the First True AI Worker](https://www.youtube.com/watch?v=OzXqJh6yOj4)**

Elon Musk just dropped bombshell after bombshell at the Abundance Summit — and honestly? The future of work may never look ...

📺 The AI Nexus

👁️ 8K • 👍 315 • 💬 26 • ⏱️ 18:24 • 1d ago

---

**[What&#39;s really going on with AI, Expert weighs in | TheStandup](https://www.youtube.com/watch?v=TtX3jDaZG8Y)**

ssh terminal.shop CHECK OUT THEIR NEW PODCAST ON CASEY'S YOUTUBE: @MollyRocket AI researcher Dimitri joins the ...

📺 The PrimeTime

👁️ 83K • 👍 2K • 💬 532 • ⏱️ 42:21 • 1d ago

---

**[Why Author Michael Pollan Thinks AI Won&#39;t Be Conscious](https://www.youtube.com/watch?v=Pr6hzszrvJU)**

Taken from JRE #2467 w/Michael Pollan YouTube: https://youtu.be/5QQun2pDQEs JRE on Spotify: ...

📺 JRE Clips

👁️ 179K • 👍 3K • 💬 968 • ⏱️ 15:01 • 2d ago

---

**[AI maps, realtime 3D worlds, multi-shot videos, new TTS, new anime model: AI NEWS](https://www.youtube.com/watch?v=qWzo3ws0uWU)**

HUGE AI NEWS: Qwen Image 2512, DeepSeek mHC, iQuest Coder, & more #ai #ainews #aitools #aivideo Thanks to our sponsor ...

📺 AI Search

👁️ 32K • 👍 2K • 💬 231 • ⏱️ 45:43 • 10h ago

---

**[AI vs Hollywood: Beyond Tilly Norwood](https://www.youtube.com/watch?v=VN4gjfpoEsM)**

AI vs Hollywood - Who's going to win? 00:00 AI vs. Hollywood 01:28 Youth & Immortality 02:18 AI in Oscar movies 04:38 Post ...

📺 FilmSelect

👁️ 6K • 👍 58 • 💬 21 • ⏱️ 8:52 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 61,629 • ❤️ 681 • 7d ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 4,529 • ❤️ 436 • 3d ago

---

**[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)**

*Lightricks*

LTX-2.3 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs, including images and text. It offers improved visual and audio quality, enhanced prompt adherence, and supports local execution with open weights.

`image-to-video`

⬇️ 551,479 • ❤️ 613 • 9d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 1,964,599 • ❤️ 831 • 13d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 220,810 • ❤️ 433 • 11d ago

---

**[NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Super-120B-A12B-BF16 is a 120B parameter LLM with a LatentMoE architecture, supporting up to 1M tokens context. It excels at agentic workflows, long-context reasoning, and high-volume tasks like IT automation, with configurable reasoning modes.

`text-generation` `123.6B`

⬇️ 20,858 • ❤️ 194 • 23h ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 5,659 • ❤️ 190 • 2d ago

---

**[tada-1b](https://huggingface.co/HumeAI/tada-1b)**

*Hume AI*

TADA-1B is a text-to-speech model that uses a novel 1:1 text-acoustic alignment for high-fidelity speech synthesis with reduced computational overhead. It enables dynamic duration synthesis and dual-stream generation, making it efficient for generating natural-sounding speech.

`text-to-speech` `2.2B`

⬇️ 12,801 • ❤️ 182 • 1d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 77,440 • ❤️ 171 • 4d ago

---

**[LocoTrainer-4B](https://huggingface.co/LocoreMind/LocoTrainer-4B)**

*LocoreMind*

LocoTrainer-4B is a 4B parameter text-generation model specialized for MS-SWIFT codebase analysis. It excels at multi-turn tool-calling for tasks like code navigation and report generation, leveraging a 32K context window for in-depth analysis.

`text-generation` `4.0B`

⬇️ 1,218 • ❤️ 162 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 10 • 💬 0 • ⭐ 34,577 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 25 • 💬 2 • ⭐ 27,314 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 93 • 💬 3 • ⭐ 2,786 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[TADA: A Generative Framework for Speech Modeling via Text-Acoustic Dual Alignment](https://huggingface.co/papers/2602.23068)**

*Trung Dang, Sharath Rao, Ananya Gupta et al. (9 authors)*

🏢 Hume AI

A novel tokenization scheme synchronizes acoustic features with text tokens in TTS systems, enabling unified modeling and reduced hallucinations through flow matching and text-only guidance.

▲ 6 • 💬 0 • ⭐ 686 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2602.23068) • [💻 code](https://github.com/HumeAI/tada) • [🔗 project](https://www.hume.ai/blog/opensource-tada)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 48 • 💬 2 • ⭐ 49,874 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 22 • 💬 1 • ⭐ 32,156 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 46 • 💬 1 • ⭐ 73,109 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 155 • 💬 19 • ⭐ 55,824 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights](https://huggingface.co/papers/2603.12228)**

*Yulu Gan, Phillip Isola*

🏢 Massachusetts Institute of Technology

Pretraining creates a parameter distribution where task-specific experts become more densely populated in large models, enabling effective ensemble methods for post-training adaptation.

▲ 4 • 💬 2 • ⭐ 96 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2603.12228) • [💻 code](https://github.com/sunrainyg/RandOpt) • [🔗 project](https://thickets.mit.edu)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 120 • 💬 8 • ⭐ 72,303 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 35.2k • 🔱 4.8k • 4d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 20.4k • 🔱 935 • 1d ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 11.7k • 🔱 1.4k • 1h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 9.4k • 🔱 844 • 9d ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 9.3k • 🔱 670 • 3h ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`HTML` `agency` `agent` `pip` `pua`

⭐ 7.2k • 🔱 332 • 1h ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"

`Python`

⭐ 7.2k • 🔱 910 • 11d ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 6.3k • 🔱 748 • 17h ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 3.4k • 🔱 669 • 18h ago

---

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**

Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop" 

`agent` `ai` `coding` `lowcode` `nocode`

⭐ 2.7k • 🔱 179 • 14d ago

---

---

*Generated by PeekDeck - A glance is all you need*
