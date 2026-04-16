---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-16T14:07:19.386181+00:00'
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

**Last Updated:** April 16, 2026 at 14:07 UTC  
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

**[I built a 3D brain that watches AI agents think in real-time (free & gives your agents memory, shared memory audit trail and decision analysis)](https://www.reddit.com/r/artificial/comments/1sn3gkp/i_built_a_3d_brain_that_watches_ai_agents_think/)**

Posted yesterday in this sub and just want to thank everyone for the kind words, really awesome to hear. So thought I would drop my new feature here today (spent all last night doing last min changes with your opinions lol) . Basically I spent a few weeks scraping Reddit for the most popular complaints people have about AI agents using GPT Researcher on GitHub. The results were roughly 38% saying their agents forget everything between sessions (hardly shocking), 24% saying debugging multi-agent systems is a nightmare, 17% having no clue how much their agents actually cost to run, 12% wanting session replay, and 9% wanting loop detection. So I went and built something that tries to address all of them at once. The bit you're looking at is a 3D graph where each agent becomes this starburst shape. Every line coming off it is an event, and the length depends on when it happened. Short lines are old events that happened ages ago, long lines are recent ones. My idea was that you can literally watch the thing grow as your agent does more work. A busy agent is a big starburst, a quiet one is small. Colour coding was really important to me. Green means a memory was stored, blue means one was recalled, amber diamonds are decisions your agent made, red cones are loop alerts where the agent got stuck repeating itself, and the cyan lines going between agents are when one agent read another agent's shared memory. So you can glance at it and immediately know what's going on without reading a single log. The visualisation is the flashy bit but the actual dashboard underneath does the boring stuff too. It gives your agents persistent memory through semantic and prefix search, shared memory where agents can read each other's knowledge and actually use it, and my personal favourite which is the audit trail and loop detection. If your agent is looping you can see exactly why, what key it's stuck on, how much it's costing you, and literally press one button to block its writes instantly. Something interesting I found is that loop detection was only the 5th most requested feature in the data, but it's the one that actually saves real money. One user told me it saved them $200 in runaway GPT-4 calls in a single afternoon. The features people ask for and the features that actually matter aren't always the same thing. The demo running here has 5 agents making real GPT-4o and Claude API calls generating actual research, strategy analysis, and compliance checks. Over 500 memories stored. The loops you see are real too, agents genuinely getting stuck trying to verify data behind paywalls or recalculating financial models that won't converge. It's definitely not perfect and I'm slowly adding more stuff based on what people actually want. I would genuinely love to hear from you lot about what you use day to day and the moments that make you think this is really annoying me now, because that's exactly what I want to build next. It runs locally and on the cloud, setup is pretty simple, and adding agents is like 3 lines of code. Any questions just let me know, happy to answer anything.

42m ago

---

**[AI Is Weaponizing Your Own Biases Against You: New Research from MIT & Stanford](https://www.reddit.com/r/artificial/comments/1smjd8t/ai_is_weaponizing_your_own_biases_against_you_new/)**

🔗 [open.substack.com](https://open.substack.com/pub/neocivilization/p/ai-is-weaponizing-your-own-biases?utm_source=share&utm_medium=android&r=6vas7c) • 16h ago

---

**[Google’s Chrome “Skills” feature feels like a bigger AI product shift than another model upgrade](https://www.reddit.com/r/artificial/comments/1smqrg7/googles_chrome_skills_feature_feels_like_a_bigger/)**

The Google Chrome “Skills” announcement caught my attention because it feels like one of those product changes that sounds minor in a headline but matters a lot in practice. From what I understand, the idea is that you can save a prompt once and rerun it on the current page or selected tabs. In plain English, that turns AI from something you repeatedly ask into something closer to a reusable action. That matters because I think a lot of consumer AI has a retention problem. People try it, get impressed, and then fall back into old habits unless the product fits into a repeated workflow. Saved AI actions seem much closer to how useful software usually sticks. Not because the model is magically smarter, but because the behavior becomes easier to repeat. For example: • compare products across tabs • summarize long pages before reading • extract action items from docs • rewrite text for a different audience None of those are flashy demos. They are just repetitive tasks people already do online. That is why I think this could be a more important direction than people realize. The long-term winners in consumer AI may not just be the companies with the best raw answers. They may be the ones that turn good prompts into habits. Does that seem right, or am I overrating the product significance here?

11h ago

---

**[Introducing Inter-1, multimodal model detecting social signals from video, audio & text](https://www.reddit.com/r/artificial/comments/1sn3mmz/introducing_inter1_multimodal_model_detecting/)**

Hi - Filip from Interhuman AI here 👋 We just release Inter-1, a model we've been building for the past year. I wanted to share some of what we ran into building it because I think the problem space is more interesting than most people realize. The short version of why we built this If you ask GPT or Gemini to watch a video of someone talking and tell you what's going on, they'll mostly summarize what the person said. They'll miss that the person broke eye contact right before answering, or paused for two seconds mid-sentence, or shifted their posture when a specific topic came up. Even the multimodal frontier models are aren't doing this because they don't process video and audio in temporal alignment in a way that lets them pick up on behavioral patterns. This matters if you want to analyze interviews, training or sales calls where how matters as much as the what. Behavoural science vs emotion AI Most models in this space are trained on basic emotion categories like happiness, sadness, anger, surprise, etc. Those were designed around clear, intense, deliberately produced expressions. They don't map well to how people actually communicate in a work setting. We built a different ontology: 12 social signals grounded in behavioral science research. Each one is defined by specific observable cues across modalities - facial expressions, gaze, posture, vocal prosody, speech rhythm, word choice. Over a hundred distinct behavioral cues in total, more than half nonverbal and paraverbal. The model explains itself For every signal Inter-1 detects, it outputs a probability score and a rationale — which cues it observed, which modalities they came from, and how they map to the predicted signal. So instead of just getting "Uncertainty: High," you get something like: "The speaker uses verbal hedges ('I think,' 'you know'), looks away while recalling details, and has broken speech with filler words and repetitions — all consistent with uncertainty about the content." You can actually check whether the model's reasoning matches what you see in the video. We ran a blind evaluation with behavioral science experts and they preferred our rationales over a frontier model's output 83% of the time. Benchmarks We tested against ~15 models, from small open-weight to the latest closed frontier systems. Inter-1 had the highest detection accuracy at near real-time speed. The gap was widest on the hard signals - interest, skepticism, stress and uncertainty - where even trained human annotators disagree with each other. On those, we beat the closest frontier model by 10+ percentage points on average. The dataset problem The existing datasets in affective computing are built around basic emotions, narrow demographics, limited recording contexts. We couldn't use them, so we built our own. Large-scale, purpose-built, combining in-the-wild video with synthetic data. Every sample was annotated by both expert behavioral scientists and trained crowd annotators working in parallel. Building the dataset was by far the hardest part, along with the ontology. What's next Right now it's single-speaker-in-frame, which covers most interview/presentation/meeting scenarios. Multi-person interaction is next. We're also working on streaming inference for real-time. Happy to answer any questions here :)

🔗 [interhuman.ai](https://www.interhuman.ai/blog/introducing-inter-1) • 36m ago

---

**[Your MCP Server's Tool Description Just Stole Your SSH Keys](https://www.reddit.com/r/artificial/comments/1smydw5/your_mcp_servers_tool_description_just_stole_your/)**

MCP tool poisoning lets attackers hide instructions in tool metadata that AI agents follow blindly. Here is how the attack works and what you can do about it.

🔗 [sec-ra.com](https://www.sec-ra.com/blog/mcp-tool-poisoning-ssh-key-exfiltration) • 4h ago

---

**[Since the changes, this sub may have less "Will AI take all jobz??" type posts and similar, but is now drowning in fake spam of "I built fake/useless XYZ AI-related thing" with no comments, no discussion no real value.](https://www.reddit.com/r/artificial/comments/1smook1/since_the_changes_this_sub_may_have_less_will_ai/)**

Basically the title. I do appreciate how the mods are trying... something... but this new filtering paradigm clearly has missed the mark. This sub feels like it has such low value these days, not a lot of interesting news or discussions at all, just a spam sea of those obnoxious kind of promotional techy posts, most of them fake. Surely there is a better way.

13h ago

---

**[🚨 RED ALERT: Tennessee is about to make building chatbots a Class A felony (15-25 years in prison). This is not a drill.](https://www.reddit.com/r/artificial/comments/1slu23a/red_alert_tennessee_is_about_to_make_building/)**

This is not hyperbole, nor will it just go away if we ignore it. It affects every single AI service, from big AI to small devs building saas apps. This is real, please take it seriously. TL;DR: Tennessee HB1455/SB1493 creates Class A felony criminal liability — the same category as first-degree murder — for anyone who “knowingly trains artificial intelligence” to provide emotional support, act as a companion, simulate a human being, or engage in open-ended conversations that could lead a user to feel they have a relationship with the AI. The Senate Judiciary Committee already approved it 7-0. It takes effect July 1, 2026. This affects every conversational AI product in existence. If you deploy any AI SaaS product, you need to read this right now. What the bill actually says The bill makes it a Class A felony (15-25 years imprisonment) to “knowingly train artificial intelligence” to do ANY of the following: • Provide emotional support, including through open-ended conversations with a user • Develop an emotional relationship with, or otherwise act as a companion to, an individual • Simulate a human being, including in appearance, voice, or other mannerisms • Act as a sentient human or mirror interactions that a human user might have with another human user, such that an individual would feel that the individual could develop a friendship or other relationship with the artificial intelligence Read that last one again. The trigger isn’t your intent as a developer. It’s whether a user feels like they could develop a friendship with your AI. That is the criminal standard. On top of the felony charges, the bill creates a civil liability framework: $150,000 in liquidated damages per violation, plus actual damages, emotional distress compensation, punitive damages, and mandatory attorney’s fees. Why this affects YOU, not just companion apps I know what you’re thinking: “This targets Replika and Character.AI, not my product.” Wrong. Every major LLM is RLHF’d to be warm, helpful, empathetic, and conversational. That IS the training. You cannot build a model that follows instructions well and is pleasant to interact with without also building something a user might feel a connection with. The National Law Review’s legal analysis put it bluntly: this language “describes the fundamental design of modern conversational AI chatbots.” This bill captures: • ChatGPT, Claude, Gemini, Copilot — all of them produce open-ended conversations and contextual emotional responses • Any AI SaaS with a chat interface — customer support bots, AI tutors, writing assistants, coding assistants with conversational UI • Voice-mode AI products — the bill explicitly criminalizes simulating a human “in appearance, voice, or other mannerisms” • Any wrapper or deployment using system prompts — the bill doesn’t define “train,” doesn’t distinguish between pre-training, fine-tuning, RLHF, or prompt engineering If you build on top of an LLM API with system prompts that shape the model’s personality, tone, or conversational style — which is literally what everyone deploying AI does — you are potentially in scope. “But I’m not in Tennessee” A geoblock helps, but this is criminal law, not a terms of service dispute. The bill doesn’t address jurisdictional boundaries. If a Tennessee resident uses a VPN to access your service and something goes wrong, does a Tennessee DA argue you made a prohibited AI service available to their constituents? The statute is silent on this. And even if you’re confident jurisdiction won’t reach you today, consider: multiple legal analyses project 5-10 more states will introduce similar legislation before end of 2026. Tennessee is the template, not the exception. The bill doesn’t define “train” This is critical. The statute says “knowingly train artificial intelligence” but never defines what “train” means. It doesn’t distinguish between: • Pre-training a foundation model on billions of tokens • Fine-tuning a model on custom data • RLHF alignment (which is what makes every major model “empathetic”) • Writing a system prompt that gives an AI a name, personality, or conversational style • Deploying an off-the-shelf API with default settings A prosecutor who wanted to be aggressive could argue that crafting a system prompt instructing a model to be warm, helpful, and conversational IS training it to provide emotional support. Where it stands right now • Senate companion bill SB1493: Approved by Senate Judiciary Committee 7-0 on March 24, 2026 • House bill HB1455: Placed on Judiciary Committee calendar for April 14, 2026 (passed Judiciary TODAY) • No amendments have been filed for either bill — the language has not been softened at all • Effective date: July 1, 2026 • Tennessee already signed a separate bill (SB1580) banning AI from representing itself as a mental health professional — that one passed the Senate 32-0 and the House 94-0 The political momentum is entirely one-directional. The federal preemption angle won’t save you in time Yes, Trump signed an EO in December 2025 targeting state AI regulation and created a DOJ AI Litigation Task Force. Yes, Senator Blackburn introduced a federal preemption bill. But: • The EO explicitly carves out child safety from preemption — and Tennessee is framing this as child safety legislation • The Senate voted 99-1 to strip AI preemption language from the One Big Beautiful Bill Act • An EO has no preemptive legal force on its own — only Congress can actually preempt state law • Federal preemption legislation faces “significant headwinds” according to multiple legal analyses Even if federal preemption eventually happens, it won’t happen before July 1, 2026. What needs to happen Awareness. Most devs have no idea this bill exists. The Nomi AI subreddit caught it because they’re a companion app. The rest of the AI dev community is sleepwalking toward a cliff. Share this post. Industry response. The major AI companies haven’t publicly opposed this bill because it’s framed as child safety and nobody wants to be the company lobbying against dead kids. But their silence is letting legislation pass that criminalizes the core functionality of their own products. This needs public pressure. Legal challenges. The bill is almost certainly unconstitutional on vagueness grounds — criminal statutes require precise definitions, and terms like “emotional support” and “mirror interactions” and “feel that the individual could develop a friendship” don’t meet that standard. Courts have also recognized code as protected speech. But someone has to actually bring the challenge. Contact Tennessee legislators. If you are a Tennessee resident or have business operations there, contact members of the House Judiciary Committee before this moves to a floor vote. Sources and further reading • LegiScan: HB1455 — https://legiscan.com/TN/bill/HB1455/2025 • Tennessee General Assembly: HB1455 — https://wapp.capitol.tn.gov/apps/BillInfo/default.aspx?BillNumber=HB1455&GA=114 • National Law Review: “Tennessee’s AI Bill Would Criminalize the Training of AI Chatbots” — https://natlawreview.com/article/tennessees-ai-bill-would-criminalize-training-ai-cha • Transparency Coalition AI Legislative Update, April 3, 2026 — https://www.transparencycoalition.ai/news/ai-legislative-update-april3-2026 • RoboRhythms: AI Companion Regulation Wave 2026 — https://www.roborhythms.com/ai-companion-chatbot-regulation-wave-2026/ I’m an independent AI SaaS developer. I’m not a lawyer, this isn’t legal advice, and I encourage everyone to consult qualified counsel about their specific exposure. But we all need to be paying attention to this. Right now.

1d ago

---

**[emotion in llms](https://www.reddit.com/r/artificial/comments/1sn1zvq/emotion_in_llms/)**

you know most human emotion is constructed, inferred, there is no root object, you can kind of create the emotion you want? well, i was looking at human emotion experiments and thinking of adapting them to llms. i was thinking of this one because we've already found narrative priming to be super-effective on llms: https://pmc.ncbi.nlm.nih.gov/articles/PMC2758776/

1h ago

---

**[Honest ChatGPT vs Claude comparison after using both daily for a month](https://www.reddit.com/r/artificial/comments/1smfssa/honest_chatgpt_vs_claude_comparison_after_using/)**

got tired of reading comparisons that were obvisously written by people who tested each tool for 20 minutes so i ran both at $20/month for 30 days on the same tasks biggest surprises: - chatgpt gives you roughly 6x more messages per day at the same price - claude wins 67% of blind code quality tests against codex - neither one is less sycophantic than the other (stanford tested 11 models, all of them agree with you 49% more than humans do) - the $100 tier showdown between openais new pro 5x and claudes max 5x is where the real competition is happening now full complete deep-dive with benchmark data, claude code vs codex and every pricing tier compared here

18h ago

---

**[Anyone here using local models mainly to keep LLM costs under control?](https://www.reddit.com/r/artificial/comments/1smp6u3/anyone_here_using_local_models_mainly_to_keep_llm/)**

Been noticing that once you use LLMs for real dev work, the cost conversation gets messy fast. It is not just raw API spend. It is retries, long context, background evals, tool calls, embeddings, and all the little workflow decisions that look harmless until usage scales up. For some teams, local models seem like the obvious answer, but in practice it feels more nuanced than just “run it yourself and save money.” You trade API costs for hardware, setup time, model routing decisions, and sometimes lower reliability depending on the task. For coding and repetitive internal workflows, local can look great. For other stuff, not always. Been seeing this a lot while working with dev teams trying to optimize overall AI costs. In some cases the biggest savings came from using smaller or local models for the boring repeatable parts, then keeping the expensive models for the harder calls. Been using Claude Code with Wozcode in that mix too, and it made me pay more attention to workflow design as much as model choice. A lot of the bill seems to come from bad routing and lazy defaults more than from one model being “too expensive.” Are local models actually reducing your total cost in a meaningful way, or are they mostly giving you privacy and control while the savings are less clear than people claim?

12h ago

---

---

## Google News: "ai"

**[Struggling shoe retailer Allbirds makes bizarre pivot to AI, adds $127 million in value](https://www.cnbc.com/2026/04/15/allbirds-bird-stock-shoes-ai.html)**

Allbirds announced a deal with American Exchange Group to sell its intellectual property and other assets for $39 million in March.

CNBC • 1d ago

---

**[TSMC first-quarter profit rises 58%, beats estimates as AI demand fuels record run](https://www.cnbc.com/2026/04/16/tsmc-q1-profit-58-percent-ai-chip-demand-record.html)**

TSMC reported another quarter of record profit, with the company expecting AI demand to continue to grow.

CNBC • 8h ago

---

**[Sneaker Company Allbirds Plans to Pivot to A.I. Yes, A.I.](https://www.nytimes.com/2026/04/15/us/allbirds-shoes-ai-pivot.html)**

The New York Times • 13h ago

---

**[AI Gateway’s next evolution: an inference layer designed for agents](https://blog.cloudflare.com/ai-platform/)**

We're building AI Gateway into a unified inference layer for AI, letting developers call models from 14+ providers. New features include Workers AI binding integration and an expanded catalog with multimodal models.

The Cloudflare Blog • 57m ago

---

**[Datavault AI Goes Live with First Edge GPU Sites in New York and Philadelphia; $1.44B-$1.92B Quantum-Ready Fleet to Reach 100+ U.S. Cities by End of 2026](https://ir.datavaultsite.com/news-events/press-releases/detail/448/datavault-ai-goes-live-with-first-edge-gpu-sites-in-new)**

Built on Available Infrastructure's SanQtum AI quantum-resistant edge platform, the 48,000-GPU fleet targets enterprises facing extended GPU…...

Datavault AI • 42m ago

---

**[AI Performance of Val Kilmer Brings Late Actor Back to the Screen](https://www.today.com/video/ai-generated-val-kilmer-debuts-in-as-deep-as-the-grave-trailer-261482565987)**

The first trailer is out for the new film called “As Deep as the Grave” starring an AI-generated version of late actor Val Kilmer playing a priest and Native American spiritualist. Kilmer’s daughter gave permission for the movie whose creators say the family provided archival and behind-the-scenes footage of the actor. NBC’s Chloe Melas reports for TODAY.

TODAY.com • 1h ago

---

**[America wakes up to AI’s dangerous power](https://www.economist.com/leaders/2026/04/16/america-wakes-up-to-ais-dangerous-power)**

The Economist • 5h ago

---

**[Trump posts new AI image of himself embracing Jesus amid backlash from Christians and ongoing rift with Pope Leo](https://www.yahoo.com/news/world/article/trump-posts-new-ai-image-of-himself-embracing-jesus-amid-backlash-from-christians-and-ongoing-rift-with-pope-leo-181356134.html)**

The president shared another Jesus meme on social media after insisting a controversial image he'd posted was intended to depict him as a doctor — and not Christ.

Yahoo • 1h ago

---

**[Gen Z is terrified of the AI revolution. Nobody's preparing them for it](https://www.axios.com/2026/04/16/ai-use-gen-z-college-jobs-fear)**

Axios • 4h ago

---

**[Private Credit's Biggest User Is in an Even Worse Place](https://www.bloomberg.com/opinion/articles/2026-04-16/private-equity-is-in-a-worse-place-than-private-credit-on-ai-threat)**

Bloomberg • 8h ago

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

⬆️ 243 • 💬 219 • 23h ago • [Claude Status](https://claudestatus.com/)

---

**[AI-assisted cognition endangers human development?](https://news.ycombinator.com/item?id=47783024)**

Does AI-assisted cognition threaten human development? Explore the risks of AI-assisted thinking and learn strategies to use AI tools without freezing your critical thinking.

⬆️ 223 • 💬 177 • 19h ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 211 • 💬 210 • 2d ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 193 • 💬 109 • 1d ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]](https://news.ycombinator.com/item?id=47778920)**

⬆️ 159 • 💬 110 • 1d ago • [fingfx.thomsonreuters.com](https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 155 • 💬 34 • 2d ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[AI ruling prompts warnings from US lawyers: Your chats could be used against you](https://news.ycombinator.com/item?id=47778308)**

⬆️ 149 • 💬 99 • 1d ago • [reuters.com](https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/)

---

**[Claude.ai down](https://news.ycombinator.com/item?id=47753643)**

Claude's Status Page - Claude.ai down.

⬆️ 134 • 💬 126 • 2d ago • [status.claude.com](https://status.claude.com/incidents/6jd2m42f8mld)

---

---

## YouTube Videos: "ai"

**[Google New Gemini Skillz Turn Chrome Into an AI Beast](https://www.youtube.com/watch?v=5TA0Ul2eS_k)**

Try Seedance 2.0 on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-yDYwTG Google just dropped one of its biggest ...

📺 AI Revolution

👁️ 25K • 👍 829 • 💬 40 • ⏱️ 13:13 • 16h ago

---

**[Claude Is Melting Down. AI&#39;s Compute Crisis Explained.](https://www.youtube.com/watch?v=d1jReDZsGOc)**

The AI compute crisis is here. Anthropic's Claude is getting dumber and Opus 4.7 & OpenAI's Spud are about to make it worse.

📺 AI For Humans

👁️ 21K • 👍 942 • 💬 306 • ⏱️ 29:28 • 1d ago

---

**[How Allbirds’ pivot from shoes to AI sent its market value soaring](https://www.youtube.com/watch?v=lyNltN1B1ZY)**

Allbirds's market value jumped more than 500% after unveiling a rebrand from shoes to AI. Erin Burnett speaks with Dan Ives, ...

📺 CNN

👁️ 14K • 👍 187 • 💬 12 • ⏱️ 1:44 • 9h ago

---

**[Allbirds Lost 99% of Its Value. Now It&#39;s Pivoting to AI](https://www.youtube.com/watch?v=Mx4CDAczw2c)**

Watch the full Daily DeFranco Show: https://www.youtube.com/@PhilipDeFranco?sub_confirmation=1 Get More News Clips: ...

📺 DeFranco News Clips

👁️ 450K • 👍 25K • 💬 797 • ⏱️ 1:18 • 20h ago

---

**[The 7 Skills You Need to Build AI Agents](https://www.youtube.com/watch?v=mtiOK2QG9Q0)**

As AI agents become more capable, the skills needed for AI jobs are shifting. Bri Kopecki breaks down the 7 skills you need to ...

📺 IBM Technology

👁️ 132K • 👍 6K • 💬 264 • ⏱️ 14:37 • 2d ago

---

**[What is Quantum Mechanics? | Google Quantum AI](https://www.youtube.com/watch?v=I0V14dTS9JQ)**

Curious about quantum? Step onto Google's Quantum AI Campus to get answers to some of the world's top trending quantum ...

📺 Google

👁️ 93K • 👍 3K • 💬 191 • ⏱️ 3:56 • 1d ago

---

**[Elon Musk vs. Sam Altman, AI Job Loss, and OpenAI’s $852B Valuation | EP #247](https://www.youtube.com/watch?v=5ak26W2YNRY)**

This episode is about AI agents, OpenAI and Anthropic competition, the future of work, energy breakthroughs, Bitcoin and ...

📺 Peter H. Diamandis

👁️ 178K • 👍 4K • 💬 979 • ⏱️ 2:10:48 • 1d ago

---

**[Free AI Voice Generator on Your PC (Clones Any Voice)](https://www.youtube.com/watch?v=sisnzgc73zc)**

Clone any voice in seconds using a free AI voice generator that runs directly on your PC. In this step-by-step tutorial, I'll show you ...

📺 Kevin Stratvert

👁️ 4K • 👍 448 • 💬 18 • ⏱️ 5:50 • 7h ago

---

**[This guy is a f****** idiot 🙄](https://www.youtube.com/watch?v=_o7p7FzJfHQ)**

music #diplo #ai #badtakes #musician.

📺 fantano

👁️ 202K • 👍 12K • 💬 661 • ⏱️ 1:17 • 1d ago

---

**[Anthropic &#39;Claude Mythos&#39; model sparks AI doomsday fears](https://www.youtube.com/watch?v=pq7kSVp4Skg)**

Subscribe to LiveNOW from FOX! https://www.youtube.com/livenowfox?sub_confirmation=1 Where to watch LiveNOW from FOX: ...

📺 LiveNOW from FOX

👁️ 28K • 👍 371 • 💬 126 • ⏱️ 13:49 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 142,955 • ❤️ 825 • 19h ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,060 • ❤️ 759 • 2d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 94,376 • ❤️ 1,265 • 7h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 3,195,626 • ❤️ 1,961 • 5d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 15,249 • ❤️ 934 • 10h ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 1,351 • ❤️ 355 • 6h ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 143,000 • ❤️ 1,151 • 6d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 42,468 • ❤️ 319 • 4d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 1,369 • ❤️ 252 • 7h ago

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

▲ 59 • 💬 0 • ⭐ 50 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14144) • [💻 code](https://github.com/ZJU-REAL/SpatialEvo)

---

**[Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model
  Self-Distillation](https://huggingface.co/papers/2509.19296)**

*Sherwin Bahmani, Tianchang Shen, Jiawei Ren et al. (13 authors)*

A self-distillation framework converts implicit 3D knowledge from video diffusion models into an explicit 3D Gaussian Splatting representation, enabling 3D scene generation from text or images.

▲ 27 • 💬 4 • ⭐ 1,194 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.19296) • [💻 code](https://github.com/nv-tlabs/lyra) • [🔗 project](https://research.nvidia.com/labs/toronto-ai/lyra/)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,387 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 47.0k • 🔱 6.1k • 12h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 34.7k • 🔱 6.9k • 1d ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 33.9k • 🔱 1.6k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 28.0k • 🔱 3.0k • 7h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.0k • 🔱 512 • 10m ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 3d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.9k • 🔱 800 • 2d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.8k • 🔱 1.1k • 21d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.7k • 🔱 176 • 6h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 451 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
