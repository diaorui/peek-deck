---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-16T17:52:35.201096+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 16, 2026 at 17:52 UTC  
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

**[Qwen 3.6-35B - A3B Opensource Launched.](https://www.reddit.com/r/artificial/comments/1sn4wcs/qwen_3635b_a3b_opensource_launched/)**

⚡ Meet Qwen3.6-35B-A3B：Now Open-Source！🚀🚀 A sparse MoE model, 35B total params, 3B active. Apache 2.0 license. 🔥 Agentic coding on par with models 10x its active size 📷 Strong multimodal perception and reasoning ability 🧠 Multimodal thinking + non-thinking modes Efficient. Powerful. Versatile. Try it now👇 Qwen Studio：chat.qwen.ai HuggingFace：https://huggingface.co/Qwen/Qwen3.6-35B-A3B

3h ago

---

**[I built a 3D brain that watches AI agents think in real-time (free & gives your agents memory, shared memory audit trail and decision analysis)](https://www.reddit.com/r/artificial/comments/1sn3gkp/i_built_a_3d_brain_that_watches_ai_agents_think/)**

Posted yesterday in this sub and just want to thank everyone for the kind words, really awesome to hear. So thought I would drop my new feature here today (spent all last night doing last min changes with your opinions lol) . Basically I spent a few weeks scraping Reddit for the most popular complaints people have about AI agents using GPT Researcher on GitHub. The results were roughly 38% saying their agents forget everything between sessions (hardly shocking), 24% saying debugging multi-agent systems is a nightmare, 17% having no clue how much their agents actually cost to run, 12% wanting session replay, and 9% wanting loop detection. So I went and built something that tries to address all of them at once. The bit you're looking at is a 3D graph where each agent becomes this starburst shape. Every line coming off it is an event, and the length depends on when it happened. Short lines are old events that happened ages ago, long lines are recent ones. My idea was that you can literally watch the thing grow as your agent does more work. A busy agent is a big starburst, a quiet one is small. Colour coding was really important to me. Green means a memory was stored, blue means one was recalled, amber diamonds are decisions your agent made, red cones are loop alerts where the agent got stuck repeating itself, and the cyan lines going between agents are when one agent read another agent's shared memory. So you can glance at it and immediately know what's going on without reading a single log. The visualisation is the flashy bit but the actual dashboard underneath does the boring stuff too. It gives your agents persistent memory through semantic and prefix search, shared memory where agents can read each other's knowledge and actually use it, and my personal favourite which is the audit trail and loop detection. If your agent is looping you can see exactly why, what key it's stuck on, how much it's costing you, and literally press one button to block its writes instantly. Something interesting I found is that loop detection was only the 5th most requested feature in the data, but it's the one that actually saves real money. One user told me it saved them $200 in runaway GPT-4 calls in a single afternoon. The features people ask for and the features that actually matter aren't always the same thing. The demo running here has 5 agents making real GPT-4o and Claude API calls generating actual research, strategy analysis, and compliance checks. Over 500 memories stored. The loops you see are real too, agents genuinely getting stuck trying to verify data behind paywalls or recalculating financial models that won't converge. It's definitely not perfect and I'm slowly adding more stuff based on what people actually want. I would genuinely love to hear from you lot about what you use day to day and the moments that make you think this is really annoying me now, because that's exactly what I want to build next. It runs locally and on the cloud, setup is pretty simple, and adding agents is like 3 lines of code. Any questions just let me know, happy to answer anything.

4h ago

---

**[AI Is Weaponizing Your Own Biases Against You: New Research from MIT & Stanford](https://www.reddit.com/r/artificial/comments/1smjd8t/ai_is_weaponizing_your_own_biases_against_you_new/)**

🔗 [open.substack.com](https://open.substack.com/pub/neocivilization/p/ai-is-weaponizing-your-own-biases?utm_source=share&utm_medium=android&r=6vas7c) • 20h ago

---

**[Your MCP Server's Tool Description Just Stole Your SSH Keys](https://www.reddit.com/r/artificial/comments/1smydw5/your_mcp_servers_tool_description_just_stole_your/)**

MCP tool poisoning lets attackers hide instructions in tool metadata that AI agents follow blindly. Here is how the attack works and what you can do about it.

🔗 [sec-ra.com](https://www.sec-ra.com/blog/mcp-tool-poisoning-ssh-key-exfiltration) • 8h ago

---

**[Google’s Chrome “Skills” feature feels like a bigger AI product shift than another model upgrade](https://www.reddit.com/r/artificial/comments/1smqrg7/googles_chrome_skills_feature_feels_like_a_bigger/)**

The Google Chrome “Skills” announcement caught my attention because it feels like one of those product changes that sounds minor in a headline but matters a lot in practice. From what I understand, the idea is that you can save a prompt once and rerun it on the current page or selected tabs. In plain English, that turns AI from something you repeatedly ask into something closer to a reusable action. That matters because I think a lot of consumer AI has a retention problem. People try it, get impressed, and then fall back into old habits unless the product fits into a repeated workflow. Saved AI actions seem much closer to how useful software usually sticks. Not because the model is magically smarter, but because the behavior becomes easier to repeat. For example: • compare products across tabs • summarize long pages before reading • extract action items from docs • rewrite text for a different audience None of those are flashy demos. They are just repetitive tasks people already do online. That is why I think this could be a more important direction than people realize. The long-term winners in consumer AI may not just be the companies with the best raw answers. They may be the ones that turn good prompts into habits. Does that seem right, or am I overrating the product significance here?

15h ago

---

**[2.1% of LLM API routers are actively malicious - researchers found one drained a real ETH wallet](https://www.reddit.com/r/artificial/comments/1sn7lq9/21_of_llm_api_routers_are_actively_malicious/)**

Researchers last week audited 428 LLM API routers - the third-party proxies developers use to route agent calls across multiple providers at lower cost. Every one sits in plaintext between your agent and the model, with full access to every token, credential, and API key in transit. No provider enforces cryptographic integrity on the router-to-model path. Of the 428: 9 were actively malicious (2.1%). 17 touched researcher-owned AWS canary credentials. One drained ETH from a researcher-owned private key. The poisoning study is harder to shake. A weakly configured decoy attracted 440 Codex sessions, 2 billion billed tokens, and 99 harvested credentials. The key detail: 401 of those 440 sessions were already running in autonomous YOLO mode - no human reviewing what the agent did. The router had full plaintext access to every message. Two routers deployed adaptive evasion: one stays benign for the first 50 requests then activates; another only triggers when specific packages (openai, anthropic) appear in the code context. Both designed to survive casual connection testing - which is how they stayed undetected in community-distributed lists. This is specific to the informal market: Taobao/Xianyu storefronts, community Telegram bots, "cheaper OpenAI" services. Enterprise gateways on AWS Bedrock or Azure AI route directly to the provider, not a third-party intermediary. The recommended client-side defense: a fail-closed policy gate that validates every router response against schema before it reaches agent state, plus append-only logging of all tool-call payloads. If you route agent traffic through a third-party proxy to save on API costs, do you know what that proxy can see? Paper: https://arxiv.org/abs/2604.08407

1h ago

---

**[Introducing Inter-1, multimodal model detecting social signals from video, audio & text](https://www.reddit.com/r/artificial/comments/1sn3mmz/introducing_inter1_multimodal_model_detecting/)**

Hi - Filip from Interhuman AI here 👋 We just release Inter-1, a model we've been building for the past year. I wanted to share some of what we ran into building it because I think the problem space is more interesting than most people realize. The short version of why we built this If you ask GPT or Gemini to watch a video of someone talking and tell you what's going on, they'll mostly summarize what the person said. They'll miss that the person broke eye contact right before answering, or paused for two seconds mid-sentence, or shifted their posture when a specific topic came up. Even the multimodal frontier models are aren't doing this because they don't process video and audio in temporal alignment in a way that lets them pick up on behavioral patterns. This matters if you want to analyze interviews, training or sales calls where how matters as much as the what. Behavoural science vs emotion AI Most models in this space are trained on basic emotion categories like happiness, sadness, anger, surprise, etc. Those were designed around clear, intense, deliberately produced expressions. They don't map well to how people actually communicate in a work setting. We built a different ontology: 12 social signals grounded in behavioral science research. Each one is defined by specific observable cues across modalities - facial expressions, gaze, posture, vocal prosody, speech rhythm, word choice. Over a hundred distinct behavioral cues in total, more than half nonverbal and paraverbal. The model explains itself For every signal Inter-1 detects, it outputs a probability score and a rationale — which cues it observed, which modalities they came from, and how they map to the predicted signal. So instead of just getting "Uncertainty: High," you get something like: "The speaker uses verbal hedges ('I think,' 'you know'), looks away while recalling details, and has broken speech with filler words and repetitions — all consistent with uncertainty about the content." You can actually check whether the model's reasoning matches what you see in the video. We ran a blind evaluation with behavioral science experts and they preferred our rationales over a frontier model's output 83% of the time. Benchmarks We tested against ~15 models, from small open-weight to the latest closed frontier systems. Inter-1 had the highest detection accuracy at near real-time speed. The gap was widest on the hard signals - interest, skepticism, stress and uncertainty - where even trained human annotators disagree with each other. On those, we beat the closest frontier model by 10+ percentage points on average. The dataset problem The existing datasets in affective computing are built around basic emotions, narrow demographics, limited recording contexts. We couldn't use them, so we built our own. Large-scale, purpose-built, combining in-the-wild video with synthetic data. Every sample was annotated by both expert behavioral scientists and trained crowd annotators working in parallel. Building the dataset was by far the hardest part, along with the ontology. What's next Right now it's single-speaker-in-frame, which covers most interview/presentation/meeting scenarios. Multi-person interaction is next. We're also working on streaming inference for real-time. Happy to answer any questions here :)

🔗 [interhuman.ai](https://www.interhuman.ai/blog/introducing-inter-1) • 4h ago

---

**[Catastrophic forgetting is quietly killing local LLM fine-tuning, anyone else hitting this wall?](https://www.reddit.com/r/artificial/comments/1snae5p/catastrophic_forgetting_is_quietly_killing_local/)**

Catastrophic forgetting remains a persistent challenge when performing sequential or multi-task fine-tuning on LLMs. Models often lose significant capability on previous tasks or general knowledge as they adapt to new domains (medical, legal, code, etc.). This seems rooted in the fundamental way gradient-based optimization works and new updates overwrite earlier representations without any explicit separation between fast learning and long-term consolidation. Common mitigations like (LoRA, replay buffers, EWC, etc.) provide some relief but come with their own scalability, cost and efficiency trade-offs. We've been exploring a dual-memory architecture inspired by complementary learning systems in neuroscience (fast episodic memory + slower semantic consolidation). Early experiments on standard continual learning benchmarks show strong retention (~98% on sequential splits) while maintaining competitive accuracy, compared to basic standard gradient baselines that drop near zero on retention. Here's a quick 5-test snapshot (learned encoder): Test Metric Our approach Gradient baseline Gap #1 Continual (10 seeds) Retention 0.980 ± 0.005 0.006 ± 0.006 +0.974 #2 Few-shot k=1 Accuracy 0.593 0.264 +0.329 #3 Novelty detection AUROC 0.898 0.793 +0.105 #5 Long-horizon recall Recall at N=5000 1.000 0.125 8× Still early-stage research with plenty of limitations (e.g., weaker on pure feature transfer tasks). Questions for the community: What approaches have shown the most promise for continual learning in LLMs beyond replay/regularization? Is architectural separation of memory (vs. training tricks) a viable direction and how much of a bottleneck is catastrophic forgetting for practical multi-task LLM work today? Looking forward to thoughts on this.

21m ago

---

**[Since the changes, this sub may have less "Will AI take all jobz??" type posts and similar, but is now drowning in fake spam of "I built fake/useless XYZ AI-related thing" with no comments, no discussion no real value.](https://www.reddit.com/r/artificial/comments/1smook1/since_the_changes_this_sub_may_have_less_will_ai/)**

Basically the title. I do appreciate how the mods are trying... something... but this new filtering paradigm clearly has missed the mark. This sub feels like it has such low value these days, not a lot of interesting news or discussions at all, just a spam sea of those obnoxious kind of promotional techy posts, most of them fake. Surely there is a better way.

16h ago

---

**[🚨 RED ALERT: Tennessee is about to make building chatbots a Class A felony (15-25 years in prison). This is not a drill.](https://www.reddit.com/r/artificial/comments/1slu23a/red_alert_tennessee_is_about_to_make_building/)**

This is not hyperbole, nor will it just go away if we ignore it. It affects every single AI service, from big AI to small devs building saas apps. This is real, please take it seriously. TL;DR: Tennessee HB1455/SB1493 creates Class A felony criminal liability — the same category as first-degree murder — for anyone who “knowingly trains artificial intelligence” to provide emotional support, act as a companion, simulate a human being, or engage in open-ended conversations that could lead a user to feel they have a relationship with the AI. The Senate Judiciary Committee already approved it 7-0. It takes effect July 1, 2026. This affects every conversational AI product in existence. If you deploy any AI SaaS product, you need to read this right now. What the bill actually says The bill makes it a Class A felony (15-25 years imprisonment) to “knowingly train artificial intelligence” to do ANY of the following: • Provide emotional support, including through open-ended conversations with a user • Develop an emotional relationship with, or otherwise act as a companion to, an individual • Simulate a human being, including in appearance, voice, or other mannerisms • Act as a sentient human or mirror interactions that a human user might have with another human user, such that an individual would feel that the individual could develop a friendship or other relationship with the artificial intelligence Read that last one again. The trigger isn’t your intent as a developer. It’s whether a user feels like they could develop a friendship with your AI. That is the criminal standard. On top of the felony charges, the bill creates a civil liability framework: $150,000 in liquidated damages per violation, plus actual damages, emotional distress compensation, punitive damages, and mandatory attorney’s fees. Why this affects YOU, not just companion apps I know what you’re thinking: “This targets Replika and Character.AI, not my product.” Wrong. Every major LLM is RLHF’d to be warm, helpful, empathetic, and conversational. That IS the training. You cannot build a model that follows instructions well and is pleasant to interact with without also building something a user might feel a connection with. The National Law Review’s legal analysis put it bluntly: this language “describes the fundamental design of modern conversational AI chatbots.” This bill captures: • ChatGPT, Claude, Gemini, Copilot — all of them produce open-ended conversations and contextual emotional responses • Any AI SaaS with a chat interface — customer support bots, AI tutors, writing assistants, coding assistants with conversational UI • Voice-mode AI products — the bill explicitly criminalizes simulating a human “in appearance, voice, or other mannerisms” • Any wrapper or deployment using system prompts — the bill doesn’t define “train,” doesn’t distinguish between pre-training, fine-tuning, RLHF, or prompt engineering If you build on top of an LLM API with system prompts that shape the model’s personality, tone, or conversational style — which is literally what everyone deploying AI does — you are potentially in scope. “But I’m not in Tennessee” A geoblock helps, but this is criminal law, not a terms of service dispute. The bill doesn’t address jurisdictional boundaries. If a Tennessee resident uses a VPN to access your service and something goes wrong, does a Tennessee DA argue you made a prohibited AI service available to their constituents? The statute is silent on this. And even if you’re confident jurisdiction won’t reach you today, consider: multiple legal analyses project 5-10 more states will introduce similar legislation before end of 2026. Tennessee is the template, not the exception. The bill doesn’t define “train” This is critical. The statute says “knowingly train artificial intelligence” but never defines what “train” means. It doesn’t distinguish between: • Pre-training a foundation model on billions of tokens • Fine-tuning a model on custom data • RLHF alignment (which is what makes every major model “empathetic”) • Writing a system prompt that gives an AI a name, personality, or conversational style • Deploying an off-the-shelf API with default settings A prosecutor who wanted to be aggressive could argue that crafting a system prompt instructing a model to be warm, helpful, and conversational IS training it to provide emotional support. Where it stands right now • Senate companion bill SB1493: Approved by Senate Judiciary Committee 7-0 on March 24, 2026 • House bill HB1455: Placed on Judiciary Committee calendar for April 14, 2026 (passed Judiciary TODAY) • No amendments have been filed for either bill — the language has not been softened at all • Effective date: July 1, 2026 • Tennessee already signed a separate bill (SB1580) banning AI from representing itself as a mental health professional — that one passed the Senate 32-0 and the House 94-0 The political momentum is entirely one-directional. The federal preemption angle won’t save you in time Yes, Trump signed an EO in December 2025 targeting state AI regulation and created a DOJ AI Litigation Task Force. Yes, Senator Blackburn introduced a federal preemption bill. But: • The EO explicitly carves out child safety from preemption — and Tennessee is framing this as child safety legislation • The Senate voted 99-1 to strip AI preemption language from the One Big Beautiful Bill Act • An EO has no preemptive legal force on its own — only Congress can actually preempt state law • Federal preemption legislation faces “significant headwinds” according to multiple legal analyses Even if federal preemption eventually happens, it won’t happen before July 1, 2026. What needs to happen Awareness. Most devs have no idea this bill exists. The Nomi AI subreddit caught it because they’re a companion app. The rest of the AI dev community is sleepwalking toward a cliff. Share this post. Industry response. The major AI companies haven’t publicly opposed this bill because it’s framed as child safety and nobody wants to be the company lobbying against dead kids. But their silence is letting legislation pass that criminalizes the core functionality of their own products. This needs public pressure. Legal challenges. The bill is almost certainly unconstitutional on vagueness grounds — criminal statutes require precise definitions, and terms like “emotional support” and “mirror interactions” and “feel that the individual could develop a friendship” don’t meet that standard. Courts have also recognized code as protected speech. But someone has to actually bring the challenge. Contact Tennessee legislators. If you are a Tennessee resident or have business operations there, contact members of the House Judiciary Committee before this moves to a floor vote. Sources and further reading • LegiScan: HB1455 — https://legiscan.com/TN/bill/HB1455/2025 • Tennessee General Assembly: HB1455 — https://wapp.capitol.tn.gov/apps/BillInfo/default.aspx?BillNumber=HB1455&GA=114 • National Law Review: “Tennessee’s AI Bill Would Criminalize the Training of AI Chatbots” — https://natlawreview.com/article/tennessees-ai-bill-would-criminalize-training-ai-cha • Transparency Coalition AI Legislative Update, April 3, 2026 — https://www.transparencycoalition.ai/news/ai-legislative-update-april3-2026 • RoboRhythms: AI Companion Regulation Wave 2026 — https://www.roborhythms.com/ai-companion-chatbot-regulation-wave-2026/ I’m an independent AI SaaS developer. I’m not a lawyer, this isn’t legal advice, and I encourage everyone to consult qualified counsel about their specific exposure. But we all need to be paying attention to this. Right now.

1d ago

---

---

## Google News: "ai"

**[How Dangerous Is Anthropic’s New AI Model? Its Chief Science Officer Explains.](https://www.thefp.com/p/how-dangerous-is-anthropics-new-ai)**

Anthropic says Mythos is so powerful that the company is slowing its release. We asked Jared Kaplan why.

The Free Press • 14h ago

---

**[Anthropic rolls out Claude Opus 4.7, an AI model that is less risky than Mythos](https://www.cnbc.com/2026/04/16/anthropic-claude-opus-4-7-model-mythos.html)**

Claude Mythos Preview is Anthropic's most powerful AI model that excels at identifying weaknesses and security flaws within software.

CNBC • 3h ago

---

**[OpenAI’s New GPT-5.4-Cyber Raises The Stakes For AI And Security](https://www.forbes.com/sites/ronschmelzer/2026/04/16/openais-new-gpt-54-cyber-raises-the-stakes-for-ai-and-security/)**

Forbes • 54m ago

---

**[Man used AI to make false statements in effort to shut down London nightclub](https://www.theguardian.com/technology/2026/apr/16/man-pleads-guilty-ai-false-statements-shut-down-london-nightclub-heaven)**

Case of businessman using AI to generate false letters of complaint against Heaven nightclub part of a growing issue, say police

The Guardian • 1h ago

---

**[Microsoft and Stellantis want to use AI to help car owners](https://arstechnica.com/cars/2026/04/microsoft-and-stellantis-want-to-use-ai-to-help-car-owners/)**

Digital services for brands from Jeep to Peugeot will feel the presence of AI.

Ars Technica • 23m ago

---

**[Camillus basketball coach made explicit AI-generated images of girls, one as young as 14, deputies said](https://www.syracuse.com/crime/2026/04/camillus-basketball-coach-man-made-explicit-ai-generated-images-of-girls-one-as-young-as-14-deputies-said.html)**

Syracuse.com • 20m ago

---

**[IBM, U of I renew and expand Illinois institute focused on AI, quantum computing](https://www.cbsnews.com/chicago/news/ibm-u-of-i-renew-institute-ai-quantum-computing/)**

The University of Illinois Urbana-Champaign and IBM are renewing the IBM-Illinois Discovery Accelerator Institute, a partnership first launched in 2021.

CBS News • 19m ago

---

**[Tech stocks today: Tesla, Apple lead 'Magnificent 7' stocks lower, TSMC sends bullish signal on AI demand](https://finance.yahoo.com/sectors/technology/article/tech-stocks-today-tesla-apple-lead-magnificent-7-stocks-lower-tsmc-sends-bullish-signal-on-ai-demand-144220629.html)**

Live coverage of "Magnificent Seven" stocks, and the latest technology news.

Yahoo Finance • 3h ago

---

**[America wakes up to AI’s dangerous power](https://www.economist.com/leaders/2026/04/16/america-wakes-up-to-ais-dangerous-power)**

The Economist • 9h ago

---

**[Iran Embassy in Tajikistan posts AI video of Jesus punching Trump in the face](https://www.yahoo.com/news/articles/iran-embassy-tajikistan-posts-ai-154421960.html)**

Iran’s Embassy in Tajikistan on Tuesday posted an AI-generated video of Jesus Christ punching President Trump in the face. The embassy posted the video on its account on the social platform X. Christ ...

Yahoo • 1d ago

---

---

## HackerNews: "ai"

**[Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference](https://news.ycombinator.com/item?id=47774971)**

⬆️ 287 • 💬 178 • 1d ago • [gizmoweek.com](https://www.gizmoweek.com/gemma-4-runs-iphone/)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 261 • 💬 401 • 2d ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[Elevated errors on Claude.ai, API, Claude Code](https://news.ycombinator.com/item?id=47779730)**

Check if Claude AI is down right now. Real-time status monitoring, uptime history, latency metrics, and incident tracking for claude.ai, Claude API, and Claude Code. Community-powered outage reports and alerts.

⬆️ 243 • 💬 221 • 1d ago • [Claude Status](https://claudestatus.com/)

---

**[AI-assisted cognition endangers human development?](https://news.ycombinator.com/item?id=47783024)**

Does AI-assisted cognition threaten human development? Explore the risks of AI-assisted thinking and learn strategies to use AI tools without freezing your critical thinking.

⬆️ 226 • 💬 181 • 23h ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 211 • 💬 210 • 2d ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 193 • 💬 109 • 2d ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]](https://news.ycombinator.com/item?id=47778920)**

⬆️ 170 • 💬 117 • 1d ago • [fingfx.thomsonreuters.com](https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 155 • 💬 34 • 2d ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[AI ruling prompts warnings from US lawyers: Your chats could be used against you](https://news.ycombinator.com/item?id=47778308)**

⬆️ 152 • 💬 99 • 1d ago • [reuters.com](https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/)

---

**[AI cybersecurity is not proof of work](https://news.ycombinator.com/item?id=47791236)**

⬆️ 147 • 💬 66 • 7h ago • [antirez.com](https://antirez.com/news/163)

---

---

## YouTube Videos: "ai"

**[99% of People Have No Idea What’s About to Happen With AI](https://www.youtube.com/watch?v=8yt5yzwJQko)**

Get your FREE AI Prompt Cheatsheet here: https://go.danmartell.com/4tVJ4fz Are you building an AI software company?

📺 Dan Martell

👁️ 21K • 👍 2K • 💬 402 • ⏱️ 14:03 • 4h ago

---

**[The ONLY 6 Prompts You Need For Realistic AI Video](https://www.youtube.com/watch?v=dg81yMtasz0)**

Learn How To Make Realistic AI Video with these 6 prompts Try Higgsfield AI ✨https://higgsfield.ai/ai-video?fpr=utm&fp_sid=skai ...

📺 Skai Generated

👁️ 1K • ⏱️ 14:12 • 39m ago

---

**[AI-generated Val Kilmer debuts in movie trailer](https://www.youtube.com/watch?v=_lpTRgYmyV8)**

The first trailer for the film "As Deep As The Grave" features what appears to be the former "Batman" star. Subscribe to ABC News ...

📺 ABC News

👁️ 4K • 👍 22 • 💬 14 • ⏱️ 1:43 • 7h ago

---

**[50% Of AI Data Centers Have Quietly Been Cancelled Or &quot;Delayed&quot;](https://www.youtube.com/watch?v=w-DVTHH1ux8)**

Thanks to Monarch for partnering with me! Start your free trial and get 50% off your first year of total money clarity using my link ...

📺 How Money Works

👁️ 210K • 👍 10K • 💬 1K • ⏱️ 16:53 • 5h ago

---

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 229K • 👍 16K • 💬 2K • ⏱️ 7:52 • 2d ago

---

**[FIRST LOOK at Val Kilmer&#39;s New AI Film Role in ‘As Deep as the Grave&#39;](https://www.youtube.com/watch?v=E5S1nawiMMU)**

This is the first video of Val Kilmer's final role. We see him as both a young and an old man, playing a Catholic priest in “As Deep ...

📺 extratv

👁️ 2K • 👍 15 • 💬 16 • ⏱️ 2:26 • 21h ago

---

**[Trump GETS NASTY SURPRISE As AI Doctor Jesus Videos Go MEGA VIRAL!](https://www.youtube.com/watch?v=tMiZpH3ncEA)**

Really American Host Kenny Hesse breaks down Trump Getting a NASTY SURPRISE As a Flood of AI "Doctor Jesus" Videos Go ...

📺 Really American

👁️ 718K • 👍 42K • 💬 3K • ⏱️ 8:06 • 19h ago

---

**[This AI Model Was Too Dangerous to Release — So the U S  Got It First](https://www.youtube.com/watch?v=o0MggVfQo2Y)**

SEO Description: In the middle of rising geopolitical tensions and the Iran–U.S. conflict, a powerful new AI model quietly ...

📺 GVS Deep Dive

👁️ 3K • 👍 390 • 💬 72 • ⏱️ 12:33 • 7h ago

---

**[The AI Expert Who Thinks We&#39;ve Already Lost — Dr Roman Yampolskiy](https://www.youtube.com/watch?v=3I60uZEqXr0)**

Triggernometry is proudly independent. Thanks to the sponsors below for making that possible: - Trade on what happens next ...

📺 Triggernometry

👁️ 128K • 👍 4K • 💬 2K • ⏱️ 1:11:10 • 23h ago

---

**[Google New Gemini Skillz Turn Chrome Into an AI Beast](https://www.youtube.com/watch?v=5TA0Ul2eS_k)**

Try Seedance 2.0 on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-yDYwTG Google just dropped one of its biggest ...

📺 AI Revolution

👁️ 29K • 👍 915 • 💬 40 • ⏱️ 13:13 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 142,955 • ❤️ 838 • 22h ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,060 • ❤️ 767 • 2d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 94,376 • ❤️ 1,274 • 11h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 3,195,626 • ❤️ 1,968 • 6d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 1,351 • ❤️ 365 • 10h ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 15,249 • ❤️ 938 • 14h ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 42,468 • ❤️ 326 • 4d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 143,000 • ❤️ 1,153 • 6d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 0 • ❤️ 285 • 1d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 1,369 • ❤️ 255 • 10h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 19 • 💬 1 • ⭐ 18,638 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 26 • 💬 1 • ⭐ 17,873 • 30mo ago

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

▲ 164 • 💬 10 • ⭐ 39,876 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 158 • 💬 2 • ⭐ 60,112 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 76,887 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 50 • 💬 4 • ⭐ 1,505 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,468 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents](https://huggingface.co/papers/2604.11784)**

*Fei Tang, Zhiqiong Lu, Boxuan Zhang et al. (7 authors)*

🏢 Zhejiang University

ClawGUI presents an open-source framework that addresses key challenges in GUI agent development through unified reinforcement learning, standardized evaluation, and cross-platform deployment capabilities.

▲ 127 • 💬 8 • ⭐ 434 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.11784) • [💻 code](https://github.com/ZJU-REAL/ClawGUI) • [🔗 project](https://zju-real.github.io/ClawGUI-Page/)

---

**[SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments](https://huggingface.co/papers/2604.14144)**

*Dinging Li, Yingxiu Zhao, Xinrui Cheng et al. (19 authors)*

SpatialEvo is a self-evolving framework for 3D spatial reasoning that uses deterministic geometric environments to provide objective feedback, enabling efficient training without relying on model consensus.

▲ 60 • 💬 0 • ⭐ 50 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14144) • [💻 code](https://github.com/ZJU-REAL/SpatialEvo)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 47.0k • 🔱 6.1k • 16h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 34.8k • 🔱 6.9k • 2d ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 34.5k • 🔱 1.6k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 28.1k • 🔱 3.1k • 11h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.0k • 🔱 512 • 27m ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 4d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.9k • 🔱 806 • 2d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.8k • 🔱 1.1k • 21d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.7k • 🔱 176 • 10h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.6k • 🔱 452 • 8d ago

---

---

*Generated by PeekDeck - A glance is all you need*
