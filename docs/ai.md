---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-10-25T19:53:19.162116+00:00'
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

**Last Updated:** October 25, 2026 at 19:53 UTC  
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

**[Forced to pick, Grok’s AI model chooses Republicans. OpenAI’s picks Democrats](https://www.reddit.com/r/artificial/comments/1xeuxt5/forced_to_pick_groks_ai_model_chooses_republicans/)**

A new study found Grok's AI overwhelmingly recommends Republican candidates while OpenAI's GPT favors Democrats, with the two AI models disagreeing in more than 90% of nearly 500 election races.

🔗 [TechCrunch](https://techcrunch.com/2026/10/24/forced-to-pick-groks-ai-model-chooses-republicans-openais-picks-democrats/) • 13h ago

---

**[Boston Dynamics employees petition to cancel $1.3M Spot robot sale to ICE](https://www.reddit.com/r/artificial/comments/1xe5pqg/boston_dynamics_employees_petition_to_cancel_13m/)**

Roughly 300 Boston Dynamics employees signed a petition urging the company to cancel a $1.3 million contract supplying Spot robot dogs to ICE through…

🔗 [Vector Wire](http://vectorwire.ai/article/boston-dynamics-employees-petition-to-cancel-1-3m-spot-robot-sale-to-ice-6ae86e) • 1d ago

---

**[Izwi 0.1.0: fully local voice AI (TTS, ASR, voice chat) for Mac, Linux, and Windows](https://www.reddit.com/r/artificial/comments/1xf7dyg/izwi_010_fully_local_voice_ai_tts_asr_voice_chat/)**

https://preview.redd.it/w59jjq3x7nxh1.png?width=1172&format=png&auto=webp&s=59d56bb30e5dad94ccf3f9525eb57cd19c56e5ef I’ve been building Izwi for a few months now and just shipped 0.1.0, the first stable release after months of public betas. It’s free and Apache-2.0. It’s a desktop app (plus a web UI, CLI and local server) for the voice side of local AI: Real-time voice conversations: local ASR → LLM → TTS TTS, voice cloning from a short sample, and voice design from a text description A Studio for long form audio like audiobooks Transcription with speaker diarization and forced alignment An OpenAI-compatible /v1 API (chat completions, audio/speech, audio/transcriptions), so existing code can point at localhost Models it runs today: TTS: Qwen3-TTS, Kokoro-82M, Fish Audio S2 Pro, VibeVoice, Voxtral TTS, LFM2.5 Audio ASR: Parakeet TDT v3, Whisper large-v3-turbo, Qwen3-ASR, Granite Speech 4.1, Nemotron 3.5 ASR, Voxtral Mini Diarization: Sortformer, Nemotron 3 diarization Chat: Qwen3.5, 3.6 and 3.8, LFM2.5 Inference runs natively in Rust on Candle, with our own Metal and CUDA work, so there’s no Python environment to manage. Repo: https://github.com/izwi-ai/izwi Download: https://izwiai.com I’d love feedback on which models to add next, and on anything that breaks on your hardware.

3h ago

---

**[AI Agent Containment Fails at Every Stack Layer, From Hypervisor to IAM](https://www.reddit.com/r/artificial/comments/1xf6xm5/ai_agent_containment_fails_at_every_stack_layer/)**

OpenAI's air-gapped training is necessary but insufficient: containment is failing from hypervisor escapes to overprivileged IAM roles faster than the…

🔗 [Vector Wire](http://vectorwire.ai/article/ai-agent-containment-fails-at-every-stack-layer-from-hypervisor-to-iam-948563) • 3h ago

---

**[Solidigm pulled its IPO and neocloud credit spreads are blowing out ahead of hyperscaler earnings](https://www.reddit.com/r/artificial/comments/1xf68po/solidigm_pulled_its_ipo_and_neocloud_credit/)**

Solidigm scrapped its IPO this week, and credit default swap spreads across neocloud companies have been widening while their stocks fall. The timing puts the AI buildout's funding under its first real stress test just days before the biggest hyperscalers report. Nvidia has moved beyond selling chips into effectively financing parts of the AI buildout, which puts an unusual amount of balance-sheet weight on one company. If neocloud borrowing costs keep climbing and new equity raises stay shut, the biggest buyers of Nvidia hardware start running low on cash to spend. Funds moved into defensives this week, and neocloud borrowers look like the group with the least cushion if capex guidance disappoints. Does Nvidia absorb the first hit, or do neocloud credit spreads crack before the stock moves?

3h ago

---

**[AgiBot's 110-Robot Sync Demo Proves Fleet Scheduling, Not Fleet Readiness](https://www.reddit.com/r/artificial/comments/1xf31xh/agibots_110robot_sync_demo_proves_fleet/)**

AgiBot's 110-humanoid swarm demo and DEEP Robotics' embodied-AI benchmarks show fleet coordination outpacing single-robot reliability, the real…

🔗 [Vector Wire](http://vectorwire.ai/article/agibot-s-110-robot-sync-demo-proves-fleet-scheduling-not-fleet-readiness-65e054) • 5h ago

---

**[GenAICode puts one API over Claude Code, Codex, Copilot, Cursor and Gemini CLI](https://www.reddit.com/r/artificial/comments/1xfbob2/genaicode_puts_one_api_over_claude_code_codex/)**

GenAICode is an open-source Apache-2.0 TypeScript toolkit that puts one API and CLI over coding agents such as Claude Code, Codex, Copilot CLI, Cursor, Gemini CLI, opencode, Muse, Mistral Vibe and Antigravity. Its README also lists a browser UI, an app-agent package and a run --verify command that sends a failing check back to the selected agent. The trade-off is that it does not hide provider ownership. The project says each agent keeps its own login, billing and sandbox. The latest 2.21.0 commit landed on October 25 at 6:00 PM Dubai time, and the repository currently shows 51 stars and 1 fork. For teams using more than one coding agent, this is a portability layer rather than a new model. It could reduce workflow switching, but the provider CLIs still define the limits. Source: https://github.com/gtanczyk/genaicode

13m ago

---

**[Is what I’m wanting even possible?](https://www.reddit.com/r/artificial/comments/1xfbnj5/is_what_im_wanting_even_possible/)**

Hi I really wanna basically have an ai to play this game for me it’s such a simple game and it’s a text based browser game so it’s literally the simplest most straight forward game for an ai to play no moving character nothing just understanding text and pressing buttons is this something I can get some help with PLEEEEASE I WANT IT BAD

13m ago

---

**[LLM Tokens and Context Windows: Why AI Forgets Your Conversation](https://www.reddit.com/r/artificial/comments/1xf53kg/llm_tokens_and_context_windows_why_ai_forgets/)**

I wrote a short article on LLM tokens and context windows—why an assistant can “forget” instructions that are still visible in your chat. It’s part of my Behind the AI Stack series. Give it a read and let me know what you think. Anything unclear or worth exploring further?

🔗 [medium.com](https://medium.com/@behind-the-stack/llm-tokens-and-context-windows-why-ai-forgets-your-conversation-9fe769f76629?sk=a766b0a282a91231ad9b33b8cdb0c024) • 4h ago

---

**[Why are people so pessimistic about AI potentially revolutionizing healthcare?](https://www.reddit.com/r/artificial/comments/1xfa9sn/why_are_people_so_pessimistic_about_ai/)**

So I attended a quantum discussion event where quantum computing and AI researchers discussed the future of the technologies and how they could potentially be extremely useful and helpful to scientists and doctors, and accelerate advances in medicine. I’m not one to think that all cancers and diseases will be cured in a decade like some clickbaiters claim but I think it can help speed up cures and treatments a lot faster than without it. But some people seem to think it’s all a sham, or that it will make things worse. So far Moderna had very successful results in their trial for the skin cancer vaccine and machine learning helped accelerate that, and knowing it’s possible opens a door for future research. Idk I’m pretty optimistic about the future of healthcare and medical field, what’s your thoughts on it?

1h ago

---

---

## Google News: "ai"

**[Put Your A.I. Agents to Work With These 5 Killer Tasks](https://www.nytimes.com/2026/10/25/technology/personaltech/openai-dots-meta-muse-killer-tasks.html)**

The New York Times • 10h ago

---

**[A Mathematician Reads the AI Future](https://www.theatlantic.com/ideas/2026/10/ai-math-human-future/689133/)**

The Atlantic • 7h ago

---

**[Elvis Presley’s rights holders sue Anthropic saying it trained AI on his music](https://www.nbcnews.com/tech/tech-news/elvis-presleys-rights-holders-sue-anthropic-saying-trained-ai-music-rcna605551)**

Anthropic has said that it “disagree[s] with the claims and intend[s] to defend this case fully.”

NBC News • 41m ago

---

**[Anthropic sued for allegedly using 274 Elvis Presley songs to train AI models](https://www.theguardian.com/us-news/2026/oct/25/elvis-presley-anthropic-lawsuit-ai-models-music)**

Authentic Brands Group says AI company infringed on rights of songs by the King such as Can’t Help Falling in Love

The Guardian • 1h ago

---

**[Elvis Presley rights holder sues Anthropic, says Claude trained on unauthorized songs](https://www.latimes.com/california/story/2026-10-25/elvis-rights-holder-sues-anthropic-says-songs-illegally-used-to-train-ai)**

The partnerships that hold rights to 274 Elvis Presley songs, including "Don't Be Cruel" and "All Shook Up," claim AI giant Anthropic illegally used the songs to train its AI tool Claude. Anthropic denied the claim.

Los Angeles Times • 11m ago

---

**[Nvidia discusses $2,000-per-GPU annual fee for software that 'runs agents on AI factories' — details unclear about potential overlaps, firm already charges more than twice that amount for its AI Enterprise software platform](https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform)**

Nvidia’s reported $2,000 annual fee per GPU could turn its software business into a multibillion-dollar revenue stream, but Huang has yet to reveal when the pricing could take effect.

Tom's Hardware • 6h ago

---

**[Nvidia’s Jensen Huang Says AI Agents Have Sent Token, GPU Demand ‘Through the Roof’: Gene Munster Sees 15 Million Bot Users Soaring to Billions](https://finance.yahoo.com/technology/ai/articles/nvidia-jensen-huang-says-ai-013010925.html)**

Nvidia Corp. CEO Jensen Huang stated that token consumption and graphics processing unit demand have gone “through the roof” due to artificial intelligence agents. Deepwater Asset Management Managing Partner Gene Munster supported this statement, predicting that daily bot users could...

Yahoo Finance • 18h ago

---

**[Nvidia (NVDA) Has Lost Its China AI Accelerator Market](https://finance.yahoo.com/technology/ai/articles/nvidia-nvda-lost-china-ai-190626796.html)**

Nvidia (NasdaqGS:NVDA) has effectively lost its China AI accelerator market after U.S. export controls restricted advanced GPU shipments. Specialist financiers are structuring large facilities backed by Nvidia GPU inventory, treating high-end chips as core collateral for AI infrastructure projects. Enterprise customers are rolling out liquid-cooled, rack-scale agentic AI factories, including deployments built around Supermicro server platforms. The collapse of Nvidia's China AI accelerator...

Yahoo Finance • 46m ago

---

**[To make AI morally good, tech companies are turning to religion. But some say it isn't that simple](https://techxplore.com/news/2026-10-ai-morally-good-tech-companies-1.html)**

Tech Xplore • 43m ago

---

**[No Signs of AI Payoff Outside the Tech Sector | The Daily Spark](https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector)**

Despite massive investments and widespread hype around artificial intelligence, the technology has delivered zero financial payoff to corporate America outside of tech. Subscribe for daily updates.

Apollo Global Management • 1d ago

---

---

## HackerNews: "ai"

**[No signs of AI payoff outside the tech sector](https://news.ycombinator.com/item?id=50224463)**

Despite massive investments and widespread hype around artificial intelligence, the technology has delivered zero financial payoff to corporate America outside of tech. Subscribe for daily updates.

⬆️ 598 • 💬 641 • 1d ago • [apollo.com](https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector)

---

**[America has lost 200k of jobs in media, film and the arts. How much is AI?](https://news.ycombinator.com/item?id=50226419)**

America is Losing Hundreds of Thousands of Jobs in Media, Film & the Arts. How Much is AI to Blame?

⬆️ 485 • 💬 514 • 20h ago • [apricitas.io](https://www.apricitas.io/p/ai-and-the-fall-of-the-creative-class)

---

**[Cerebras Deploys Trillion-Parameter AI Models](https://news.ycombinator.com/item?id=50227356)**

Learn how Cerebras maps trillion-parameter frontier models across WSE-3T wafers to deliver scalable inference at 1,000–2,000+ tokens per second.

⬆️ 333 • 💬 118 • 18h ago • [cerebras.ai](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras)

---

**[Why is AI generated language so hard to understand?](https://news.ycombinator.com/item?id=50223647)**

There is a widespread sense that AI-generated text has recently become harder to understand. In this study, we investigate a set of psycholinguistic features that are known to correlate with human processing difficulty (e.g., object relative clauses, long syntactic dependencies, low-frequency n-grams). Using a novel corpus of AI-generated text across diverse domains, we find that AI models use these difficult features more often than paraphrases generated by round-trip translation. Compared with human writing, all nine frontier and near-frontier models use more inanimate subjects with animate verbs and more low-frequency n-grams, and most also use longer dependencies, more stacked nouns, and more reduced object relatives in conversation; we also demonstrate substantial variation across model families. We propose and test a hypothesis as to why: while human language is optimized for successful communication, AI-generated text is increasingly optimized for other goals like math, code, and reasoning, in which there is a pressure for \textit{information density} rather than successful communication. We provide a proof-of-concept for this hypothesis by fine-tuning a language model under a length penalty, which leads to a divergence from human-like linguistic behavior. Our findings highlight the axes of misalignment between linguistic processing demands in humans and LLMs, and point toward possible remedies.

⬆️ 236 • 💬 191 • 1d ago • [arXiv.org](https://arxiv.org/abs/2610.29162)

---

**[Air Purifiers as White Noise Machines](https://news.ycombinator.com/item?id=50212507)**

White noise machines are widely used for sound masking, increasing privacy in offices and helping people sleep. The  classic approach is a fan in a box, though in the past ten years people have mostly switched over to electronic ones. But a fan is really a great approach; you just need to put it to better use: have the fan clean the air.  Instead of spinning a fan in free air to make noise, you ca

⬆️ 176 • 💬 167 • 2d ago • [jefftk.com](https://www.jefftk.com/p/air-purifiers-as-white-noise-machines)

---

**[The same AI request emits 8.5 times more CO2 in Texas than in Sweden](https://news.ycombinator.com/item?id=50205229)**

Swedish AI provider Berget AI releases an open-source method for calculating the carbon emissions of every individual AI request, developed with researchers from SEI, WattTime and Klimatkollen — and customers can now follow their emissions per request in the console.

⬆️ 142 • 💬 157 • 2d ago • [Berget AI](https://berget.ai/en/blog/per-request-co2-press-release)

---

**[Nikon photography contest winner loses title after scientists spot signs of AI](https://news.ycombinator.com/item?id=50229827)**

Nikon's 16th annual Small World in Motion contest is open to any movie or digital time-lapse photography taken through the microscope.

⬆️ 117 • 💬 51 • 10h ago • [TechSpot](https://www.techspot.com/news/114171-nikon-photography-contest-winner-loses-title-after-scientists.html)

---

**[AI use leads UC Berkeley math professor to see 'no point' in grading homework](https://news.ycombinator.com/item?id=50233304)**

Richard Borcherds, a UC Berkeley professor and Fields medalist, no longer grades his students’ homework. After seeing how many of his students used AI to consistently receive top scores, he

⬆️ 110 • 💬 173 • 3h ago • [Daily Cal | Berkeley news](https://www.dailycal.org/news/campus/academics/ai-use-leads-uc-berkeley-math-professor-to-see-no-point-in-grading-homework/article_bdf1eae2-c08b-491f-b9f1-81a7cea177de.html)

---

**[AI-Assisted Paper on Z-Library Cites a TorrentFreak Article That Doesn't Exist](https://news.ycombinator.com/item?id=50220204)**

A fresh academic paper on Z-Library cites a TorrentFreak article that doesn’t exist, and several other sources in the paper are also unfindable. The authors disclose that they used AI tools, which may explain what is going on. The use of AI in an academic paper on shadow libraries is also somewhat ironic, as rightsholders are suing AI companies for using these sites to train AI models.

⬆️ 97 • 💬 61 • 1d ago • [torrentfreak.com](https://torrentfreak.com/ai-assisted-paper-on-z-library-cites-a-torrentfreak-article-that-doesnt-exist/)

---

**[Most Americans Say AI Is Bad for Society, Oppose More Data Centers](https://news.ycombinator.com/item?id=50200843)**

Majorities see risks in AI and fewer see benefits.

⬆️ 91 • 💬 67 • 2d ago • [ABC News](https://abcnews.com/Politics/americans-ai-bad-society-oppose-data-centers-abcpostipsos/story?id=137414085)

---

---

## YouTube Videos: "ai"

**[Why so many AI developers are freaked out about AI](https://www.youtube.com/watch?v=OnXVUXktKxQ)**

AI developers don't know every detail about how frontier AIs work. And the gap between what's known and what AI is capable of is ...

📺 CNN

👁️ 28K • 👍 172 • 💬 83 • ⏱️ 9:05 • 5h ago

---

**[US banks scramble to control their AI agent activity](https://www.youtube.com/watch?v=oMpCkdFn754)**

FOX Business correspondent Darren Botelho has the latest on artificial intelligence reportedly acting independently on behalf of ...

📺 Fox News Clips

👁️ 205K • 👍 839 • 💬 669 • ⏱️ 2:04 • 1d ago

---

**[I Bought Every AI Scam on TikTok](https://www.youtube.com/watch?v=fLMXvFtPXog)**

Get free shipping on your order and 365-day returns. Now available in Canada and the UK, too. And when Quince asks where ...

📺 Layze

👁️ 932K • 👍 54K • 💬 6K • ⏱️ 42:13 • 23h ago

---

**[Featherweight Ep 22 - A WLW | GL ai series video](https://www.youtube.com/watch?v=MZflyPTPQJ0)**

Explore the Featherweight universe on YouArt: https://youart.ai/originals/the-veeverse-collection-featherweight Spotify: ...

📺 vee

👁️ 14K • 👍 844 • 💬 86 • ⏱️ 20:16 • 4h ago

---

**[Why Rust Is The New GOAT For AI](https://www.youtube.com/watch?v=R-tLX37Xgx8)**

The Copilot runtime was rewritten in Rust and starting a session fell from over five seconds to under 300 milliseconds. The Codex ...

📺 Better Stack

👁️ 187K • 👍 2K • 💬 293 • ⏱️ 6:24 • 1d ago

---

**[Researchers &amp; Bank Execs SOUND THE ALARM On AI](https://www.youtube.com/watch?v=T16ubDxRXi8)**

Reports reveal AI models pose major threats to bank accounts and critical infrastructure. Cenk Uygur and John Iadarola discuss ...

📺 The Young Turks

👁️ 125K • 👍 2K • 💬 836 • ⏱️ 12:29 • 1d ago

---

**[The AI Bubble&#39;s Worst Nightmare Just Became Reality](https://www.youtube.com/watch?v=R4dUq9yG2L8)**

Ship AI-generated code you can actually trust with CodeRabbit's free 14-day trial! Get started using my link: ...

📺 House of El: AI

👁️ 368K • 👍 14K • 💬 2K • ⏱️ 26:19 • 2d ago

---

**[The AI Bubble Just Cracked... And Oil Made It Worse](https://www.youtube.com/watch?v=FnyQgKGNWhI)**

"There's a scarcity of capital," Jensen Huang said on Thursday, the same day oil jumped four percent and the Nasdaq had its ...

📺 Why X

👁️ 52K • 👍 373 • 💬 55 • ⏱️ 18:31 • 1d ago

---

**[Who Really Pays for AI Data Centers?](https://www.youtube.com/watch?v=NyOeLB0WVNE)**

Go to https://surfshark.com/boyle or use code BOYLE at checkout to get 4 extra months of Surfshark! Americans now oppose new ...

📺 Patrick Boyle

👁️ 627K • 👍 13K • 💬 2K • ⏱️ 31:01 • 1d ago

---

**[Something Very Strange Is Happening in the Treasury Market (AI BUBBLE)](https://www.youtube.com/watch?v=OIQjt0KoluE)**

The AI boom is being funded with debt, and the numbers are getting hard to ignore. In this video I break down how much Big Tech ...

📺 MHFIN

👁️ 22K • 👍 326 • 💬 43 • ⏱️ 17:08 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)**

*DeepSeek*

DeepSeek-V4.1-Flash-1017 is an image-text-to-text model that enhances reasoning, coding, and agentic tasks with reduced execution time and output length. It excels in benchmarks like HLE, Terminal-Bench, and ProgramBench, offering improved performance-cost efficiency for complex applications.

`image-text-to-text` `763.2B`

⬇️ 85,275 • ❤️ 2,956 • 8d ago

---

**[flint](https://huggingface.co/RecursiveSI/flint)**

*Recursive Superintelligence, Inc. *

Flint is a 39.8B parameter Mixture-of-Experts language model optimized for coding agents, capable of code investigation, bug fixing, feature implementation, and test generation. It excels in reasoning and multi-turn tool use, achieving high scores on benchmarks like SWE-bench.

`text-generation` `39.8B`

⬇️ 6,444 • ❤️ 840 • 4d ago

---

**[flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)**

*Black Forest Labs*

FLUX 3 Image Klein is a 5.6B parameter model for ComfyUI enabling text-to-image generation and advanced image editing with multi-reference composition and bounding box control. It utilizes Qwen3-VL-4B-Instruct as its text encoder and supports features like text rendering within images.

`image-to-image`

⬇️ 660,874 • ❤️ 1,584 • 8d ago

---

**[Spark-X2.6-4B](https://huggingface.co/XHToken/Spark-X2.6-4B)**

*SparkLLM*

Spark-X2.6-4B is a compact, general-purpose language model optimized for on-device deployment, excelling in coding, agentic workflows, and long-context tasks with controllable thinking budgets for balanced performance and efficiency.

`text-generation` `4.1B`

⬇️ 3,488 • ❤️ 488 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of image-to-video, text-to-video, and video-to-video generation, offering advanced control for creative applications.

`image-to-video`

⬇️ 2,107,108 • ❤️ 9,309 • 14d ago

---

**[MOSS-Image-SFT](https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT)**

*OpenMOSS*

MOSS-Image-SFT is a supervised fine-tuned text-to-image diffusion model that generates images from natural language prompts, supporting structured control over text placement and object arrangement via tag sequences or JSON layouts. It's ideal for applications requiring precise visual composition and multilingual text rendering.

`text-to-image` `5.1B`

⬇️ 10,757 • ❤️ 723 • 4d ago

---

**[MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)**

*MiniMax*

MiniMax-M3.1-Flash is a native multimodal MoE model supporting text, image, and video inputs with a 1M token context window. It excels in agentic tasks, coding, and cybersecurity, featuring efficient inference through sparse attention and speculative decoding.

`image-text-to-text` `220.5B`

⬇️ 7,355 • ❤️ 343 • 2d ago

---

**[Qwen-Image-2.1-Uncensored-Quantized](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-Quantized)**

*Ahmet Benzer*

This is a quantized, uncensored text-to-image diffusion model based on Qwen-Image-2.1, optimized for local inference via GGUF and MLX formats. It supports various quantization levels (e.g., FP8, INT8, MLX 4-bit) for efficient use with tools like ComfyUI, balancing performance and VRAM usage.

`text-to-image` `7.1B`

⬇️ 2,235,846 • ❤️ 5,031 • 13d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic tasks, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,762,014 • ❤️ 18,386 • 2mo ago

---

**[drama-3](https://huggingface.co/fishaudio/drama-3)**

*Fish Audio*

Drama 3 is a 35B parameter text-to-speech model supporting multi-speaker generation, voice cloning, and natural language control across 40+ languages. It excels at generating multi-character scenes and long-form content with features like speaker tags and automatic long text chunking for streaming.

`text-to-speech` `35.9B`

⬇️ 21,375 • ❤️ 1,008 • 8d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 123 • 💬 2 • ⭐ 19,389 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 154 • 💬 6 • ⭐ 114,187 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 62 • 💬 4 • ⭐ 43,684 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 30 • 💬 9 • ⭐ 7,151 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**

*MOSI. AI*

🏢 OpenMOSS

MOSS-Image is an open diffusion transformer that combines high-fidelity synthesis with intent-aware prompt enhancement to generate text-rich, layout-coherent images, achieving state-of-the-art open-weight results on long-form text and layout benchmarks.

▲ 102 • 💬 4 • ⭐ 1,817 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2610.23374) • [💻 code](https://github.com/OpenMOSS/MOSS-Image) • [🔗 project](https://openmoss.ai/MOSS-Image/)

---

**[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**

*Guangyi Liu, Yong Liu, Jiangning Zhang*

🏢 Zhejiang University

Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is a kind of software, not a model, and until now had no open counterpart. This report defines the personal agent in five questions and three horizons. It reads how Muse is built from Meta's public record and a copy of its production prompt, each statement marked by its source. It then presents nanoMuse, the open-source counterpart under the GPL-3.0, one agent on every device a person owns, with hands on the phone's screen and the computer's. They share one conversation over a relay anyone can run; every action goes through a Sentinel, memory is files the person can read, and the model is their choice. Its size and cost are given as estimates. What is open, memory with provenance, an evaluation suite for the hands and an open model for them, is set out as a roadmap.

▲ 120 • 💬 3 • ⭐ 2,549 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2610.08699) • [💻 code](https://github.com/nano-muse/nanoMuse) • [🔗 project](https://nanomuse.cn/)

---

**[StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions](https://huggingface.co/papers/2610.17309)**

*Xialie Zhuang, Zunhai Su, Jia Pan et al. (6 authors)*

🏢 StartLux

StartLux-Decision introduces efficient and adaptive decision models using single-pass prediction and confidence-guided reasoning, trained via a three-stage pipeline with RLCD² reinforcement learning, and evaluates them on Decision Index and the DecisionPivot benchmark.

▲ 81 • 💬 4 • ⭐ 1,520 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2610.17309) • [💻 code](https://github.com/StartLuxLabs/StartLux-Decision) • [🔗 project](https://decision.startlux.com/)

---

**[Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training](https://huggingface.co/papers/2610.05416)**

*Shuyuan Tu, Qi Tian, Yinming Huang et al. (11 authors)*

🏢 Tencent Hunyuan

Prism accelerates native joint video-audio generation at 2K by using dynamic sparse attention guided by local visual variance and audio-visual cross-attention to preserve semantic coherence and cross-modal interactions.

▲ 23 • 💬 1 • ⭐ 1,092 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2610.05416) • [💻 code](https://github.com/Tencent-Hunyuan/Prism) • [🔗 project](https://francis-rings.github.io/Prism/)

---

**[Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://huggingface.co/papers/2610.14162)**

*Hermann Kumbong, Ishan S. Khare, Iddah Mlauzi et al. (9 authors)*

🏢 Stanford University

Next-Concept Modeling uses hierarchical discrete codes and parallel level-wise generation to accelerate diffusion language models while improving quality and reasoning performance.

▲ 16 • 💬 2 • ⭐ 997 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2610.14162) • [💻 code](https://github.com/HazyResearch/ncm) • [🔗 project](https://hazyresearch.stanford.edu/blog/2026-10-12-ncm)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 71 • 💬 4 • ⭐ 33,972 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

---

## GitHub Repositories: "ai"

**[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)**

一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

`TypeScript` `ai` `chinese` `content-curation` `daily-digest` `docker-compose`

⭐ 8.6k • 🔱 2.1k • 1d ago

---

**[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)**

A tiny friend in your Mac's notch and on your iPhone that keeps an eye on your AI coding agents: Claude Code, Codex, Cursor, Gemini CLI, Antigravity and more. Approve from the notch or your Lock Screen.

`Swift` `ai-agents` `anthropic` `antigravity` `claude` `claude-code`

⭐ 6.4k • 🔱 1.0k • 2d ago

---

**[CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)**

Your always-on AI coworkers that move between text, calls, and Slack.

`TypeScript`

⭐ 6.0k • 🔱 874 • 3d ago

---

**[omlahore/RemoveMacAI](https://github.com/omlahore/RemoveMacAI)**

Debloat macOS: turn off Apple Intelligence, analytics, ads and pop-ups. A native app and CLI, and every change can be undone.

`Swift` `ai-blocker` `anti-ai` `apple-intelligence` `cli` `debloat`

⭐ 5.2k • 🔱 152 • 11h ago

---

**[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)**

A comprehensive logo-design skill for Claude, Gemini CLI, Codex and other AI agents: principles, process, SVG craft, testing tools and a 1,400+ logo reference library.

`HTML` `agent-skills` `branding` `claude` `claude-skills` `codex`

⭐ 4.6k • 🔱 346 • 5d ago

---

**[QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)**

Answer me with HTML — an agent skill that answers hard questions with a one-page HTML you can actually read. 让 AI Agent 用一页 HTML 回答复杂问题。

`JavaScript` `agent-skill` `ai-agent` `claude-code` `claude-code-skill` `claude-skill`

⭐ 4.4k • 🔱 299 • 14h ago

---

**[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)**

A Claude Code / Codex plugin that helps you learn how to build while AI writes the code.

`Python`

⭐ 4.0k • 🔱 155 • 16d ago

---

**[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)**

Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

`C` `ai-agent` `airplay` `automation` `computer-use` `esp32`

⭐ 3.9k • 🔱 510 • 3d ago

---

**[Folkbench/folkbench](https://github.com/Folkbench/folkbench)**

AI API 中转站评测排行与切换工具：实测可用率、延迟与价格 · Open-source AI API relay benchmark, rankings & switcher for Claude Code / Codex

`Rust` `ai` `api-relay` `api-relay-pricing` `benchmark` `benchmarks`

⭐ 3.6k • 🔱 20 • 10h ago

---

**[openfilm/openfilm](https://github.com/openfilm/openfilm)**

The open source AI video agent: turns any coding agent into a video agent, with an editor to change anything it makes.

`TypeScript` `ai-video` `claude-code` `codex` `coding-agents` `html`

⭐ 2.8k • 🔱 263 • 5m ago

---

---

*Generated by PeekDeck - A glance is all you need*
