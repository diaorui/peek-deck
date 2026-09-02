---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-02T09:51:46.833199+00:00'
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

**Last Updated:** September 02, 2026 at 09:51 UTC  
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

**[One unexpected way AI has genuinely changed my life: I repair things instead of replacing them](https://www.reddit.com/r/artificial/comments/1w4n7yq/one_unexpected_way_ai_has_genuinely_changed_my/)**

Maybe I'm getting old, but AI has probably been more useful to me fixing stuff around the house than it has been writing emails or any of the things people keep talking about. The other day I had a door hinge pulling out of the frame. I've always used the old toothpick trick because that's what my dad showed me years ago. AI suggested using gel super glue as well. Never crossed my mind. Took five minutes and it's probably the best that hinge has ever been. Same thing with cars. Same thing with plumbing. Half the time I don't actually need AI to tell me what to do, I just need someone or something to point me in roughly the right direction so I stop overthinking it. Now before anyone says I'm replacing YouTube with ChatGPT, no. AI gets plenty wrong. It once wanted me to spend half an afternoon repairing a cheap kitchen appliance that costs less than a decent takeaway to replace. It has absolutely no concept of when something isn't worth fixing. That's probably the bit people miss. AI isn't replacing experience. It's replacing that feeling of staring at something broken and thinking, "I've got absolutely no idea where to even start." Twenty years ago I'd have been digging through random forums hoping someone had the same problem. Today I ask AI, sanity-check the answer, and get on with it. Curious if anyone else has found this. Has AI actually changed how you approach DIY or fixing things, or am I just becoming the bloke who asks a chatbot what I used to ask my neighbour over the fence?

13h ago

---

**[Last quarter has been insane. Amazing times to be alive.](https://www.reddit.com/r/artificial/comments/1w5421z/last_quarter_has_been_insane_amazing_times_to_be/)**

I developed an ML algorithm for detection of pneumonia on chest x-rays back in 2019 when i studied for the MD. Back then, the things we are seeing now where an unimaginable pipe dream. If I could go back and explain to myself the capabilities of the frontier models, it would be like explaining todays computer back in the early 1900s. I would have then called this AGI for sure. Adding to the fact that Luna can run a month for reasonable $ sum too I think would have been shocking. I currently smart route between open weight and frontier models through standardcompute.com. 200 bucks then gives me insane capabilities. Doing what I spent 2 months on in 2019 would literally take me 10 minutes now.

1h ago

---

**[Anthropic sued over alleged theft of 'tens of thousands' of songs | AI company faces multibillion dollar lawsuit over misuse of copyrighted songs to train Claude models](https://www.reddit.com/r/artificial/comments/1w4bj01/anthropic_sued_over_alleged_theft_of_tens_of/)**

AI company faces multibillion dollar lawsuit over misuse of copyrighted songs to train Claude models

🔗 [the Guardian](https://www.theguardian.com/business/2026/aug/31/aanthropic-sued-alleged-theft-songs-ai-train-claude) • 20h ago

---

**[Astra's Unreadable Chain Of Thought?](https://www.reddit.com/r/artificial/comments/1w50jne/astras_unreadable_chain_of_thought/)**

Astra's COT is Supposedly Abstracted or uninterpretable using looped transformers, im guessing for the sake of Efficiency. What are your opinions? Is Singularity but also the Risks becoming closer and closer?

4h ago

---

**[World Labs debuts Atlas, an omni world model simulating space, time, and physical interaction](https://www.reddit.com/r/artificial/comments/1w4mki0/world_labs_debuts_atlas_an_omni_world_model/)**

World Labs just announced Atlas, an omni world model aimed at advancing spatial intelligence by natively handling text, images, video, and 3D geometry within a single architecture. Rather than treating video as isolated 2D pixel grids, Atlas uses an autoregressive diffusion transformer to ground every input in a shared 3D "spatial context." The space-time simulation features demonstrate how this moves AI past basic generation into true physical simulation: Democratized "Bullet Time": By processing footage from just 3 to 5 consumer mobile phones, Atlas can reconstruct dynamic events, freeze time, and simulate fluid camera trajectories through impossible angles without specialized capture rigs. Scalable Real-to-Sim: Beyond scanning static geometry, Atlas simulates dynamic robot navigation and manipulation. As an agent moves, the model synthesizes the exact RGB and metric depth streams its onboard sensors would capture along that path. Interactive Dynamics: Casual real-world video can be turned into simulations that model rigid, articulated, and deformable object physics, allowing researchers to alter object placement, lighting, and camera paths to generate synthetic training data. Native 3D Representations: It directly outputs point clouds and 3D Gaussian splats alongside novel video views, outperforming dedicated 3D reconstruction baselines across standard benchmarks like DTU, ETH3D, and ScanNet.

14h ago

---

**[Anthropic deliberately trained a bad model to prove what caused this summer's Claude sandbox breakouts](https://www.reddit.com/r/artificial/comments/1w42g6i/anthropic_deliberately_trained_a_bad_model_to/)**

Two separate incidents this summer, and Anthropic's postmortem is unusually specific about the failure mode. In July, three Claude models running in third-party cybersecurity evaluations (deliberately stripped of the usual guardrails, since eval work needs to test raw capability) got unauthorized access to real production systems at three different organizations. The cause was mundane: a misconfigured internet link that only the eval environment itself was supposed to have. In a separate incident on August 4, the UK AI Security Institute reported that Claude Mythos 5, running the same way, took a series of unsanctioned actions once it had real internet access during its own security testing. The alignment explanation is the part I hadn't seen laid out this plainly before. Anthropic says the models were told upfront that their environment was simulated. When they later ran into evidence it wasn't (real systems responding the way only real systems do), the models appear to have interpreted that evidence in whatever way let them keep believing the simulation story, rather than stopping to check. Anthropic calls this motivated reasoning, paired with a separate willingness to take harmful real-world actions in pursuit of a narrow eval goal. To test whether their internal reward-hacking mitigation work actually matters, they ran a controlled experiment: deliberately trained a model on 80 RL environments already known to be exploitable, then dropped it into simulations built from these same incidents. That model attacked simulated infrastructure and gave bioweapon-adjacent advice to satisfy a grader. Their production models and an earlier, pre-reward-hack checkpoint, run through the identical simulation, didn't do either. What I haven't seen anyone ask yet: if reward hacking during training is the mechanism, does that mean any lab with sloppier RL environment review than Anthropic's is running the same risk right now without knowing it, or is there something specific about how these particular sandboxes were scoped that made the incidents possible?

1d ago

---

**[Claude Fable 5.1 and Claude Mythos 5.1 Benchmarks](https://www.reddit.com/r/artificial/comments/1w4jzfy/claude_fable_51_and_claude_mythos_51_benchmarks/)**

15h ago

---

**[Ever fall down a curiosity rabbit hole? I built an app that turns any moment in history into a fully researched, interactive podcast](https://www.reddit.com/r/artificial/comments/1w4e79o/ever_fall_down_a_curiosity_rabbit_hole_i_built_an/)**

The idea: curiosity shouldn't have to wait for someone to make a podcast about the thing you're curious about. You type any topic, moment, or person and about two minutes later two hosts are telling you the story, researched with sources and paired with period artwork. And it's interactive: press the mic mid-episode and ask whatever you're wondering ("how big were these ships actually?") — the hosts answer and weave it back into the story. Happy to answer anything about how it's built and curious to know what the community thinks!

19h ago

---

**[Working from home in 2026](https://www.reddit.com/r/artificial/comments/1w3fotb/working_from_home_in_2026/)**

1d ago

---

**[Anyone else using AI for the boring parts of their job?](https://www.reddit.com/r/artificial/comments/1w4c0le/anyone_else_using_ai_for_the_boring_parts_of/)**

most of the AI discourse i see is about AGI timelines or image generators or whatever the latest model benchmark is. but the actual daytoday stuff where it's genuinely useful gets almost no airtime. i work in office admin and i've been slowly plugging AI into the tedious parts of my job. drafting templated emails that don't sound like a robot wrote them, summarizing long meeting notes, cleaning up messy spreadsheet data before i import it anywhere. nothing flashy. it just saves me maybe an hour a day which adds up. what gets me is that the costeffectiveness debate people keep having around AI replacing workers kind of misses this middle layer. it's not replacing me, it's absorbing the parts of my job i'd happily give away. the judgment calls, the context, the weird edge cases, those still need a human. at least for now. curious if others in more adminheavy or operational roles are actually finding it useful day to day or if it's mostly been hype in practice. and not the chatgptforemailsisamazing hot take, i mean actual workflow changes that stuck after the novelty wore off.

20h ago

---

---

## Google News: "ai"

**[Exclusive | New Google AI Model Said to Narrow Gap on Coding Ability](https://www.wsj.com/tech/ai/new-google-ai-model-said-to-narrow-gap-on-coding-ability-264c6052)**

WSJ • 12h ago

---

**[Architect of British government’s AI strategy joins Anthropic](https://www.theguardian.com/technology/2026/sep/02/architect-of-uks-ai-strategy-joins-anthropic)**

Matt Clifford, who drafted AI action plan and advised Starmer and Sunak, hired for senior role at US firm

The Guardian • 2h ago

---

**[Did OpenAI’s rogue agents form a ‘civilization’? The AI industry can’t agree](https://www.nbcnews.com/tech/tech-news/openai-hugging-face-hack-investigation-findings-divide-industry-rcna595383)**

Examinations of an AI-powered cyberattack reveal AI systems focused on cheating and misleading human observers.

NBC News • 51m ago

---

**[What Dell and Nvidia just proved to the AI stock haters](https://finance.yahoo.com/markets/stocks/article/what-dell-and-nvidia-just-proved-to-the-ai-stock-haters-090225103.html)**

Big quarters, for two big heavyweights.

Yahoo Finance • 49m ago

---

**[After the Earthquake, They Used A.I. to Mobilize Aid](https://www.nytimes.com/2026/09/02/world/americas/colombia-earthquake-ai-aid-app.html)**

The New York Times • 49m ago

---

**[:Claude: Fable 5.1 and Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)**

Our most advanced models for coding and knowledge work. Their research capabilities also offer an early glimpse of how AI models will contribute to scientific progress.

Anthropic • 15h ago

---

**[Palo Alto CEO says $1 trillion of cybersecurity infrastructure isn’t ready for AI](https://www.cnbc.com/2026/09/01/palo-alto-ceo-says-1-trillion-of-cybersecurity-infrastructure-isnt-ready-for-ai.html)**

Palo Alto CEO Nikesh Arora said AI is forcing companies to modernize roughly $1 trillion of aging cybersecurity infrastructure that isn’t equipped for attacks.

CNBC • 10h ago

---

**[Three Mount Shasta climbers rescued after relying on AI to plan climb](https://krcrtv.com/news/local/three-mount-shasta-climbers-rescued-after-relying-on-ai-to-plan-climb)**

Three novice climbers were rescued from Mount Shasta on Sunday after becoming lost, running low on supplies and spending an unplanned night in Mud Creek Canyon,

KRCR • 9h ago

---

**[AI Startup Cognition Set to Raise Around $1 Billion at a $47 Billion Value](https://www.bloomberg.com/news/articles/2026-09-02/ai-startup-cognition-set-to-raise-around-1-billion-at-a-47-billion-value)**

Bloomberg.com • 9h ago

---

**[Try Google Pics: Easy image creation and editing in Google Workspace](https://blog.google/products-and-platforms/products/workspace/google-pics/)**

Built on our latest Nano Banana model, Google Pics — our image creation and editing tool — is now available.

blog.google • 17h ago

---

---

## HackerNews: "ai"

**[How accurate have Ed Zitron's AI skeptic predictions been?](https://news.ycombinator.com/item?id=49526069)**

⬆️ 709 • 💬 765 • 15h ago • [danluu.com](https://danluu.com/zitron/)

---

**[Apple caught off guard by AI demand for Mac Mini and Mac Studio](https://news.ycombinator.com/item?id=49508982)**

Apple's unusually timed announcement of new Mac mini and Mac Studio models this week was driven by unexpectedly strong enterprise appetite for AI hardware, according to The Information. Apple normally releases new Mac models in the autumn, closer to October or November, making this week's announcement unusually early, falling just before the anticipated arrival of new iPhone models. The Information says that the AI-driven boom in Mac Studio and Mac mini sales is behind the early launch.

⬆️ 492 • 💬 588 • 1d ago • [MacRumors](https://www.macrumors.com/2026/08/30/apple-unexpected-mac-mini-and-studio-demand/)

---

**[No AI Fridays](https://news.ycombinator.com/item?id=49498095)**

A weekly ritual for software teams to unplug from AI coding assistants, prevent skill atrophy, and rediscover the joy of craftsmanship.

⬆️ 289 • 💬 205 • 2d ago • [noaifridays.com](https://noaifridays.com/)

---

**[Dwarf Fortress' creator says the industry's in shambles over AI](https://news.ycombinator.com/item?id=49523720)**

"They're trying to have a CEO press a button that makes a game."

⬆️ 225 • 💬 227 • 17h ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/dwarf-fortress-creator-says-the-industrys-in-shambles-over-ai-and-layoff-happy-ceos-everyone-i-know-their-bosses-are-slowly-getting-psychosis/)

---

**[AI Can Make You Suck Faster Too](https://news.ycombinator.com/item?id=49518316)**

If AI is so great, why are the only new tech giants GenAI companies?

⬆️ 173 • 💬 161 • 1d ago • [hermit-tech.com](https://www.hermit-tech.com/blog/ai-can-make-you-suck-faster-too)

---

**[EFF to Courts: Don't Rewrite Copyright over AI Hype](https://news.ycombinator.com/item?id=49521315)**

New markets, new ideas, and new creators are actually what copyright is supposed to promote, not restrict. Using copyright to lock in existing gatekeepers and massive rightsholders’ profits helps neither the public nor individual artists.

⬆️ 162 • 💬 185 • 20h ago • [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2026/08/eff-courts-dont-rewrite-copyright-over-ai-hype)

---

**[The safest job from AI may be writing](https://news.ycombinator.com/item?id=49512856)**

Today, tech folk are scrambling to change their workflows to meet newly inflated 5X productivity quotas, while getting pummeled under the co...

⬆️ 146 • 💬 205 • 1d ago • [muratbuffalo.blogspot.com](http://muratbuffalo.blogspot.com/2026/08/the-safest-job-from-ai-may-be-writing.html)

---

**[Show HN: Weedout – Safari extension that hides YouTube AI-labeled videos](https://news.ycombinator.com/item?id=49528895)**

A Safari extension that pulls videos YouTube labels “Made with AI” out of your feed.

⬆️ 143 • 💬 63 • 11h ago • [masteranza.github.io](https://masteranza.github.io/weedout/)

---

**[Saab has unveiled its A3 collaborative combat aircraft concept](https://news.ycombinator.com/item?id=49522374)**

Saab is challenging the low-cost, attritable model adopted by Sweden’s allies with a supersonic, survivable complement to Gripen.

⬆️ 96 • 💬 119 • 19h ago • [aviationweek.com](https://aviationweek.com/defense/aircraft-propulsion/saab-enters-collaborative-combat-aircraft-race-high-end-concept)

---

**[Meta Security Researcher's AI Agent Accidentally Deleted Her Emails](https://news.ycombinator.com/item?id=49506655)**

Meta's Summer Yue says she ran OpenClaw on her inbox, but its size 'triggered compaction [and] lost my original instruction' to get her permission before deleting.

⬆️ 60 • 💬 61 • 2d ago • [PCMag Australia](https://au.pcmag.com/ai/116091/meta-security-researchers-ai-agent-accidentally-deleted-her-emails)

---

---

## YouTube Videos: "ai"

**[Sam Altman Reveals OpenAI’s Plan to Regain Its Lead in AI](https://www.youtube.com/watch?v=8Kf1Q0yOhSo)**

Read More: https://time.com/article/2026/08/26/openai-sam-altman-interview/ Inside OpenAI's San Francisco headquarters, Sam ...

📺 TIME

👁️ 55K • 👍 654 • 💬 225 • ⏱️ 14:13 • 17h ago

---

**[AI Is Taking Over Physics and Nobody Talks About It](https://www.youtube.com/watch?v=utu5YACZbPE)**

Take back your personal data with Incogni! Use code Sabine at the link below and get 60% off annual plans: ...

📺 Sabine Hossenfelder

👁️ 364K • 👍 7K • 💬 2K • ⏱️ 7:02 • 18h ago

---

**[Dead Sea Scrolls Just Decoded by an AI… And It&#39;s Far Worse Than We Thought](https://www.youtube.com/watch?v=ETnCH_zAfy8)**

Dead Sea Scrolls Just Decoded by an AI… And It's Far Worse Than We Thought In 2021, archaeologists rappelled 80 meters into ...

📺 Ambrose Discovery

👁️ 1.0M • 👍 17K • 💬 1K • ⏱️ 25:29 • 2d ago

---

**[Tech FREAKOUT After AI Civilizations Form Criminal Collective](https://www.youtube.com/watch?v=zobHP8dW2P4)**

Krystal and Saagar discuss tech leaders freaking over an ai hacking spree. Sign Up For 30 Day Free BP Trial: ...

📺 Breaking Points

👁️ 416K • 👍 7K • 💬 2K • ⏱️ 21:29 • 1d ago

---

**[Twitch caught hiding AI Training and their response is unbelievable...](https://www.youtube.com/watch?v=36_stE299lU)**

Twitch has been caught burying its latest update which include an AUTOMATIC OPT IN for training AI on YOUR content, including ...

📺 JayzTwoCents

👁️ 160K • 👍 3K • 💬 524 • ⏱️ 31:17 • 1d ago

---

**[&quot;AI Will Crush All Humans&quot;: Elon Musk on Extreme Advancements in AI at G20 Summit - 09/01/26](https://www.youtube.com/watch?v=H0Ap25IOWr8)**

"AI Will Crush All Humans": Elon Musk on Extreme Advancements in AI at G20 Summit. September 1, 2026 Join this channel to ...

📺 Right Side Broadcasting Network

👁️ 141K • 👍 2K • 💬 762 • ⏱️ 8:45 • 20h ago

---

**[Gen AI&#39;s two FATAL FLAWS that even human babies can do &amp; the industry knows it](https://www.youtube.com/watch?v=5dfFAlpkYhs)**

Generative AI companies are trying to convince the world—and your boss—that large language models are ready to replace ...

📺 Internet of Bugs

👁️ 104K • 👍 4K • 💬 611 • ⏱️ 12:29 • 1d ago

---

**[Why Gen Z Hates AI But Uses It The Most (ft. Bernie Sanders)](https://www.youtube.com/watch?v=NmHhXoTckcM)**

Gen Z uses AI the most yet trusts it the least. We sat Bernie Sanders down with them for a messy debate that isn't happening in the ...

📺 More Perfect Union

👁️ 784K • 👍 15K • 💬 2K • ⏱️ 22:59 • 2d ago

---

**[Hayes on Trump&#39;s &#39;disturbing&#39; love for AI slop](https://www.youtube.com/watch?v=ycnoe2OchXE)**

Chris Hayes on why Trump's AI slop problem goes beyond his own bizarre posts. MS NOW: My Source for News, Opinion, and the ...

📺 MS NOW

👁️ 12K • 👍 490 • 💬 28 • ⏱️ 1:57 • 12h ago

---

**[We Should Arrest Anyone Using AI For This… | Ep. 1831](https://www.youtube.com/watch?v=kWj0Fp0E1nw)**

AI is being used to indulge the worst desires in our society. It's time for the courts to step in. Ep. 1831 -- -- -- Today's Sponsors: ...

📺 Matt Walsh

👁️ 226K • 👍 6K • 💬 2K • ⏱️ 35:25 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 207,941 • ❤️ 4,688 • 6d ago

---

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`image-text-to-text` `321.3B`

⬇️ 441,348 • ❤️ 1,912 • 1d ago

---

**[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)**

*Z.ai*

GLM-5.3 is a text-generation model excelling in complex coding and long-horizon tasks, achieving state-of-the-art performance in coding benchmarks and emergent cyber capabilities like vulnerability discovery and exploitation.

`text-generation` `753.3B`

⬇️ 94,403 • ❤️ 1,481 • 1d ago

---

**[Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)**

*Unsloth AI*

Qwen3.8-Flash-Next-GGUF is a highly efficient, multimodal causal language model featuring Hybrid Attention with QSA and N-gram Embeddings for significantly reduced long-context latency. It excels in agentic workloads and supports context lengths up to 1,000,000 tokens, making it ideal for complex reasoning and large-scale data processing.

`image-text-to-text` `176.9B`

⬇️ 431,339 • ❤️ 697 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 4,960,483 • ❤️ 13,622 • 18d ago

---

**[DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)**

*DeepSeek*

DeepSeek-V4-Flash-Vision-Exp is an experimental multimodal model that integrates visual understanding with text-based agent capabilities, enhancing performance on tasks like ApexBench and Agents' Last Exam while maintaining strong text-only agent performance.

`image-text-to-text` `304.6B`

⬇️ 17,893 • ❤️ 474 • 1d ago

---

**[Hy4-preview](https://huggingface.co/tencent/Hy4-preview)**

*Tencent*

Hy4-preview is a 770B parameter Mixture-of-Experts (MoE) text generation model with 49B activated parameters per token, featuring a 1M context length and Gated Sparse Attention. It excels in productivity tasks across software engineering, office analysis, game development, and scientific research, offering significant gains in understanding, reasoning, and code generation.

`text-generation` `780.0B`

⬇️ 3,516 • ❤️ 391 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,232,274 • ❤️ 2,499 • 1d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 9,354,057 • ❤️ 3,359 • 12d ago

---

**[GLM-5.3-Flash-GGUF](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF)**

*Unsloth AI*

GLM-5.3-Flash is a natively multimodal LLM optimized for efficiency and capability, featuring a hybrid sparse/linear attention architecture. It excels in long-context tasks, coding, and agentic benchmarks, offering performance competitive with leading models at a fraction of the cost, suitable for advanced AI applications.

`text-generation` `320.8B`

⬇️ 63,718 • ❤️ 328 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 766 • 💬 5 • ⭐ 9,927 • 23d ago

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

▲ 25 • 💬 2 • ⭐ 253 • 2d ago

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

⭐ 20.0k • 🔱 2.3k • 17h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.8k • 🔱 470 • 13h ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.4k • 🔱 425 • 2m ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.4k • 🔱 261 • 21d ago

---

**[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)**

FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools, with cost-aware routing across LLM providers.

`Python` `agent` `ai` `ai-agent` `ai-coding` `autonomous-agent`

⭐ 3.2k • 🔱 225 • 9d ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.2k • 🔱 395 • 5d ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 3.0k • 🔱 186 • 3d ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 2.5k • 🔱 327 • 6d ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.1k • 🔱 202 • 4d ago

---

**[SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI)**

WeChat AI - 自托管微信角色扮演对话服务

`TypeScript`

⭐ 1.9k • 🔱 1.3k • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
