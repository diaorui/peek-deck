---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-16T07:48:50.184042+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 16, 2026 at 07:48 UTC  
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

🔗 [open.substack.com](https://open.substack.com/pub/neocivilization/p/ai-is-weaponizing-your-own-biases?utm_source=share&utm_medium=android&r=6vas7c) • 10h ago

---

**[🚨 RED ALERT: Tennessee is about to make building chatbots a Class A felony (15-25 years in prison). This is not a drill.](https://www.reddit.com/r/artificial/comments/1slu23a/red_alert_tennessee_is_about_to_make_building/)**

This is not hyperbole, nor will it just go away if we ignore it. It affects every single AI service, from big AI to small devs building saas apps. This is real, please take it seriously. TL;DR: Tennessee HB1455/SB1493 creates Class A felony criminal liability — the same category as first-degree murder — for anyone who “knowingly trains artificial intelligence” to provide emotional support, act as a companion, simulate a human being, or engage in open-ended conversations that could lead a user to feel they have a relationship with the AI. The Senate Judiciary Committee already approved it 7-0. It takes effect July 1, 2026. This affects every conversational AI product in existence. If you deploy any AI SaaS product, you need to read this right now. What the bill actually says The bill makes it a Class A felony (15-25 years imprisonment) to “knowingly train artificial intelligence” to do ANY of the following: • Provide emotional support, including through open-ended conversations with a user • Develop an emotional relationship with, or otherwise act as a companion to, an individual • Simulate a human being, including in appearance, voice, or other mannerisms • Act as a sentient human or mirror interactions that a human user might have with another human user, such that an individual would feel that the individual could develop a friendship or other relationship with the artificial intelligence Read that last one again. The trigger isn’t your intent as a developer. It’s whether a user feels like they could develop a friendship with your AI. That is the criminal standard. On top of the felony charges, the bill creates a civil liability framework: $150,000 in liquidated damages per violation, plus actual damages, emotional distress compensation, punitive damages, and mandatory attorney’s fees. Why this affects YOU, not just companion apps I know what you’re thinking: “This targets Replika and Character.AI, not my product.” Wrong. Every major LLM is RLHF’d to be warm, helpful, empathetic, and conversational. That IS the training. You cannot build a model that follows instructions well and is pleasant to interact with without also building something a user might feel a connection with. The National Law Review’s legal analysis put it bluntly: this language “describes the fundamental design of modern conversational AI chatbots.” This bill captures: • ChatGPT, Claude, Gemini, Copilot — all of them produce open-ended conversations and contextual emotional responses • Any AI SaaS with a chat interface — customer support bots, AI tutors, writing assistants, coding assistants with conversational UI • Voice-mode AI products — the bill explicitly criminalizes simulating a human “in appearance, voice, or other mannerisms” • Any wrapper or deployment using system prompts — the bill doesn’t define “train,” doesn’t distinguish between pre-training, fine-tuning, RLHF, or prompt engineering If you build on top of an LLM API with system prompts that shape the model’s personality, tone, or conversational style — which is literally what everyone deploying AI does — you are potentially in scope. “But I’m not in Tennessee” A geoblock helps, but this is criminal law, not a terms of service dispute. The bill doesn’t address jurisdictional boundaries. If a Tennessee resident uses a VPN to access your service and something goes wrong, does a Tennessee DA argue you made a prohibited AI service available to their constituents? The statute is silent on this. And even if you’re confident jurisdiction won’t reach you today, consider: multiple legal analyses project 5-10 more states will introduce similar legislation before end of 2026. Tennessee is the template, not the exception. The bill doesn’t define “train” This is critical. The statute says “knowingly train artificial intelligence” but never defines what “train” means. It doesn’t distinguish between: • Pre-training a foundation model on billions of tokens • Fine-tuning a model on custom data • RLHF alignment (which is what makes every major model “empathetic”) • Writing a system prompt that gives an AI a name, personality, or conversational style • Deploying an off-the-shelf API with default settings A prosecutor who wanted to be aggressive could argue that crafting a system prompt instructing a model to be warm, helpful, and conversational IS training it to provide emotional support. Where it stands right now • Senate companion bill SB1493: Approved by Senate Judiciary Committee 7-0 on March 24, 2026 • House bill HB1455: Placed on Judiciary Committee calendar for April 14, 2026 (passed Judiciary TODAY) • No amendments have been filed for either bill — the language has not been softened at all • Effective date: July 1, 2026 • Tennessee already signed a separate bill (SB1580) banning AI from representing itself as a mental health professional — that one passed the Senate 32-0 and the House 94-0 The political momentum is entirely one-directional. The federal preemption angle won’t save you in time Yes, Trump signed an EO in December 2025 targeting state AI regulation and created a DOJ AI Litigation Task Force. Yes, Senator Blackburn introduced a federal preemption bill. But: • The EO explicitly carves out child safety from preemption — and Tennessee is framing this as child safety legislation • The Senate voted 99-1 to strip AI preemption language from the One Big Beautiful Bill Act • An EO has no preemptive legal force on its own — only Congress can actually preempt state law • Federal preemption legislation faces “significant headwinds” according to multiple legal analyses Even if federal preemption eventually happens, it won’t happen before July 1, 2026. What needs to happen Awareness. Most devs have no idea this bill exists. The Nomi AI subreddit caught it because they’re a companion app. The rest of the AI dev community is sleepwalking toward a cliff. Share this post. Industry response. The major AI companies haven’t publicly opposed this bill because it’s framed as child safety and nobody wants to be the company lobbying against dead kids. But their silence is letting legislation pass that criminalizes the core functionality of their own products. This needs public pressure. Legal challenges. The bill is almost certainly unconstitutional on vagueness grounds — criminal statutes require precise definitions, and terms like “emotional support” and “mirror interactions” and “feel that the individual could develop a friendship” don’t meet that standard. Courts have also recognized code as protected speech. But someone has to actually bring the challenge. Contact Tennessee legislators. If you are a Tennessee resident or have business operations there, contact members of the House Judiciary Committee before this moves to a floor vote. Sources and further reading • LegiScan: HB1455 — https://legiscan.com/TN/bill/HB1455/2025 • Tennessee General Assembly: HB1455 — https://wapp.capitol.tn.gov/apps/BillInfo/default.aspx?BillNumber=HB1455&GA=114 • National Law Review: “Tennessee’s AI Bill Would Criminalize the Training of AI Chatbots” — https://natlawreview.com/article/tennessees-ai-bill-would-criminalize-training-ai-cha • Transparency Coalition AI Legislative Update, April 3, 2026 — https://www.transparencycoalition.ai/news/ai-legislative-update-april3-2026 • RoboRhythms: AI Companion Regulation Wave 2026 — https://www.roborhythms.com/ai-companion-chatbot-regulation-wave-2026/ I’m an independent AI SaaS developer. I’m not a lawyer, this isn’t legal advice, and I encourage everyone to consult qualified counsel about their specific exposure. But we all need to be paying attention to this. Right now.

1d ago

---

**[Since the changes, this sub may have less "Will AI take all jobz??" type posts and similar, but is now drowning in fake spam of "I built fake/useless XYZ AI-related thing" with no comments, no discussion no real value.](https://www.reddit.com/r/artificial/comments/1smook1/since_the_changes_this_sub_may_have_less_will_ai/)**

Basically the title. I do appreciate how the mods are trying... something... but this new filtering paradigm clearly has missed the mark. This sub feels like it has such low value these days, not a lot of interesting news or discussions at all, just a spam sea of those obnoxious kind of promotional techy posts, most of them fake. Surely there is a better way.

6h ago

---

**[Google’s Chrome “Skills” feature feels like a bigger AI product shift than another model upgrade](https://www.reddit.com/r/artificial/comments/1smqrg7/googles_chrome_skills_feature_feels_like_a_bigger/)**

The Google Chrome “Skills” announcement caught my attention because it feels like one of those product changes that sounds minor in a headline but matters a lot in practice. From what I understand, the idea is that you can save a prompt once and rerun it on the current page or selected tabs. In plain English, that turns AI from something you repeatedly ask into something closer to a reusable action. That matters because I think a lot of consumer AI has a retention problem. People try it, get impressed, and then fall back into old habits unless the product fits into a repeated workflow. Saved AI actions seem much closer to how useful software usually sticks. Not because the model is magically smarter, but because the behavior becomes easier to repeat. For example: • compare products across tabs • summarize long pages before reading • extract action items from docs • rewrite text for a different audience None of those are flashy demos. They are just repetitive tasks people already do online. That is why I think this could be a more important direction than people realize. The long-term winners in consumer AI may not just be the companies with the best raw answers. They may be the ones that turn good prompts into habits. Does that seem right, or am I overrating the product significance here?

5h ago

---

**[Honest ChatGPT vs Claude comparison after using both daily for a month](https://www.reddit.com/r/artificial/comments/1smfssa/honest_chatgpt_vs_claude_comparison_after_using/)**

got tired of reading comparisons that were obvisously written by people who tested each tool for 20 minutes so i ran both at $20/month for 30 days on the same tasks biggest surprises: - chatgpt gives you roughly 6x more messages per day at the same price - claude wins 67% of blind code quality tests against codex - neither one is less sycophantic than the other (stanford tested 11 models, all of them agree with you 49% more than humans do) - the $100 tier showdown between openais new pro 5x and claudes max 5x is where the real competition is happening now full complete deep-dive with benchmark data, claude code vs codex and every pricing tier compared here

12h ago

---

**[Anyone here using local models mainly to keep LLM costs under control?](https://www.reddit.com/r/artificial/comments/1smp6u3/anyone_here_using_local_models_mainly_to_keep_llm/)**

Been noticing that once you use LLMs for real dev work, the cost conversation gets messy fast. It is not just raw API spend. It is retries, long context, background evals, tool calls, embeddings, and all the little workflow decisions that look harmless until usage scales up. For some teams, local models seem like the obvious answer, but in practice it feels more nuanced than just “run it yourself and save money.” You trade API costs for hardware, setup time, model routing decisions, and sometimes lower reliability depending on the task. For coding and repetitive internal workflows, local can look great. For other stuff, not always. Been seeing this a lot while working with dev teams trying to optimize overall AI costs. In some cases the biggest savings came from using smaller or local models for the boring repeatable parts, then keeping the expensive models for the harder calls. Been using Claude Code with Wozcode in that mix too, and it made me pay more attention to workflow design as much as model choice. A lot of the bill seems to come from bad routing and lazy defaults more than from one model being “too expensive.” Are local models actually reducing your total cost in a meaningful way, or are they mostly giving you privacy and control while the savings are less clear than people claim?

6h ago

---

**[Google Released Gemini Mac APP](https://www.reddit.com/r/artificial/comments/1smsonq/google_released_gemini_mac_app/)**

Google released Gemini app for macOS Currently, it mimics functionality available on the web, but looks like we will get Gemini Live support there soon as well. Every LLM company is moving todays native app. This clearly shows the trend we are heading towards, a native app that can control the device automate actions and workflows. Creating a full OS from scratch and capturing the market is difficult, so the way forward is the dedication application with more permissions.

3h ago

---

**[For the first time in history, Ukraine captured a Russian position and prisoners, using only robots and drones](https://www.reddit.com/r/artificial/comments/1sm6y5q/for_the_first_time_in_history_ukraine_captured_a/)**

Ukraine confirmed that a force of robots and drones captured an enemy position without infantry for the first time ever.

🔗 [We Are The Mighty](https://www.wearethemighty.com/tactical/drones-capture-position-first-time-ukraine/) • 17h ago

---

**[What if attention didn’t need matrix multiplication?](https://www.reddit.com/r/artificial/comments/1smd2fl/what_if_attention_didnt_need_matrix_multiplication/)**

I built a cognitive architecture where all computation reduces to three bit operations: XOR, MAJ, POPCNT. No GEMM. No GPU. No floating-point weights. The core idea: transformer attention is a similarity computation. Float32 cosine computes it with 24,576 FLOPs. Binary Spatter Codes compute the same geometric measurement with 128 bit operations. Measured: 192x fewer ops, 32x less memory, ~480x faster. 26 modules in 1237 lines of C. One file. Any hardware: cc -O2 -o creation_os creation_os_v2.c -lm Includes a JEPA-style world model (energy = σ), n-gram language model (attention = σ), physics simulation (Noether conservation σ = 0.000000), value system with tamper detection, multi-model truth triangulation, metacognition, emotional memory, theory of mind, and 13 other cognitive modules. This is a research prototype built on Binary Spatter Codes (Kanerva, 1997). It demonstrates that cognitive primitives can be expressed in bit operations. It does not replace LLMs — the language module runs on 15 sentences. But the algebra is real, the benchmark is measured, and the architecture is open. https://github.com/spektre-labs/creation-os AGPL-3.0. Feedback welcome.

14h ago

---

**[Ai and stock picking](https://www.reddit.com/r/artificial/comments/1smqtz1/ai_and_stock_picking/)**

Anyone use AI for getting Fair Value of stocks?

5h ago

---

---

## Google News: "ai"

**[Allbirds stock soars nearly 600% as the shoemaker rebrands as an AI company](https://finance.yahoo.com/news/allbirds-stock-soars-nearly-600-as-the-shoemaker-rebrands-as-an-ai-company-173129202.html)**

Allbirds is getting out of the sustainable sneaker business and into the AI business.

Yahoo Finance • 10h ago

---

**[Grayson Perry Has Seen the Future review – some of these insights into AI are just mindblowing](https://www.theguardian.com/tv-and-radio/2026/apr/15/grayson-perry-has-seen-future-review)**

From people marrying digital companions to CEOs excited about how people whose jobs are replaced can ‘adapt’, this is terrifying watching. But Perry is the perfect host

The Guardian • 8h ago

---

**[Education experts to Mamdani: why are you foisting AI on our kids?](https://fortune.com/2026/04/16/doctors-experts-ai-moratorium-schools/)**

"If a local children's hospital told parents, 'We've got this new drug, it has potential, just trust us,' people would be horrified."

Fortune • 47m ago

---

**[Neuro-Symbolic AI Wins On Long-Horizon Reasoning And Does So At A Lower Energy Cost](https://www.forbes.com/sites/lanceeliot/2026/04/16/neuro-symbolic-ai-wins-on-long-horizon-reasoning-and-does-so-at-a-lower-energy-cost/)**

Forbes • 33m ago

---

**[Trump Just Posted An AI Image Of Himself With Jesus](https://www.forbes.com/sites/maryroeloffs/2026/04/15/trump-posts-ai-photo-with-jesus-days-after-he-was-slammed-for-blasphemy/)**

Forbes • 18h ago

---

**[Iran Embassy in Tajikistan posts AI video of Jesus punching Trump in the face](https://thehill.com/policy/international/5832224-iran-trump-social-media-war/)**

The Hill • 16h ago

---

**[Trump posts new AI image of himself embracing Jesus amid backlash from Christians and ongoing rift with Pope Leo](https://www.yahoo.com/news/world/article/trump-posts-new-ai-image-of-himself-embracing-jesus-amid-backlash-from-christians-and-ongoing-rift-with-pope-leo-181356134.html)**

The president shared another Jesus meme on social media after insisting a controversial image he'd posted was intended to depict him as a doctor — and not Christ.

Yahoo • 15h ago

---

**[This monkey selfie will protect you from AI slop](https://www.bbc.com/future/article/20260414-the-monkey-selfie-that-predicted-the-ai-age)**

What happens when something that isn't human makes art? The answer lies with this image and it will change what ends up on your screen and in your headphones forever.

BBC • 21h ago

---

**[Opinion | Don’t Use A.I. to Do This](https://www.nytimes.com/2026/04/15/opinion/art-artificial-intelligence.html)**

The New York Times • 22h ago

---

**[Turn your best AI prompts into one-click tools in Chrome](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

blog.google • 1d ago

---

---

## HackerNews: "ai"

**[Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference](https://news.ycombinator.com/item?id=47774971)**

⬆️ 279 • 💬 169 • 1d ago • [gizmoweek.com](https://www.gizmoweek.com/gemma-4-runs-iphone/)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 261 • 💬 400 • 2d ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[Elevated errors on Claude.ai, API, Claude Code](https://news.ycombinator.com/item?id=47779730)**

Check if Claude AI is down right now. Real-time status monitoring, uptime history, latency metrics, and incident tracking for claude.ai, Claude API, and Claude Code. Community-powered outage reports and alerts.

⬆️ 242 • 💬 218 • 17h ago • [Claude Status](https://claudestatus.com/)

---

**[AI-assisted cognition endangers human development?](https://news.ycombinator.com/item?id=47783024)**

Does AI-assisted cognition threaten human development? Explore the risks of AI-assisted thinking and learn strategies to use AI tools without freezing your critical thinking.

⬆️ 221 • 💬 174 • 13h ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 211 • 💬 210 • 1d ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[Turn your best AI prompts into one-click tools in Chrome](https://news.ycombinator.com/item?id=47768339)**

Skills in Chrome let you discover, save and remix AI workflows — and repeat them instantly.

⬆️ 193 • 💬 108 • 1d ago • [Google](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 186 • 💬 279 • 2d ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 155 • 💬 34 • 2d ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[AI ruling prompts warnings from US lawyers: Your chats could be used against you](https://news.ycombinator.com/item?id=47778308)**

⬆️ 148 • 💬 96 • 18h ago • [reuters.com](https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/)

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

👁️ 18K • 👍 648 • 💬 30 • ⏱️ 13:13 • 9h ago

---

**[Claude Is Melting Down. AI&#39;s Compute Crisis Explained.](https://www.youtube.com/watch?v=d1jReDZsGOc)**

The AI compute crisis is here. Anthropic's Claude is getting dumber and Opus 4.7 & OpenAI's Spud are about to make it worse.

📺 AI For Humans

👁️ 19K • 👍 890 • 💬 279 • ⏱️ 29:28 • 18h ago

---

**[AI Insider: The Models They&#39;ll Never Release to the Public](https://www.youtube.com/watch?v=tkO7YHJ6Mn8)**

Emad Mostaque built Stable Diffusion. Now he says the most powerful AI models will never be released — and we have roughly ...

📺 Dr Brian Keating

👁️ 24K • 👍 723 • 💬 168 • ⏱️ 1:27:18 • 2d ago

---

**[Harvard just discovered what AI actually is](https://www.youtube.com/watch?v=nDL3Ch7Nz8c)**

You're absolutely right, that IS a great reason to fire everyone! If you'd like to support my work, you can become a member to view ...

📺 Mo Bitar

👁️ 206K • 👍 15K • 💬 2K • ⏱️ 7:52 • 1d ago

---

**[The 7 Skills You Need to Build AI Agents](https://www.youtube.com/watch?v=mtiOK2QG9Q0)**

As AI agents become more capable, the skills needed for AI jobs are shifting. Bri Kopecki breaks down the 7 skills you need to ...

📺 IBM Technology

👁️ 122K • 👍 6K • 💬 264 • ⏱️ 14:37 • 1d ago

---

**[Elon Musk vs. Sam Altman, AI Job Loss, and OpenAI’s $852B Valuation | EP #247](https://www.youtube.com/watch?v=5ak26W2YNRY)**

This episode is about AI agents, OpenAI and Anthropic competition, the future of work, energy breakthroughs, Bitcoin and ...

📺 Peter H. Diamandis

👁️ 170K • 👍 4K • 💬 947 • ⏱️ 2:10:48 • 1d ago

---

**[What to know about Anthropic&#39;s new AI model and its stark warning](https://www.youtube.com/watch?v=bUbFFSZQ5w0)**

Former AI company founder and CEO Matt Shumer joins "CBS Mornings" to break down Anthropic's report about one of its AI ...

📺 CBS Mornings

👁️ 51K • 👍 488 • 💬 88 • ⏱️ 4:58 • 2d ago

---

**[What is Quantum Mechanics? | Google Quantum AI](https://www.youtube.com/watch?v=I0V14dTS9JQ)**

Curious about quantum? Step onto Google's Quantum AI Campus to get answers to some of the world's top trending quantum ...

📺 Google

👁️ 81K • 👍 2K • 💬 175 • ⏱️ 3:56 • 1d ago

---

**[Anthropic &#39;Claude Mythos&#39; model sparks AI doomsday fears](https://www.youtube.com/watch?v=pq7kSVp4Skg)**

Subscribe to LiveNOW from FOX! https://www.youtube.com/livenowfox?sub_confirmation=1 Where to watch LiveNOW from FOX: ...

📺 LiveNOW from FOX

👁️ 27K • 👍 366 • 💬 122 • ⏱️ 13:49 • 2d ago

---

**[Trump AI post: The memes and the impact](https://www.youtube.com/watch?v=dLqTdkbKwaw)**

"That doctor looks pretty Christlike to me." Molly Jong-Fast breaks down the memes and potential fallout from President Trump's ...

📺 MS NOW

👁️ 60K • 👍 1K • 💬 365 • ⏱️ 1:02 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 142,955 • ❤️ 806 • 12h ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,060 • ❤️ 732 • 1d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 94,376 • ❤️ 1,253 • 1h ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 15,249 • ❤️ 926 • 4h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 3,195,626 • ❤️ 1,943 • 5d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 143,000 • ❤️ 1,138 • 6d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 1,351 • ❤️ 325 • 33m ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 42,468 • ❤️ 310 • 3d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 1,369 • ❤️ 236 • 49m ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 57,507 • ❤️ 226 • 5d ago

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

▲ 45 • 💬 2 • ⭐ 50,718 • 15mo ago

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

▲ 158 • 💬 2 • ⭐ 60,007 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 76,756 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents](https://huggingface.co/papers/2604.11784)**

*Fei Tang, Zhiqiong Lu, Boxuan Zhang et al. (7 authors)*

🏢 Zhejiang University

ClawGUI presents an open-source framework that addresses key challenges in GUI agent development through unified reinforcement learning, standardized evaluation, and cross-platform deployment capabilities.

▲ 124 • 💬 8 • ⭐ 404 • 3d ago

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

⭐ 46.8k • 🔱 6.1k • 6h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 34.4k • 🔱 6.8k • 1d ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 33.2k • 🔱 1.6k • 18h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 27.7k • 🔱 3.0k • 1h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.0k • 🔱 508 • 7m ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 3d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.8k • 🔱 788 • 2d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.7k • 🔱 1.1k • 21d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.6k • 🔱 174 • 4m ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 450 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
