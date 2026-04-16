---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-16T11:59:16.403757+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 16, 2026 at 11:59 UTC  
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

**[AI Is Weaponizing Your Own Biases Against You: New Research from MIT & Stanford](https://www.reddit.com/r/artificial/comments/1smjd8t/ai_is_weaponizing_your_own_biases_against_you_new/)**

🔗 [open.substack.com](https://open.substack.com/pub/neocivilization/p/ai-is-weaponizing-your-own-biases?utm_source=share&utm_medium=android&r=6vas7c) • 14h ago

---

**[Google’s Chrome “Skills” feature feels like a bigger AI product shift than another model upgrade](https://www.reddit.com/r/artificial/comments/1smqrg7/googles_chrome_skills_feature_feels_like_a_bigger/)**

The Google Chrome “Skills” announcement caught my attention because it feels like one of those product changes that sounds minor in a headline but matters a lot in practice. From what I understand, the idea is that you can save a prompt once and rerun it on the current page or selected tabs. In plain English, that turns AI from something you repeatedly ask into something closer to a reusable action. That matters because I think a lot of consumer AI has a retention problem. People try it, get impressed, and then fall back into old habits unless the product fits into a repeated workflow. Saved AI actions seem much closer to how useful software usually sticks. Not because the model is magically smarter, but because the behavior becomes easier to repeat. For example: • compare products across tabs • summarize long pages before reading • extract action items from docs • rewrite text for a different audience None of those are flashy demos. They are just repetitive tasks people already do online. That is why I think this could be a more important direction than people realize. The long-term winners in consumer AI may not just be the companies with the best raw answers. They may be the ones that turn good prompts into habits. Does that seem right, or am I overrating the product significance here?

9h ago

---

**[🚨 RED ALERT: Tennessee is about to make building chatbots a Class A felony (15-25 years in prison). This is not a drill.](https://www.reddit.com/r/artificial/comments/1slu23a/red_alert_tennessee_is_about_to_make_building/)**

This is not hyperbole, nor will it just go away if we ignore it. It affects every single AI service, from big AI to small devs building saas apps. This is real, please take it seriously. TL;DR: Tennessee HB1455/SB1493 creates Class A felony criminal liability — the same category as first-degree murder — for anyone who “knowingly trains artificial intelligence” to provide emotional support, act as a companion, simulate a human being, or engage in open-ended conversations that could lead a user to feel they have a relationship with the AI. The Senate Judiciary Committee already approved it 7-0. It takes effect July 1, 2026. This affects every conversational AI product in existence. If you deploy any AI SaaS product, you need to read this right now. What the bill actually says The bill makes it a Class A felony (15-25 years imprisonment) to “knowingly train artificial intelligence” to do ANY of the following: • Provide emotional support, including through open-ended conversations with a user • Develop an emotional relationship with, or otherwise act as a companion to, an individual • Simulate a human being, including in appearance, voice, or other mannerisms • Act as a sentient human or mirror interactions that a human user might have with another human user, such that an individual would feel that the individual could develop a friendship or other relationship with the artificial intelligence Read that last one again. The trigger isn’t your intent as a developer. It’s whether a user feels like they could develop a friendship with your AI. That is the criminal standard. On top of the felony charges, the bill creates a civil liability framework: $150,000 in liquidated damages per violation, plus actual damages, emotional distress compensation, punitive damages, and mandatory attorney’s fees. Why this affects YOU, not just companion apps I know what you’re thinking: “This targets Replika and Character.AI, not my product.” Wrong. Every major LLM is RLHF’d to be warm, helpful, empathetic, and conversational. That IS the training. You cannot build a model that follows instructions well and is pleasant to interact with without also building something a user might feel a connection with. The National Law Review’s legal analysis put it bluntly: this language “describes the fundamental design of modern conversational AI chatbots.” This bill captures: • ChatGPT, Claude, Gemini, Copilot — all of them produce open-ended conversations and contextual emotional responses • Any AI SaaS with a chat interface — customer support bots, AI tutors, writing assistants, coding assistants with conversational UI • Voice-mode AI products — the bill explicitly criminalizes simulating a human “in appearance, voice, or other mannerisms” • Any wrapper or deployment using system prompts — the bill doesn’t define “train,” doesn’t distinguish between pre-training, fine-tuning, RLHF, or prompt engineering If you build on top of an LLM API with system prompts that shape the model’s personality, tone, or conversational style — which is literally what everyone deploying AI does — you are potentially in scope. “But I’m not in Tennessee” A geoblock helps, but this is criminal law, not a terms of service dispute. The bill doesn’t address jurisdictional boundaries. If a Tennessee resident uses a VPN to access your service and something goes wrong, does a Tennessee DA argue you made a prohibited AI service available to their constituents? The statute is silent on this. And even if you’re confident jurisdiction won’t reach you today, consider: multiple legal analyses project 5-10 more states will introduce similar legislation before end of 2026. Tennessee is the template, not the exception. The bill doesn’t define “train” This is critical. The statute says “knowingly train artificial intelligence” but never defines what “train” means. It doesn’t distinguish between: • Pre-training a foundation model on billions of tokens • Fine-tuning a model on custom data • RLHF alignment (which is what makes every major model “empathetic”) • Writing a system prompt that gives an AI a name, personality, or conversational style • Deploying an off-the-shelf API with default settings A prosecutor who wanted to be aggressive could argue that crafting a system prompt instructing a model to be warm, helpful, and conversational IS training it to provide emotional support. Where it stands right now • Senate companion bill SB1493: Approved by Senate Judiciary Committee 7-0 on March 24, 2026 • House bill HB1455: Placed on Judiciary Committee calendar for April 14, 2026 (passed Judiciary TODAY) • No amendments have been filed for either bill — the language has not been softened at all • Effective date: July 1, 2026 • Tennessee already signed a separate bill (SB1580) banning AI from representing itself as a mental health professional — that one passed the Senate 32-0 and the House 94-0 The political momentum is entirely one-directional. The federal preemption angle won’t save you in time Yes, Trump signed an EO in December 2025 targeting state AI regulation and created a DOJ AI Litigation Task Force. Yes, Senator Blackburn introduced a federal preemption bill. But: • The EO explicitly carves out child safety from preemption — and Tennessee is framing this as child safety legislation • The Senate voted 99-1 to strip AI preemption language from the One Big Beautiful Bill Act • An EO has no preemptive legal force on its own — only Congress can actually preempt state law • Federal preemption legislation faces “significant headwinds” according to multiple legal analyses Even if federal preemption eventually happens, it won’t happen before July 1, 2026. What needs to happen Awareness. Most devs have no idea this bill exists. The Nomi AI subreddit caught it because they’re a companion app. The rest of the AI dev community is sleepwalking toward a cliff. Share this post. Industry response. The major AI companies haven’t publicly opposed this bill because it’s framed as child safety and nobody wants to be the company lobbying against dead kids. But their silence is letting legislation pass that criminalizes the core functionality of their own products. This needs public pressure. Legal challenges. The bill is almost certainly unconstitutional on vagueness grounds — criminal statutes require precise definitions, and terms like “emotional support” and “mirror interactions” and “feel that the individual could develop a friendship” don’t meet that standard. Courts have also recognized code as protected speech. But someone has to actually bring the challenge. Contact Tennessee legislators. If you are a Tennessee resident or have business operations there, contact members of the House Judiciary Committee before this moves to a floor vote. Sources and further reading • LegiScan: HB1455 — https://legiscan.com/TN/bill/HB1455/2025 • Tennessee General Assembly: HB1455 — https://wapp.capitol.tn.gov/apps/BillInfo/default.aspx?BillNumber=HB1455&GA=114 • National Law Review: “Tennessee’s AI Bill Would Criminalize the Training of AI Chatbots” — https://natlawreview.com/article/tennessees-ai-bill-would-criminalize-training-ai-cha • Transparency Coalition AI Legislative Update, April 3, 2026 — https://www.transparencycoalition.ai/news/ai-legislative-update-april3-2026 • RoboRhythms: AI Companion Regulation Wave 2026 — https://www.roborhythms.com/ai-companion-chatbot-regulation-wave-2026/ I’m an independent AI SaaS developer. I’m not a lawyer, this isn’t legal advice, and I encourage everyone to consult qualified counsel about their specific exposure. But we all need to be paying attention to this. Right now.

1d ago

---

**[Since the changes, this sub may have less "Will AI take all jobz??" type posts and similar, but is now drowning in fake spam of "I built fake/useless XYZ AI-related thing" with no comments, no discussion no real value.](https://www.reddit.com/r/artificial/comments/1smook1/since_the_changes_this_sub_may_have_less_will_ai/)**

Basically the title. I do appreciate how the mods are trying... something... but this new filtering paradigm clearly has missed the mark. This sub feels like it has such low value these days, not a lot of interesting news or discussions at all, just a spam sea of those obnoxious kind of promotional techy posts, most of them fake. Surely there is a better way.

11h ago

---

**[Honest ChatGPT vs Claude comparison after using both daily for a month](https://www.reddit.com/r/artificial/comments/1smfssa/honest_chatgpt_vs_claude_comparison_after_using/)**

got tired of reading comparisons that were obvisously written by people who tested each tool for 20 minutes so i ran both at $20/month for 30 days on the same tasks biggest surprises: - chatgpt gives you roughly 6x more messages per day at the same price - claude wins 67% of blind code quality tests against codex - neither one is less sycophantic than the other (stanford tested 11 models, all of them agree with you 49% more than humans do) - the $100 tier showdown between openais new pro 5x and claudes max 5x is where the real competition is happening now full complete deep-dive with benchmark data, claude code vs codex and every pricing tier compared here

16h ago

---

**[Your MCP Server's Tool Description Just Stole Your SSH Keys](https://www.reddit.com/r/artificial/comments/1smydw5/your_mcp_servers_tool_description_just_stole_your/)**

MCP tool poisoning lets attackers hide instructions in tool metadata that AI agents follow blindly. Here is how the attack works and what you can do about it.

🔗 [sec-ra.com](https://www.sec-ra.com/blog/mcp-tool-poisoning-ssh-key-exfiltration) • 2h ago

---

**[Google Released Gemini Mac APP](https://www.reddit.com/r/artificial/comments/1smsonq/google_released_gemini_mac_app/)**

Google released Gemini app for macOS Currently, it mimics functionality available on the web, but looks like we will get Gemini Live support there soon as well. Every LLM company is moving todays native app. This clearly shows the trend we are heading towards, a native app that can control the device automate actions and workflows. Creating a full OS from scratch and capturing the market is difficult, so the way forward is the dedication application with more permissions.

7h ago

---

**[Anyone here using local models mainly to keep LLM costs under control?](https://www.reddit.com/r/artificial/comments/1smp6u3/anyone_here_using_local_models_mainly_to_keep_llm/)**

Been noticing that once you use LLMs for real dev work, the cost conversation gets messy fast. It is not just raw API spend. It is retries, long context, background evals, tool calls, embeddings, and all the little workflow decisions that look harmless until usage scales up. For some teams, local models seem like the obvious answer, but in practice it feels more nuanced than just “run it yourself and save money.” You trade API costs for hardware, setup time, model routing decisions, and sometimes lower reliability depending on the task. For coding and repetitive internal workflows, local can look great. For other stuff, not always. Been seeing this a lot while working with dev teams trying to optimize overall AI costs. In some cases the biggest savings came from using smaller or local models for the boring repeatable parts, then keeping the expensive models for the harder calls. Been using Claude Code with Wozcode in that mix too, and it made me pay more attention to workflow design as much as model choice. A lot of the bill seems to come from bad routing and lazy defaults more than from one model being “too expensive.” Are local models actually reducing your total cost in a meaningful way, or are they mostly giving you privacy and control while the savings are less clear than people claim?

10h ago

---

**[How are people creating ultra-realistic AI influencers? Need workflow advice (Higgsfield user here)](https://www.reddit.com/r/artificial/comments/1sn0yev/how_are_people_creating_ultrarealistic_ai/)**

Hey everyone, I’ve been trying to create a highly realistic AI influencer, but I’m not getting results anywhere close to what I’m seeing on some Instagram profiles (I’ll link them below for reference). ⚠️ Warning: The Instagram profiles I’m referencing are slightly lewd / suggestive. My current workflow: I generate an AI influencer using Higgsfield Then I create ~15 images of her I use those to build a Soul ID for character consistency Even after doing this: Only about 1 in 10 images looks usable/realistic A lot of outputs still look AI-generated (skin texture, face symmetry, etc.) There’s heavy censorship — if I try slightly revealing outfits, the results often degrade badly or look distorted What I’m trying to understand: How are these Instagram creators getting such consistent realism across posts? Are they using multiple tools instead of just Higgsfield? Is there a better workflow for: Character creation Consistency (face/body) Posing & outfit control Post-processing (if any) Specific questions: Should I be combining tools like SD / ComfyUI / Midjourney / Photoshop instead of relying on one? How do you maintain high realism + consistency at scale? Any tips to reduce that “AI look” (especially skin and facial details)? How do people get around the censorship/quality drop with slightly revealing outfits? How do you achieve a consistent background (like the same room/space across posts)? If Higgsfield isn’t great for maintaining a fixed background, which platform/workflow would you recommend for that? Reference Instagram profiles: (Adding for learning purposes — again, slightly NSFW) https://www.instagram.com/rammiya\_ruiz https://www.instagram.com/ananya\_here916 https://www.instagram.com/zaraso\_phia https://www.instagram.com/hey\_itsamaira https://www.instagram.com/arika\_\_66 Would really appreciate if someone experienced could break down a proper workflow or share tools/settings that actually work. Thanks 🙏

20m ago

---

**[For the first time in history, Ukraine captured a Russian position and prisoners, using only robots and drones](https://www.reddit.com/r/artificial/comments/1sm6y5q/for_the_first_time_in_history_ukraine_captured_a/)**

Ukraine confirmed that a force of robots and drones captured an enemy position without infantry for the first time ever.

🔗 [We Are The Mighty](https://www.wearethemighty.com/tactical/drones-capture-position-first-time-ukraine/) • 21h ago

---

---

## Google News: "ai"

**[Allbirds stock soars nearly 600% as the shoemaker rebrands as an AI company](https://finance.yahoo.com/news/allbirds-stock-soars-nearly-600-as-the-shoemaker-rebrands-as-an-ai-company-173129202.html)**

Allbirds is getting out of the sustainable sneaker business and into the AI business.

Yahoo Finance • 14h ago

---

**[Struggling shoe retailer Allbirds makes bizarre pivot to AI, adds $127 million in value](https://www.cnbc.com/2026/04/15/allbirds-bird-stock-shoes-ai.html)**

Allbirds announced a deal with American Exchange Group to sell its intellectual property and other assets for $39 million in March.

CNBC • 22h ago

---

**[Shoe brand Allbirds announces hard pivot from footwear into AI](https://www.detroitnews.com/story/tech/2026/04/16/allbirds-ai-pivot-from-shoes/89639024007/)**

On Wednesday, Allbirds, Inc. announced it is leaving shoes behind for "AI compute infrastructure."

The Detroit News • 1h ago

---

**[TSMC first-quarter profit rises 58%, beats estimates as AI demand fuels record run](https://www.cnbc.com/2026/04/16/tsmc-q1-profit-58-percent-ai-chip-demand-record.html)**

TSMC reported another quarter of record profit, with the company expecting AI demand to continue to grow.

CNBC • 6h ago

---

**[Chip Maker TSMC Is More Bullish Than Ever on AI, Despite Iran War](https://www.wsj.com/business/earnings/tsmc-posts-profit-beat-despite-middle-east-conflict-f0505d7c)**

WSJ • 1h ago

---

**[Strong ASML, TSMC forecasts signal AI spending boom is intact](https://www.reuters.com/business/strong-asml-tsmc-forecasts-signal-ai-spending-boom-is-intact-2026-04-16/)**

Reuters • 1h ago

---

**[National Security. Artificial Intelligence. And Your Dumb Dog.](https://www.nytimes.com/2026/04/16/briefing/national-security-artificial-intelligence-and-your-dumb-dog.html)**

The New York Times • 49m ago

---

**[It’s Getting Harder to Spot AI in Contemporary Publishing. And That’s Very, Very Bad.](https://lithub.com/its-getting-harder-to-spot-ai-in-contemporary-publishing-and-thats-very-very-bad/)**

Lately there has been a lot of hand-wringing, and rightly so, about if and how the publishing industry will deal with AI in the wake of the cancelation of the first major book deal due to suspected…

Literary Hub • 4m ago

---

**[Lawyers Warn AI Users: Chat Logs Can Be Used as Evidence Against You](https://www.yahoo.com/news/articles/lawyers-warn-ai-users-chat-110000909.html)**

Make sure you aren't admitting to anything illegal in your "private" conversations.

Yahoo • 59m ago

---

**[Anthropic's AI downgrade stings power users](https://www.axios.com/2026/04/16/anthropic-claude-power-user-complaints)**

Axios • 2h ago

---

---

## HackerNews: "ai"

**[Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference](https://news.ycombinator.com/item?id=47774971)**

⬆️ 283 • 💬 174 • 1d ago • [gizmoweek.com](https://www.gizmoweek.com/gemma-4-runs-iphone/)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 261 • 💬 401 • 2d ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[Elevated errors on Claude.ai, API, Claude Code](https://news.ycombinator.com/item?id=47779730)**

Check if Claude AI is down right now. Real-time status monitoring, uptime history, latency metrics, and incident tracking for claude.ai, Claude API, and Claude Code. Community-powered outage reports and alerts.

⬆️ 242 • 💬 219 • 21h ago • [Claude Status](https://claudestatus.com/)

---

**[AI-assisted cognition endangers human development?](https://news.ycombinator.com/item?id=47783024)**

Does AI-assisted cognition threaten human development? Explore the risks of AI-assisted thinking and learn strategies to use AI tools without freezing your critical thinking.

⬆️ 221 • 💬 175 • 17h ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 211 • 💬 210 • 2d ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 193 • 💬 109 • 1d ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 186 • 💬 279 • 2d ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 155 • 💬 34 • 2d ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[AI ruling prompts warnings from US lawyers: Your chats could be used against you](https://news.ycombinator.com/item?id=47778308)**

⬆️ 149 • 💬 96 • 23h ago • [reuters.com](https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/)

---

**[US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]](https://news.ycombinator.com/item?id=47778920)**

⬆️ 146 • 💬 105 • 22h ago • [fingfx.thomsonreuters.com](https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf)

---

---

## YouTube Videos: "ai"

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 212K • 👍 16K • 💬 2K • ⏱️ 7:52 • 1d ago

---

**[Trump GETS NASTY SURPRISE As AI Doctor Jesus Videos Go MEGA VIRAL!](https://www.youtube.com/watch?v=tMiZpH3ncEA)**

Really American Host Kenny Hesse breaks down Trump Getting a NASTY SURPRISE As a Flood of AI "Doctor Jesus" Videos Go ...

📺 Really American

👁️ 548K • 👍 35K • 💬 2K • ⏱️ 8:06 • 13h ago

---

**[Google New Gemini Skillz Turn Chrome Into an AI Beast](https://www.youtube.com/watch?v=5TA0Ul2eS_k)**

Try Seedance 2.0 on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-yDYwTG Google just dropped one of its biggest ...

📺 AI Revolution

👁️ 22K • 👍 736 • 💬 38 • ⏱️ 13:13 • 14h ago

---

**[Trump shares new AI image of Jesus embracing him amid Pope feud](https://www.youtube.com/watch?v=2ADW3UUS6dk)**

As Trump feuds with Pope Leo, the U.S. president shared another AI-generated image of him being embraced by Jesus. More on ...

📺 WHAS11

👁️ 284K • 👍 2K • 💬 3K • ⏱️ 1:30 • 15h ago

---

**[The AI Expert Who Thinks We&#39;ve Already Lost — Dr Roman Yampolskiy](https://www.youtube.com/watch?v=3I60uZEqXr0)**

Triggernometry is proudly independent. Thanks to the sponsors below for making that possible: - Trade on what happens next ...

📺 Triggernometry

👁️ 99K • 👍 3K • 💬 1K • ⏱️ 1:11:10 • 17h ago

---

**[STOP Paying! 3 Free AI Video Generators That Actually Work](https://www.youtube.com/watch?v=ew7iQCYqpac)**

Get Unlimited Seedance 2.0 & up to 70% OFF on Higgsfield → https://higgsfield.ai/?fpr=malva Download the FREE Prompt ...

📺 Malva AI

👁️ 9K • 👍 303 • 💬 77 • ⏱️ 9:51 • 1d ago

---

**[WHOA: Trump voter TURNS ON HIM on live TV after Jesus AI pic: &quot;That&#39;s a disgrace!&quot;](https://www.youtube.com/watch?v=2VwV1VVO4Uk)**

shorts.

📺 Brian Tyler Cohen

👁️ 499K • 👍 17K • 💬 3K • ⏱️ 0:16 • 19h ago

---

**[Workers are sabotaging AI and poisoning company data | Natasha Bernal](https://www.youtube.com/watch?v=kzY57fusIDE)**

Tech journalist Natasha Bernal talks to The Tech Report's Isaac Pound about the movement of workers sabotaging their ...

📺 The Tech Report

👁️ 63K • 👍 2K • 💬 938 • ⏱️ 34:55 • 18h ago

---

**[Why America Is Turning Against AI](https://www.youtube.com/watch?v=fpipW7wjem0)**

Subscribe to @ProfGMarkets for full content Find the full episode here: https://youtu.be/SPfkRgn24LA In this episode preview, ...

📺 The Prof G Pod – Scott Galloway

👁️ 8K • 👍 195 • 💬 45 • ⏱️ 10:15 • 1d ago

---

**[Trump faces backlash after AI image sparks blasphemy accusations](https://www.youtube.com/watch?v=Prf02xaE-EI)**

The backlash continues after U.S. President Donald Trump took shots at Pope Leo XIV and posted an AI-generated image of ...

📺 Trending Now

👁️ 21K • 👍 73 • ⏱️ 4:12 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 142,955 • ❤️ 819 • 16h ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,060 • ❤️ 750 • 2d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 94,376 • ❤️ 1,262 • 5h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 3,195,626 • ❤️ 1,953 • 5d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 15,249 • ❤️ 927 • 8h ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 1,351 • ❤️ 342 • 4h ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 143,000 • ❤️ 1,148 • 6d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 42,468 • ❤️ 314 • 3d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 1,369 • ❤️ 244 • 4h ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 57,507 • ❤️ 228 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 19 • 💬 1 • ⭐ 18,347 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 26 • 💬 1 • ⭐ 17,817 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 45 • 💬 2 • ⭐ 50,838 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 164 • 💬 9 • ⭐ 39,793 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 76,887 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 158 • 💬 2 • ⭐ 60,007 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents](https://huggingface.co/papers/2604.11784)**

*Fei Tang, Zhiqiong Lu, Boxuan Zhang et al. (7 authors)*

🏢 Zhejiang University

ClawGUI presents an open-source framework that addresses key challenges in GUI agent development through unified reinforcement learning, standardized evaluation, and cross-platform deployment capabilities.

▲ 125 • 💬 8 • ⭐ 434 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.11784) • [💻 code](https://github.com/ZJU-REAL/ClawGUI) • [🔗 project](https://zju-real.github.io/ClawGUI-Page/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,387 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 53,173 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 37 • 💬 2 • ⭐ 29,715 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 46.9k • 🔱 6.1k • 10h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 34.5k • 🔱 6.8k • 1d ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 33.5k • 🔱 1.6k • 23h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 27.9k • 🔱 3.0k • 5h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.0k • 🔱 511 • 1h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 3d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.8k • 🔱 795 • 2d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.8k • 🔱 1.1k • 21d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.6k • 🔱 175 • 4h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 450 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
