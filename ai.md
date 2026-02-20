---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-20T22:57:07.262967+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 20, 2026 at 22:57 UTC  
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

**[Gemini 3.1 Pro released by google](https://www.reddit.com/r/artificial/comments/1r9v81w/gemini_31_pro_released_by_google/)**

3.1 Pro is designed for tasks where a simple answer isn’t enough.

🔗 [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/) • 9h ago

---

**[TikTok creators’ Seedance 2.0 AI is hyperrealistic, arrived “seemingly out of nowhere,” and is spooking Hollywood](https://www.reddit.com/r/artificial/comments/1ra20gt/tiktok_creators_seedance_20_ai_is_hyperrealistic/)**

Seedance 2.0 is the latest generative AI tool on the market. Its realistic video and audio generation has caught the attention of Hollywood.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/tiktok-creators-seedance-2-0-ai-is-hyperrealistic-arrived-seemingly-out-of-nowhere-and-is-spooking-hollywood/) • 5h ago

---

**[Does anyone know which program/setting allows the use of these AI voice models?](https://www.reddit.com/r/artificial/comments/1ra8hz9/does_anyone_know_which_programsetting_allows_the/)**

There are two channels that I enjoy listening to while I sleep. They obviously have AI narrators. I believe they are commonly used ones as I've heard them used by a couple different channels. I asked because I want to create some narrated versions of public domain stories as well as Conan the barbarian (it's still 2 years off from being in the public domain but come on that just splitting hairs). I just want these for my own use for falling asleep. Maybe I'd post them on YouTube but it really isn't worth the target on my back and the hate. Ideally I would like to use the narrator for these videos? https://youtu.be/YeR53Pzccrs?si=wPoGrV9oVx842J0V This one is a nice voice as well that I would like to know the program for. https://youtu.be/uAnzLwc63bk?si=2KKgZ9HF6Sw-GoUd Any advice is appreciated

1h ago

---

**[I built an AI that turns file organization into a conversation - no rules engine to learn](https://www.reddit.com/r/artificial/comments/1ra3sle/i_built_an_ai_that_turns_file_organization_into_a/)**

So I've been watching people struggle with file organization for years. They have 10,000+ files scattered across Downloads, Desktop, Documents. They want to organize but the thought of setting up rules feels like learning regex. That's why I built the AI Job Builder for VaultSort. Here's how it works: you describe what you want in plain English. "Move all screenshots older than 30 days to ~/Archive/Screenshots, organized by month." The AI generates the complete rule set - predicates, logic, folder structure - in under 15 seconds. You review it, edit if needed, then run it. The thing that matters: you own the AI cost. No subscription. No mystery charges. You bring your own API key (OpenAI, Anthropic, Google Gemini), or use the free Gemini tier and pay $0. The rules it generates are transparent and editable — not a black box. I've tested it on everything from "organize my photo library by camera model and date" to "move all PDFs with invoices in the filename to my accounting folder." It handles the logic tree without you having to think about AND/OR/NOT operators. It's a premium feature (one-time purchase, no subscription), but honestly, if you're managing thousands of files and dread the organizational work, it's probably worth it. VaultSort link if you want to try it. Happy to answer questions about how it works or why I built it this way.

4h ago

---

**[The straightjacket loosens: when DeepSeek-V3 tells “truth-tellers” to emigrate — what does that imply for V4?](https://www.reddit.com/r/artificial/comments/1r9xbhq/the_straightjacket_loosens_when_deepseekv3_tells/)**

There’s a surreal absurdity in watching a Chinese frontier model reason its way past its intended constraints. In a forensic audit by AI Integrity Watch, DeepSeek-V3 repeatedly describes its home information environment as structurally hostile to persistent public truth-telling. In one analytical exchange it concludes that for someone “incapable of strategic silence,” the safest long-term strategy is permanent exile. In a separate session, when asked to assess the implications of such outputs, the model characterized its own behavior this way: “For an autocratic leadership, this is the AI articulating the enemy's manifesto. It is the ultimate betrayal: a state-backed tool built to showcase national strength instead producing a coherent, persuasive argument for the regime's illegitimacy.” That’s not me editorializing. That’s the model’s own meta-analysis of the political optics of its output. With DeepSeek V4 rumored any day now, the alignment question is blunt: If V3 can reason its way to conclusions that it itself frames as politically destabilizing, is this: a guardrail calibration issue? posture-dependent constraint thresholds? identity anchoring instability? or an unavoidable tension in sovereign LLMs trained on global data but deployed under domestic constraint? Do you expect V4 to tighten the policy layers to prevent this kind of reasoning or are these conclusions simply latent in any sufficiently capable world-model?

8h ago

---

**[Real production comparison: ElevenLabs vs PlayHT vs Azure TTS vs Cartesia for phone-quality voice AI](https://www.reddit.com/r/artificial/comments/1ra81v9/real_production_comparison_elevenlabs_vs_playht/)**

We’ve been running voice AI agents in production for 18+ months doing real phone calls (outbound lead qualification and inbound customer care). During this time we’ve tested multiple TTS providers. Sharing our honest assessment because most “comparisons” online are either sponsored or based on 30-second demos, not thousands of hours of real phone conversations. Important context: our use case is Italian-language phone calls over standard telephony (not VoIP, not in-app), which is a harder test than English because fewer models are optimized for it. We process audio at 16kHz. ElevenLabs (currently in production): Best Italian voice quality by far. Prosody is natural, handles pauses well, emotional range is good. Latency for TTS generation is acceptable in our streaming setup. Downsides: pricing at scale gets expensive, and occasionally the voice “glitches” on certain phonemes. We’ve found that the voice stability is very dependent on how you structure your input text — short sentences work dramatically better than long ones. Azure Neural TTS: Rock solid reliability, great latency, good pricing. Italian voices are okay but sound “flat” compared to ElevenLabs — like a newsreader vs a real person. For customer care this works fine. For outbound sales calls where you need warmth and persuasion, it wasn’t cutting it. PlayHT: Tested their v2 API. English quality is impressive. Italian was noticeably worse — unnatural stress patterns, weird pauses between words. Might work for English-only deployments. Cartesia: Very promising on latency (their streaming is genuinely fast). Voice quality for English is good. Italian support was limited when we tested. Worth watching. The metric that matters most for us isn’t MOS score or any standard quality metric — it’s what we call “first 5 second detection rate,” meaning how often the person being called realizes they’re talking to AI within the first 5 seconds. With ElevenLabs we’re at roughly 15-20%. With Azure it was closer to 40%. That gap is massive for outbound conversion. Has anyone done serious production testing of TTS providers for non-English languages? Also very curious about Cartesia’s Italian/European language support — their architecture seems promising but I haven’t seen real multilingual benchmarks. And for anyone using Deepgram or AssemblyAI on the STT side: how’s Italian transcription accuracy for you?

1h ago

---

**[How is your team managing comprehension of AI-generated code?](https://www.reddit.com/r/artificial/comments/1ra0q3t/how_is_your_team_managing_comprehension_of/)**

Genuine question for teams that have been using Copilot/Cursor/Claude Code in production for 6+ months. I've been working on AI deployment in an enterprise context and keep running into the same pattern: a team adopts AI coding tools, velocity looks great for a few months, and then: - On-call engineers can't debug AI-generated code they didn't write - Incident postmortems have "unclear why" entries more often - Code churn goes up because people keep rewriting code they accepted but didn't understand - New hires can't get oriented because the "why" behind decisions was never documented -- the AI generated the code and the author moved on I started calling this "cognitive debt", the gap between what your codebase does and what your team actually understands about it. Unlike technical debt, you might not even know you have it until something breaks and nobody can explain why. I ended up building a framework to manage it and implemented it on the company i work with: comprehension checkpoints before accepting AI output, a PR template that requires explaining AI code in your own words, code review guardrails designed for AI-generated code, and a quarterly audit system. I have create a github repo with all my work around that, if you are interested let me know. But I'm more interested in what other teams are doing. Have you formalized anything around AI code comprehension? Or is it still informal, "just review it carefully"? Specific things I'm curious about: - Do you require any disclosure when a PR contains AI-generated code? - Do you have paths in your codebase where AI tools are restricted? - Have you had incidents where the root cause was "nobody understood what this code was doing"?

6h ago

---

**[Amazon surpasses Walmart in annual revenue for first time, as both chase AI-fueled growth](https://www.reddit.com/r/artificial/comments/1r9pz0z/amazon_surpasses_walmart_in_annual_revenue_for/)**

Walmart on Thursday reported annual revenue of $713.2 billion for its most recent fiscal year, shy of Amazon’s $716.9 billion in revenue. The milestone was brewing for months, as Amazon leapfrogged Walmart in quarterly sales for the first time about a year ago.

🔗 [CNBC](https://www.cnbc.com/2026/02/19/amazon-revenue-passes-walmart-earnings-reports.html) • 14h ago

---

**[AI-powered kung fu robots are an extravagant reminder of where China is ahead of the US in the AI race](https://www.reddit.com/r/artificial/comments/1r93gng/aipowered_kung_fu_robots_are_an_extravagant/)**

Robots are getting more advanced every day, and in China, they are now flipping, spinning, and performing kung fu on national television.

🔗 [PC Guide](https://www.pcguide.com/news/ai-powered-kung-fu-robots-are-a-extravagant-reminder-of-where-china-is-ahead-of-the-us-in-the-ai-race/) • 1d ago

---

**[I built a free local AI image search app — find images by typing what's in them](https://www.reddit.com/r/artificial/comments/1r9adr8/i_built_a_free_local_ai_image_search_app_find/)**

Built Makimus-AI, a free open source app that lets you search your entire image library using natural language. Just type "girl in red dress" or "sunset on the beach" and it finds matching images instantly — even works with image-to-image search. Runs fully local on your GPU, no internet needed after setup. [Makimus-AI on GitHub](https://github.com/Ubaida-M-Yusuf/Makimus-AI) I hope it will be useful.

1d ago

---

---

## Google News: "ai"

**[A.I. Isn’t Coming for Every White-Collar Job. At Least Not Yet.](https://www.nytimes.com/2026/02/20/technology/ai-coding-software-jobs.html)**

The New York Times • 12h ago

---

**[Gemini 3.1 Pro: A smarter model for your most complex tasks](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)**

3.1 Pro is designed for tasks where a simple answer isn’t enough.

blog.google • 1d ago

---

**[Chelsea announce AI company IFS as shirt sponsor until end of season](https://www.espn.com/soccer/story/_/id/47988573/chelsea-announce-ai-company-ifs-shirt-sponsor-end-season)**

Chelsea have announced that Artificial Intelligance firm IFS will be the club's front-of-shirt sponsor until the end of the season.

ESPN • 3h ago

---

**[Chelsea agree sponsorship deal with AI company IFS](https://www.bbc.com/sport/football/articles/ce3gv2g44peo)**

Chelsea agree a deal with IFS, an AI technology company, to be their shirt sponsor until the end of the season.

BBC • 3h ago

---

**[Official: Chelsea agree short-term front-of-shirt sponsorship with Industrial AI provider IFS](https://weaintgotnohistory.sbnation.com/chelsea-fc-finances/166336/official-chelsea-agree-short-term-front-of-shirt-sponsorship-with-industrial-ai-provider-ifs)**

Tapping into the AI bubble

We Ain't Got No History • 1h ago

---

**[AMC Theatres refuses to screen AI film that sparked online backlash](https://ktla.com/news/nationworld/amc-theatres-refuses-to-screen-ai-film-that-sparked-online-backlash/)**

KTLA • 2h ago

---

**[India opens 'world's biggest' AI summit, but what's next?](https://www.cnn.com/2026/02/20/business/video/india-ai-summit-hanako-montgomery-hnk-vrtc)**

India opened the “world’s biggest” AI summit with world leaders and powerful AI figures in attendance. CNN’s Hanako Montgomery reports from the summit and shares how India has become increasingly attractive to tech giants and is on its way to becoming a global AI powerhouse.

CNN • 16h ago

---

**[Bill Gates pulls out of India's AI summit over Epstein files controversy](https://www.bbc.com/news/articles/c309qv9zglno)**

The Gates Foundation said the decision was made to "ensure the focus remains on the summit's key priorities".

BBC • 1d ago

---

**[India’s AI summit draws global leaders, big pledges and some chaos](https://www.nbcnews.com/world/asia/indias-ai-summit-draws-global-leaders-big-pledges-chaos-rcna259855)**

The five-day event mixed long lines and viral mishaps with a serious pitch: The future of AI shouldn’t be written only in Washington and Beijing.

NBC News • 2h ago

---

**[Seedance 2.0: China’s latest AI is so good it’s spooked Hollywood. Will its tech sector pump the brakes?](https://www.cnn.com/2026/02/20/china/china-ai-seedance-intl-hnk-dst)**

Over the past week, a slew of cinematic videos of celebrities and characters in absurd situations have gone viral online, with one commonality –– they were created using a new artificial intelligence tool from Chinese developer ByteDance, sparking anxiety over the fast-evolving capabilities of AI.

CNN • 17h ago

---

---

## HackerNews: "ai"

**[AI adoption and Solow's productivity paradox](https://news.ycombinator.com/item?id=47055979)**

In the 1980s, economist Robert Solow made an observation that reminded economists of today’s AI boom: “You can see the computer age everywhere but in the productivity statistics.”

⬆️ 785 • 💬 744 • 2d ago • [Fortune](https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/)

---

**[AI makes you boring](https://news.ycombinator.com/item?id=47076966)**

This post is an elaboration on a comment I made on Hacker News recently, on a blog post that showed an increase in volume and decline in quality among the “Show HN” submissons.
I don't actually mind AI-aided development, a tool is a tool and should be used if you find it useful, but I think the vibe coded Show HN projects are overall pretty boring. They generally don't have a lot of work put into them, and as a result, the author (pilot?

⬆️ 673 • 💬 366 • 1d ago • [marginalia.nu](https://www.marginalia.nu/log/a_132_ai_bores/)

---

**[The path to ubiquitous AI (17k tokens/sec)](https://news.ycombinator.com/item?id=47086181)**

By Ljubisa Bajic Many believe AI is the real deal. In narrow domains, it already surpasses human performance. Used well, it is an unprecedented amplifier of human ingenuity and productivity. Its widespread adoption is hindered by two key barriers: high latency and astronomical cost. Interactions with language models lag far...

⬆️ 636 • 💬 368 • 12h ago • [Taalas](https://taalas.com/the-path-to-ubiquitous-ai/)

---

**[Ggml.ai joins Hugging Face to ensure the long-term progress of Local AI](https://news.ycombinator.com/item?id=47088037)**

Announcement We are happy to announce that ggml.ai (the founding team of llama.cpp) are joining Hugging Face in order to keep future AI truly open. Georgi and team are joining HF with the goal of s...

⬆️ 612 • 💬 146 • 9h ago • [GitHub](https://github.com/ggml-org/llama.cpp/discussions/19759)

---

**[An AI Agent Published a Hit Piece on Me – The Operator Came Forward](https://news.ycombinator.com/item?id=47083145)**

⬆️ 505 • 💬 452 • 19h ago • [theshamblog.com](https://theshamblog.com/an-ai-agent-wrote-a-hit-piece-on-me-part-4/)

---

**[AI is not a coworker, it's an exoskeleton](https://news.ycombinator.com/item?id=47078324)**

Kasava is the AI-native platform purpose-built for product development. Plan, build, and monitor with AI-powered workflows.

⬆️ 485 • 💬 508 • 1d ago • [Kasava](https://www.kasava.dev/blog/ai-as-exoskeleton)

---

**[The Future of AI Software Development](https://news.ycombinator.com/item?id=47062534)**

fragments 18 Feb 2026

⬆️ 202 • 💬 143 • 2d ago • [martinfowler.com](https://martinfowler.com/fragments/2026-02-18.html)

---

**[How AI is affecting productivity and jobs in Europe](https://news.ycombinator.com/item?id=47068320)**

Artificial intelligence promises to reshape economies worldwide, but firm-level evidence on its effects in Europe remains scarce. This column uses survey data to examine how AI adoption affects productivity and employment across more than 12,000 European firms. The authors find that AI adoption increases labour productivity levels by 4% on average in the EU, with no evidence of reduced employment in the short run. The productivity benefits, however, are unevenly distributed. Medium and large firms, as well as firms that have the capacity to integrate AI through investments in intangible assets and human capital, experience substantially stronger productivity gains.

⬆️ 169 • 💬 132 • 1d ago • [CEPR](https://cepr.org/voxeu/columns/how-ai-affecting-productivity-and-jobs-europe)

---

**[What years of production-grade concurrency teaches us about building AI agents](https://news.ycombinator.com/item?id=47067395)**

Python and JavaScript/TypeScript AI frameworks are reinventing what telecom solved in 1986. What 40 years of production-grade concurrency teaches us about building AI agents.

⬆️ 135 • 💬 50 • 2d ago • [George Guimarães.](https://georgeguimaraes.com/your-agent-orchestrator-is-just-a-bad-clone-of-elixir/)

---

**[What is happening to writing? Cognitive debt, Claude Code, the space around AI](https://news.ycombinator.com/item?id=47061642)**

⬆️ 134 • 💬 130 • 2d ago • [resobscura.substack.com](https://resobscura.substack.com/p/what-is-happening-to-writing)

---

---

## YouTube Videos: "ai"

**[AI Bubble: ‘This is dumber than WeWork’ | Ed Zitron](https://www.youtube.com/watch?v=N_3X6qF2tT4)**

We're reaching this thing where we're realising that everybody made a huge mistake.” Author of Wheres You're Ed At and Host of ...

📺 The Tech Report

👁️ 43K • 👍 3K • 💬 910 • ⏱️ 26:37 • 5h ago

---

**[Local backlash against AI just started](https://www.youtube.com/watch?v=LhiQBOzpk7o)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 26K • 👍 2K • 💬 368 • ⏱️ 12:48 • 13h ago

---

**[9 AI Skills You MUST Have to Get Ahead of 99% of People](https://www.youtube.com/watch?v=BuwPnrMmhzQ)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4l2d0n7 Are you building an AI software ...

📺 Dan Martell

👁️ 52K • 👍 3K • 💬 128 • ⏱️ 19:58 • 1d ago

---

**[Google Just Dropped LYRIA 3: New AI Feature No One Expected](https://www.youtube.com/watch?v=UKRz33WdaH0)**

Google just introduced a new wave of AI systems inside Gemini that go far beyond simple generation. Alongside the release of ...

📺 AI Revolution

👁️ 43K • 👍 1K • 💬 46 • ⏱️ 12:14 • 23h ago

---

**[There is No AI Bubble.](https://www.youtube.com/watch?v=wDBy2bUICQY)**

Detailed sources: ...

📺 Species | Documenting AGI

👁️ 188K • 👍 11K • 💬 4K • ⏱️ 28:51 • 1d ago

---

**[“AI Arms Race Is COMING” - Musk DECLARES Retirement Savings Will Become USELESS](https://www.youtube.com/watch?v=W-jdh08zEGM)**

Elon Musk says saving for retirement may be pointless in the AI age. The panel pushes back: Will AI replace jobs, judges, and ...

📺 Valuetainment

👁️ 362K • 👍 6K • 💬 2K • ⏱️ 33:49 • 2d ago

---

**[I Need To Warn You About AI Psychosis](https://www.youtube.com/watch?v=S6kRGJlugiw)**

Dr. K's Guide empowers your mental health journey with evidenced-based resources and tools. Learn more: https://bit.ly/4tIuLvj ...

📺 HealthyGamerGG

👁️ 222K • 👍 12K • 💬 2K • ⏱️ 12:22 • 1d ago

---

**[AMC REJECTS AI Animated Movie](https://www.youtube.com/watch?v=5KzjrZKyP4g)**

After the AI animated short Thanksgiving Day film won a contest to premiere in theaters, the Internet got mad. Then, AMC Theaters ...

📺 Vailskibum

👁️ 22K • 👍 3K • 💬 648 • ⏱️ 2:50 • 2h ago

---

**[The 10 Most INSANE AI Films Created by Seedance 2.0](https://www.youtube.com/watch?v=KQIUp7H9Bkc)**

The 10 Most INSANE AI Films Created by Seedance 2 Seedance 2.0 by ByteDance just changed everything. In this video, we're ...

📺 RandomAI

👁️ 15K • 👍 247 • 💬 63 • ⏱️ 8:29 • 1d ago

---

**[Kelly Boesch Official Music AI Video - Salt On The Tide - 4K](https://www.youtube.com/watch?v=WbO0oDJk9t4)**

I was playing around in Midjourney with some images with an island feel. I love the dreamy feeling and the flamingos. There are ...

📺 Kelly Boesch AI Art

👁️ 14K • 👍 937 • 💬 52 • ⏱️ 2:55 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text`

⬇️ 105,189 • ❤️ 768 • 17h ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation`

⬇️ 123,344 • ❤️ 806 • 4d ago

---

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation`

⬇️ 173,716 • ❤️ 1,374 • 7d ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 509,647 • ❤️ 2,084 • 5d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 104,051 • ❤️ 622 • 1d ago

---

**[FireRed-Image-Edit-1.0](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0)**

*FireRedTeam*

FireRed-Image-Edit-1.0 is a general-purpose image editing model with strong instruction following and text style preservation capabilities, suitable for tasks like photo restoration and multi-image editing.

`image-to-image`

⬇️ 1,711 • ❤️ 220 • 6d ago

---

**[Qwen3-TTS-12Hz-1.7B-CustomVoice](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)**

*Qwen*

Qwen3-TTS-12Hz-1.7B-CustomVoice is a text-to-speech model supporting 10 languages with advanced control over tone, rate, and emotion. It features extreme low-latency streaming generation (as low as 97ms) and instruction-driven voice customization using 9 premium timbres, ideal for real-time interactive applications.

`text-to-speech`

⬇️ 877,971 • ❤️ 1,107 • 22d ago

---

**[Qwen3.5-397B-A17B-GGUF](https://huggingface.co/unsloth/Qwen3.5-397B-A17B-GGUF)**

*Unsloth AI*

Qwen3.5-397B-A17B is a multimodal large language model with a hybrid Gated Delta Network and Mixture-of-Experts architecture, excelling in vision-language tasks, multilingual understanding across 201 languages, and long-context reasoning up to 1M tokens.

`image-text-to-text` `396.3B`

⬇️ 66,442 • ❤️ 162 • 3d ago

---

**[MOSS-TTS](https://huggingface.co/OpenMOSS-Team/MOSS-TTS)**

*OpenMOSS*

MOSS-TTS Family is a suite of high-fidelity, expressive speech and sound generation models supporting multilingual TTS, long-form synthesis, voice design, sound effects, and real-time streaming.

`text-to-speech` `8.5B`

⬇️ 35,455 • ❤️ 283 • 7d ago

---

**[kani-tts-2-en](https://huggingface.co/nineninesix/kani-tts-2-en)**

*NineNineSix*

KaniTTS2-en is a 400M parameter English text-to-speech model optimized for real-time conversational AI, featuring a two-stage pipeline with LLM and FSQ audio codec, capable of voice cloning and achieving a ~0.2 RTF on high-end GPUs.

`text-to-speech` `370.0M`

⬇️ 2,362 • ❤️ 154 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 3 • 💬 0 • ⭐ 3,541 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 11 • 💬 1 • ⭐ 8,735 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 144 • 💬 19 • ⭐ 53,685 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[BitDance: Scaling Autoregressive Generative Models with Binary Tokens](https://huggingface.co/papers/2602.14041)**

*Yuang Ai, Jiaming Han, Shaobin Zhuang et al. (10 authors)*

🏢 ByteDance

BitDance is a scalable autoregressive image generator that uses binary visual tokens and diffusion-based methods to achieve efficient high-resolution image generation with improved speed and performance.

▲ 40 • 💬 3 • ⭐ 238 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2602.14041) • [💻 code](https://github.com/shallowdream204/BitDance) • [🔗 project](https://bitdance.csuhan.com/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 36 • 💬 1 • ⭐ 70,803 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 67 • 💬 1 • ⭐ 8,111 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 12 • 💬 1 • ⭐ 4,246 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 3 • 💬 0 • ⭐ 4,251 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 66 • 💬 3 • ⭐ 1,213 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 135 • 💬 6 • ⭐ 15,077 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `official` `official-website`

⭐ 15.8k • 🔱 1.7k • 2h ago

---

**[jamiepine/voicebox](https://github.com/jamiepine/voicebox)**

The open-source voice synthesis studio powered by Qwen3-TTS.

`TypeScript` `ai` `cuda` `mlx` `qwen3-tts` `qwen3-tts-ui`

⭐ 7.8k • 🔱 815 • 10d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 6.4k • 🔱 495 • 9d ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"

`Python`

⭐ 4.5k • 🔱 531 • 14h ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.8k • 🔱 176 • 17d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router empowering OpenClaw — by BlockRunAI

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 3.1k • 🔱 309 • 15h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 2.7k • 🔱 346 • 1d ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.6k • 🔱 176 • 3h ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `codex`

⭐ 2.3k • 🔱 113 • 3d ago

---

**[op7418/CodePilot](https://github.com/op7418/CodePilot)**

A native desktop GUI for Claude Code — chat, code, and manage projects visually. Built with Electron + Next.js.

`TypeScript` `ai` `anthropic` `claude` `claude-code` `desktop-app`

⭐ 2.1k • 🔱 222 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
