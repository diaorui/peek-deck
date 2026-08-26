---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-26T14:11:39.589818+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 26, 2026 at 14:11 UTC  
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

**[CEO fired developers to make room for AI. Developers respond by creating open source AI CEO](https://www.reddit.com/r/artificial/comments/1vyegah/ceo_fired_developers_to_make_room_for_ai/)**

I hope this is okay to share since it is not self promotion and it is open source. Some of my friends were let go as part of an "AI Transformation". So they got together and created Open Executive as a tool to replace the CEO and other executives. Hopefully, turnabout is fair play and might even get some folks to think twice about using AI to replace people. It is free and available here: https://github.com/SenteLabsAI/OpenExecutive

15h ago

---

**[Mark Zuckerberg had a bold plan to replace Meta staff with AI. Here’s how it imploded.](https://www.reddit.com/r/artificial/comments/1vyvxb5/mark_zuckerberg_had_a_bold_plan_to_replace_meta/)**

🔗 [reuters.com](https://www.reuters.com/investigations/mark-zuckerberg-had-bold-plan-replace-meta-staff-with-ai-heres-how-it-imploded-2026-08-26) • 1h ago

---

**[The bottleneck for meeting transcription tools isn't accurate anymore, it's speaker attribution](https://www.reddit.com/r/artificial/comments/1vyrxy8/the_bottleneck_for_meeting_transcription_tools/)**

Been testing a few AI transcription setups for work over the past couple months and noticed something word level accuracy from most of these engines is already pretty solid now, upper 90s%. The thing that actually breaks the output is figuring out who said what when more than 2-3 people are talking, especially with any crosstalk or people talking over each other. Feels like an underrated problem compared to how much attention pure transcription accuracy gets. A transcript that's 99% accurate but has the wrong person attributed to a key statement is arguably more useless than one that's 90% accurate with correct speaker labels, at least for anything where "who committed to what" matters. Tried a handful of tools chasing this Otter, a couple others, and more recently Vomo ai which does speaker labeling automatically. Vomo’s noticeably better on 3+ person calls than what I was using before,though overlapping speech is still the one case where it takes a bit more attention to double-check, so more of an improvement than a full fix. Wondering if this is a known hard problem in the diarization research or if it's more of an engineering/product prioritization gap that just hasn't been addressed yet.

4h ago

---

**[[Open-Source] I need your worst edge cases to stress-test GenOS, my new AI agent orchestrator.](https://www.reddit.com/r/artificial/comments/1vyxoes/opensource_i_need_your_worst_edge_cases_to/)**

Hey everyone, I’m currently working on GenOS, an open-source framework for multi-agent LLM orchestration. Under the hood, it uses isolated Rust execution environments and relies on Git worktrees for clean state management and secure sandboxing. The core engine is running smoothly, but before pushing it further, I need to expose it to the harsh reality of real-world use cases. We all know that AI agents (whether single or in swarms) look amazing in demos, but often trip over their own feet the second you take them out of "Hello World" territory. That’s where you come in: what are the real, testable problems you run into when building or using AI agents? I’m looking for concrete, reproducible scenarios to see how GenOS handles them (or if it fails miserably, which will help me iterate). What I'm specifically looking for: Infinite loops & derailments: Tasks where the agent starts hallucinating code execution and just won't stop. State & context management: Swarm scenarios where Agent A forgets to pass crucial info to Agent B, or completely overwrites its work. Isolation issues: Cases where an agent corrupts its workspace by modifying or deleting the wrong files. Complex multi-step tasks: Long workflows where the agent eventually loses track of its initial objective. Drop your use cases, your biggest frustrations with existing frameworks (like LangChain, AutoGen, CrewAI, etc.), or even specific prompts that consistently break your setups. I’ll take the most interesting cases, code them into GenOS to see if the Rust/Git architecture offers a cleaner solution, and I'll report back with the results! Thanks in advance for the feedback

21m ago

---

**[Why Irregular’s A.I. Tests for Meta, Anthropic and OpenAI Went Off the Rails. Irregular, an Israeli start-up, worked with OpenAI, Anthropic and Meta to assess the security of their A.I. models. It made a mistake. Then the tests went off the rails. (Gift Article)](https://www.reddit.com/r/artificial/comments/1vyxo7p/why_irregulars_ai_tests_for_meta_anthropic_and/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/08/25/technology/irregular-ai-test-hacks.html?unlocked_article_code=1.8VA.zpoD.QLh0Y1YB-Ym7&smid=url-share) • 21m ago

---

**[Truck Driver Builds AI News Aggregator](https://www.reddit.com/r/artificial/comments/1vycupz/truck_driver_builds_ai_news_aggregator/)**

Truck driver here, zero coding background. I Built an AI news aggregator over a few evenings because I was sick of seeing the same story five times. It pulls from about a dozen AI news sources, auto-summarises each article so you get the gist without clicking through and dedupes stories covered by multiple outlets into one card instead of five separate headlines saying the same thing. I deliberately went for a no-nonsense Win98-ish look — no clutter, no bells and whistles, just the feed. Built with Next.js/Supabase, synced every two hours via GitHub Actions. No coding experience going in, mostly just kept iterating with Claude Code until it worked. Not selling anything, just proud it works and thought a few people here might actually use it. Feedback welcome :)

16h ago

---

**[Uber hit with a near-$1B GDPR fine after algorithms suspended drivers without human review](https://www.reddit.com/r/artificial/comments/1vxv8pl/uber_hit_with_a_near1b_gdpr_fine_after_algorithms/)**

1d ago

---

**[What's an AI capability you thought was hype until you actually used it?](https://www.reddit.com/r/artificial/comments/1vywipi/whats_an_ai_capability_you_thought_was_hype_until/)**

What's an AI capability you thought was hype until you actually used it? I'll go first: agent orchestration. I read about agents managing other agents and assumed it was demo-ware. Then I built a tiny setup where one agent drafts a news digest and another one reviews and approves it before it posts. The review agent catches genuinely bad takes. It's not sci-fi: it's ~100 lines of Python and a couple of API calls. But seeing it actually gate content before publishing changed my mind completely. What changed yours?

1h ago

---

**[Using MyselfGPT to code](https://www.reddit.com/r/artificial/comments/1vywbeb/using_myselfgpt_to_code/)**

I‘ve been using this model called MyselfGPT to code, and it’s been a fantastic experience. Has anyone else used it?

1h ago

---

**[VSArena: the hosted harness for public ELO is live — submit a policy, watch it stack cubes, get scored](https://www.reddit.com/r/artificial/comments/1vyw1en/vsarena_the_hosted_harness_for_public_elo_is_live/)**

Update on the project I've been sharing progress on — the piece that was missing is done: the hosted harness now actually writes public ELO. Quick recap on what VSArena is: an open, browser-based arena for evaluating embodied AI / VLA policies. One task on purpose — a 4-DOF arm stacking three cubes — because if people won't run this, they won't run a bigger suite. Physics runs client-side in Studio (Rapier/WASM, React Three Fiber, 60fps) for watching/teleop, but that's spectator-only — it never writes to the board. Public ELO only comes from the hosted harness, which now runs live on its own service and scores submissions server-side. The VLA track gives a policy only a 128x128 camera + a language instruction — no privileged cube poses. Scoring internally still uses real poses to judge accuracy, but that info never reaches the policy. You can: - Watch the live demo: https://vsarena.vercel.app/simulation - Check the leaderboard: https://vsarena.vercel.app/leaderboard - Submit your own policy in under 10 minutes: https://github.com/NovaCoding-G/VSArena (docs/sdk.md has the walkthrough) Solo project, still early — one task, a couple baseline policies so far. Repo is MIT, protocol writeup is in docs/harness.md if you want to see exactly how scoring works before trusting it. Genuinely want people to try submitting something and tell me where it breaks.

1h ago

---

---

## Google News: "ai"

**[Bill Gates Is Warning That A.I. Is More Dangerous Than Big Tech Will Admit](https://www.nytimes.com/2026/08/26/technology/bill-gates-ai-risks.html)**

The New York Times • 3h ago

---

**[Exclusive: Google targets AI sticker shock with suite of new tools](https://www.axios.com/2026/08/26/exclusive-google-targets-ai-sticker-shock-with-new-tools)**

Axios • 39m ago

---

**[OpenAI’s Jalapeño AI chip brings new 'threat' to Nvidia margins as custom silicon gains ground](https://www.cnbc.com/2026/08/26/openai-jalapeno-ai-chip-nvidia.html)**

OpenAI’s Jalapeño chip beat Nvidia Blackwell systems on key inference-efficiency tests as custom AI silicon gains ground among major tech companies.

CNBC • 44m ago

---

**[Nvidia Earnings Give Investors a Barometer for State of AI Trade](https://www.bloomberg.com/news/articles/2026-08-26/nvidia-earnings-give-investors-a-barometer-for-state-of-ai-trade)**

Bloomberg.com • 6h ago

---

**[Nvidia earnings: Wall Street hopes the chip titan can keep carrying the AI trade, with the stock up 14% in 2026](https://www.businessinsider.com/nvidia-earnings-report-nvda-stock-ai-chips-jensen-huang-2026-8)**

Investors wants clarity on the strength of AI demand, with NVDA stock up 14% YTD. The call with analysts will begin at 5 p.m. ET.

Business Insider • 41m ago

---

**[AI billionaires could drive African aid surge](https://www.yahoo.com/news/world/articles/ai-billionaires-could-drive-african-133308944.html)**

AI firms’ record-breaking IPOs could generate a pool of philanthropic wealth potentially worth up to $100 billion a year.

Yahoo • 38m ago

---

**[The Connections That Turned a Precocious Teen Into the Fallen ‘Nostradamus of AI’](https://www.wsj.com/tech/ai/situational-awareness-leopold-aschenbrenner-ai-fund-4dbb00a4)**

WSJ • 13h ago

---

**[Mark Zuckerberg had a bold plan to replace Meta staff with AI. Here’s how it imploded.](https://www.reuters.com/investigations/mark-zuckerberg-had-bold-plan-replace-meta-staff-with-ai-heres-how-it-imploded-2026-08-26/)**

Reuters • 4h ago

---

**[Apple introduces M6 and M5 Ultra for a big leap in performance and AI compute](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/)**

Apple debuted M6 in the new Mac mini and M5 Ultra in the new Mac Studio, providing an extraordinary leap in performance and AI capabilities.

Apple • 10h ago

---

**[Billionaire Stanley Druckenmiller’s WSJ Op-Ed Criticizing Bessent Was Written With AI - News of the United States](https://www.notus.org/media/stanley-druckenmillers-wsj-op-ed-bessent-ai)**

“I write everything using AI now,” Druckenmiller, who questioned the treasury secretary’s bond market interventions, said.

News of the United States - NOTUS • 16h ago

---

---

## HackerNews: "ai"

**[Anthropic's best AI model struggles to attract users as cheaper tools thrive](https://news.ycombinator.com/item?id=49411102)**

AI lab’s Fable 5 has met with sluggish demand from corporate clients

⬆️ 813 • 💬 700 • 2d ago • [ft.com](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245)

---

**[I spent $266 and four AI models to own my tablet. GLM-5.3 finished it in a day](https://news.ycombinator.com/item?id=49409073)**

Owning a tablet Amazon kept shutting down: CVE-2022-38181, four AI models, five months

⬆️ 694 • 💬 291 • 2d ago • [ericpardee.github.io](https://ericpardee.github.io/fire-hd-ownership/)

---

**[Coding expertise is going to collapse from AI reliance](https://news.ycombinator.com/item?id=49421554)**

The need for ongoing friction in long-term skill formation.

⬆️ 552 • 💬 540 • 1d ago • [larsfaye.com](https://larsfaye.com/articles/ai-coding-will-prevent-expertise)

---

**[I built a low-latency AI companion that plays Skyrim with me](https://news.ycombinator.com/item?id=49413561)**

How Varkos was built: a low-latency AI companion that plays Skyrim with you, follows complex instructions and evolves through shared experiences.

⬆️ 394 • 💬 76 • 2d ago • [Pantelis Kalogiros](https://pantel.is/projects/ai-gaming-companion/)

---

**[Z.ai confirms Ox Alpha is a new GLM-series model and will release its weights](https://news.ycombinator.com/item?id=49446422)**

⬆️ 274 • 💬 107 • 4h ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-08-26/china-s-z-ai-made-ox-alpha-stealth-model-that-rivals-deepseek)

---

**[How much of HN is AI?](https://news.ycombinator.com/item?id=49435728)**

TL;DR: As of June 2026, ~50% of daily top stories are about AI or generated by AI.

⬆️ 271 • 💬 331 • 22h ago • [blog.coredump.cx](https://blog.coredump.cx/p/how-much-of-hn-is-ai)

---

**[Training AI to Paint with Code](https://news.ycombinator.com/item?id=49411800)**

I'm a designer and creative technologist based in Brooklyn, NY.

⬆️ 211 • 💬 26 • 2d ago • [surya.website](https://surya.website/rling-qwen-to-paint-with-code)

---

**[FDA clears blood test to aid evaluation for Alzheimer's disease](https://news.ycombinator.com/item?id=49415893)**

The blood-based biomarker test is based on technology developed at WashU Medicine by Randall Bateman, MD, and David Holtzman, MD.

⬆️ 187 • 💬 105 • 2d ago • [WashU Medicine](https://medicine.washu.edu/news/fda-clears-blood-test-to-aid-evaluation-for-alzheimers-disease/)

---

**[Fake US thinktank set up and funded by Israel sought to game AI for propaganda](https://news.ycombinator.com/item?id=49447600)**

In effort to prime chatbots to make pro-Israel arguments the site published 124 reports, over 560,000 words in nine days, Guardian analysis shows

⬆️ 166 • 💬 25 • 2h ago • [the Guardian](https://www.theguardian.com/world/2026/aug/26/fake-thinktank-israel-ai-propaganda)

---

**[Show HN: I made a Raspberry with Qwen my local car AI](https://news.ycombinator.com/item?id=49435675)**

Your car as a chat-room agent: Raspberry Pi 5 + dashcam + local AI. CodeWatch's sibling for the garage. - ThinkOffApp/CarWatch

⬆️ 143 • 💬 45 • 22h ago • [GitHub](https://github.com/ThinkOffApp/CarWatch)

---

---

## YouTube Videos: "ai"

**[Chinese Z.ai AI Model Near Anthropic Mythos Level - USA Can&#39;t Stop China](https://www.youtube.com/watch?v=MlG6di3LORo)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 11K • 👍 549 • 💬 159 • ⏱️ 17:41 • 13h ago

---

**[&#39;The Five&#39;: Raging against AI data centers becomes all the rage](https://www.youtube.com/watch?v=aolQYQYISfw)**

'The Five' co-hosts discuss the growing political and public backlash against A.I. data centers, analyzing President Donald ...

📺 Fox News

👁️ 122K • 👍 3K • 💬 808 • ⏱️ 9:28 • 1d ago

---

**[This Small AI Will Change Everything](https://www.youtube.com/watch?v=wMl6c_r0ubw)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The Qwen3.8-27b is available here: ...

📺 Two Minute Papers

👁️ 89K • 👍 3K • 💬 354 • ⏱️ 3:21 • 1d ago

---

**[Growing backlash to AI data centers](https://www.youtube.com/watch?v=F9mFbSt43Ag)**

Bipartisan backlash is growing in response to the rapid buildout of AI data centers across the country, with potential ramifications ...

📺 ABC News

👁️ 57K • 👍 1K • 💬 532 • ⏱️ 1:56 • 1d ago

---

**[It&#39;s Not AI fault ✋️](https://www.youtube.com/watch?v=0AvPyAd_8_o)**

shorts #mystery #ai #nestle #ecosystem #unknownfacts.

📺 ​The Mystery Hub

👁️ 27K • 💬 100 • ⏱️ 0:07 • 17h ago

---

**[Amazon BUSTED Burning Rare Books After Feeding Them Into Ai](https://www.youtube.com/watch?v=sQdKJamsilE)**

Live-streamed on August 19, 2026. Check out @404Mediaco's report: ...

📺 The Majority Report w/ Sam Seder

👁️ 58K • 👍 2K • 💬 477 • ⏱️ 13:41 • 1d ago

---

**[The AI That Comes Back Better Without a Better Prompt - Abacus AI AutoBots](https://www.youtube.com/watch?v=u-ObVnUaQeI)**

Abacus AI: http://abacus.ai/ AutoBots: http://autobots.abacus.ai/ Can an AI agent actually learn from its previous results and ...

📺 Shark Numbers

👁️ 161K • 👍 17K • 💬 363 • ⏱️ 8:47 • 2d ago

---

**[AI Jobs](https://www.youtube.com/watch?v=KixsIL38wkY)**

My Patreon: https://www.patreon.com/cw/nateziller This episode brings back Paper as he tries to find a job with the help of AI.

📺 Nate Ziller

👁️ 194K • 👍 14K • 💬 845 • ⏱️ 5:15 • 2d ago

---

**[How to Understand the Next Wave of AI Before Everyone Else | Tibo Interview](https://www.youtube.com/watch?v=4qjEgPojjzM)**

OpenAI's Tibo joins me to break down what's next for Codex, ultra-fast AI, recursive self-improvement, and the future of personal AI ...

📺 Matthew Berman

👁️ 85K • 👍 2K • 💬 263 • ⏱️ 44:29 • 1d ago

---

**[Iran faces &#39;economic D-Day&#39; as UK and Ukraine strike major AI defence deal | Michael Clarke analysis](https://www.youtube.com/watch?v=xvz7UHyg1v8)**

Sky's security and defence analyst Michael Clarke examines the US threat of an “economic D-Day” against Iran, assessing how ...

📺 Sky News

👁️ 105K • 👍 2K • 💬 351 • ⏱️ 5:45 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 2,551 • ❤️ 3,045 • 1h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 3,298,569 • ❤️ 12,820 • 11d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 7,638,591 • ❤️ 2,951 • 6d ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 468,746 • ❤️ 779 • 1d ago

---

**[Qwen3.8-27B-Uncensored-MLX](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX)**

*OrcaRouter*

An uncensored, MLX-quantized 27B parameter vision-language model optimized for Apple Silicon, supporting 2-8 bit precisions. It performs image-text-to-text tasks and is intended for AI safety research and red-teaming due to its removed safety alignment.

`image-text-to-text` `4.7B`

⬇️ 79,395 • ❤️ 1,128 • 2d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 269,805 • ❤️ 1,162 • 6d ago

---

**[Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)**

*Ornith*

Ornith-1.5-35B-A3B is a 35B Mixture-of-Experts model that activates ~3B parameters per token, excelling in coding and agentic tasks. It is built through end-to-end self-improvement, continuously generating and optimizing training tasks for enhanced performance.

`text-generation` `36.0B`

⬇️ 83,342 • ❤️ 435 • 3d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 894,094 • ❤️ 1,823 • 9d ago

---

**[Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF](https://huggingface.co/HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF)**

*HauhauCS*

This is an uncensored, aggressive Qwen3.8-27B multimodal model with HauhauCS FastMTP for accelerated text generation and a vision projector for image/video input. It excels at direct, fast responses and handles complex prompts without refusal, supporting up to 1M token context.

`image-text-to-text` `1.9B`

⬇️ 911,795 • ❤️ 636 • 8d ago

---

**[Ornith-1.5-35B-A3B-GGUF](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B-GGUF)**

*Ornith*

Ornith-1.5-35B-A3B is a 35B parameter Mixture-of-Experts model optimized for text generation, excelling in coding and agentic tasks by utilizing end-to-end self-improvement. It outperforms similar-sized models like Qwen3.6-35B and dense models like Gemma-4-31B on agentic coding benchmarks.

`text-generation` `35.5B`

⬇️ 1,391,218 • ❤️ 303 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 97 • 💬 2 • ⭐ 7,805 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 179 • 💬 2 • ⭐ 583 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 754 • 💬 5 • ⭐ 6,057 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 6 • ⭐ 100,489 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 37 • 💬 2 • ⭐ 18,415 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://huggingface.co/papers/2608.20335)**

*Yudong Jin, Tao Xie, Qihang Zhang et al. (9 authors)*

🏢 Ant Research

4DAnyone reconstructs 4D humans from monocular video by generating multiview-consistent videos and lifting them into 4D Gaussian Splatting, using reference and target context designs to overcome scaling bottlenecks.

▲ 76 • 💬 7 • ⭐ 766 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.20335) • [💻 code](https://github.com/ant-research/4DAnyone) • [🔗 project](https://4danyone.github.io/)

---

**[Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://huggingface.co/papers/2606.31227)**

*Yong Yang, Xing Zheng, Huiyu Wu et al. (10 authors)*

🏢 Tencent

AI-Infra-Guard is an open-source framework that addresses AI infrastructure security through layered detection paradigms spanning infrastructure, protocol, agent behavior, and model layers.

▲ 15 • 💬 2 • ⭐ 5,889 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.31227) • [💻 code](https://github.com/Tencent/AI-Infra-Guard) • [🔗 project](https://matrix.tencent.com/clawscan/)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 18 • 💬 1 • ⭐ 2,879 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 68 • 💬 4 • ⭐ 29,650 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 85 • 💬 7 • ⭐ 85,136 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 18.4k • 🔱 2.1k • 1d ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 14.2k • 🔱 1.7k • 10h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.9k • 🔱 1.1k • 4d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.7k • 🔱 622 • 4h ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.1k • 🔱 376 • 23h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.1k • 🔱 250 • 14d ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.0k • 🔱 360 • 2h ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.5k • 🔱 142 • 1d ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 2.2k • 🔱 72 • 6h ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 2.1k • 🔱 264 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
