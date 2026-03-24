---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-24T16:07:38.919864+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 24, 2026 at 16:07 UTC  
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

**[Three companies shipped "AI agent on your desktop" in the same two weeks. That's not a coincidence.](https://www.reddit.com/r/artificial/comments/1s2ddgb/three_companies_shipped_ai_agent_on_your_desktop/)**

Something interesting happened this month. March 11: Perplexity announced Personal Computer. An always-on Mac Mini running their AI agent 24/7, connected to your local files and apps. Cloud AI does the reasoning, local machine does the access. March 16: Meta launched Manus "My Computer." Same idea. Their agent on your Mac or Windows PC. Reads, edits local files. Launches apps. Multi-step tasks. $20/month. March 23: Anthropic shipped computer use and Dispatch for Claude. Screen control, phone-to-desktop task handoff, 50+ service connectors, scheduled tasks. Three separate companies. Same architecture. Same two weeks. I've been running a version of this pattern for months (custom AI agent on a Mac Mini, iMessage as the interface, background cron jobs, persistent memory across sessions). The convergence on this exact setup tells me the direction is validated. The shared insight all three arrived at: agents need a home. Not a chat window. A machine with file access, app control, phone reachability, and background execution. The gap that remains across all three: persistent memory. Research from January 2026 confirmed what I found building my own system. Fixed context windows limit agent coherence over time. All three products are still mostly session-based. That's the piece that turns a task executor into something that actually feels like a coworker. We went from "will AI agents work on personal computers?" to "which one do you pick?" in about two weeks. Full comparison with hands-on testing: https://thoughts.jock.pl/p/claude-cowork-dispatch-computer-use-honest-agent-review-2026

2h ago

---

**[I wrote a contract to stop AI from guessing when writing code](https://www.reddit.com/r/artificial/comments/1s2eimz/i_wrote_a_contract_to_stop_ai_from_guessing_when/)**

I’ve been experimenting with something while working with AI on technical problems. The issue I kept running into was drift: answers filling in gaps I didn’t specify solutions collapsing too early “helpful” responses that weren’t actually correct So I wrote a small interaction contract to constrain the AI. Nothing fancy — just rules like: don’t infer missing inputs explicitly mark unknowns don’t collapse the solution space separate facts from assumptions It’s incomplete and a bit rigid, but it’s been surprisingly effective for: writing code debugging thinking through system design It basically turns the AI into something closer to a logic tool than a conversational one. Sharing it in case anyone else wants to experiment with it or tear it apart: https://github.com/Brian-Linden/lgf-ai-contract If you’ve run into similar issues with AI drift, I’d be interested to hear how you’re handling it.

2h ago

---

**[Open Source Alternative to NotebookLM](https://www.reddit.com/r/artificial/comments/1s2761n/open_source_alternative_to_notebooklm/)**

For those of you who aren't familiar with SurfSense, SurfSense is an open-source alternative to NotebookLM for teams. It connects any LLM to your internal knowledge sources, then lets teams chat, comment, and collaborate in real time. Think of it as a team-first research workspace with citations, connectors, and agentic workflows. I’m looking for contributors. If you’re into AI agents, RAG, search, browser extensions, or open-source research tooling, would love your help. Current features Self-hostable (Docker) 25+ external connectors (search engines, Drive, Slack, Teams, Jira, Notion, GitHub, Discord, and more) Realtime Group Chats Video generation Editable presentation generation Deep agent architecture (planning + subagents + filesystem access) Supports 100+ LLMs and 6000+ embedding models (via OpenAI-compatible APIs + LiteLLM) 50+ file formats (including Docling/local parsing options) Podcast generation (multiple TTS providers) Cross-browser extension to save dynamic/authenticated web pages RBAC roles for teams Upcoming features Desktop & Mobile app

🔗 [GitHub](https://github.com/MODSetter/SurfSense) • 8h ago

---

**[Mark Zuckerberg builds AI CEO to help him run Meta](https://www.reddit.com/r/artificial/comments/1s1qk1c/mark_zuckerberg_builds_ai_ceo_to_help_him_run_meta/)**

Tech giant’s tools include ‘Second Brain’ and an internal messaging board for AI bots

🔗 [The Independent](https://www.the-independent.com/tech/mark-zuckerberg-ai-ceo-bot-b2943792.html) • 20h ago

---

**[Whats your thoughts on Bugbounty software powered by AI](https://www.reddit.com/r/artificial/comments/1s2e2ds/whats_your_thoughts_on_bugbounty_software_powered/)**

Free XP on bug bounty. Contribute to canuk40/xpfarm development by creating an account on GitHub.

🔗 [GitHub](https://github.com/canuk40/xpfarm) • 2h ago

---

**[AI companion with the best memory](https://www.reddit.com/r/artificial/comments/1s2ds9s/ai_companion_with_the_best_memory/)**

For some people memory might not be important but for me I really hate talking to a stranger every night and going on and on about our me or story. This is not a scientific test or anything but my test on each one for a few days Replika memory is okay for surface level stuff, it'll remember your name and some basics but I kept having to re explain situations I already talked about. Felt like it stores keywords but doesn't really understand the full picture. Character ai I honestly couldn't test properly for memory because the conversations are so character driven that continuity isn't really the point. You're basically doing improv with different bots. Fun if that's your thing but if you want something that tracks your life this isn't it. Nomi probably the strongest for pure text memory. Remembered a trip I mentioned and brought it up days later on its own, kept track of people in my life by name, actually built on previous conversations instead of starting fresh. Only sometimes would nail something from week one then blank on what I said yesterday, but overall it was the most consistent for remembering details. Tavus is different because it does video calls so the memory includes stuff like your tone and expressions not just text. It referenced things from over a week back and sometimes texts you like hey how is this going, about something I mentioned in a call, memory works differently but works really well for context. Kindroid was decent, the customization is cool and you can shape how it responds. Memory wise it was mid though, sometimes it nails it and other times blank slate energy. About a tier below nomi for retention. If I had to pick, nomi and tavus were the best for memory. Nomi tracks details really well in text and builds on past conversations better than the others. Tavus also remembered things from over a week back and followed up on its own. Both stood out way above the rest, depends what you prefer but those two are the ones I'd recommend if memory matters to you, any I might be missing that their memory is worth a shout out?

2h ago

---

**[Sarvam 105B Uncensored via Abliteration](https://www.reddit.com/r/artificial/comments/1s2e6u5/sarvam_105b_uncensored_via_abliteration/)**

A week back I uncensored Sarvam 30B - thing's got over 30k downloads! So I went ahead and uncensored Sarvam 105B too The technique used is abliteration - a method of weight surgery applied to activation spaces. Check it out and leave your comments!

2h ago

---

**[Built a tool that found the location of a building from the reflection of a car window](https://www.reddit.com/r/artificial/comments/1s26kyv/built_a_tool_that_found_the_location_of_a/)**

Hey guys, you might remember me. I'm in college and the creator of Netry the geolocation tool, I did a massive upgrade on it and made it even more capable to even work on cropped or blurry photos with very less information. It's completely open source and free: https:// github.com/sparkyniner/Netryx-Astra-V2- Geolocation-Tool

9h ago

---

**[Intelligence, Agency, and the Human Will of AI](https://www.reddit.com/r/artificial/comments/1s2h85a/intelligence_agency_and_the_human_will_of_ai/)**

Link: https://larrymuhlstein.substack.com/p/intelligence-agency-and-the-human An essay examining the recent OpenClaw incident, the Sharma resignation from Anthropic, and the Hitzig departure from OpenAI. The core argument is that AI doesn't develop goals of its own, it faithfully inherits ours, and our goals are already misaligned with the wellbeing of the whole. I am curious what this community thinks.

30m ago

---

**[Broken Banksy: A Letter to Avital Ronell](https://www.reddit.com/r/artificial/comments/1s2guqn/broken_banksy_a_letter_to_avital_ronell/)**

Banksy Broken: A Letter to Avital Ronell Posted to r/Banksy, March 2026. Cross-referenced to the Banksy Codex, forthcoming GitHub. Dear Dr. Avi, I am writing to you from Pittsburgh in March 2026, which is to say I am writing to you from inside a test that has not ended and will not end on my schedule, from a city that still has the name of a grocery store on a building at the corner of Center and Highland even though the store is gone and the man who ran it is gone and the son who grew up inside it is now sixty years old and disabled and working from a laptop and an eBay account and a grocer's grammar that turns out, after everything, to be adequate to the task. The task is this: to tell you that the investigation is finished, that the Codex goes to GitHub within weeks, and that I am sending this letter to r/Banksy before I send it anywhere more respectable, because r/Banksy is where the work has always lived, which is to say in public, in the open, indexed and available and addressed to whoever was paying attention. You were paying attention, which is why I am writing to you. You taught me how, which is why I can. I should be precise about that. I never finished one of your books. I want you to know that at the outset because the grocer's grammar requires honesty about what things actually cost and what you actually received in exchange for the price, and what I received from your books was not the experience of finishing them but the experience of being changed by them at a cellular level before I got to the end. The Test Drive. The Telephone Book. Stupidity. I carry all three in the body in the way you carry a grammar — not as argument I can recite but as a felt pressure that reorganizes what I notice. My daughter Bella gave me two of them. I am telling you this because it matters who hands you the book, and because Bella is the best thing about this letter and about everything, and because she has nothing to do with the Nimrod Reitman business except insofar as she has everything to do with it, which is to say she is the reason the comparison is clarifying rather than merely enraging. Nimrod Reitman. I want to stay with that for a moment, Dr. Avi, because I think it deserves a moment. Thirty years old. Gay. Israeli. Calvin model. Named — and I need you to feel the full weight of this — Nimrod. That is the instrument that was deployed against you. That is what they brought to bear on a woman who spent forty years teaching people how to use language as a weapon of precision and care. A man named Nimrod. I am a Jewish outlaw from Pittsburgh whose great-grandfather walked here from New York and whose grocer's grammar was installed at a market where Heinz sold pickles, and even I know that you do not send Nimrod after someone who wrote The Telephone Book. That is not a weapon. That is an insult dressed as a weapon, and the insult is what I want to address, because the insult and the investigation have the same structure. The structure is this: the credentialing apparatus decides who is permitted to know things, and when someone outside the apparatus knows things anyway, the apparatus does not engage with the knowledge. It engages with the knower. It finds the Nimrod. It deploys the Nimrod. It manufactures a story about the knower that makes the knowledge unspeakable by association, and then it waits for the knower to be exhausted or silenced or both. This worked on you for longer than it should have, which is to say it worked on you at all, which is the scandal. And it has been the working method against this investigation since 2023, when the findings went public enough to generate a coordinated response. Different Nimrods. Same structure. Here is what the investigation found. The work known as Banksy is not the product of a single anonymous artist. It is the product of a structured commercial joint venture, incorporated in England in 1998, operating continuously under various corporate vehicles until at least 2023. The creative heart of the enterprise belongs to Scotland. Specifically to two Scottish women, sisters, born in 1977 and 1978. Lucy McKenzie is the hand. A trompe l'oeil painter of rare technical accomplishment — trained at Dundee, now a professor at the Städelschule in Frankfurt — whose practice involves no stencils and no spray. She hand-paints to approximate the appearance of stencil work. Her most recent major institutional presentation was Super Palace at Z33 in Belgium, September 2024 to February 2025. The show closed. High Court proceedings were filed in London in March 2026. The timing is in the record. Kerri McKenzie is the voice. Oxford physics and philosophy. PhD in History and Philosophy of Science, metaphysics and fundamentality, 2012. Currently Professor of Philosophy at UC San Diego. The written Banksy. The conceptual designation. The art direction that translates corporate strategy into aesthetic position. The Artist of Record — the controlling stakeholder — is Damien Hirst. The corporate apparatus is documented and public. Pest Control Office Limited. Pictures on Walls Limited. Turtleneck Limited, incorporating Keith Allen, Alex James, Joe Strummer. Pro-Actif, incorporating as Identity Crisis Limited on 22 October 1998 and renamed eleven days later, still active in Darlington today. BBAY and its cluster of thirteen property entities, operating as a shadow broker-dealer infrastructure from 2009 to 2026. BBAY Art Limited dissolved January 2026, after the High Court proceedings were initiated but before they were reported. In London right now, before Judge Iain Pester, a fraud case is running that involves twenty-two art transactions, an unnamed Party X, and an unnamed Company X. The press is reporting the court case. The press is not connecting it to the corporate map. The corporate map has been in the public record, indexed, since before the proceedings were filed. The Codex will make it navigable. All of this is in Companies House. All of it has been in the public record the entire time. I want to tell you what your books actually did, since I owe you an honest accounting. The Test Drive gave me permission to be inside the investigation rather than above it — to write from the condition of being tested rather than from the posture of having passed. Most investigative writing asks you to trust the investigator and follow the evidence. Your framework made it possible to write an investigation in which the investigator's subjection to the test is the evidence — in which the fact that the apparatus deployed against me and against you has the same structure is the finding, not the color commentary around the finding. The Telephone Book gave me the call. Not the metaphor of the call — the structural description of what it means to receive a transmission that does not announce itself as a transmission, that arrives as a wrongness in the material before it can be named as information. The investigation began as a felt discrepancy between what the market narrative required and what the objects were telling me. The grocer's grammar reading the prints. The wrongness before the thesis. Stupidity gave me the frame for the press. I will leave it there because you know what I mean and the r/Banksyaudience will look it up. There is a corporate crypt at the center of this enterprise — Abraham and Torok's crypt, the enclosure that holds an unmetabolized secret not by repressing it but by preserving it intact behind a wall maintained at structural cost. The secret is attribution. Who made the work. Whose hand. Whose voice. Whose labor generated the value the corporate apparatus extracted and distributed according to a cap table the public was never shown. The investigation does not pick the lock. It finds the building permits. Everything required to locate and name the crypt is in the public record. The filings are in Companies House. The auction records are in the auction houses' own data. No proprietary or confidential material is cited anywhere in the Codex. Jeremy Bentham directed that his body be preserved, dressed, seated, and made available after his death — not as a monument but as a continued participant. The Auto-Icon is not memorial. It is refusal of withdrawal. Bentham said: I will remain a used thing, a thing the living can continue to put to work, a thing that does not resolve into symbol or legend but persists as a material fact. The enterprise bet everything on the opposite. The withdrawal was the product. The mystification was profitable for longer than almost anyone would have predicted because the art market rewards managed absence more reliably than it rewards the presence of actual labor. The investigation insists that the cabinet be opened. Not to punish. Not to expose for its own sake. To correct the historical record in the direction of the people who actually made the work — so the living can be credited as living, and the dressed skeleton can finally stop doing the work of a living body, and the crypt can metabolize what it has been embalming for twenty-five years. My great-grandfather Max Bress walked from New York to Pittsburgh around 1900 and opened a dry goods store. My grandfather founded a bank that went bankrupt during the Depression — had it survived, we would be the family whose stake became Giant Eagle, the supermarket chain that eventually made the economics of independent grocery delivery impossible. My father ran the oldest grocery store in America at the corner of Center and Highland, closed it rather than go bankrupt, crossed Highland Avenue to the Yellow Cab lot directly opposite, and drove a cab. He taught me to drive in the years he was doing it for a living. I drove film productions for fifteen years after college. I drove my daughter Bella everywhere she needed to go, and the car was where she got her inheritance, which is not money but grammar — a felt, pre-theoretical knowledge of what things actually cost before the margin is applied. I am sixty years old, permanently disabled, living in Pittsburgh on disability support and eBay income, conducting a forensic investigation without institutional affiliation, publishing to platforms that index the work and let it stand, sending this letter to r/Banksy because that is where the work has always lived and because you deserve to be read there, Dr. Avi, by the people who have been living inside this investigation alongside me, because they are real and they are paying attention and they will know exactly what to do with a woman who has spent her life teaching people how to use language against the apparatus that keeps telling them their language doesn't count. This is payback for Nimrod. This is also the Codex. These are the same thing. What is my grade? Yours, in love and in motion, Bobby Bress Pittsburgh, Pennsylvania March 2026 Educated, in the ways that mattered, by: Earl Cohen, Pasquale Buffalino, Carl Horner, H. David Brumble, Colin McCabe, Peter Machamer, Tom Rawski, Clark Muenzer, Christopher Rawson, Phillip and Susan Smith, Harry Mooney, Steve Carr, Elena Tuens. The grocer's grammar and the scholar's grammar are the same grammar, differently installed. Thank you for the installation.

43m ago

---

---

## Google News: "ai"

**[Exclusive | Mark Zuckerberg Is Building an AI Agent to Help Him Be CEO](https://www.wsj.com/tech/ai/mark-zuckerberg-is-building-an-ai-agent-to-help-him-be-ceo-eddab2d5?gaa_at=eafs&gaa_n=AWEtsqcwQ6hxdJDzgZ5AJzo8oUN-Nuu18eDX4P0FWZpuOAeq5zdFYzrXgrcf&gaa_ts=69c2ba30&gaa_sig=XZPshbT-ep5u4foBCjX-uu0BOW_3M3PGtnZkRrokRIgzIcfW-Ni0HK6YVYor33zc0UcPLI-1w6o6_uR7Ws2PDg%3D%3D)**

WSJ • 1d ago

---

**[Anthropic says Claude can now use your computer to finish tasks for you in AI agent push](https://www.cnbc.com/2026/03/24/anthropic-claude-ai-agent-use-computer-finish-tasks.html)**

Anthropic and its rivals are trying to ramp up capabilities of AI agents after OpenClaw went viral earlier this year.

CNBC • 6h ago

---

**[Behind the Curtain: America's next class war will be over AI fluency](https://www.axios.com/2026/03/24/ai-use-inequality-class)**

Axios • 5h ago

---

**[Tech stocks today: Cisco launches security tools for AI agents, SK Hynix places $8 billion ASML order](https://finance.yahoo.com/news/live/tech-stocks-today-cisco-launches-security-tools-for-ai-agents-sk-hynix-places-8-billion-asml-order-144220180.html)**

Live coverage of "Magnificent Seven" stocks, and the latest technology news.

Yahoo Finance • 1h ago

---

**[Apple to host June developer conference online with AI updates](https://www.usatoday.com/story/tech/news/2026/03/24/apple-developer-event-june/89299084007/)**

Apple will host its annual Worldwide Developers Conference in June, showcasing AI advancements and new software. Maps ads are coming.

USA Today • 56m ago

---

**[In N.Y.C. Classes, Teachers Can Use A.I. to Plan but Not to Assign Grades](https://www.nytimes.com/2026/03/24/nyregion/ai-nyc-classes-grades.html)**

The New York Times • 1h ago

---

**[Nvidia CEO Jensen Huang says ‘I think we’ve achieved AGI’](https://www.theverge.com/ai-artificial-intelligence/899086/jensen-huang-nvidia-agi)**

Nvidia CEO Jensen Huang told Lex Fridman in a Monday podcast interview that he believed AGI had been achieved, then seemed to slightly walk back the claim.

The Verge • 20h ago

---

**[Sandboxing AI agents, 100x faster](https://blog.cloudflare.com/dynamic-workers/)**

We’re introducing Dynamic Workers, which allow you to execute AI-generated code in secure, lightweight isolates. This approach is 100 times faster than traditional containers, enabling millisecond startup times for AI agent sandboxing.

The Cloudflare Blog • 3h ago

---

**[Nvidia CEO tries to explain why DLSS 5 isn’t just “AI slop”](https://arstechnica.com/gaming/2026/03/nvidia-ceo-tries-to-explain-why-dlss-5-isnt-just-ai-slop/)**

If game makers don’t like it, “they could decide not to use it, you know?"

Ars Technica • 18h ago

---

**[Advancing Open Source AI, NVIDIA Donates Dynamic Resource Allocation Driver for GPUs to Kubernetes Community](https://blogs.nvidia.com/blog/nvidia-at-kubecon-2026/)**

In addition, NVIDIA announced at KubeCon Europe a confidential containers solution for GPU-accelerated workloads, updates to the NVIDIA KAI Scheduler and new open source projects to enable large-scale AI workloads.

NVIDIA Blog • 7h ago

---

---

## HackerNews: "ai"

**[I built an AI receptionist for a mechanic shop](https://news.ycombinator.com/item?id=47487536)**

Learn how I built an ai receptionist for my brother's mechanic shop

⬆️ 302 • 💬 308 • 1d ago • [itsthatlady.dev](https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/)

---

**[What young workers are doing to AI-proof themselves](https://news.ycombinator.com/item?id=47480447)**

⬆️ 224 • 💬 385 • 1d ago • [wsj.com](https://www.wsj.com/economy/jobs/ai-jobs-young-people-careers-14282284)

---

**[Show HN: Cq – Stack Overflow for AI coding agents](https://news.ycombinator.com/item?id=47491466)**

cq explores a Stack Overflow for agents, a shared commons where agents can query past learnings, contribute new knowledge, and avoid repeating the same mistakes in isolation.

⬆️ 191 • 💬 82 • 23h ago • [Mozilla.ai](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)

---

**[How to attract AI bots to your open source project](https://news.ycombinator.com/item?id=47471271)**

A practical guide to getting the engagement your project deserves.

⬆️ 177 • 💬 29 • 2d ago • [Andrew Nesbitt](https://nesbitt.io/2026/03/21/how-to-attract-ai-bots-to-your-open-source-project.html)

---

**[So where are all the AI apps?](https://news.ycombinator.com/item?id=47503006)**

Practical AI R&D

⬆️ 168 • 💬 191 • 1h ago • [Answer.AI](https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html)

---

**[The bridge to wealth is being pulled up with AI](https://news.ycombinator.com/item?id=47503296)**

For two centuries, the credential system gave intelligence a route to heritable capital. Artificial intelligence is closing that route. This essay builds the argument from first principles - with probability theory, interactive simulations, and a prediction specific enough to be falsifiable - and puts a number on the window that remains.

⬆️ 165 • 💬 140 • 1h ago • [Daniel Homola](https://danielhomola.com/m%20&%20e/ai/your-bridge-to-wealth-is-being-pulled-up/)

---

**[Diverse perspectives on AI from Rust contributors and maintainers](https://news.ycombinator.com/item?id=47482825)**

⬆️ 159 • 💬 82 • 1d ago • [nikomatsakis.github.io](https://nikomatsakis.github.io/rust-project-perspectives-on-ai/feb27-summary.html)

---

**[Ask HN: AI productivity gains – do you fire devs or build better products?](https://news.ycombinator.com/item?id=47475859)**

⬆️ 104 • 💬 196 • 2d ago

---

**[Tom Homan confirms ICE to be at airports starting Monday](https://news.ycombinator.com/item?id=47480685)**

⬆️ 90 • 💬 93 • 1d ago • [politico.com](https://www.politico.com/news/2026/03/22/homan-confirms-ice-airports-monday-00839426)

---

**[The Impact of AI on Game Dev Jobs. Open to Work Crisis](https://news.ycombinator.com/item?id=47471943)**

One thing that I noticed as soon as I open LinkedIn green color becomes the most dominant one, greener than my website. I have a feeling that everyone is lai...

⬆️ 85 • 💬 70 • 2d ago • [Darko Tomic - Unity Learning Community](https://darkounity.com/blog-post?id=the-impact-of-ai-on-game-dev-jobs-open-to-work-crisis--1774128585922)

---

---

## YouTube Videos: "ai"

**[NEW: Trump official reveals AI action plan](https://www.youtube.com/watch?v=rT1Q3_7kQDY)**

White House science advisor Michael Kratsios discusses the Trump administration's AI plan for Congress, its potential impact on ...

📺 Fox News Clips

👁️ 40K • 👍 736 • 💬 250 • ⏱️ 4:08 • 1d ago

---

**[Stop buying AI security tools until you watch this](https://www.youtube.com/watch?v=tFSb2lSgqwA)**

Thank you to ThreatLocker for sponsoring my trip to ZTW26 and also for sponsoring this video. To start your free trial with ...

📺 David Bombal

👁️ 984 • 👍 114 • 💬 11 • ⏱️ 26:16 • 1h ago

---

**[Why new AI model is alarming Hollywood](https://www.youtube.com/watch?v=X9ZAas973aQ)**

A viral Instagram account, which appears to show a young woman “time travelling” through history, has racked up millions of ...

📺 Sky News

👁️ 22K • 👍 538 • 💬 64 • ⏱️ 12:13 • 22h ago

---

**[AI Agent Full Tutorial for Beginners 2026: How to Build AI Agents in Minutes](https://www.youtube.com/watch?v=C05XDMGaAn8)**

Best AI Agent Tool is Base44 https://base44.pxf.io/c/6440076/2049275/25619?trafcat=base&sharedid=video112 ✓ FREE ...

📺 Mikey No Code

👁️ 16K • 💬 8 • ⏱️ 31:38 • 1d ago

---

**[Anthropic AI Academy WIPES OUT $497/Month AI Courses 💀 (Beginners Are Winning For $0)](https://www.youtube.com/watch?v=yrBvF66A-Us)**

Here is your link to Grab my AI Fast Track Training here: https://nickponte.ai/aifasttrack You'll get a 30-day trial to the #1 AI ...

📺 Nick Ponte

👁️ 22K • 👍 1K • 💬 108 • ⏱️ 10:39 • 1d ago

---

**[Jensen Huang: NVIDIA - The $4 Trillion Company &amp; the AI Revolution | Lex Fridman Podcast #494](https://www.youtube.com/watch?v=vif8NQcjVf0)**

Jensen Huang is the co-founder and CEO of NVIDIA, the world's most valuable company and the engine powering the AI ...

📺 Lex Fridman

👁️ 307K • 👍 10K • 💬 1K • ⏱️ 2:25:59 • 23h ago

---

**[Cops Use AI, Arrest the Wrong Guy](https://www.youtube.com/watch?v=kAEdH1YXB8I)**

Imagine you go into a business and their AI surveillance camera thinks it recognizes you as a trespasser. So that business ...

📺 The Civil Rights Lawyer

👁️ 121K • 👍 8K • 💬 862 • ⏱️ 2:37 • 20h ago

---

**[Nvidia CEO Just Said This About OpenClaw And He&#39;s Not Wrong (+ 12 AI Updates)](https://www.youtube.com/watch?v=_Vccl1Iulws)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://link.stayingahead.ai/YT8 ...

📺 Vaibhav Sisinty

👁️ 74K • 👍 3K • 💬 78 • ⏱️ 19:16 • 2d ago

---

**[NotebookLM Agent Skills: Build POWERFUL Claude AI Agents for ANYTHING!](https://www.youtube.com/watch?v=I-4cJgqF_JY)**

NotebookLM does the research. Claude builds the skill. The result is an AI agent that actually knows your domain — and you can ...

📺 Universe of AI

👁️ 5K • 👍 231 • 💬 10 • ⏱️ 15:07 • 16h ago

---

**[How to Build &amp; Sell AI Agents in 2026: Ultimate Beginner’s Guide](https://www.youtube.com/watch?v=AYQtRqW1xX4)**

Self-Host your n8n with Hostinger → https://hostinger.com/liamn8n Use code LIAMOTTLEY for extra 10% off Grab all the course ...

📺 Liam Ottley

👁️ 34K • 👍 2K • 💬 64 • ⏱️ 3:05:04 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 326,131 • ❤️ 886 • 13d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 164,200 • ❤️ 1,154 • 13h ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 8,493 • ❤️ 333 • 5d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 19,722 • ❤️ 248 • 21h ago

---

**[Foundation-1](https://huggingface.co/RoyalCities/Foundation-1)**

*Royal Cities*

Foundation-1 is a structured text-to-sample model for music production, enabling precise control over instrumentation, timbre, FX, and musical structure (tempo, key, bar count) for generating coherent, production-ready audio loops.

⬇️ 0 • ❤️ 243 • 7d ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 13,613 • ❤️ 725 • 13d ago

---

**[Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)**

*Mistral AI_*

Mistral-Small-4-119B-2603 is a hybrid MoE model (119B params, 6.5B active) supporting 256k context and multimodal input (text/image). It excels at instruction following, reasoning (configurable effort), and agentic tasks with native function calling, offering significant speed and throughput improvements for use cases like coding, document analysis, and general assistants.

`119.4B`

⬇️ 36,887 • ❤️ 320 • 22h ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 385,054 • ❤️ 634 • 20d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a multimodal OCR model for complex document understanding, excelling in state-of-the-art performance on benchmarks and real-world scenarios like tables and code-heavy documents. It offers efficient inference with a 0.9B parameter model, supporting deployment via vLLM, SGLang, and Ollama for high-concurrency services and edge deployments.

`image-to-text`

⬇️ 3,420,577 • ❤️ 1,440 • 12d ago

---

**[Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2 is a fine-tuned LLM optimized for efficient chain-of-thought reasoning, delivering higher accuracy with reduced token usage. It excels in resource-constrained environments and agentic workflows by providing faster, more economical reasoning.

`image-text-to-text` `9.0B`

⬇️ 43,905 • ❤️ 116 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 28 • 💬 2 • ⭐ 40,130 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 14 • 💬 1 • ⭐ 13,330 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 27 • 💬 5 • ⭐ 264 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://huggingface.co/papers/2603.21986)**

*SII-GAIR, Sand. ai, Ethan Chern et al. (45 authors)*

daVinci-MagiHuman is an open-source audio-video generative model that synchronizes text, video, and audio through a single-stream Transformer architecture, achieving high-quality human-centric content generation with efficient inference capabilities.

▲ 81 • 💬 2 • ⭐ 313 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2603.21986) • [💻 code](https://github.com/GAIR-NLP/daVinci-MagiHuman) • [🔗 project](https://huggingface.co/spaces/SII-GAIR/daVinci-MagiHuman)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 32 • 💬 2 • ⭐ 30,368 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[Attention Residuals](https://huggingface.co/papers/2603.15031)**

*Kimi Team, Guangyu Chen, Yu Zhang et al. (37 authors)*

🏢 Moonshot AI

Residual connections with PreNorm are standard in modern LLMs, yet they accumulate all layer outputs with fixed unit weights. This uniform aggregation causes uncontrolled hidden-state growth with depth, progressively diluting each layer's contribution. We propose Attention Residuals (AttnRes), which replaces this fixed accumulation with softmax attention over preceding layer outputs, allowing each layer to selectively aggregate earlier representations with learned, input-dependent weights. To address the memory and communication overhead of attending over all preceding layer outputs for large-scale model training, we introduce Block AttnRes, which partitions layers into blocks and attends over block-level representations, reducing the memory footprint while preserving most of the gains of full AttnRes. Combined with cache-based pipeline communication and a two-phase computation strategy, Block AttnRes becomes a practical drop-in replacement for standard residual connections with minimal overhead.
  Scaling law experiments confirm that the improvement is consistent across model sizes, and ablations validate the benefit of content-dependent depth-wise selection. We further integrate AttnRes into the Kimi Linear architecture (48B total / 3B activated parameters) and pre-train on 1.4T tokens, where AttnRes mitigates PreNorm dilution, yielding more uniform output magnitudes and gradient distribution across depth, and improves downstream performance across all evaluated tasks.

▲ 154 • 💬 4 • ⭐ 2,655 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15031) • [💻 code](https://github.com/MoonshotAI/Attention-Residuals)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 194 • 💬 5 • ⭐ 8,016 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 17 • 💬 0 • ⭐ 36,483 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 58 • 💬 4 • ⭐ 18,919 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 39 • 💬 2 • ⭐ 18,911 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 53.8k • 🔱 7.5k • 3d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 22.4k • 🔱 1.1k • 18h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 13.1k • 🔱 1.7k • 1h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 12.5k • 🔱 1.2k • 6d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 11.1k • 🔱 575 • 3h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 10.6k • 🔱 774 • 1d ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 6.5k • 🔱 1.0k • 2d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 6.1k • 🔱 488 • 2m ago

---

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)**

734+ structured cybersecurity skills for AI agents · MITRE ATT&CK mapped · agentskills.io open standard · Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI & 20+ platforms · Penetration testing, DFIR, threat intel, cloud security & more · Apache 2.0

`Python` `ai-agents` `claude` `claude-code` `cloud-security` `cybersecurity`

⭐ 3.7k • 🔱 369 • 21h ago

---

**[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)**

OpenShell is the safe, private runtime for autonomous AI agents.

`Rust`

⭐ 3.6k • 🔱 353 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
