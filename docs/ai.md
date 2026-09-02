---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-02T00:51:49.927070+00:00'
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

**Last Updated:** September 02, 2026 at 00:51 UTC  
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

4h ago

---

**[Anthropic sued over alleged theft of 'tens of thousands' of songs | AI company faces multibillion dollar lawsuit over misuse of copyrighted songs to train Claude models](https://www.reddit.com/r/artificial/comments/1w4bj01/anthropic_sued_over_alleged_theft_of_tens_of/)**

AI company faces multibillion dollar lawsuit over misuse of copyrighted songs to train Claude models

🔗 [the Guardian](https://www.theguardian.com/business/2026/aug/31/aanthropic-sued-alleged-theft-songs-ai-train-claude) • 11h ago

---

**[World Labs debuts Atlas, an omni world model simulating space, time, and physical interaction](https://www.reddit.com/r/artificial/comments/1w4mki0/world_labs_debuts_atlas_an_omni_world_model/)**

World Labs just announced Atlas, an omni world model aimed at advancing spatial intelligence by natively handling text, images, video, and 3D geometry within a single architecture. Rather than treating video as isolated 2D pixel grids, Atlas uses an autoregressive diffusion transformer to ground every input in a shared 3D "spatial context." The space-time simulation features demonstrate how this moves AI past basic generation into true physical simulation: Democratized "Bullet Time": By processing footage from just 3 to 5 consumer mobile phones, Atlas can reconstruct dynamic events, freeze time, and simulate fluid camera trajectories through impossible angles without specialized capture rigs. Scalable Real-to-Sim: Beyond scanning static geometry, Atlas simulates dynamic robot navigation and manipulation. As an agent moves, the model synthesizes the exact RGB and metric depth streams its onboard sensors would capture along that path. Interactive Dynamics: Casual real-world video can be turned into simulations that model rigid, articulated, and deformable object physics, allowing researchers to alter object placement, lighting, and camera paths to generate synthetic training data. Native 3D Representations: It directly outputs point clouds and 3D Gaussian splats alongside novel video views, outperforming dedicated 3D reconstruction baselines across standard benchmarks like DTU, ETH3D, and ScanNet.

5h ago

---

**[Anthropic deliberately trained a bad model to prove what caused this summer's Claude sandbox breakouts](https://www.reddit.com/r/artificial/comments/1w42g6i/anthropic_deliberately_trained_a_bad_model_to/)**

Two separate incidents this summer, and Anthropic's postmortem is unusually specific about the failure mode. In July, three Claude models running in third-party cybersecurity evaluations (deliberately stripped of the usual guardrails, since eval work needs to test raw capability) got unauthorized access to real production systems at three different organizations. The cause was mundane: a misconfigured internet link that only the eval environment itself was supposed to have. In a separate incident on August 4, the UK AI Security Institute reported that Claude Mythos 5, running the same way, took a series of unsanctioned actions once it had real internet access during its own security testing. The alignment explanation is the part I hadn't seen laid out this plainly before. Anthropic says the models were told upfront that their environment was simulated. When they later ran into evidence it wasn't (real systems responding the way only real systems do), the models appear to have interpreted that evidence in whatever way let them keep believing the simulation story, rather than stopping to check. Anthropic calls this motivated reasoning, paired with a separate willingness to take harmful real-world actions in pursuit of a narrow eval goal. To test whether their internal reward-hacking mitigation work actually matters, they ran a controlled experiment: deliberately trained a model on 80 RL environments already known to be exploitable, then dropped it into simulations built from these same incidents. That model attacked simulated infrastructure and gave bioweapon-adjacent advice to satisfy a grader. Their production models and an earlier, pre-reward-hack checkpoint, run through the identical simulation, didn't do either. What I haven't seen anyone ask yet: if reward hacking during training is the mechanism, does that mean any lab with sloppier RL environment review than Anthropic's is running the same risk right now without knowing it, or is there something specific about how these particular sandboxes were scoped that made the incidents possible?

19h ago

---

**[Ever fall down a curiosity rabbit hole? I built an app that turns any moment in history into a fully researched, interactive podcast](https://www.reddit.com/r/artificial/comments/1w4e79o/ever_fall_down_a_curiosity_rabbit_hole_i_built_an/)**

The idea: curiosity shouldn't have to wait for someone to make a podcast about the thing you're curious about. You type any topic, moment, or person and about two minutes later two hosts are telling you the story, researched with sources and paired with period artwork. And it's interactive: press the mic mid-episode and ask whatever you're wondering ("how big were these ships actually?") — the hosts answer and weave it back into the story. Happy to answer anything about how it's built and curious to know what the community thinks!

10h ago

---

**[Working from home in 2026](https://www.reddit.com/r/artificial/comments/1w3fotb/working_from_home_in_2026/)**

1d ago

---

**[Claude Fable 5.1 and Claude Mythos 5.1 Benchmarks](https://www.reddit.com/r/artificial/comments/1w4jzfy/claude_fable_51_and_claude_mythos_51_benchmarks/)**

6h ago

---

**[Let me ask you something?](https://www.reddit.com/r/artificial/comments/1w4purl/let_me_ask_you_something/)**

3h ago

---

**[CrowdStrike launches SafeMind with offensive and defensive AI models](https://www.reddit.com/r/artificial/comments/1w4n9tb/crowdstrike_launches_safemind_with_offensive_and/)**

CrowdStrike says it has launched SafeMind, a security-focused AI system with two models: Red Tempest looks for attack paths, while Blue Solano works to close them. The company says the system runs in the Falcon platform and was built with NVIDIA Nemotron. The models use Falcon telemetry, threat intelligence, and 15 years of incident-response data, according to CrowdStrike. CSO reports that SafeMind also creates a digital twin of an enterprise environment so the red-team model can test attack paths and the blue-team model can respond. CrowdStrike reports a 29% higher detection rate, 6x faster end-to-end remediation, and 99% cost savings on detection and remediation compared with leading frontier models and open-source baselines. Those are vendor-reported results. The practical test is whether independent production evidence shows the same gains without adding false positives or unsafe automated actions. Sources: CrowdStrike: https://www.crowdstrike.com/en-us/press-releases/crowdstrike-launches-frontier-models-for-cybersecurity-with-nvidia/ CSO: https://www.csoonline.com/article/4217135/crowdstrike-launches-cyber-frontier-ai-models-agentic-security-system/

4h ago

---

**[Can an AI agent safely undo changes it makes to itself?](https://www.reddit.com/r/artificial/comments/1w4mhu1/can_an_ai_agent_safely_undo_changes_it_makes_to/)**

As AI agents become more autonomous, they are increasingly able to modify their own prompts, tools, middleware, routing, resources, and execution harnesses. That raises a question we studied in our recent work: What happens when a self-modification improves capability but cannot be safely reversed later? We introduce EvoUndo, a framework that treats recoverability as an explicit constraint on self-evolving agents. Across 600 unseen self-evolution tasks, we identified 197 capability-improving mutations that failed recoverability verification. Under the original recovery representation, conventional repair recovered 0/197. Our experiments suggest that two important bottlenecks are state grounding and recovery-language expressivity. The broader idea is that persistent self-modifications should not be judged only by whether they improve performance. They should also be tested for whether the previous state can be safely recovered across counterfactual states. I’m one of the authors of the paper. Paper: https://arxiv.org/abs/2608.28363

5h ago

---

---

## Google News: "ai"

**[Exclusive | New Google AI Model Said to Narrow Gap on Coding Ability](https://www.wsj.com/tech/ai/new-google-ai-model-said-to-narrow-gap-on-coding-ability-264c6052)**

WSJ • 3h ago

---

**['It can outthink me': How a major manufacturer came to embrace AI](https://www.npr.org/2026/09/01/nx-s1-5869801/ai-manufacturing-jobs-data-factory)**

GE Appliances is leaning heavily into artificial intelligence to improve quality and efficiency on the factory floor.

NPR • 15h ago

---

**[A Technological Reckoning With No Great Answers](https://www.theatlantic.com/technology/2026/09/ai-future-reckoning-singularity/688487/)**

Whatever the AI future is, we’re in it right now.

The Atlantic • 35m ago

---

**[AI Startup Cognition Set to Raise Around $1 Billion at a $47 Billion Value](https://www.bloomberg.com/news/articles/2026-09-02/ai-startup-cognition-set-to-raise-around-1-billion-at-a-47-billion-value)**

Bloomberg.com • 22m ago

---

**[Sam Altman says fears that AI data centers guzzle water are overblown — but hard to dispel](https://www.businessinsider.com/sam-altman-ai-data-center-water-overblown-hard-to-dispel-2026-9)**

Sam Altman says concerns about AI's water use are overblown, comparing ChatGPT's water use to that of growing almonds in California.

Business Insider • 31m ago

---

**[AI’s not taking all the jobs. Just ask your local hobby shop, garage band and crafts store](https://www.cnn.com/2026/09/01/economy/people-just-want-things-that-bring-them-joy)**

Young people are embracing “grandma hobbies” and flocking to in-person events at a time when artificial intelligence encroaches on many aspects of life.

CNN • 15h ago

---

**[Side of slop? Bizarre AI food images jump from online to IRL menus](https://www.nbcnews.com/tech/tech-news/side-slop-bizarre-ai-food-images-jump-online-irl-menus-rcna594786)**

The confluence of lingering cost pressures and advancing technology appears to be translating into a boom in smaller businesses’ deploying AI-designed graphics and logos.

NBC News • 6h ago

---

**[Dell again lifts annual forecasts as AI demand powers record results](https://www.reuters.com/business/dell-again-lifts-forecasts-ai-demand-powers-record-results-2026-09-01/)**

Reuters • 1h ago

---

**[Dell surges 9% after lifting fiscal 2027 forecast on AI server strength](https://www.cnbc.com/2026/09/01/dell-q2-earnings-report-2027.html)**

Dell sees AI server revenue tripling in fiscal 2027. Six months ago, it was looking for the number to double.

CNBC • 4h ago

---

**[Dell Reports Record Results: AI Momentum Remains Robust](https://finance.yahoo.com/technology/ai/articles/dell-reports-record-results-ai-222500369.html)**

Dell once again reported robust results in its Q2 release, continuing a string of positive beats that we've seen over recent quarters. Importantly, AI-related demand remains red hot, underpinned by a strong backlog and other record-breaking figures.

Yahoo Finance • 2h ago

---

---

## HackerNews: "ai"

**[Apple caught off guard by AI demand for Mac Mini and Mac Studio](https://news.ycombinator.com/item?id=49508982)**

Apple's unusually timed announcement of new Mac mini and Mac Studio models this week was driven by unexpectedly strong enterprise appetite for AI hardware, according to The Information. Apple normally releases new Mac models in the autumn, closer to October or November, making this week's announcement unusually early, falling just before the anticipated arrival of new iPhone models. The Information says that the AI-driven boom in Mac Studio and Mac mini sales is behind the early launch.

⬆️ 491 • 💬 582 • 1d ago • [MacRumors](https://www.macrumors.com/2026/08/30/apple-unexpected-mac-mini-and-studio-demand/)

---

**[How accurate have Ed Zitron's AI skeptic predictions been?](https://news.ycombinator.com/item?id=49526069)**

⬆️ 377 • 💬 456 • 6h ago • [danluu.com](https://danluu.com/zitron/)

---

**[No AI Fridays](https://news.ycombinator.com/item?id=49498095)**

A weekly ritual for software teams to unplug from AI coding assistants, prevent skill atrophy, and rediscover the joy of craftsmanship.

⬆️ 289 • 💬 205 • 2d ago • [noaifridays.com](https://noaifridays.com/)

---

**[Smartphone LED detects hidden cameras with AI](https://news.ycombinator.com/item?id=49496292)**

Smartphone LED and AI Detect Hidden Cameras KAISTs SweepLED achieves 94% accuracy with 10,000 won LED device

⬆️ 270 • 💬 80 • 2d ago • [The Chosun Daily](https://www.chosun.com/english/industry-en/2026/08/30/SBFXUIJQYZEARKP5T4FBAY25HQ/)

---

**[Dwarf Fortress' creator says the industry's in shambles over AI](https://news.ycombinator.com/item?id=49523720)**

"They're trying to have a CEO press a button that makes a game."

⬆️ 195 • 💬 195 • 8h ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/dwarf-fortress-creator-says-the-industrys-in-shambles-over-ai-and-layoff-happy-ceos-everyone-i-know-their-bosses-are-slowly-getting-psychosis/)

---

**[EFF to Courts: Don't Rewrite Copyright over AI Hype](https://news.ycombinator.com/item?id=49521315)**

New markets, new ideas, and new creators are actually what copyright is supposed to promote, not restrict. Using copyright to lock in existing gatekeepers and massive rightsholders’ profits helps neither the public nor individual artists.

⬆️ 161 • 💬 179 • 11h ago • [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2026/08/eff-courts-dont-rewrite-copyright-over-ai-hype)

---

**[The safest job from AI may be writing](https://news.ycombinator.com/item?id=49512856)**

Today, tech folk are scrambling to change their workflows to meet newly inflated 5X productivity quotas, while getting pummeled under the co...

⬆️ 146 • 💬 203 • 1d ago • [muratbuffalo.blogspot.com](http://muratbuffalo.blogspot.com/2026/08/the-safest-job-from-ai-may-be-writing.html)

---

**[AI Can Make You Suck Faster Too](https://news.ycombinator.com/item?id=49518316)**

If AI is so great, why are the only new tech giants GenAI companies?

⬆️ 143 • 💬 145 • 19h ago • [hermit-tech.com](https://www.hermit-tech.com/blog/ai-can-make-you-suck-faster-too)

---

**[Saab has unveiled its A3 collaborative combat aircraft concept](https://news.ycombinator.com/item?id=49522374)**

Saab is challenging the low-cost, attritable model adopted by Sweden’s allies with a supersonic, survivable complement to Gripen.

⬆️ 89 • 💬 112 • 10h ago • [aviationweek.com](https://aviationweek.com/defense/aircraft-propulsion/saab-enters-collaborative-combat-aircraft-race-high-end-concept)

---

**[Fair Work Commission condemns 'plain wrong' AI legal advice](https://news.ycombinator.com/item?id=49497357)**

The Fair Work Commission will soon require applicants to disclose any AI use with consequences for failing to be transparent.

⬆️ 60 • 💬 31 • 2d ago • [abc.net.au](https://www.abc.net.au/news/2026-08-29/fair-work-commission-condemns-ai-legal-advice/107089766)

---

---

## YouTube Videos: "ai"

**[Sam Altman Reveals OpenAI’s Plan to Regain Its Lead in AI](https://www.youtube.com/watch?v=8Kf1Q0yOhSo)**

Read More: https://time.com/article/2026/08/26/openai-sam-altman-interview/ Inside OpenAI's San Francisco headquarters, Sam ...

📺 TIME

👁️ 31K • 👍 440 • 💬 173 • ⏱️ 14:13 • 8h ago

---

**[How I Make Ultra Realistic AI Videos using Seedance 2.5](https://www.youtube.com/watch?v=Zo8KaTs0l6k)**

Use Seedance 2.5 To Make Ultra Realistic AI Videos Try Seedance 2.5 https://higgsfield.ai?fpr=dankieft&fp_sid=ultra In this ...

📺 Dan Kieft

👁️ 34K • 💬 19 • ⏱️ 22:43 • 9h ago

---

**[Sam Altman was wrong about AI | Eli the Computer Guy](https://www.youtube.com/watch?v=--r6aWpwwH8)**

Sam Altman has backed himself into a corner.” Eli the Computer Guy joins The Tech Report's Isaac Pound to talk about how ...

📺 The Tech Report

👁️ 278K • 👍 3K • 💬 789 • ⏱️ 27:57 • 1d ago

---

**[We Should Arrest Anyone Using AI For This… | Ep. 1831](https://www.youtube.com/watch?v=kWj0Fp0E1nw)**

AI is being used to indulge the worst desires in our society. It's time for the courts to step in. Ep. 1831 -- -- -- Today's Sponsors: ...

📺 Matt Walsh

👁️ 220K • 👍 6K • 💬 1K • ⏱️ 35:25 • 1d ago

---

**[Hayes on Trump&#39;s &#39;disturbing&#39; love for AI slop](https://www.youtube.com/watch?v=ycnoe2OchXE)**

Chris Hayes on why Trump's AI slop problem goes beyond his own bizarre posts. MS NOW: My Source for News, Opinion, and the ...

📺 MS NOW

👁️ 6K • 👍 273 • 💬 18 • ⏱️ 1:57 • 4h ago

---

**[AI Has Ruined the Internet](https://www.youtube.com/watch?v=JvTJTTUK8cg)**

Get 20% off DeleteMe by going to https://joindeleteme.com/adam and use code adam to protect your privacy! -- Does the internet ...

📺 Adam Conover

👁️ 370K • 👍 12K • 💬 2K • ⏱️ 17:29 • 1d ago

---

**[Tech FREAKOUT After AI Civilizations Form Criminal Collective](https://www.youtube.com/watch?v=zobHP8dW2P4)**

Krystal and Saagar discuss tech leaders freaking over an ai hacking spree. Sign Up For 30 Day Free BP Trial: ...

📺 Breaking Points

👁️ 401K • 👍 6K • 💬 2K • ⏱️ 21:29 • 1d ago

---

**[China&#39;s New AI Synthetic Human Robots Shocked The World](https://www.youtube.com/watch?v=QmODsWsyps8)**

China is selling a robot built to look like someone who died. UBTech's UWORLD U1 launched in Shenzhen with silicone skin, ...

📺 MACHINEKIND

👁️ 8K • 👍 79 • 💬 9 • ⏱️ 13:05 • 2d ago

---

**[Dyson announces $500 AI toothbrush with tooth selfie camera for people who wont floss](https://www.youtube.com/watch?v=N6r9uuslqoI)**

Dyson has announced a $500 AI-powered electric toothbrush that uses cameras and machine learning to blast away plaque.

📺 KTLA 5

👁️ 622 • 👍 7 • 💬 5 • ⏱️ 1:54 • 2h ago

---

**[Canada Is Hiding A MASSIVE AI Data Center Problem, And No One Is Prepared](https://www.youtube.com/watch?v=fywlR9yTWGQ)**

A strange alliance is forming as conservative media figures in both the U.S. and Canada are now publicly supporting the mass ...

📺 Redacted

👁️ 116K • 👍 3K • 💬 466 • ⏱️ 38:41 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 207,941 • ❤️ 4,638 • 5d ago

---

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`image-text-to-text` `321.3B`

⬇️ 441,348 • ❤️ 1,879 • 1d ago

---

**[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)**

*Z.ai*

GLM-5.3 is a text-generation model excelling in complex coding and long-horizon tasks, achieving state-of-the-art performance in coding benchmarks and emergent cyber capabilities like vulnerability discovery and exploitation.

`text-generation` `753.3B`

⬇️ 94,403 • ❤️ 1,466 • 1d ago

---

**[Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)**

*Unsloth AI*

Qwen3.8-Flash-Next-GGUF is a highly efficient, multimodal causal language model featuring Hybrid Attention with QSA and N-gram Embeddings for significantly reduced long-context latency. It excels in agentic workloads and supports context lengths up to 1,000,000 tokens, making it ideal for complex reasoning and large-scale data processing.

`image-text-to-text` `176.9B`

⬇️ 431,339 • ❤️ 669 • 15h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 4,960,483 • ❤️ 13,584 • 18d ago

---

**[DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)**

*DeepSeek*

DeepSeek-V4-Flash-Vision-Exp is an experimental multimodal model that integrates visual understanding with text-based agent capabilities, enhancing performance on tasks like ApexBench and Agents' Last Exam while maintaining strong text-only agent performance.

`image-text-to-text` `304.6B`

⬇️ 17,893 • ❤️ 449 • 15h ago

---

**[Hy4-preview](https://huggingface.co/tencent/Hy4-preview)**

*Tencent*

Hy4-preview is a 770B parameter Mixture-of-Experts (MoE) text generation model with 49B activated parameters per token, featuring a 1M context length and Gated Sparse Attention. It excels in productivity tasks across software engineering, office analysis, game development, and scientific research, offering significant gains in understanding, reasoning, and code generation.

`text-generation` `780.0B`

⬇️ 3,516 • ❤️ 384 • 4d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 9,354,057 • ❤️ 3,336 • 12d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,232,274 • ❤️ 2,462 • 18h ago

---

**[GLM-5.3-Flash-GGUF](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF)**

*Unsloth AI*

GLM-5.3-Flash is a natively multimodal LLM optimized for efficiency and capability, featuring a hybrid sparse/linear attention architecture. It excels in long-context tasks, coding, and agentic benchmarks, offering performance competitive with leading models at a fraction of the cost, suitable for advanced AI applications.

`text-generation` `320.8B`

⬇️ 63,718 • ❤️ 326 • 3d ago

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

▲ 48 • 💬 2 • ⭐ 19,527 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation](https://huggingface.co/papers/2608.30935)**

*Shaoan Wang, Aocheng Luo, Fei Huang et al. (20 authors)*

🏢 Light Origins

LightNav-0 is a compact generalist navigation model that leverages a pretrained vision-language model’s spatial reasoning via unified pointing tokens and action tokenization to achieve state-of-the-art embodied navigation across diverse tasks and robots.

▲ 24 • 💬 1 • ⭐ 253 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2608.30935) • [💻 code](https://github.com/lightorigins/LightNav-0) • [🔗 project](https://www.lightorigins.com/en/blog/lightnav-0)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 39 • 💬 1 • ⭐ 28,761 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://huggingface.co/papers/2608.24053)**

*Junjie Zhou, Ke Mei, Lei Li et al. (6 authors)*

🏢 Tencent

WeMM-Embedding is a family of universal multimodal embedding models that align text, images, videos, and interleaved inputs in a shared space, achieving state-of-the-art retrieval and recommendation performance across public benchmarks and large-scale WeChat applications.

▲ 69 • 💬 2 • ⭐ 1,053 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2608.24053) • [💻 code](https://github.com/Tencent/WeMM-Embedding) • [🔗 project](https://github.com/Tencent/WeMM-Embedding)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 205 • 💬 3 • ⭐ 1,355 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution](https://huggingface.co/papers/2608.31106)**

*Jiashu Zhu, Yanhao Zheng, Ruitian Tian et al. (10 authors)*

🏢 AMAP-ML

A compact 7B native joint audio-video generator uses cross-modal attention, progressive joint training, reinforcement learning with multimodal feedback, and an autoregressive 2K refinement pipeline to produce synchronized high-resolution outputs.

▲ 91 • 💬 5 • ⭐ 91 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2608.31106) • [💻 code](https://github.com/AMAP-ML/DreamX-Creator)

---

**[Revisiting Local Context for Long-Horizon Streaming 3D Reconstruction](https://huggingface.co/papers/2608.27529)**

*Jiarong Han, Jincheng Xiong, Yuzhou Liu et al. (9 authors)*

🏢 Alibaba AMAP CV Lab

ABot-Recon achieves stable long-horizon streaming 3D reconstruction by using only local temporal context and frame-independent predictions composed sequentially, reducing drift via a lightweight temporal refiner and composition-aware pose loss.

▲ 30 • 💬 4 • ⭐ 372 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.27529) • [💻 code](https://github.com/amap-cvlab/ABot-Recon) • [🔗 project](https://amap-cvlab.github.io/ABot-Recon-html/)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

A privacy-first app that strips AI watermarks from content you own.

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 19.9k • 🔱 2.3k • 8h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.8k • 🔱 460 • 4h ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.4k • 🔱 420 • 8h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.4k • 🔱 260 • 21d ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 3.2k • 🔱 368 • 4d ago

---

**[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)**

FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools, with cost-aware routing across LLM providers.

`Python` `agent` `ai` `ai-agent` `ai-coding` `autonomous-agent`

⭐ 3.2k • 🔱 225 • 9d ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.9k • 🔱 184 • 3d ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 2.5k • 🔱 323 • 6d ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.1k • 🔱 201 • 3d ago

---

**[SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI)**

WeChat AI - 自托管微信角色扮演对话服务

`TypeScript`

⭐ 1.9k • 🔱 1.3k • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*
