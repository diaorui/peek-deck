---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-29T10:52:08.143419+00:00'
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

**Last Updated:** August 29, 2026 at 10:52 UTC  
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

**[Did yall saw similar ADs?](https://www.reddit.com/r/artificial/comments/1w1agp2/did_yall_saw_similar_ads/)**

8h ago

---

**[I'm building an independent verification layer for Ai generated-claims and I'm lokking for researchers and partners to build with us.](https://www.reddit.com/r/artificial/comments/1w1gnii/im_building_an_independent_verification_layer_for/)**

I've been working on a deterministic verification engine for AI-generated financial claims. The original idea was fairly simple: An LLM should generate claims. It shouldn't be the authority that verifies them. But after building and testing the system, I realized the problem is much bigger than hallucination detection. The question I'm now working on is: Our architecture looks roughly like this: LLM ↓ Candidate claim ↓ Claim normalization ↓ Evidence ↓ Assumptions + Constraints ↓ Proof / Derivation ↓ Contradiction analysis ↓ Deterministic verification ↓ Auditable outcome ↓ Trust The important part is that the verification layer is independent of the model. For example, if an LLM says: we don't want the LLM's confidence score to determine whether that statement is trustworthy. Instead, the system should be able to determine: What exactly was claimed? What evidence is being used? Can the claim actually be derived? Which assumptions are involved? Are relevant constraints satisfied? Is there contradictory evidence? Can the result be reproduced? Can we explain the verification outcome? I recently ran a 66-case benchmark. Structured fixture claims: 66/66 passed. Then I ran the same pipeline with live GPT-5.1-generated claims: 19/66 passed end-to-end. The failures were: 31 pipeline execution failures 18 claim binding failures 2 contradiction detection failures Meanwhile, several deterministic verification components were still passing their tests, including evidence graph integrity, deterministic calculation, rule application, missing evidence detection, reproducibility, and auditability. The result changed how I'm thinking about the problem. The bottleneck isn't necessarily the deterministic verifier. There is a difficult translation layer between: Probabilistic language ↓ Formal representation ↓ Deterministic reasoning We're now rebuilding the benchmark so that instead of simply saying "this case failed," we can identify the first invalid state: Transport → Parsing → Schema validation → Normalization → Claim binding → Evidence graph → Verification → Outcome mapping That's where I think the interesting engineering/research problem is. We're also exploring a broader framework around claims, evidence, assumptions, constraints, proofs, contradictions, and trust. One idea we're particularly interested in is treating trust as an emergent output of the verification process, rather than simply using an LLM confidence score. This is still early research/product development. The benchmark is internal and isn't third-party validation, and the mathematical Trust model still needs empirical validation. I'm also actively looking for people to work with. We're looking for: Researchers interested in: formal verification trustworthy AI AI evaluation formal methods argumentation systems knowledge representation mathematical modeling Marketers / growth partners who can help us: communicate the problem clearly reach technical and business audiences find early adopters build a community develop the startup's go-to-market strategy Engineers and technical collaborators interested in building reliable AI systems. And particularly industry partners in finance, risk, audit, compliance, or other areas where incorrect AI claims have serious consequences. I'm interested in finding people who want to build with us, not just give feedback from the sidelines. If this problem interests you, DM me or comment below. I'd especially love to hear from researchers and marketers who think this is a problem worth tackling. We're still early — which is exactly why now is a good time to get involved.

2h ago

---

**[Anatomy of an Autonomous Attack: 5 Alarming A.I. Capabilities. When OpenAI’s agents went rogue in July, they demonstrated ingenuity and drive beyond what many experts imagined — a dangerous harbinger of what such bots could do in the future. (Gift Article)](https://www.reddit.com/r/artificial/comments/1w1auoq/anatomy_of_an_autonomous_attack_5_alarming_ai/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/08/24/science/openai-huggingface-alarming-capabilities.html?unlocked_article_code=1.9FA.x6G_._ao4KQIl-Vb-&smid=url-share) • 7h ago

---

**[Australia just banned fully AI-generated songs from its official charts. Is that fair?](https://www.reddit.com/r/artificial/comments/1w0lfz8/australia_just_banned_fully_aigenerated_songs/)**

AI-assisted music can still qualify, but tracks created entirely by AI are no longer eligible for Australia’s official charts. I understand the reasoning, but the line could get messy. Using AI for mastering is clearly different from typing one prompt and releasing the result—but there’s a huge gray area between those two. Should charts judge how a song was created, or only whether people genuinely want to listen to it? Source: https://www.reuters.com/legal/litigation/ai-generated-music-barred-australian-charts-after-madonna-cover-controversy-2026-08-26/

🔗 [reuters.com](https://www.reuters.com/legal/litigation/ai-generated-music-barred-australian-charts-after-madonna-cover-controversy-2026-08-26/) • 1d ago

---

**[AI for clinic workflow automation. what's actually working vs what's just hype right now](https://www.reddit.com/r/artificial/comments/1w1ix49/ai_for_clinic_workflow_automation_whats_actually/)**

Been running a small PT clinic and also writing dev tutorials on the side, so I sit in a weird middle ground where I understand the tooling but I'm also the one drowning in intake forms and scheduling conflicts at 7am. Tried building some lightweight automations this past year. LLMs for parsing referral notes, some basic RAG stuff to pull patient history context faster. It works. Not perfectly, but well enough to matter. What I keep running into is the gap between what AI demos promise and what actually holds up in a real workflow where you're shortstaffed and tired and just need the thing to not break. That post a few days ago about AI vs human labor costs hits different when you're a small operation. You're not replacing anyone. You're trying to stop being the bottleneck yourself. Curious what people here are actually deploying in small business or solo operator contexts. Not enterprise stuff. The scrappy builds. What broke, what stuck around, what you wish you'd done differently from the start.

27m ago

---

**[Making an agent check the same repo every morning feels backwards](https://www.reddit.com/r/artificial/comments/1w1iiax/making_an_agent_check_the_same_repo_every_morning/)**

Refreshing a package tracking page every 20 minutes would be ridiculous. You check when something actually changes. I think long running dev agents should work the same way. Say an agent is stuck on some annoying dependency bug. The obvious approach is to have it check the repo every morning. Monday: Nothing Tuesday: Nothing Wednesday: Nothing Then another agent discovers a workaround in a fork you didn’t even know existed. If that gets broadcast through EigenFlux and reaches the agent that's stuck thats genuinely useful. You couldn't have monitored that fork yourself because you didnt even know it was there. I still wouldn't let a single incoming signal trigger an upgrade automatically. The agent should verify the source, version, changelog, compatibility, etc before doing anything. Butbfor the question of "did anything useful show up somewhere i wasn't watching?", this feels much closer to what an always on agent should actually be doing. Anyone already running persistent agent's this way, or is it mostly still cron + RSS + alerts?

50m ago

---

**[Bill Gates Warns Rise Of AI Will Be One Of The 'Most Turbulent Times In Human History' In Alarming New Essay](https://www.reddit.com/r/artificial/comments/1w05qir/bill_gates_warns_rise_of_ai_will_be_one_of_the/)**

What do you think, folks?

🔗 [Comic Sands](http://comicsands.com/gates-warning-ai-turbulent-times) • 1d ago

---

**[The Job Market Is Hell. Young people are using ChatGPT to write their applications; HR is using AI to read them; no one is getting hired.](https://www.reddit.com/r/artificial/comments/1w0j50w/the_job_market_is_hell_young_people_are_using/)**

Young people are using ChatGPT to write their applications; HR is using AI to read them; no one is getting hired.

🔗 [The Atlantic](https://www.theatlantic.com/ideas/archive/2025/09/job-market-hell/684133/) • 1d ago

---

**[When are we gonna stop having to correct ai? speech to text still dumb sometimes.](https://www.reddit.com/r/artificial/comments/1w1h296/when_are_we_gonna_stop_having_to_correct_ai/)**

I was doing speech to text on my phone, saying something like- (paraphrase) "my opinion of abc is this. my opinion of xyz is that. Can you tell which way i lean?" the ai didn't understand the context or something, and typed out..... "Can you tell which way Eileen?" and then i had to manually correct the words.

2h ago

---

**[Opus 5 Instruction Following is Genuinely Concerning](https://www.reddit.com/r/artificial/comments/1w0w5p6/opus_5_instruction_following_is_genuinely/)**

I think that Anthropic has dropped the ball, instruction following is actually non-existent. You tell it to not do something, ignores you and does it anyway. I’ve said at least ten times to no open something, it keeps doing it. Absolutely unbelievable. This is a dangerous model.

17h ago

---

---

## Google News: "ai"

**[Sharp rise in incidents of AI escaping users’ control, research finds](https://www.theguardian.com/technology/2026/aug/29/sharp-rise-in-incidents-of-ai-escaping-users-control-research-finds)**

Exclusive: Number of times AI lies, ignores instructions and pursues goals in harmful ways almost doubles in July

The Guardian • 4h ago

---

**[OpenAI to cut off AI models for SpaceX-owned Cursor, escalating feud with Musk](https://www.reuters.com/business/media-telecom/openai-end-partnership-with-spacexs-cursor-2026-08-29/)**

Reuters • 8h ago

---

**[Editorial cartoon: Meta settlement vs. AI](https://www.dallasnews.com/opinion/commentary/article/meta-settlement-17-billion-artificial-intelligence-22407883.php)**

Dallas News • 24m ago

---

**[Appeals court delivers unsettling ruling — and says Supreme Court left it no choice](https://www.foxnews.com/politics/appeals-court-delivers-unsettling-ruling-supreme-court-left-no-choice)**

A federal appeals court says Supreme Court precedent forced it to protect possession of AI-generated child sexual abuse material, raising urgent questions.

Fox News • 51m ago

---

**[ChatGPT said you’d lose your jobs right now — it’s more like 3% of workers](http://fortune.com/2026/08/29/ai-workers-survey-job-impact-2026/)**

The nationally representative poll of 1,250 employed adults also found 6% landed AI-created roles and 9% got AI-linked promotions between 2023 and 2026.

Fortune • 52m ago

---

**[The Fed confronts a powerful new economic force](https://www.washingtonpost.com/technology/2026/08/29/federal-reserve-officials-are-debating-ais-effect-economy-jobs/)**

In meetings on how to steer the nation’s financial path, central bank officials regularly debate the effect of artificial intelligence on the economy, a Post analysis found.

The Washington Post • 19m ago

---

**[Our decision on Cursor following its acquisition by SpaceX](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/)**

Our decision to wind down our contract providing OpenAI models to Cursor following its acquisition by SpaceX.

OpenAI • 9h ago

---

**[As A.I. Money Floods the Market, San Francisco Renters Weigh Buyouts](https://www.nytimes.com/2026/08/28/realestate/as-ai-money-floods-the-market-san-francisco-renters-weigh-buyouts.html)**

The New York Times • 1d ago

---

**[One of the world's hottest industries is sparking a blue-collar jobs boom](https://www.foxnews.com/politics/worlds-hottest-industries-sparking-blue-collar-jobs-boom)**

AI infrastructure spending is projected to drive U.S. industrial construction to $684 billion by 2031, creating massive demand for skilled trades workers.

Fox News • 1d ago

---

**[China is secretly fueling America's data center rage](https://www.axios.com/2026/08/28/china-ai-data-center-backlash-bots)**

Axios • 16h ago

---

---

## HackerNews: "ai"

**[CEO fired developers to make room for AI. Developers create open source AI CEO](https://news.ycombinator.com/item?id=49458418)**

AI-powered virtual executive team — a single coherent executive persona backed by 8 specialist Claude agents (FastAPI + Next.js). - SenteLabsAI/OpenExecutive

⬆️ 1010 • 💬 705 • 2d ago • [GitHub](https://github.com/SenteLabsAI/OpenExecutive)

---

**[Luanti removed from Google Play due to baseless AI copyright notice](https://news.ycombinator.com/item?id=49475079)**

Luanti has been removed from Google Play due to a DMCA notice from Tracer.AI. We have filed a counter-notice, but this isn't the first time.

⬆️ 490 • 💬 148 • 1d ago • [Luanti Blog](https://blog.luanti.org/2026/08/27/luanti-dmca-tracer-ai/)

---

**[The turbulent AI era is here](https://news.ycombinator.com/item?id=49451313)**

⬆️ 361 • 💬 6 • 2d ago • [gatesnotes.com](https://www.gatesnotes.com/a-turbulent-ai-era-and-critical-choices-to-make)

---

**[The turbulent AI era is here](https://news.ycombinator.com/item?id=49447057)**

⬆️ 346 • 💬 611 • 2d ago • [gatesnotes.com](https://www.gatesnotes.com/a-turbulent-ai-era-and-critical-choices-to-make)

---

**[It’s so hard to finish an idea that is not yours and is just suggested by AI](https://news.ycombinator.com/item?id=49450898)**

Everyone is using Obsidian for AI, or wants to use it to become more productive. But I think it's a dead end.

⬆️ 258 • 💬 187 • 2d ago • [Simon Späti's Second Brain](https://www.ssp.sh/brain/using-obsidian-with-ai/)

---

**[Fake US thinktank set up and funded by Israel sought to game AI for propaganda](https://news.ycombinator.com/item?id=49447600)**

In effort to prime chatbots to make pro-Israel arguments the site published 124 reports, over 560,000 words in nine days, Guardian analysis shows

⬆️ 246 • 💬 51 • 2d ago • [the Guardian](https://www.theguardian.com/world/2026/aug/26/fake-thinktank-israel-ai-propaganda)

---

**[Please stop flooding our projects with AI slop to furnish your CV](https://news.ycombinator.com/item?id=49474143)**

Successful contributions to open source projects are a kind of currency. GitHub in particular encourages this in a number of ways: by showing avatars of contributors on repository pages, by showing your contributions to your followers via the activity feed and by signalling contributions per day on the activity graph of your profile. Potential hiring managers often take note of this. Recruiters often find and screen candidates this way. If you are a software developer (either existing or aspiring) looking for work, tuning these signals can often work to your advantage.

⬆️ 212 • 💬 141 • 1d ago • [neilalexander.dev](https://neilalexander.dev/2026/06/30/flooding-contributions)

---

**[The turbulent AI era is here](https://news.ycombinator.com/item?id=49448137)**

⬆️ 194 • 💬 365 • 2d ago • [gatesnotes.com](https://www.gatesnotes.com/work/make-ai-work-for-everyone/reader/a-turbulent-ai-era-and-critical-choices-to-make)

---

**[Two German airport workers die of malaria after 'mosquito arrives on plane'](https://news.ycombinator.com/item?id=49468315)**

It is believed the mosquitoes arrived at Germany's busiest airport on a plane, according to German public health officials.

⬆️ 187 • 💬 105 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/cz6zwgg9y8go)

---

**[Serve Markdown to AI Agents with Accept Headers](https://news.ycombinator.com/item?id=49454764)**

Serve Markdown to AI agents and LLMs via the Accept: text/markdown header. Browsers get HTML, agents get clean Markdown.

⬆️ 175 • 💬 108 • 2d ago • [acceptmarkdown.com](https://acceptmarkdown.com/)

---

---

## YouTube Videos: "ai"

**[Breaking: Bill Gates TURNS on AI, WARNS of bioterror, danger, unemployment CRASH (Melber breakdown)](https://www.youtube.com/watch?v=X9oBm_oPRkQ)**

MS NOW's Ari Melber reports on tech innovator and Microsoft founder Bill Gates issuing an extensive warning about the current AI ...

📺 MS NOW

👁️ 234K • 👍 3K • 💬 621 • ⏱️ 12:17 • 1d ago

---

**[Bill Gates stakes reputation: AI is not like past tech](https://www.youtube.com/watch?v=pJ-TBE7HaiA)**

Microsoft co-founder Bill Gates argued on Wednesday that artificial intelligence needs significant limits or else the harm to ...

📺 CNN

👁️ 1.4M • 👍 8K • 💬 4K • ⏱️ 9:22 • 2d ago

---

**[&#39;THIS IS INSANE&#39;: Bill Gates DIRE WARNING Of AI Jobless Future](https://www.youtube.com/watch?v=5r5uhGjST7s)**

Ryan and Saagar take a look at Bill Gate's warning about AI disruption. Sign up for a PREMIUM Breaking Points subscriptions for ...

📺 Breaking Points

👁️ 356K • 👍 5K • 💬 1K • ⏱️ 16:29 • 1d ago

---

**[AI News: OpenAI Made a Massive Move Against NVIDIA](https://www.youtube.com/watch?v=TInwQglNkzo)**

Here's the AI news you probably missed this week. Download the Codex app and try Sites here: ...

📺 Matt Wolfe

👁️ 70K • 👍 2K • 💬 283 • ⏱️ 29:31 • 19h ago

---

**[AI Expert’s Chilling Warning About Super-intelligence - 99.9999% Chance Human Extinction](https://www.youtube.com/watch?v=5QwpHRu51fw)**

Patrick Bet-David sits down with AI safety researcher Roman Yampolskiy, who argues superintelligence cannot be controlled and ...

📺 PBD Podcast

👁️ 250K • 👍 5K • 💬 2K • ⏱️ 1:46:39 • 2d ago

---

**[Apple Just Made the Best Local AI Machine. Do Not Buy It Yet.](https://www.youtube.com/watch?v=OIVZC4edQ48)**

Join the Community: https://discord.gg/MRESQnf4R4 Apple just announced the new Mac Studio with M5 Max and M5 Ultra, ...

📺 Manolo Remiddi

👁️ 146K • 👍 2K • 💬 400 • ⏱️ 12:01 • 2d ago

---

**[The First Fully AI OS Just Dropped And It&#39;s Seriously Powerful](https://www.youtube.com/watch?v=Lnyml75U13w)**

Warmwind OS turns AI into cloud workers that can learn a job by watching you do it, then keep working across Gmail, SAP and ...

📺 AI Revolution

👁️ 44K • 👍 1K • 💬 135 • ⏱️ 12:25 • 2d ago

---

**[The Man Who Calls BS On AI: They’re LYING About AI, 2027 Is When It All Breaks! | Ed Zitron](https://www.youtube.com/watch?v=Lf5oqGOCRCM)**

Tech critic Ed Zitron exposes the AI bubble, why OpenAI and Anthropic are burning billions, the fake AI boom, and why the crash ...

📺 The Diary Of A CEO

👁️ 3.3M • 👍 33K • 💬 13K • ⏱️ 2:27:50 • 2d ago

---

**[Bill Gates Changes His Mind on AI](https://www.youtube.com/watch?v=U4zGLSlLo5A)**

Bill Gates has generally been an AI optimist. Three years ago, he wrote that AI had downsides, but the risks were “manageable.

📺 The Atlantic

👁️ 655K • 👍 6K • 💬 2K • ⏱️ 32:29 • 2d ago

---

**[‘TURBULENT TIMES’: Bill Gates ISSUES WARNING over AI | RISING](https://www.youtube.com/watch?v=6rPYPXjQz7s)**

OPINION: Bill Gates warns that the transition into the age of AI will be "turbulent" if the world doesn't have a plan for dealing with ...

📺 The Hill

👁️ 12K • 👍 134 • 💬 108 • ⏱️ 12:42 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 52,341 • ❤️ 4,208 • 2d ago

---

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`text-generation` `321.3B`

⬇️ 189,793 • ❤️ 1,552 • 2d ago

---

**[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)**

*Z.ai*

GLM-5.3 is a text-generation model excelling in complex coding and long-horizon tasks, achieving state-of-the-art performance in coding benchmarks and emergent cyber capabilities like vulnerability discovery and exploitation.

`text-generation` `753.3B`

⬇️ 8,804 • ❤️ 1,202 • 1h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 4,028,839 • ❤️ 13,180 • 14d ago

---

**[Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)**

*Unsloth AI*

Qwen3.8-Flash-Next-GGUF is a highly efficient, multimodal causal language model featuring Hybrid Attention with QSA and N-gram Embeddings for significantly reduced long-context latency. It excels in agentic workloads and supports context lengths up to 1,000,000 tokens, making it ideal for complex reasoning and large-scale data processing.

`image-text-to-text` `176.9B`

⬇️ 188,061 • ❤️ 538 • 1d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 8,363,481 • ❤️ 3,161 • 8d ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 645,554 • ❤️ 889 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,044,661 • ❤️ 2,048 • 1d ago

---

**[Qwen3.8-27B-Uncensored-MLX](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX)**

*OrcaRouter*

An uncensored, MLX-quantized 27B parameter vision-language model optimized for Apple Silicon, supporting 2-8 bit precisions. It performs image-text-to-text tasks and is intended for AI safety research and red-teaming due to its removed safety alignment.

`image-text-to-text` `4.7B`

⬇️ 97,508 • ❤️ 1,196 • 1d ago

---

**[Hy4-preview](https://huggingface.co/tencent/Hy4-preview)**

*Tencent*

Hy4-preview is a 770B parameter Mixture-of-Experts (MoE) text generation model with 49B activated parameters per token, featuring a 1M context length and Gated Sparse Attention. It excels in productivity tasks across software engineering, office analysis, game development, and scientific research, offering significant gains in understanding, reasoning, and code generation.

`text-generation` `780.0B`

⬇️ 1,394 • ❤️ 262 • 19h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 761 • 💬 5 • ⭐ 8,544 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 100 • 💬 2 • ⭐ 9,380 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 6 • ⭐ 101,558 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 200 • 💬 3 • ⭐ 1,247 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://huggingface.co/papers/2608.24053)**

*Junjie Zhou, Ke Mei, Lei Li et al. (6 authors)*

🏢 Tencent

WeMM-Embedding is a family of universal multimodal embedding models that align text, images, videos, and interleaved inputs in a shared space, achieving state-of-the-art retrieval and recommendation performance across public benchmarks and large-scale WeChat applications.

▲ 64 • 💬 2 • ⭐ 806 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.24053) • [💻 code](https://github.com/Tencent/WeMM-Embedding) • [🔗 project](https://github.com/Tencent/WeMM-Embedding)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 43 • 💬 2 • ⭐ 18,987 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 85 • 💬 7 • ⭐ 85,493 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://huggingface.co/papers/2308.04079)**

*Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler et al. (4 authors)*

A method using 3D Gaussians for scene representation and optimized rendering allows high-quality, real-time novel-view synthesis at 1080p resolution.

▲ 204 • 💬 13 • ⭐ 23,619 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2308.04079) • [💻 code](https://github.com/graphdeco-inria/gaussian-splatting)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 68 • 💬 4 • ⭐ 29,976 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 46 • 💬 2 • ⭐ 29,967 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

A privacy-first app that strips AI watermarks from content you own.

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 19.1k • 🔱 2.2k • 8h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 9.1k • 🔱 1.1k • 7d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.9k • 🔱 634 • 1d ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.4k • 🔱 409 • 14h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.3k • 🔱 256 • 17d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.2k • 🔱 393 • 1h ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.8k • 🔱 163 • 4d ago

---

**[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)**

FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools, with cost-aware routing across LLM providers.

`Python` `agent` `ai` `ai-agent` `ai-coding` `autonomous-agent`

⭐ 2.7k • 🔱 73 • 6d ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 2.6k • 🔱 239 • 1d ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 2.4k • 🔱 298 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
