---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-25T17:35:47.019073+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 25, 2026 at 17:35 UTC  
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

**[I Built a Fully Playable FPS Using Only Prompts (No Manual Code)](https://www.reddit.com/r/artificial/comments/1recjbv/i_built_a_fully_playable_fps_using_only_prompts/)**

Hello! I want to share an experiment I’ve been running. Over the past few weeks, I’ve been developing a desktop HTML first-person shooter called Zombie Slayer. The core constraint of the project is this: every line of code was generated through prompts. I never manually edited the source. For context: I have never built a 3D game before, and I’ve never programmed in HTML. I also have nearly zero coding experience. This project has been less about traditional development and more about testing the boundary conditions of prompt-driven creation. The game was built in Antigravity using Gemini 3 Pro, with Three.js handling real-time 3D rendering. All geometry is procedurally generated at runtime. Sound effects are synthesized dynamically, and the music was also generated with AI (Suno). The entire playable build is under 900KB in file size and is an easily shareable HTML file. From a systems perspective: - HTML desktop game (<1MB total footprint) Procedural geometry generated at runtime Real-time sound generation - 10 escalating stages with objectives + economy layer (coin-based Black Market) - Enemy scaling model (each kill increases enemy population and variety) - Weapon and physics modifiers (jetpack thrust, anti-gravity cannon, nuke projectile, etc.) - Dynamic environmental interactions (flood events, teleport well, destructible elements) To my knowledge, this may be the first playable first-person shooter built entirely through prompting (at least at this level of complexity and intentional design). If I’m wrong, I’d genuinely love to see comparable examples. The goal is to continue expanding the game exclusively through prompts and release it for free. I’d appreciate any technical feedback, skepticism, or discussion. I’m treating this as an open experiment in what “AI-native” game development might look like.

4h ago

---

**[Anthropic Drops Flagship Safety Pledge](https://www.reddit.com/r/artificial/comments/1re0m36/anthropic_drops_flagship_safety_pledge/)**

In an abrupt shift, the company may release future AI models without ironclad safety guarantees

🔗 [TIME](https://time.com/7380854/exclusive-anthropic-drops-flagship-safety-pledge/) • 15h ago

---

**[Looking for AI software that can generate documents for company based on the documents we feed "him"](https://www.reddit.com/r/artificial/comments/1re896u/looking_for_ai_software_that_can_generate/)**

Hi, I’m looking for AI software that allows us to upload a large number of our existing Word/PDF documents (templates, past client documents, standard clauses, etc.) and then generate new documents based on those patterns. What I’m NOT looking for is just a chatbot that answers questions about the documents. I need something that can: Learn from our document structure and wording Reuse our formatting and style Generate full new documents based on prompts and documents we feed it (ideally if you coul connect dropbox) Ideally integrate with Dropbox or similar cloud storage Export properly formatted Word documents Support for non-English languages (in thi case Slovak) would be important as well. Does anyone have experience with tools that can do this reliably?

8h ago

---

**[Anthropic believes RSI (recursive self improvement) could arrive “as soon as early 2027”](https://www.reddit.com/r/artificial/comments/1rdujgd/anthropic_believes_rsi_recursive_self_improvement/)**

Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

🔗 [anthropic.com](https://www.anthropic.com/responsible-scaling-policy/roadmap) • 19h ago

---

**[Knowledge is the key to unlocking AI's full potential as a creative tool](https://www.reddit.com/r/artificial/comments/1re43cm/knowledge_is_the_key_to_unlocking_ais_full/)**

I had this insight as I was vibecoding the night away. Of course people are going to use AI in lieu of learning how to do things, but I also think there will be a more compelling group that will realize that the more knowledge you have, the higher you can go with these tools, and this will inspire people to learn, so that they can then use that knowledge to create things with AI.

12h ago

---

**[IBM stock tumbles 10% after Anthropic launches COBOL AI tool](https://www.reddit.com/r/artificial/comments/1rcxj45/ibm_stock_tumbles_10_after_anthropic_launches/)**

Investing.com -- IBM (NYSE:IBM) shares hit a session low Monday afternoon, falling 10%, after Anthropic announced an AI tool designed to streamline COBOL code modernization. Accenture (NYSE:ACN) and Cognizant Technology Solutions (NASDAQ:CTSH) also declined following the news.

🔗 [Yahoo Finance](https://finance.yahoo.com/news/ibm-stock-tumbles-10-anthropic-194042677.html) • 1d ago

---

**[Meta strikes up to $100B AMD chip deal as it chases 'personal superintelligence'](https://www.reddit.com/r/artificial/comments/1rdm17p/meta_strikes_up_to_100b_amd_chip_deal_as_it/)**

Meta is buying billions of dollars in AMD AI chips in a multiyear deal tied to a 160 million-share warrant, deepening its push to diversify beyond Nvidia and expand data center capacity.

🔗 [TechCrunch](https://techcrunch.com/2026/02/24/meta-strikes-up-to-100b-amd-chip-deal-as-it-chases-personal-superintelligence/) • 1d ago

---

**[I've been running blind reviews between AI models for six months. here's what I didn't expect](https://www.reddit.com/r/artificial/comments/1rdilvu/ive_been_running_blind_reviews_between_ai_models/)**

context: I've been building a system that sends the same question to multiple models in parallel, then has each model review the others. six months, a few thousand sessions, mostly legal and financial questions the design decision I agonized over the most turned out to matter more than any other choice I made blind review changes everything I tested two versions. in one, the reviewing model sees "this is Claude's response." in the other, it just sees "Response A" the difference is kind of alarming when models know they're reviewing a named model, they hedge. they find "nuanced perspectives." there's something resembling professional courtesy baked into these things. makes sense if you think about the training data. reddit threads and twitter posts where people debate which model is better, lots of human-written comparisons that try to be balanced. the politeness is learned behavior with blind review, the gloves come off. scores spread out. critiques get specific. Claude in particular gets almost mean when it doesn't know it's reviewing GPT. it'll identify logical leaps, flag unstated assumptions, point out when a claim needs a citation that isn't there. stuff it would politely sidestep in the named version I don't have a rigorous paper on this. few hundred sessions, skewed toward legal and financial questions. but the pattern was consistent enough that I built the entire system around blind review and never looked back courtesy bias has a direction here's the thing I still don't understand. the courtesy effect is stronger in some directions than others. Claude reviewing GPT blind vs named shows the biggest delta. GPT reviewing Claude shows less difference. I have no good theory for why agreement is less useful than disagreement I assumed the point was to find consensus. three models agree, you're probably right. but sessions with the lowest initial agreement actually produce the best final answers model agreement on factual stuff: 70-80%. analytical or strategic questions: 40-50%. and the low-agreement sessions, where models are fighting, tend to surface things no single model caught. forced convergence seems to produce higher quality than natural consensus I suspect agreement means the models are pulling from the same training patterns. disagreement means at least one found a different path through the problem. the different path is usually where the insight lives the tool I built around this is in my profile if anyone wants to see blind review in action. curious whether others working with multi-model systems have noticed similar patterns

1d ago

---

**[Hegseth and Anthropic CEO set to meet as debate intensifies over the military's use of AI](https://www.reddit.com/r/artificial/comments/1rdj2lr/hegseth_and_anthropic_ceo_set_to_meet_as_debate/)**

Defense Secretary Pete Hegseth plans to meet with the CEO of Anthropic. The artificial intelligence company is the only one of its peers to not supply its technology to a new U.S. military internal network.

🔗 [AP News](https://apnews.com/article/anthropic-hegseth-ai-pentagon-military-3d86c9296fe953ec0591fcde6a613aba) • 1d ago

---

**[AI Reveals Unexpected New Physics in the Fourth State of Matter](https://www.reddit.com/r/artificial/comments/1rd9ivd/ai_reveals_unexpected_new_physics_in_the_fourth/)**

I predicted early in January that ai will discover new physics before 2028 is over, came earlier than expected.

🔗 [SciTechDaily](https://scitechdaily.com/ai-reveals-unexpected-new-physics-in-the-fourth-state-of-matter/) • 1d ago

---

---

## Google News: "ai"

**[Anthropic ditches its core safety promise in the middle of an AI red line fight with the Pentagon](https://www.cnn.com/2026/02/25/tech/anthropic-safety-policy-change)**

Anthropic, a company founded by OpenAI exiles worried about the dangers of AI, is loosening its core safety principle in response to competition.

CNN • 3h ago

---

**[Anthropic Is Dropping Its Signature Safety Pledge Amid a Heated AI Race](https://www.businessinsider.com/anthropic-changing-safety-policy-2026-2)**

Anthropic said it will no longer "pause the scaling and/or delay the deployment of new models" when the updates would outpace its own safety measures.

Business Insider • 15m ago

---

**[Anthropic Drops Hallmark Safety Pledge in Race With AI Peers](https://finance.yahoo.com/news/anthropic-drops-hallmark-safety-pledge-080051173.html)**

The company in 2023 said in its Responsible Scaling Policy that it would delay AI development that might be dangerous.  In a Tuesday blog post, Anthropic said it was updating its rules to say it would no longer do so if it believes it lacks a significant lead over a competitor.  “The policy environment has shifted toward prioritizing AI competitiveness and economic growth, while safety-oriented discussions have yet to gain meaningful traction at the federal level,” Anthropic said in its post.

Yahoo Finance • 3h ago

---

**[Tech Firms Aren’t Just Encouraging Their Workers to Use AI. They’re Enforcing It.](https://www.wsj.com/tech/ai/tech-firms-arent-just-encouraging-their-workers-to-use-ai-theyre-enforcing-it-d43ebf84?gaa_at=eafs&gaa_n=AWEtsqfr5OwHvyQgWbRUA7ag8xrRz70kVTp5IczRso4dtC2p4rWkCx3JnoOQ&gaa_ts=699f3654&gaa_sig=2iD1zaY51GbOk6DWdw31_psX3O_Lf89OSH5Q_Viwv54XPzFeTP56H4v-tBiToemhVt7PdQP0fQ-fHJ63Z6dscw%3D%3D)**

WSJ • 16h ago

---

**[Robotaxis are learning to drive in an AI-simulated world](https://www.axios.com/2026/02/25/ai-waymo-robotaxis-av)**

Axios • 32m ago

---

**[Alpha School student shares how AI helps her learn](https://www.foxnews.com/video/6389893925112)**

11-year-old Alpha School student Everest Nevraumont joins 'America's Newsroom' to discuss her experience attending the State of the Union address and her experience utilizing AI at Alpha School to accelerate learning.

Fox News • 29m ago

---

**[San Jose animal shelter warns of fake AI photo claiming dog was to be euthanized](https://www.cbsnews.com/sanfrancisco/news/san-jose-animal-shelter-warns-fake-ai-photo-claiming-dog-to-be-euthanized/)**

A San Francisco Bay Area animal shelter said it has been flooded with phone calls after a fake AI-generated post claiming one of its dogs would be euthanized went viral.

CBS News • 33m ago

---

**[These Tools Say They Can Spot A.I. Fakes. Do They Really Work?](https://www.nytimes.com/2026/02/25/technology/ai-detection-generated-photos-video.html)**

The New York Times • 7h ago

---

**[AI Panic Is Opportunity for Stock Pickers, Morgan Stanley Says](https://finance.yahoo.com/news/ai-panic-opportunity-stock-pickers-120414620.html)**

Investors should seek out what the team referred to as AI incumbents, strong growers and high-quality names to take advantage of lower prices and momentum behind adoption of the technology.  The investment case for AI adopters with high pricing power continues to strengthen, strategists including Andrew Pauker said.  “Nearer-term AI adoption tailwinds help to offset longer-term disruption fears for impacted areas and for the overall market,” Pauker wrote.

Yahoo Finance • 5h ago

---

**[Jamie Dimon says AI is already reshaping JPMorgan Chase's workforce as bank plans 'huge redeployment’](https://www.cnbc.com/2026/02/24/jpm-ceo-jamie-dimon-ai-reshaping-workforce-redeployment.html)**

JPMorgan, the world's biggest bank by market cap, has the industry's largest annual tech budget at nearly $20 billion, and it has outlined an ambitious AI plan.

CNBC • 21h ago

---

---

## HackerNews: "ai"

**[IDF killed Gaza aid workers at point blank range in 2025 massacre: Report](https://news.ycombinator.com/item?id=47136179)**

A minute-by-minute reconstruction of the massacre by Earshot and Forensic Architecture found Israeli soldiers fired over 900 bullets at the aid workers, killing 15.

⬆️ 1975 • 💬 818 • 1d ago • [dropsitenews.com](https://www.dropsitenews.com/p/israeli-soldiers-tel-sultan-gaza-red-crescent-civil-defense-massacre-report-forensic-architecture-earshot)

---

**[Ladybird adopts Rust, with help from AI](https://news.ycombinator.com/item?id=47120899)**

We're adopting Rust as our C++ successor language, and using AI agents to accelerate the transition.

⬆️ 1261 • 💬 696 • 2d ago • [ladybird.org](https://ladybird.org/posts/adopting-rust/)

---

**[Google restricting Google AI Pro/Ultra subscribers for using OpenClaw](https://news.ycombinator.com/item?id=47115805)**

I’m seeking assistance regarding a sudden restriction on my Google AI Ultra account that has persisted for three days. I received no prior warnings or notifications regarding a potential violation.  The only recent change in my workflow was connecting Gemini models via OpenClaw OAuth. If third-party integrations are the issue, I would expect the platform to block the integration rather than restrict a paid account ($249/mo) without communication.  I have already emailed support but haven’t recei...

⬆️ 798 • 💬 693 • 2d ago • [Google AI Developers Forum](https://discuss.ai.google.dev/t/account-restricted-without-warning-google-ai-ultra-oauth-via-openclaw/122778)

---

**[Pope tells priests to use their brains, not AI, to write homilies](https://news.ycombinator.com/item?id=47119210)**

⬆️ 571 • 💬 442 • 2d ago • [ewtnnews.com](https://www.ewtnnews.com/vatican/pope-leo-xiv-tells-priests-to-use-their-brains-not-ai-to-write-homilies)

---

**[How we rebuilt Next.js with AI in one week](https://news.ycombinator.com/item?id=47142156)**

One engineer used AI to rebuild Next.js on Vite in a week. vinext builds up to 4x faster, produces 57% smaller bundles, and deploys to Cloudflare Workers with a single command.

⬆️ 487 • 💬 201 • 21h ago • [The Cloudflare Blog](https://blog.cloudflare.com/vinext/)

---

**[Firefox 148 Launches with AI Kill Switch Feature and More Enhancements](https://news.ycombinator.com/item?id=47133313)**

The latest update of Firefox, version 148, introduces a much-anticipated "AI kill switch" feature, allowing users to disable AI functionalities such as chatbot prompts and AI-generated link summaries. Mozilla emphasizes that once AI features are turned off, future updates will not override this choice. This decision reflects the company’s new revenue-focused strategy regarding AI integrations. […]

⬆️ 455 • 💬 383 • 1d ago • [ServerHost Hosting Solutions Blog](https://serverhost.com/blog/firefox-148-launches-with-exciting-ai-kill-switch-feature-and-more-enhancements/)

---

**[FreeBSD doesn't have Wi-Fi driver for my old MacBook, so AI built one for me](https://news.ycombinator.com/item?id=47129361)**

My old 2016 MacBook Pro has been collecting dust in a cabinet for some time now. The laptop suffers from a “flexgate” problem, and I don’t have any practical use for it. For quite some time, I’ve been thinking about repurposing it as a guinea pig, to play with FreeBSD — an OS that I’d aspired to play with for a long while, but had never had a real reason to.
During the recent holiday season, right after FreeBSD 15 release, I’ve finally found time to set the laptop up. Doing that I didn’t plan, or even think, this may turn into a story about AI coding.

⬆️ 428 • 💬 358 • 1d ago • [Vladimir Varankin](https://vladimir.varank.in/notes/2026/02/freebsd-brcmfmac/)

---

**[AI Added 'Basically Zero' to US Economic Growth Last Year, Goldman Sachs Says](https://news.ycombinator.com/item?id=47130208)**

Imported chips and hardware mean the AI investments are translating into US GDP growth.

⬆️ 285 • 💬 270 • 1d ago • [Gizmodo](https://gizmodo.com/ai-added-basically-zero-to-us-economic-growth-last-year-goldman-sachs-says-2000725380)

---

**[Osaka: Kansai Airport proud to have never lost single piece of luggage (2024)](https://news.ycombinator.com/item?id=47139224)**

<p>IZUMI-SANO, Osaka — Kansai Airport is proud to have never had a lost baggage incident in the 30 years since it opened in 1994, earning recognition as the airport with the world’s best baggage service.</p>

⬆️ 217 • 💬 105 • 1d ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/features/japan-focus/20241228-229891/)

---

**[Show HN: AI Timeline – 171 LLMs from Transformer (2017) to GPT-5.3 (2026)](https://news.ycombinator.com/item?id=47119871)**

Track every major LLM from 2017 to 2026. From Transformers → GPT → ChatGPT → Claude → Gemini → DeepSeek and beyond.

⬆️ 169 • 💬 57 • 2d ago • [LLM Timeline](https://llm-timeline.com/)

---

---

## YouTube Videos: "ai"

**[I Used AI To Copy A YouTube Channel Making $1k+/Day](https://www.youtube.com/watch?v=TNJ6qh12nmA)**

I replicated this faceless AI YouTube channel step-by-step. Here's how... ▻ Get 50% Off Wondercraft: ...

📺 Wholesale Ted

👁️ 20K • 👍 2K • 💬 238 • ⏱️ 18:46 • 23h ago

---

**[(FREE) 3 UNCENSORED AI Video Generators That Are Actually FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=t9QR_barT_U)**

Discover how to use Seedance 2 Pro for free and unlimited access without paying for early access. In this video, I reveal two ...

📺 Brain Project

👁️ 7K • 👍 250 • 💬 116 • ⏱️ 10:42 • 1d ago

---

**[The AI Tsunami is Here &amp; Society Isn&#39;t Ready | Dario Amodei x Nikhil Kamath | People by WTF](https://www.youtube.com/watch?v=68ylaeBbdsg)**

I sat down with Dario Amodei in Bangalore. He built Claude, but he started as a biologist looking for a tool to cure disease. Today ...

📺 Nikhil Kamath

👁️ 342K • 👍 8K • 💬 1K • ⏱️ 1:08:35 • 1d ago

---

**[The AI Music Tool That&#39;s About to Break the Internet (And It&#39;s Free Right Now)](https://www.youtube.com/watch?v=fK886jyF9Hw)**

The most unhinged AI music generator just dropped — and right now, it's completely free. Sonauto V3 is here, and it is not holding ...

📺 Theoretically Media

👁️ 25K • 👍 1K • 💬 440 • ⏱️ 14:49 • 18h ago

---

**[AI is changing the World Of Theoretical Physics, Fast.](https://www.youtube.com/watch?v=JvgaZ_myFE4)**

Grab your free seat to the 2-Day AI Mastermind: https://link.outskill.com/SABINEHOSFEB4 100% Discount for the first 1000 ...

📺 Sabine Hossenfelder

👁️ 230K • 👍 13K • 💬 2K • ⏱️ 7:09 • 1d ago

---

**[Market CRASH After Viral AI Doom Post](https://www.youtube.com/watch?v=kNInY3ZAMWo)**

Krystal and Saagar discuss markets tanking over AI fears. Sign up for a PREMIUM Breaking Points subscriptions for full early ...

📺 Breaking Points

👁️ 254K • 👍 7K • 💬 2K • ⏱️ 12:54 • 22h ago

---

**[7 Google AI Courses to Learn AI That Cost Nothing](https://www.youtube.com/watch?v=UsVSWMGCrBA)**

In this video, I break down five free Google AI courses that teach how AI actually works under the hood instead of just how to ...

📺 James Blue

👁️ 3K • ⏱️ 11:13 • 2h ago

---

**[the SCARIEST chart in AI](https://www.youtube.com/watch?v=yuW0939jtco)**

Details in the Newsletter: https://natural20.beehiiv.com/p/the-scariest-chart-in-ai-metr-ai-agents-capability-accelerating The Site ...

📺 Wes Roth

👁️ 64K • 👍 2K • 💬 729 • ⏱️ 24:44 • 1d ago

---

**[Tracy Morgan Is TERRIFIED of AI 😂 “I’ll Just Pull the Plug!” #shorts #funny #comedy](https://www.youtube.com/watch?v=5w-xKKeHQY4)**

Tracy Morgan talking about AI is the funniest thing you'll hear today. In this classic interview moment, Tracy Morgan jokes about ...

📺 The Comedy Compound

👁️ 2K • 👍 65 • 💬 3 • ⏱️ 0:12 • 9h ago

---

**[Urgent research needed to tackle AI threats, says Google AI boss | BBC News](https://www.youtube.com/watch?v=j5o8iD8qz3k)**

More research on the threats of artificial intelligence (AI) "needs to be done urgently", the boss of Google DeepMind has told BBC ...

📺 BBC News

👁️ 38K • 👍 297 • 💬 133 • ⏱️ 3:17 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 482,910 • ❤️ 1,052 • 2d ago

---

**[Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)**

*Qwen*

Qwen3.5-35B-A3B is a 35B parameter vision-language model with a 3B activated MoE architecture, excelling in multimodal reasoning and coding across 201 languages. It supports a native context length of 262,144 tokens, making it suitable for complex cross-modal tasks and multilingual applications.

`image-text-to-text` `36.0B`

⬇️ 20,991 • ❤️ 366 • 1d ago

---

**[Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)**

*Qwen*

Qwen3.5-27B is a 27B parameter multimodal foundation model with an efficient hybrid architecture, excelling in vision-language understanding and generation across 201 languages. Its key capabilities include early fusion multimodal training, scalable RL generalization, and a long context length (262K+ tokens), making it suitable for advanced reasoning, coding, and agent-based applications.

`image-text-to-text` `27.8B`

⬇️ 6,875 • ❤️ 257 • 14h ago

---

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 181,706 • ❤️ 1,548 • 12d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 227,984 • ❤️ 792 • 3d ago

---

**[Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)**

*Qwen*

Qwen3.5-122B-A10B is a 122B parameter multimodal causal language model with an efficient hybrid architecture (Gated Delta Networks + MoE) and a 262k context window. It excels at unified vision-language tasks, multilingual understanding (201 languages), and complex reasoning, making it suitable for advanced AI applications requiring cross-modal comprehension and broad linguistic capabilities.

`image-text-to-text` `125.1B`

⬇️ 3,320 • ❤️ 226 • 1d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation`

⬇️ 240,246 • ❤️ 928 • 9d ago

---

**[Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF](https://huggingface.co/TeichAI/Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF)**

*TeichAI*

A distilled 14B parameter Qwen3 model fine-tuned on Claude 4.5 Opus high-reasoning data for enhanced coding, science, and general-purpose text generation tasks.

`text-generation` `14.8B`

⬇️ 43,099 • ❤️ 202 • 2d ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 537,707 • ❤️ 2,197 • 9d ago

---

**[LocoOperator-4B](https://huggingface.co/LocoreMind/LocoOperator-4B)**

*LocoreMind*

LocoOperator-4B is a 4B-parameter tool-calling agent optimized for multi-turn codebase exploration. It excels at reading files, searching code, and navigating project structures with 100% JSON validity for tool calls, enabling local, zero-API-cost agent deployment via llama.cpp.

`text-generation` `4.0B`

⬇️ 232 • ❤️ 175 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 6 • 💬 0 • ⭐ 8,116 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 14 • 💬 1 • ⭐ 9,695 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 13 • 💬 1 • ⭐ 4,768 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 3 • 💬 0 • ⭐ 4,721 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based portrait animation framework that improves real-time performance through hybrid implicit signals, appearance distillation, and autoregressive streaming generation.

▲ 37 • 💬 3 • ⭐ 2,221 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.11253) • [💻 code](https://github.com/GVCLab/PersonaLive)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 147 • 💬 19 • ⭐ 54,101 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 18 • 💬 1 • ⭐ 30,653 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 38 • 💬 1 • ⭐ 71,149 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 69 • 💬 2 • ⭐ 8,516 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 26 • 💬 4 • ⭐ 18,075 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `official` `official-website`

⭐ 19.1k • 🔱 2.3k • 1h ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 7.2k • 🔱 558 • 14d ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"

`Python`

⭐ 5.5k • 🔱 674 • 11h ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`Python`

⭐ 4.0k • 🔱 210 • 3h ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router empowering OpenClaw — by BlockRunAI

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 3.5k • 🔱 348 • 13h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 3.3k • 🔱 432 • 1d ago

---

**[HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app)**

Toonflow 是一款 AI 短剧漫剧工具，能够利用 AI 技术将小说自动转化为剧本，并结合 AI 生成的图片和视频，实现高效的短剧创作。借助 Toonflow，可以轻松完成从文字到影像的全流程，让短剧制作变得更加智能与便捷。

`HTML`

⭐ 2.9k • 🔱 335 • 1d ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.8k • 🔱 192 • 4h ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 2.4k • 🔱 489 • 3h ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 2.4k • 🔱 267 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*
