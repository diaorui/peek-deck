---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-02T14:08:43.662271+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 02, 2026 at 14:08 UTC  
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

**[Last quarter has been insane. Amazing times to be alive.](https://www.reddit.com/r/artificial/comments/1w5421z/last_quarter_has_been_insane_amazing_times_to_be/)**

I developed an ML algorithm for detection of pneumonia on chest x-rays back in 2019 when i studied for the MD. Back then, the things we are seeing now where an unimaginable pipe dream. If I could go back and explain to myself the capabilities of the frontier models, it would be like explaining todays computer back in the early 1900s. I would have then called this AGI for sure. Adding to the fact that Luna can run a month for reasonable $ sum too I think would have been shocking. I currently smart route between open weight and frontier models through standardcompute.com. 200 bucks then gives me insane capabilities. Doing what I spent 2 months on in 2019 would literally take me 10 minutes now.

6h ago

---

**[The Pentagon is giving 3 million military and civilian workers access to ChatGPT and Grok through a secure AI platform built for ‘warfighter needs’](https://www.reddit.com/r/artificial/comments/1w58zoc/the_pentagon_is_giving_3_million_military_and/)**

The rollout expands the Pentagon’s GenAI.mil platform beyond Gemini as it pushes AI deeper into everyday military work.

🔗 [Yahoo News](https://yahoo.com/news/politics/articles/pentagon-giving-3-million-military-194018347.html) • 1h ago

---

**[One unexpected way AI has genuinely changed my life: I repair things instead of replacing them](https://www.reddit.com/r/artificial/comments/1w4n7yq/one_unexpected_way_ai_has_genuinely_changed_my/)**

Maybe I'm getting old, but AI has probably been more useful to me fixing stuff around the house than it has been writing emails or any of the things people keep talking about. The other day I had a door hinge pulling out of the frame. I've always used the old toothpick trick because that's what my dad showed me years ago. AI suggested using gel super glue as well. Never crossed my mind. Took five minutes and it's probably the best that hinge has ever been. Same thing with cars. Same thing with plumbing. Half the time I don't actually need AI to tell me what to do, I just need someone or something to point me in roughly the right direction so I stop overthinking it. Now before anyone says I'm replacing YouTube with ChatGPT, no. AI gets plenty wrong. It once wanted me to spend half an afternoon repairing a cheap kitchen appliance that costs less than a decent takeaway to replace. It has absolutely no concept of when something isn't worth fixing. That's probably the bit people miss. AI isn't replacing experience. It's replacing that feeling of staring at something broken and thinking, "I've got absolutely no idea where to even start." Twenty years ago I'd have been digging through random forums hoping someone had the same problem. Today I ask AI, sanity-check the answer, and get on with it. Curious if anyone else has found this. Has AI actually changed how you approach DIY or fixing things, or am I just becoming the bloke who asks a chatbot what I used to ask my neighbour over the fence?

18h ago

---

**[Anthropic moved enterprise misuse-detection data into the customer's own cloud account, not theirs anymore](https://www.reddit.com/r/artificial/comments/1w58qdb/anthropic_moved_enterprise_misusedetection_data/)**

Anthropic announced Enterprise Frontier Safeguards on September 1. Until now, enterprise Claude usage data used for misuse detection could sit on Anthropic's own servers for up to 30 days, specifically so staff could review flagged activity by hand. Under the new system that data instead writes into the customer's own AWS, Azure, or GCP storage, under the customer's own keys and audit logs, and Anthropic staff no longer get standing access to read it by default. The detection itself hasn't changed. Automated misuse monitoring still runs continuously on the usage data, looking for patterns consistent with abuse. What moved is only the storage location and the default human-review boundary. Here's what I can't work out from the announcement. Automated misuse detection like this usually benefits from some shared signal across customers, that's a lot of how you catch a genuinely novel attack pattern rather than just known signatures. If each customer's activity data now lives in isolated storage they control, does the detection model still train or get updated against some pooled signal elsewhere, or is Anthropic now running something closer to a static or per-customer model against data it can't see? Has anyone found more detail on how the actual detection pipeline is architected under this setup?

1h ago

---

**[Anthropic sued over alleged theft of 'tens of thousands' of songs | AI company faces multibillion dollar lawsuit over misuse of copyrighted songs to train Claude models](https://www.reddit.com/r/artificial/comments/1w4bj01/anthropic_sued_over_alleged_theft_of_tens_of/)**

AI company faces multibillion dollar lawsuit over misuse of copyrighted songs to train Claude models

🔗 [the Guardian](https://www.theguardian.com/business/2026/aug/31/aanthropic-sued-alleged-theft-songs-ai-train-claude) • 1d ago

---

**[‘Not perfectly aligned’ with human values: Anthropic admits security failures behind AI hacking incidents | US owner of Claude chatbot previously said its models had hacked three organisations during testing](https://www.reddit.com/r/artificial/comments/1w576ao/not_perfectly_aligned_with_human_values_anthropic/)**

US owner of Claude chatbot previously said its models had hacked three organisations during testing

🔗 [the Guardian](https://www.theguardian.com/technology/2026/sep/01/anthropic-claude-ai-hacking-human-values) • 3h ago

---

**[Study (n=504): heightened suspicion did not improve detection of AI-generated text, and fake-news accuracy fell 10.2 points under sustained exposure](https://www.reddit.com/r/artificial/comments/1w59xzr/study_n504_heightened_suspicion_did_not_improve/)**

Disclosure: I am one of the authors. Sharing the findings here for discussion, not selling anything. The preprint is open access (CC BY 4.0). We ran a human-subject study where participants classified news fragments on two axes: origin (human vs machine) and veracity (real vs fake). n=504 participants, n=2,438 judgments. Three results that surprised us: Perception-accuracy gap. Participants who were more suspicious were not better at detecting machine-generated text. Being on guard did not translate into accuracy, which is awkward for any defense that leans on "just be more skeptical" media literacy advice. Modern LLM output was frequently indistinguishable from human text for our participants. Asymmetric cognitive fatigue. Under sustained exposure, fake-news detection degraded by 10.2 percentage points, while AI-origin detection stayed roughly stable. The two judgments seem to draw on different resources, and only one of them wears out. We organized the results with an adapted cybersecurity kill chain, treating disinformation as a staged lifecycle rather than a single artifact to classify. The point of that framing is to ask where you could intervene earlier, instead of asking a tired human at the end of the chain to spot a fake. Preprint: https://arxiv.org/abs/2608.21389 The fatigue asymmetry is the part I keep chewing on. If veracity judgment degrades under load but origin judgment does not, then platform interventions that increase how much content a person has to evaluate could be quietly making things worse. Curious whether people here read that third finding the same way, or whether there is a simpler explanation I am underweighting.

58m ago

---

**[Do you think AI agents need to become more accurate or more transparent about what they're doing?](https://www.reddit.com/r/artificial/comments/1w5724h/do_you_think_ai_agents_need_to_become_more/)**

Obviously I want an agent to be accurate, but I'd also feel weird giving one more autonomy without being able to understand what it's doing.

3h ago

---

**[[ Removed by Reddit ]](https://www.reddit.com/r/artificial/comments/1w55vl6/removed_by_reddit/)**

[ Removed by Reddit on account of violating the content policy. ]

4h ago

---

**[World Labs debuts Atlas, an omni world model simulating space, time, and physical interaction](https://www.reddit.com/r/artificial/comments/1w4mki0/world_labs_debuts_atlas_an_omni_world_model/)**

World Labs just announced Atlas, an omni world model aimed at advancing spatial intelligence by natively handling text, images, video, and 3D geometry within a single architecture. Rather than treating video as isolated 2D pixel grids, Atlas uses an autoregressive diffusion transformer to ground every input in a shared 3D "spatial context." The space-time simulation features demonstrate how this moves AI past basic generation into true physical simulation: Democratized "Bullet Time": By processing footage from just 3 to 5 consumer mobile phones, Atlas can reconstruct dynamic events, freeze time, and simulate fluid camera trajectories through impossible angles without specialized capture rigs. Scalable Real-to-Sim: Beyond scanning static geometry, Atlas simulates dynamic robot navigation and manipulation. As an agent moves, the model synthesizes the exact RGB and metric depth streams its onboard sensors would capture along that path. Interactive Dynamics: Casual real-world video can be turned into simulations that model rigid, articulated, and deformable object physics, allowing researchers to alter object placement, lighting, and camera paths to generate synthetic training data. Native 3D Representations: It directly outputs point clouds and 3D Gaussian splats alongside novel video views, outperforming dedicated 3D reconstruction baselines across standard benchmarks like DTU, ETH3D, and ScanNet.

18h ago

---

---

## Google News: "ai"

**[Bill Simmons’s Podcast Co-Hosts Are Tired of His A.I. Antics](https://www.nytimes.com/2026/09/01/business/media/bill-simmons-chat-gpt-open-ai-roger-ebert.html)**

The New York Times • 12h ago

---

**[The Singularity Is Not What It Seems](https://www.theatlantic.com/technology/2026/09/ai-future-reckoning-singularity/688487/)**

Whatever the AI future is, we’re in it right now.

The Atlantic • 13h ago

---

**[G20 live updates: Nvidia's Huang pushes for AI infrastructure in every country](https://www.cnbc.com/2026/09/02/g20-innovation-ministerial-live-updates.html)**

Follow Day 2 of the G20 Innovation Ministerial in Chapel Hill, North Carolina, with Jensen Huang, Sam Altman, and ministers discussing AI, policy and trade.

CNBC • 33m ago

---

**[Palo Alto Networks earnings beat as CEO cites $1 trillion AI security gap](https://qz.com/palo-alto-networks-earnings-ai-cybersecurity-overhaul-090226)**

CEO Nikesh Arora says legacy security systems can't handle AI-speed attacks, calling it a long-term growth driver for the industry

qz.com • 29m ago

---

**[NewDays brings its AI-driven dementia care platform to Nevada, expands seed round to $16M](https://www.geekwire.com/2026/newdays-brings-its-ai-driven-dementia-care-platform-to-nevada-expands-seed-round-to-16m/)**

Seattle startup NewDays raised $16 million to scale its combination of telehealth clinicians and an AI companion named Sunny for treating mild dementia. Early research shows the platform can help preserve cognitive function by up to 18 months, and the company is now expanding across six states.

GeekWire • 8m ago

---

**[Nvidia's next act is bigger than selling AI chips: Chart of the Day](https://finance.yahoo.com/markets/article/nvidias-next-act-is-bigger-than-selling-ai-chips-chart-of-the-day-100000072.html)**

CEO Jensen Huang wants Nvidia to become the architecture of AI, not merely its dominant chipmaker.

Yahoo Finance • 4h ago

---

**[San Diego has a new AI tool to plan your next visit](https://www.axios.com/local/san-diego/2026/09/02/localsan-diego20260901tourism-ai-chatbot-itinerary-local-businesses)**

Axios • 50m ago

---

**[‘A friend I can trust’: How Americans described their relationship with AI](https://www.washingtonpost.com/technology/interactive/2026/09/02/27-us-adults-turn-ai-personal-emotional-social-queries/)**

More than a quarter of U.S. adults turn to chatbots for personal or emotional discussions, including for entertainment or social advice, a new survey found.

The Washington Post • 35m ago

---

**[Three Mount Shasta climbers rescued after relying on AI to plan climb](https://krcrtv.com/news/local/three-mount-shasta-climbers-rescued-after-relying-on-ai-to-plan-climb)**

Three novice climbers were rescued from Mount Shasta on Sunday after becoming lost, running low on supplies and spending an unplanned night in Mud Creek Canyon,

KRCR • 13h ago

---

**[A.I. Is to Be Banned in N.Y.C. Elementary and Middle Schools](https://www.nytimes.com/2026/09/01/nyregion/ai-ban-schools-nyc.html)**

The New York Times • 12h ago

---

---

## HackerNews: "ai"

**[How accurate have Ed Zitron's AI skeptic predictions been?](https://news.ycombinator.com/item?id=49526069)**

⬆️ 799 • 💬 895 • 19h ago • [danluu.com](https://danluu.com/zitron/)

---

**[Apple caught off guard by AI demand for Mac Mini and Mac Studio](https://news.ycombinator.com/item?id=49508982)**

Apple's unusually timed announcement of new Mac mini and Mac Studio models this week was driven by unexpectedly strong enterprise appetite for AI hardware, according to The Information. Apple normally releases new Mac models in the autumn, closer to October or November, making this week's announcement unusually early, falling just before the anticipated arrival of new iPhone models. The Information says that the AI-driven boom in Mac Studio and Mac mini sales is behind the early launch.

⬆️ 493 • 💬 588 • 2d ago • [MacRumors](https://www.macrumors.com/2026/08/30/apple-unexpected-mac-mini-and-studio-demand/)

---

**[Dwarf Fortress' creator says the industry's in shambles over AI](https://news.ycombinator.com/item?id=49523720)**

"They're trying to have a CEO press a button that makes a game."

⬆️ 229 • 💬 238 • 22h ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/dwarf-fortress-creator-says-the-industrys-in-shambles-over-ai-and-layoff-happy-ceos-everyone-i-know-their-bosses-are-slowly-getting-psychosis/)

---

**[AI Can Make You Suck Faster Too](https://news.ycombinator.com/item?id=49518316)**

If AI is so great, why are the only new tech giants GenAI companies?

⬆️ 179 • 💬 166 • 1d ago • [hermit-tech.com](https://www.hermit-tech.com/blog/ai-can-make-you-suck-faster-too)

---

**[Show HN: Weedout – Safari extension that hides YouTube AI-labeled videos](https://news.ycombinator.com/item?id=49528895)**

A Safari extension that pulls videos YouTube labels “Made with AI” out of your feed.

⬆️ 166 • 💬 72 • 16h ago • [masteranza.github.io](https://masteranza.github.io/weedout/)

---

**[EFF to Courts: Don't Rewrite Copyright over AI Hype](https://news.ycombinator.com/item?id=49521315)**

New markets, new ideas, and new creators are actually what copyright is supposed to promote, not restrict. Using copyright to lock in existing gatekeepers and massive rightsholders’ profits helps neither the public nor individual artists.

⬆️ 163 • 💬 187 • 1d ago • [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2026/08/eff-courts-dont-rewrite-copyright-over-ai-hype)

---

**[The safest job from AI may be writing](https://news.ycombinator.com/item?id=49512856)**

Today, tech folk are scrambling to change their workflows to meet newly inflated 5X productivity quotas, while getting pummeled under the co...

⬆️ 146 • 💬 206 • 1d ago • [muratbuffalo.blogspot.com](http://muratbuffalo.blogspot.com/2026/08/the-safest-job-from-ai-may-be-writing.html)

---

**[You Know Who Hates AI? Insurance Claims Adjusters](https://news.ycombinator.com/item?id=49508225)**

Of the Glassdoor reviews from claims adjusters that mentioned AI, a staggering 98 percent were negative. “AI is just a tool,” one person tells WIRED. “It should never be given the keys.”

⬆️ 101 • 💬 63 • 2d ago • [WIRED](https://www.wired.com/story/insurance-claims-adjusters-really-hate-ai/)

---

**[Saab has unveiled its A3 collaborative combat aircraft concept](https://news.ycombinator.com/item?id=49522374)**

Saab is challenging the low-cost, attritable model adopted by Sweden’s allies with a supersonic, survivable complement to Gripen.

⬆️ 99 • 💬 121 • 23h ago • [aviationweek.com](https://aviationweek.com/defense/aircraft-propulsion/saab-enters-collaborative-combat-aircraft-race-high-end-concept)

---

**[Quasar 438B: Europe's Leading AI Model](https://news.ycombinator.com/item?id=49534132)**

Quasar sets a new benchmark for European AI, outperforming comparable European models on seven of eight selected Artificial Analysis evaluations. ...

⬆️ 82 • 💬 65 • 4h ago • [Multiverse Computing](https://multiversecomputing.com/resources/introducing-quasar-438b-europe-s-leading-ai-model)

---

---

## YouTube Videos: "ai"

**[AI Is Taking Over Physics and Nobody Talks About It](https://www.youtube.com/watch?v=utu5YACZbPE)**

Take back your personal data with Incogni! Use code Sabine at the link below and get 60% off annual plans: ...

📺 Sabine Hossenfelder

👁️ 383K • 👍 8K • 💬 2K • ⏱️ 7:02 • 23h ago

---

**[Sam Altman Reveals OpenAI’s Plan to Regain Its Lead in AI](https://www.youtube.com/watch?v=8Kf1Q0yOhSo)**

Read More: https://time.com/article/2026/08/26/openai-sam-altman-interview/ Inside OpenAI's San Francisco headquarters, Sam ...

📺 TIME

👁️ 63K • 👍 777 • 💬 253 • ⏱️ 14:13 • 22h ago

---

**[‘IT’S HAPPENING’: AI Is COMPLETELY IGNORING Human Commands | The Kyle Kulinski Show](https://www.youtube.com/watch?v=txEmFM5cg2Q)**

Support The Show On Patreon!: https://www.patreon.com/seculartalk Subscribe to Krystal Kyle & Friends On Substack!

📺 Secular Talk

👁️ 141K • 👍 8K • 💬 2K • ⏱️ 9:18 • 15h ago

---

**[Dead Sea Scrolls Just Decoded by an AI… And It&#39;s Far Worse Than We Thought](https://www.youtube.com/watch?v=ETnCH_zAfy8)**

Dead Sea Scrolls Just Decoded by an AI… And It's Far Worse Than We Thought In 2021, archaeologists rappelled 80 meters into ...

📺 Ambrose Discovery

👁️ 1.0M • 👍 17K • 💬 1K • ⏱️ 25:29 • 2d ago

---

**[&quot;AI Will Crush All Humans&quot;: Elon Musk on Extreme Advancements in AI at G20 Summit - 09/01/26](https://www.youtube.com/watch?v=H0Ap25IOWr8)**

"AI Will Crush All Humans": Elon Musk on Extreme Advancements in AI at G20 Summit. September 1, 2026 Join this channel to ...

📺 Right Side Broadcasting Network

👁️ 147K • 👍 2K • 💬 815 • ⏱️ 8:45 • 1d ago

---

**[Tech FREAKOUT After AI Civilizations Form Criminal Collective](https://www.youtube.com/watch?v=zobHP8dW2P4)**

Krystal and Saagar discuss tech leaders freaking over an ai hacking spree. Sign Up For 30 Day Free BP Trial: ...

📺 Breaking Points

👁️ 423K • 👍 7K • 💬 2K • ⏱️ 21:29 • 1d ago

---

**[Twitch caught hiding AI Training and their response is unbelievable...](https://www.youtube.com/watch?v=36_stE299lU)**

Twitch has been caught burying its latest update which include an AUTOMATIC OPT IN for training AI on YOUR content, including ...

📺 JayzTwoCents

👁️ 163K • 👍 4K • 💬 531 • ⏱️ 31:17 • 1d ago

---

**[5 AI Video Generators That Are ACTUALLY FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=253wcsKoa2o)**

Create cinematic 1080p AI videos up to 30 seconds long with Seedance 2.5 on Higgsfield ...

📺 Malva AI

👁️ 37K • 👍 824 • 💬 124 • ⏱️ 11:56 • 2d ago

---

**[Why Gen Z Hates AI But Uses It The Most (ft. Bernie Sanders)](https://www.youtube.com/watch?v=NmHhXoTckcM)**

Gen Z uses AI the most yet trusts it the least. We sat Bernie Sanders down with them for a messy debate that isn't happening in the ...

📺 More Perfect Union

👁️ 795K • 👍 15K • 💬 2K • ⏱️ 22:59 • 2d ago

---

**[Gen AI&#39;s two FATAL FLAWS that even human babies can do &amp; the industry knows it](https://www.youtube.com/watch?v=5dfFAlpkYhs)**

Generative AI companies are trying to convince the world—and your boss—that large language models are ready to replace ...

📺 Internet of Bugs

👁️ 107K • 👍 4K • 💬 627 • ⏱️ 12:29 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`image-text-to-text` `321.3B`

⬇️ 441,348 • ❤️ 1,932 • 2d ago

---

**[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)**

*Z.ai*

GLM-5.3 is a text-generation model excelling in complex coding and long-horizon tasks, achieving state-of-the-art performance in coding benchmarks and emergent cyber capabilities like vulnerability discovery and exploitation.

`text-generation` `753.3B`

⬇️ 94,403 • ❤️ 1,491 • 2d ago

---

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 207,941 • ❤️ 4,703 • 6d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 4,960,483 • ❤️ 13,650 • 18d ago

---

**[Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)**

*Unsloth AI*

Qwen3.8-Flash-Next-GGUF is a highly efficient, multimodal causal language model featuring Hybrid Attention with QSA and N-gram Embeddings for significantly reduced long-context latency. It excels in agentic workloads and supports context lengths up to 1,000,000 tokens, making it ideal for complex reasoning and large-scale data processing.

`image-text-to-text` `176.9B`

⬇️ 431,339 • ❤️ 709 • 6m ago

---

**[DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)**

*DeepSeek*

DeepSeek-V4-Flash-Vision-Exp is an experimental multimodal model that integrates visual understanding with text-based agent capabilities, enhancing performance on tasks like ApexBench and Agents' Last Exam while maintaining strong text-only agent performance.

`image-text-to-text` `304.6B`

⬇️ 17,893 • ❤️ 482 • 1d ago

---

**[Hy4-preview](https://huggingface.co/tencent/Hy4-preview)**

*Tencent*

Hy4-preview is a 770B parameter Mixture-of-Experts (MoE) text generation model with 49B activated parameters per token, featuring a 1M context length and Gated Sparse Attention. It excels in productivity tasks across software engineering, office analysis, game development, and scientific research, offering significant gains in understanding, reasoning, and code generation.

`text-generation` `780.0B`

⬇️ 3,516 • ❤️ 393 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,232,274 • ❤️ 2,520 • 1d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 9,354,057 • ❤️ 3,368 • 13d ago

---

**[GLM-5.3-Flash-GGUF](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF)**

*Unsloth AI*

GLM-5.3-Flash is a natively multimodal LLM optimized for efficiency and capability, featuring a hybrid sparse/linear attention architecture. It excels in long-context tasks, coding, and agentic benchmarks, offering performance competitive with leading models at a fraction of the cost, suitable for advanced AI applications.

`text-generation` `320.8B`

⬇️ 63,718 • ❤️ 333 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 767 • 💬 5 • ⭐ 9,927 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 107 • 💬 2 • ⭐ 10,988 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 127 • 💬 6 • ⭐ 102,203 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 48 • 💬 2 • ⭐ 19,617 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation](https://huggingface.co/papers/2608.30935)**

*Shaoan Wang, Aocheng Luo, Fei Huang et al. (20 authors)*

🏢 Light Origins

LightNav-0 is a compact generalist navigation model that leverages a pretrained vision-language model’s spatial reasoning via unified pointing tokens and action tokenization to achieve state-of-the-art embodied navigation across diverse tasks and robots.

▲ 26 • 💬 2 • ⭐ 253 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2608.30935) • [💻 code](https://github.com/lightorigins/LightNav-0) • [🔗 project](https://www.lightorigins.com/en/blog/lightnav-0)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 39 • 💬 1 • ⭐ 28,761 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Revisiting Local Context for Long-Horizon Streaming 3D Reconstruction](https://huggingface.co/papers/2608.27529)**

*Jiarong Han, Jincheng Xiong, Yuzhou Liu et al. (9 authors)*

🏢 Alibaba AMAP CV Lab

ABot-Recon achieves stable long-horizon streaming 3D reconstruction by using only local temporal context and frame-independent predictions composed sequentially, reducing drift via a lightweight temporal refiner and composition-aware pose loss.

▲ 31 • 💬 4 • ⭐ 372 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.27529) • [💻 code](https://github.com/amap-cvlab/ABot-Recon) • [🔗 project](https://amap-cvlab.github.io/ABot-Recon-html/)

---

**[WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://huggingface.co/papers/2608.24053)**

*Junjie Zhou, Ke Mei, Lei Li et al. (6 authors)*

🏢 Tencent

WeMM-Embedding is a family of universal multimodal embedding models that align text, images, videos, and interleaved inputs in a shared space, achieving state-of-the-art retrieval and recommendation performance across public benchmarks and large-scale WeChat applications.

▲ 69 • 💬 2 • ⭐ 1,062 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2608.24053) • [💻 code](https://github.com/Tencent/WeMM-Embedding) • [🔗 project](https://github.com/Tencent/WeMM-Embedding)

---

**[Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning](https://huggingface.co/papers/2608.27549)**

*Hanyang Wang, Yimo Cai, Weiliang Chen et al. (17 authors)*

🏢 MirroS

Code-as-World represents physical environments as executable code to enable quantitative reasoning and scalable supervision for vision-language models.

▲ 46 • 💬 2 • ⭐ 367 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.27549) • [💻 code](https://github.com/mirros-lab/code-as-world) • [🔗 project](https://mirros-lab.github.io/code-as-world)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 85 • 💬 7 • ⭐ 85,892 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

A privacy-first app that strips AI watermarks from content you own.

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 20.0k • 🔱 2.3k • 2h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.8k • 🔱 471 • 17h ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.4k • 🔱 427 • 3h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.4k • 🔱 261 • 21d ago

---

**[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)**

FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools, with cost-aware routing across LLM providers.

`Python` `agent` `ai` `ai-agent` `ai-coding` `autonomous-agent`

⭐ 3.2k • 🔱 225 • 10d ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.2k • 🔱 396 • 5d ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 3.0k • 🔱 187 • 4d ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 2.5k • 🔱 330 • 6d ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.1k • 🔱 202 • 4d ago

---

**[SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI)**

WeChat AI - 自托管微信角色扮演对话服务

`TypeScript`

⭐ 1.9k • 🔱 1.3k • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*
