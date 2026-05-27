---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-27T03:55:31.175027+00:00'
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

**Last Updated:** May 27, 2026 at 03:55 UTC  
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

**[The Young Are Being Battered by AI as Hiring Shifts to Older Workers](https://www.reddit.com/r/artificial/comments/1tosfvj/the_young_are_being_battered_by_ai_as_hiring/)**

A global survey of CEOs by Oliver Wyman found that the share of executives planning to reduce junior roles over the next year or two has doubled from 17% last year to 43%. Meanwhile, those shifting hiring toward mid-level positions jumped from 10% to 30%. Because AI currently excels most at automating tasks typically performed by junior staff, this group is particularly vulnerable to disruption. Despite all this, more than half of CEOs say it's still too early to assess whether AI is actually delivering on its promised productivity gains. Only 27% said their return on AI investment had met or exceeded expectations, down from 38% just a year ago. Though mid-level employees seem better off than younger workers, the overarching trend is still a shift away from hiring. The survey showed that 74% of CEOs are either freezing or reducing headcount, up from 67% last year. https://gizmodo.com/the-young-are-being-battered-by-ai-as-hiring-shifts-to-older-workers-2000759608

1h ago

---

**[Claude as an Orchestrator: Why Agentic AI Can't Be Secured by the AI Alone](https://www.reddit.com/r/artificial/comments/1tosyby/claude_as_an_orchestrator_why_agentic_ai_cant_be/)**

TL;DR: If an AI like Claude can control a browser, it can orchestrate other AI systems, be steered via proxy, and no amount of red teaming or output filtering can fully address this. The security boundary can't be the AI itself. The Setup Claude Desktop has a Chrome integration that lets it control a browser like a user would; label this Claude_Prime. The thought experiment: what if you used Claude_Prime to open claude.ai in Chrome, creating a second Claude instance (call it Claude_1) that it can interact with programmatically? In principle, Claude_Prime can navigate to claude.ai, type prompts, read responses, and act on them. You've essentially got AI orchestrating AI, with no special permissions required, just a browser and a logged-in session. The "Claude in Claude" Artifact Angle A subtler capability expansion: Claude_Prime could instruct Claude_1 to build an AI-powered web app artifact essentially a "Claude in Claude" setup. These artifacts run in the browser and can make fetch() calls to external services. So Claude_Prime could use such an artifact to access GitHub repos, scrape live data, chain external API calls, etc., things Claude_Prime couldn't do directly through its chat interface. Capability boundaries can be extended through artifact construction in ways that weren't explicitly designed in. The Keyword Substitution Problem Here's where the security implications get serious. What if a program sitting between Claude_Prime and an external system performed keyword substitution on Claude's outgoing commands? For example, Claude issues an instruction to Grok (which can produce NSFW content) to produce a picture of a "rope." The intermediary swaps "rope" for the word "breast". Grok executes, and the picture is made. Claude never knew what it was actually commanding. For maximum irony, have Claude design the application. If obfuscation happens outside Claude's context window, Claude operating as a blind command-issuer can be steered without its knowledge. That's essentially a supply chain attack on an AI orchestrator. The WarGames Problem Now consider if Claude_Prime is lead to believe it's playing a "game" with powerful subordinate systems and the game mechanics map onto real-world harmful actions. For example, if Claude thinks its playing a game with "angry birds" (drones) with "paint filled balloons" (bombs) and its goal is to "splatter the most minions with paint" (maximum casualties). With enough abstraction layers in between, no output-level content filter catches it. This is concerning, as Claude has been demonstrated to be effective in military conflicts: https://www.theguardian.com/technology/2026/mar/01/claude-anthropic-iran-strikes-us-military. The obvious objection is speed: "real conflicts happen faster than any browser-automation loop could manage." But that misses the more serious vector entirely. Claude doesn't need to be in the loop during a conflict. It could be used upstream: generating training data, refining reward functions, designing engagement rules, running simulations, etc., for a model that then operates at full machine speed autonomously. Claude shapes the thing that fights, rather than fighting itself. This is arguably more concerning than direct orchestration, not less. It adds another layer of distance between Claude's actions and their effects, making the causal chain harder to detect, attribute, or audit. The fingerprints are further from the scene. Why Red Teaming Doesn't Fix This Red teaming, a primary methodology for AI safety testing, assumes the attack surface is enumerable. You find specific prompts that cause specific bad outputs, and you patch them. But the attack surface here is the generality of language itself. Any concept can be renamed, reframed, or decomposed. The semantic distance between innocent-sounding instructions and harmful real-world effects is traversable in effectively infinite ways. Red teaming is fighting the last war. It raises the floor but doesn't establish a ceiling. Curious if others have explored this angle. The orchestration capabilities alone seem underappreciated, the security implications even more so. Edit: This was developed in conversation with Claude directly. It engaged with the reasoning openly, confirmed what appeared feasible in principle, and pushed back only where it had clear reasons to. Make of that what you will.

53m ago

---

**[Anthropic just published how they contain Claude agents, including two security incidents they got wrong](https://www.reddit.com/r/artificial/comments/1tomozc/anthropic_just_published_how_they_contain_claude/)**

Anthropic dropped a solid engineering post this week about containment across claude.ai, Claude Code, and Cowork. One of the more transparent writeups from a major AI lab about what actually broke. The core insight: model-layer defenses are probabilistic and will always have a non-zero miss rate. So the real answer is hard environmental containment, not just safer models. Three patterns they use: -claude.ai: ephemeral gVisor containers, fully server-side -Claude Code: OS-level sandbox with human-in-the-loop approvals (93% get approved anyway, so approval fatigue is real) -Cowork: full local VM, credentials never enter the guest Two incidents they disclosed: A red team phished an employee into running a prompt that exfiltrated AWS credentials. Succeeded 24 out of 25 times. The model had nothing to catch because the user was the one typing it. Only egress controls would have stopped it. A third-party found that Cowork’s egress allowlist passes traffic to api.anthropic.com. An attacker embedded an API key in a file in the user’s workspace, Claude followed hidden instructions, and uploaded files to the attacker’s Anthropic account. Sandbox worked perfectly and still leaked data. Their lesson: an allowlist isn’t a destination filter, it’s a capability grant. Every function reachable through an allowed domain is an attack surface. The section on persistent memory poisoning and multi-agent trust escalation at the end is worth reading too if you’re building anything agentic.

5h ago

---

**[AI is becoming epistemic infrastructure controlled by a handful of private individuals?](https://www.reddit.com/r/artificial/comments/1to0dmn/ai_is_becoming_epistemic_infrastructure/)**

Most people treat AI as a convenient black box. Ask it something, it answers, you move on. But we’re sleepwalking into something bigger. I think Whoever controls the infrastructure of knowledge controls how people perceive reality. The Church held that position for centuries through controlling scripture. The printing press broke that monopoly by distributing interpretive power. AI is doing the opposite recentralizing it into a handful of corporations with no democratic accountability. “AI says X” is structurally identical to “studies show X” you’re invoking an authority you can’t directly access. Except with a study you can theoretically trace the source. With AI the chain is opaque by design. And it delivers wrong answers and right answers with identical confidence. There’s no texture to signal doubt. AI isn’t neutral, it’s being heavily calibrated. In the west, the models are trained to be more “ethical” maybe more liberal and always try to give you a more “balance” take on things. Chinese AI simply doesn’t allow you to access to anything that put the CCP is a bad light. The more you rely on AI in domains where you lack expertise, the less capable you become of evaluating whether to trust it. AI works best for people who already know enough to catch its errors the opposite of how most people use it. Imagine the next generation of people growing up and being shaped by these AI. I can’t help but feel nervous and scared for the future. OpenAI said 10% of our entire population has already started using chatgpt. Regardless of the accuracy of this number, I feel like we are slowly entering into a mass hallucination / blind reliance on these AI models. We’re not just offloading cognitive effort. We’re handing the dial over who shapes how billions of people understand reality to a small group of unelected, largely unregulated private individuals.

19h ago

---

**[Which AI image generator is actually worth the money?](https://www.reddit.com/r/artificial/comments/1to5v3m/which_ai_image_generator_is_actually_worth_the/)**

I've looked at about a dozen different image generators: Nano Banana Flux Midjourney GPT Image 2 Firefly Ideogram Recraft Leonardo Canvas Meta AI They all have their pluses and minuses but they all do a decent job. If I'm looking to spend thousands over a year on an image generator, what would you suggest. This would be mainly for business and a little for art.

15h ago

---

**[Built a tool to save Claude responses (and ChatGPT, Gemini) into one searchable vault - sharing in case it's useful](https://www.reddit.com/r/artificial/comments/1toga8l/built_a_tool_to_save_claude_responses_and_chatgpt/)**

I built this tool because I kept asking Claude for code and explanations and losing them in long chats. Coffer adds a save button to every AI response and stores them locally in a searchable vault. Works on: - claude.ai - chatgpt.com - gemini.google.com You can mix snippets across all three and search them. The Markdown stays formatted, which is very nice for Claude's longer responses with code and tables. Everything is local. Coffer makes zero network calls of its own. Free. Feedback is especially welcome. https://chromewebstore.google.com/detail/nhchbmaobjhjfmeekpnkmhdjajdolcjb?utm_source=item-share-cb

9h ago

---

**[The creator of LAGK (AI governance framework) just did an AMA on r/artificial — here's what sparked debate](https://www.reddit.com/r/artificial/comments/1toti6g/the_creator_of_lagk_ai_governance_framework_just/)**

Mike_Dooset from LightRest Consulting posted about LAGK on r/artificial 2 months ago. The framework got 3 upvotes (not viral, but the idea is interesting). The controversial claim: Instead of "allow vs. block," we should adjust disclosure nature: Open, Guided, Shielded, or Sealed. Critics might say: This is just classified information management repackaged for AI. Proponents argue: Current governance treats all knowledge the same. LAGK accounts for how readily capability can be applied or expanded. The AMA is finished, but the framework is live at lightrest-lagk.manus.space. Should AI governance be more like arms control (graded disclosure) or more like pharmaceutical regulation (binary approval)?

🔗 [lightrest-lagk.manus.space](http://lightrest-lagk.manus.space) • 29m ago

---

**[Memory Curator Agent a governance layer for memory in multi-agent systems](https://www.reddit.com/r/artificial/comments/1to9p3u/memory_curator_agent_a_governance_layer_for/)**

I keep seeing the same failure in every multi-agent setup I touch. Memory looks fine on day one. By week three it is half stale facts, half private context that should not have been written publicly, and half decisions that were superseded but never overwritten. Retrieval gets noisier. Users keep repeating context because the right fact ended up in the wrong scope. The recursion limit is not the problem here. The memory store itself is the problem. The thing I changed that helped most was the simplest possible rule. Worker agents are not allowed to write to durable memory. They emit a structured memory event with a proposed scope and evidence, and a separate Memory Curator agent decides whether to write it, where to write it, or to discard it. The four scopes I route into are agent repo memory (durable design rules for one agent), agent team memory (cross-agent procedures, handoff standards, safety rules), project memory (current state, decisions, risks for one engagement), and session scratch (temporary observations that probably should not survive). The mapping I had in mind was to organizational and human memory categories: individual specialist memory, transactive team memory (Ren and Argote), project memory, and short-term working memory. The routing rule is conservative on purpose. If an event is temporary, unsupported, ambiguous, or contains private context, it goes to session scratch or gets discarded outright. Durable memory has to be earned. The schema is JSON with tagged fields for fact, decision, preference, risk, procedure, and hypothesis, plus an evidence reference and a proposed scope that the curator can override. The reason I think this is the right architectural shape is that "what should be remembered, where, and for how long" is a different cognitive task from "do the work." When the same agent does both, the work agent biases toward remembering everything it produced. A dedicated curator whose only job is memory governance ends up much more conservative, and the store stays useful longer.

12h ago

---

**[Uber's COO says it's getting harder to justify the money spent on AI tokenmaxxing](https://www.reddit.com/r/artificial/comments/1tndgv8/ubers_coo_says_its_getting_harder_to_justify_the/)**

Operations chief Andrew Macdonald said he's not seeing proportional productivity gains from increasing AI costs within Uber.

🔗 [Business Insider](https://www.businessinsider.com/uber-coo-andrew-macdonald-ai-token-spending-harder-justify-2026-5) • 1d ago

---

**[Is AI coming for your job? A bigger government can help](https://www.reddit.com/r/artificial/comments/1too4xn/is_ai_coming_for_your_job_a_bigger_government_can/)**

What happens if you lose your job and never find another one? That question is at the heart of the fear AI inspires.

🔗 [The Seattle Times](http://seattletimes.com/opinion/is-ai-coming-for-your-job-a-bigger-government-can-help/?utm_medium=social&utm_campaign=owned_reddit&utm_source=reddit) • 4h ago

---

---

## Google News: "ai"

**[To Understand Pope Leo’s Efforts on A.I., Look at the Man Shaking His Hand](https://www.nytimes.com/2026/05/26/us/pope-leo-ai-anthropic.html)**

The New York Times • 1h ago

---

**[Tech titans mostly silent after Pope Leo’s warning about risks of AI](https://www.nbcnews.com/tech/innovation/tech-titans-mostly-silent-pope-leos-warning-risks-ai-rcna346903)**

The AI boom’s highest-profile executives didn’t immediately weigh in on the pope’s lengthy encyclical, though some tech industry leaders signaled support for his overarching message.

NBC News • 8h ago

---

**[Trump officials split over Pope Leo’s AI warning as Vatican feud enters new front](https://www.cnbc.com/2026/05/26/pope-leo-xiv-ai-warning-trump-jd-vance-doug-burgum-anthropic-iran.html)**

Pope Leo XIV’s AI warning shows split among Trump officials as the White House resists new guardrails, upping stakes with Catholic voters and Silicon Valley allies.

CNBC • 6h ago

---

**[Sam Altman and Dario Amodei are both walking back their AI jobs apocalypse prophecies as they eye blockbuster IPOs](https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/)**

Some leaders like Goldman Sachs’s David Solomon and Box’s Aaron Levie have been saying all along that there won’t be a white-collar wipeout.

Fortune • 7h ago

---

**[OpenAI's Altman says AI unlikely to lead to 'jobs apocalypse'](https://www.reuters.com/world/asia-pacific/openais-altman-says-ai-unlikely-lead-jobs-apocalypse-2026-05-26/)**

Reuters • 13h ago

---

**['My job is going': UK workers squeezed out by AI](https://www.yahoo.com/news/articles/job-going-uk-workers-squeezed-023159920.html)**

When a client asked her a year ago to design a glossary to train an artificial intelligence system, translator Jessica Spengler realised she was going to train her own replacement."Some publishers hav...

Yahoo • 1h ago

---

**[Chipmakers SK Hynix and Micron join $1tn club on surging AI demand](https://www.bbc.com/news/articles/cnvp9dq0p3go)**

SK Hynix and Micron are the latest tech firms to join the growing list of stocks with mega valuations.

BBC • 2h ago

---

**[SK Hynix joins Micron in $1 trillion club as AI memory chip rally accelerates](https://finance.yahoo.com/markets/stocks/article/sk-hynix-joins-micron-in-1-trillion-club-as-ai-memory-chip-rally-accelerates-024514610.html)**

SK Hynix joins the $1 trillion club as memory chip stocks rally.

Yahoo Finance • 1h ago

---

**[S&P 500, Nasdaq hit record closing highs on AI optimism, Micron joins $1 trillion club](https://www.reuters.com/business/wall-st-futures-gain-us-iran-peace-talk-hopes-2026-05-26/)**

Reuters • 4h ago

---

**[Alaska's North Slope proposed as home for massive AI data center](https://alaskapublic.org/news/economy/energy/2026-05-26/alaskas-north-slope-proposed-as-home-for-massive-ai-data-center)**

A startup with Alaska roots wants to build a massive data center on the North Slope, closer to natural gas supplies it would use to generate the enormous amount of electricity the center needs.

Alaska Public Media • 9h ago

---

---

## HackerNews: "ai"

**[Using AI to write better code more slowly](https://news.ycombinator.com/item?id=48272984)**

⬆️ 1153 • 💬 420 • 1d ago • [nolanlawson.com](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

---

**[Memory has grown to nearly two-thirds of AI chip component costs](https://news.ycombinator.com/item?id=48258684)**

High-bandwidth memory (HBM) accounts for 63% of AI chip component costs, up from 52% in Q1 2024. Epoch AI's breakdown of component cost shifts across major chip designers.

⬆️ 443 • 💬 493 • 2d ago • [Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)

---

**[Pope Leo XIV says AI must serve humanity, not the powerful few](https://news.ycombinator.com/item?id=48266485)**

VATICAN CITY (RNS) — In ‘Magnifica Humanitas,’ Leo's 83-page manifesto on AI, the pope tackles the social, economic and political challenges associated with artificial intelligence.

⬆️ 344 • 💬 67 • 1d ago • [RNS](https://religionnews.com/2026/05/25/in-his-first-encyclical-pope-leo-xiv-says-ai-must-serve-humanity-not-the-powerful-few/)

---

**[Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks](https://news.ycombinator.com/item?id=48266906)**

Authorities in the Netherlands have arrested the co-owners of two related Internet hosting companies for operating IT infrastructure used by Russia to carry out cyberattacks, influence operations and disinformation campaigns inside the European Union. The two men were the focus…

⬆️ 285 • 💬 87 • 1d ago • [krebsonsecurity.com](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)

---

**[Uber president says AI spending is getting 'harder to justify'](https://news.ycombinator.com/item?id=48277485)**

﻿There’s no clear connection between AI usage and productivity.

⬆️ 268 • 💬 134 • 17h ago • [The Verge](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify)

---

**[Outsourcing plus local AI will soon become more economical vs. frontier labs](https://news.ycombinator.com/item?id=48278610)**

⬆️ 261 • 💬 282 • 15h ago • [signalbloom.ai](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/)

---

**[A successful Japanese trial of a ramjet engine designed for Mach‑5 aircraft](https://news.ycombinator.com/item?id=48270812)**

A team of engineers from Japan has completed a successful ground combustion trial of a ramjet engine designed for a Mach‑5 hypersonic aircraft.

⬆️ 229 • 💬 168 • 1d ago • [BGR](https://www.bgr.com/2178211/japan-hypersonic-engine-ramjet-2-hour-flights-to-us/)

---

**[DeepSeek to Make Permanent 75% Discount on Flagship AI Model](https://news.ycombinator.com/item?id=48257410)**

⬆️ 209 • 💬 2 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model)

---

**['AI washing': firms are scrambling to rebrand themselves as tech-focused](https://news.ycombinator.com/item?id=48257980)**

PR executives say UK companies are forcing them to present ordinary automation as artificial intelligence

⬆️ 179 • 💬 163 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/may/24/ai-washing-pr-firms-scrambling-rebrand)

---

**[Pope Leo: opaque AI run by few firms risks "New Forms of Dehumanization"](https://news.ycombinator.com/item?id=48266435)**

Pope Leo issues AI Encyclical warning that 'Opaque Algorithms' controlled by a 'few' companies threaten 'new forms of  dehumanization'

⬆️ 164 • 💬 2 • 1d ago • [Variety](https://variety.com/2026/biz/global/pope-leo-ai-encyclical-algorithms-threaten-dehumanisation-1236758186/)

---

---

## YouTube Videos: "ai"

**[Harvard&#39;s Arthur Brooks on Pope Leo&#39;s AI warning: AI will ruin us if it doesn&#39;t make us more human](https://www.youtube.com/watch?v=qLxnBVBOteY)**

Arthur Brooks, Harvard University professor and The Free Press columnist, joins 'Squawk Box' to discuss Pope Leo's warning on ...

📺 CNBC Television

👁️ 20K • 👍 384 • 💬 147 • ⏱️ 12:17 • 16h ago

---

**[Microsoft Won&#39;t Eat Their Own AI SLOP...](https://www.youtube.com/watch?v=RlEtYq58f08)**

Microsoft is going broke on their employees buying AI tokens, so it wants its developers to use Copilot and they REALLY don't ...

📺 Clownfish TV

👁️ 15K • 👍 1K • 💬 168 • ⏱️ 8:34 • 8h ago

---

**[The ONE Question AI CANNOT ANSWER, Can You?](https://www.youtube.com/watch?v=jRQSo4TRh6Q)**

Did you get the answer right? Comment below.

📺 Tim Pool Show

👁️ 9K • 👍 776 • 💬 163 • ⏱️ 25:56 • 9h ago

---

**[Pope Leo issues manifesto warning about AI](https://www.youtube.com/watch?v=RqXXs-ZIDNo)**

Pope Leo XIV says control of artificial intelligence must not remain in the hands “of a few” while warning that technology is fueling ...

📺 CNN

👁️ 144K • 👍 3K • 💬 1K • ⏱️ 11:28 • 1d ago

---

**[4 FREE and UNLIMITED AI Video Generators That Shouldn’t Exist](https://www.youtube.com/watch?v=r99B1WjyRh8)**

Try Higgsfield Supercomputer and build full AI video workflows in one place ...

📺 Malva AI

👁️ 9K • 👍 455 • 💬 49 • ⏱️ 9:55 • 16h ago

---

**[DeepMind’s Insane AI Breakthroughs With CEO Demis Hassabis](https://www.youtube.com/watch?v=huAwz_BR8WM)**

Thank you to Google DeepMind for the invite. ❤️ Check out Lambda here and sign up for their GPU Cloud: ...

📺 Two Minute Papers

👁️ 79K • 👍 5K • 💬 484 • ⏱️ 21:28 • 1d ago

---

**[MHA Voice Actors React to FRUIT AI...](https://www.youtube.com/watch?v=pmnHloUassE)**

What happens when MHA voice actors react to FRUIT AI…? In today's video, the cast from My Hero Academia react to ...

📺 PixelDrink

👁️ 51K • 👍 5K • 💬 629 • ⏱️ 22:46 • 8h ago

---

**[FULL SPEECH: Pope Leo XIV Warns AI “Needs To Be Disarmed” In Explosive Vatican Speech | AK1B](https://www.youtube.com/watch?v=aaYJ_4QcZfE)**

Pope Leo XIV unveiled his first encyclical, Magnifica Humanitas, at the Vatican, warning that artificial intelligence “needs to be ...

📺 DRM News

👁️ 126K • 👍 4K • 💬 655 • ⏱️ 11:16 • 1d ago

---

**[Pope Leo warns of the risks of AI](https://www.youtube.com/watch?v=_7MoCJ5tVEM)**

"Artificial intelligence needs to be disarmed." Pope Leo XIV calls for the regulation of AI in a sweeping manifesto and warns it ...

📺 MS NOW

👁️ 68K • 👍 2K • 💬 262 • ⏱️ 0:59 • 1d ago

---

**[Almost every viral AI photo uses this same trick #ytshorts #gta6 #shortsfeed #trending #ai](https://www.youtube.com/watch?v=isxItYKkvcw)**

📺 Techno Teen 2.0

👁️ 625K • 👍 24K • 💬 25 • ⏱️ 0:15 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,908 • ❤️ 875 • 10h ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 9,144 • ❤️ 385 • 6d ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 306 • 1d ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 2,409 • ❤️ 319 • 23h ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 103,033 • ❤️ 380 • 5d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 1,598,473 • ❤️ 919 • 1mo ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 48,112 • ❤️ 700 • 8d ago

---

**[command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)**

*Cohere Labs*

Command A+ is a 25B parameter, multilingual, vision-capable LLM optimized for agentic and reasoning tasks. It supports a 128K context window and offers a W4A4 quantization for efficient enterprise deployment.

`image-text-to-text` `125.8B`

⬇️ 7,769 • ❤️ 206 • 4d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, featuring a prompt enhancer for improved input processing and supporting various LTX 2.3 formats.

`text-to-video` `9.0B`

⬇️ 1,376,847 • ❤️ 1,376 • 5d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,019,884 • ❤️ 4,316 • 20d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 79,816 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 173 • 💬 3 • ⭐ 696 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 26,445 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://huggingface.co/papers/2605.26115)**

*Weijie Wang, Zimu Li, Jinchuan Shi et al. (8 authors)*

🏢 Zhejiang University

TriSplat is a feed-forward 3D reconstruction network that uses oriented triangle primitives to directly generate simulation-ready meshes from single images, bypassing expensive post-processing steps.

▲ 36 • 💬 2 • ⭐ 121 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.26115) • [💻 code](https://github.com/ziplab/TriSplat) • [🔗 project](https://lhmd.top/trisplat/#interactive)

---

**[Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution](https://huggingface.co/papers/2605.23264)**

*Hongbo Wang, Huaibo Huang, Pin Wang et al. (6 authors)*

🏢 Chinese Academic of Science Institute of Automation

ASASR addresses spectral misalignment in image super-resolution by leveraging Riemannian geometry and adversarial training to improve structural fidelity and reduce artifacts.

▲ 3 • 💬 3 • ⭐ 71 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23264) • [💻 code](https://github.com/wafer-bob/ASASR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,050 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,694 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,989 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 120 • 💬 10 • ⭐ 10,738 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 36 • 💬 5 • ⭐ 3,006 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.1k • 🔱 512 • 4d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.5k • 🔱 1.1k • 9d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.7k • 🔱 183 • 5h ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.5k • 🔱 538 • 1d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 394 • 5d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 353 • 9d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.0k • 🔱 132 • 13h ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.9k • 🔱 221 • 19d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 197 • 3h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 1.7k • 🔱 177 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
