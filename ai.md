---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-19T20:50:04.973410+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 19, 2026 at 20:50 UTC  
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

**[Politicians Are Trying to Change What Chatbots Say About Them](https://www.reddit.com/r/artificial/comments/1v0x0my/politicians_are_trying_to_change_what_chatbots/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/07/19/us/politics/chatbots-political-campaigns.html) • 3h ago

---

**[Can countries really regulate AI if they don’t control the compute?](https://www.reddit.com/r/artificial/comments/1v0xckk/can_countries_really_regulate_ai_if_they_dont/)**

I keep hearing AI governance discussed as if every country is sitting at the same table with roughly the same amount of influence. But most countries don’t control the chips, cloud infrastructure, data centers, or frontier models they’re being asked to regulate. They can write rules, but enforcement still depends heavily on infrastructure owned by a small number of governments and private companies. That makes me wonder whether this is really a regulation problem or an ownership problem. Can a country meaningfully govern advanced AI if it cannot independently inspect the systems, control the compute they run on, or enforce decisions against the companies operating them? I’m not saying regulation is pointless. I’m just not convinced legal authority means much without technical leverage behind it. Curious how people here see it. Does regulation eventually reshape who controls the infrastructure, or will the countries that own the compute always have the final say?

2h ago

---

**[Chinese open-weight model beats Opus 4.8 on some benchmarks, first time this has happened](https://www.reddit.com/r/artificial/comments/1v0x2za/chinese_openweight_model_beats_opus_48_on_some/)**

Moonshot released Kimi K3 July 17: 2.8 trillion parameters, fully open-source. Artificial Analysis independently ranks it ahead of Anthropic's Opus 4.8 on frontier benchmarks, first Chinese open-weight model to do that. Still behind Claude Fable 5 and GPT-5.6 overall, but Moonshot doesn't claim otherwise. Artificial Analysis and Arena.ai placed it there independently. It also topped web interface engineering evals in blind human-preference comparisons against Claude Fable. Three competing Chinese AI companies (Zhipu, MiniMax, Z.ai) lost 15-28% of their value in a single day. Nasdaq dropped, Nvidia briefly surrendered its most-valuable-company spot to Apple. Companies don't sell off like that over a research demo. Moonshot's moving to IPO within six months, targeting $30B+ valuation, pricing near Anthropic Sonnet levels. Open-weight models typically undercut on price. Moonshot isn't. Is one clean benchmark win against a closed frontier lab is enough to shift enterprise buying decisions? What would it actually take?

3h ago

---

**[How not to become lazy with AI?](https://www.reddit.com/r/artificial/comments/1v0pmhf/how_not_to_become_lazy_with_ai/)**

I think this is not really AI problem, its more about mindset and it repeats with every new technology. Calculators, Internet - every time people get a tool that thinks for them, some become lazy and some learn to use it without turning off their brain. AI is just the next round, much stronger round. Maybe some kind of the final boss. So probably there is no universal fix and everyone has to find their own way. How do you deal with it? Would like to hear different opinions.

8h ago

---

**[I built a voice lock screen, realized nobody needs it, then Microsoft showed me what I should actually be building.](https://www.reddit.com/r/artificial/comments/1v10z3d/i_built_a_voice_lock_screen_realized_nobody_needs/)**

Honest story because the pivot is the interesting part. Six months ago I wanted to replace the Windows lock screen with voice recognition. Not a passphrase, actual speaker verification. Say anything, it checks your voiceprint on your own machine, unlocks. A friend says the same words, rejected. Got it working. Then I realized nobody needs this. Windows Hello does biometric unlock for free. I was building a worse version of something that already exists. I almost quit the whole thing. Then I watched Microsoft Build 2026. They are turning Windows into an AI agent OS. Copilot, Manus, every agent racing to live on your machine and touch your files. And I noticed something that nobody seems to be talking about. Not one of them knows who is talking to it. They will execute commands from anyone sitting at your keyboard. Right now that is fine because AI agents cannot do much. But agents are getting access to files, money, communications, the ability to run code. When that happens, who is allowed to give it instructions becomes the most important security question on your machine. And nobody is answering it. That is what I am actually building now. Not a lock screen. An identity layer for AI agents on your PC. The idea: before any AI on your machine does anything, it knows it is you. Your voice is the key, verified locally, voiceprint never leaves your device. Then there is a permission dial you control. The AI has exactly the access you gave it, nothing more. You can set it to read only, or open apps, or act on its own while you are away. An AI with full access to your PC is terrifying. An AI with exactly the access you chose is something you would actually install. What works today: voice unlock and a voice assistant you just talk to. It answers out loud, knows who it is talking to, speech to text runs on your device so only text ever goes to the cloud. What I want to build next and I genuinely do not know which matters more to people so tell me: system awareness so you can ask it about your actual machine, why is my PC slow, what is using all my RAM, is this file worth keeping. Or the remote dial, control it from your phone, approve what it does while you are out, get pinged when something needs you. Or the permission system itself, building the actual trust model for what an AI agent is allowed to do on a personal machine. The limits right now: Ctrl Alt Del bypasses it because the deep Windows lock layer is not finished. No liveness detection so a recording of my voice would probably work. Assistant talks but does not act yet. Installer is unsigned. Zero real users outside me. That is why I am posting before building more. What would you actually let an AI do on your machine? Would identity verification change that? Tell me I am solving the wrong problem. [github.com/AadiSharma49/Senti] · [senti-kappa.vercel.app]

21m ago

---

**[the sprint review nobody wants to write is a join problem, not a writing problem](https://www.reddit.com/r/artificial/comments/1v103fu/the_sprint_review_nobody_wants_to_write_is_a_join/)**

The take that ai is good at summarizing and bad at judgment is basically right, and I think it undersells the summarizing half. Every sprint review I've written is about 20 minutes of writing sitting on top of an hour of pulling. Linear for what actually moved, GitHub for what shipped versus what's still open, Slack for the incident nobody ever filed a ticket for. The bit I'd add is that the pulling is exactly the part a model upgrade does nothing for. A smarter model still can't see three tools at once from inside a chat window. What changed it for me was moving the thing onto the desktop, where it could read all three and hand back a draft with deploy status already stitched in, plus an approval step before anything went near the channel. quality of the writeup went from fine to fine. The actual difference was that it existed on friday instead of monday. If your digest tool only reads one source, you've automated the 20 minutes and kept the hour.

57m ago

---

**[Using AI makes people less likely to admit they don't know something](https://www.reddit.com/r/artificial/comments/1v101tm/using_ai_makes_people_less_likely_to_admit_they/)**

Researchers found confidence increased even as accuracy fell

🔗 [theregister](https://www.theregister.com/ai-and-ml/2026/07/19/using-ai-makes-people-less-likely-to-admit-they-dont-know-something/5274567) • 59m ago

---

**[Best AI 3D generator in 2026, breakdown after testing 5 tools](https://www.reddit.com/r/artificial/comments/1v0zksv/best_ai_3d_generator_in_2026_breakdown_after/)**

A friend asked me which AI 3D generator to pick for his project and I realized I couldn't give him a straight answer based on anything I'd actually tested myself. So I spent about three weeks running the same 30 prompts through Meshy, Tripo, Rodin, Hunyuan, and CSM to figure out what each one is actually good at. Tested props, characters, hard surface objects, and paid attention to success rate, texture quality, mesh cleanliness, and how long it took to get something genuinely usable. The speed tools are Tripo and CSM. Tripo's Smart Mesh P1.0 generates in literal seconds and the output is clean enough for blockouts. Falls behind on texture detail and the animation library is smaller, but if you need volume and speed it's hard to beat. CSM was similar, fast and decent for simple shapes, but the style defaulted to something more realistic and getting it to match a stylized look took a lot of prompt engineering. Neither is what I'd pick for final quality. On the quality end Rodin Gen 2.5 has the highest peak when it lands, character detail is a tier above everything else. Costs more per generation, failure rate is higher, and the meshes need heavy cleanup, but for hero pieces nothing else touches it. Meshy sits in the middle, clean topology with quads, full PBR maps in one pass, decent plugin support. What held it back for me was consistency on complex organic shapes, some generations came out with surface artifacts that needed manual fixing. The built in printability stuff is genuinely unique though if 3D printing is your thing. Hunyuan is free and open source. Quality is competitive on good rolls but consistency is lower and there's no rig or animation pipeline. Bottom line is most people I know end up using two or three tools depending on the task. Rodin for hero shots, Tripo for speed, Hunyuan if you're on a zero budget, and Meshy as a decent all rounder that covers the most ground. Chasing a single "best" is the wrong question.

1h ago

---

**[AI saved me so much time...](https://www.reddit.com/r/artificial/comments/1v0on87/ai_saved_me_so_much_time/)**

...that I now spend that extra time fixing AI mistakes. Don't get me wrong I use AI almost every day, and it's incredibly useful. But I've noticed something funny: Instead of doing the work myself, I now spend my time fact-checking, rewriting, and correcting what AI generated. It still saves time overall, but it's definitely not the "press one button and you're done" future people imagined. What's one task AI actually saves you time on, and one task where it creates more work than it solves?

8h ago

---

**[I built Synapse – a local MCP server that gives Claude instant knowledge of your codebase](https://www.reddit.com/r/artificial/comments/1v0yfat/i_built_synapse_a_local_mcp_server_that_gives/)**

Synapse indexes your codebase locally and connects it to Claude Code via MCP. Ask Claude "how does the payment flow work?" and it searches your actual code instead of asking you to paste it. - 100% local — no cloud, no API key required - Uses nomic-embed-text-v1.5 + LanceDB - 2 MCP tools: recall (semantic search) and context (full file retrieval) - pip install synapse-mcp MIT licensed, open source. GitHub: https://github.com/nrkoka786/synapse

2h ago

---

---

## Google News: "ai"

**[The CIA Operative Who Spied on the U.A.E.—and Played a Role in Its AI Win](https://www.wsj.com/world/middle-east/cia-spy-united-arab-emirates-ai-49d909a8)**

WSJ • 19h ago

---

**[Could AI be conscious?](https://www.theguardian.com/technology/2026/jul/19/could-ai-be-conscious)**

Experts believe it’s at least possible. We urgently need a plan to navigate the ethical implications

The Guardian • 4h ago

---

**[CFOs Face a New Question This Earnings Season: What Do Your AI Tokens Cost?](https://www.bloomberg.com/news/newsletters/2026-07-19/cfos-face-questions-around-ai-token-costs-zm-jpm-fds)**

Bloomberg.com • 50m ago

---

**['Dr. Doom' Nouriel Roubini says we're headed for universal basic income or 'some form of socialism' as AI revolutionizes work—He calls that optimistic](https://fortune.com/2026/07/18/nouriel-roubini-universal-basic-income-socialism-ai-revolution-work-agi-government-stakes/)**

"Essentially, the government is going to take over some fraction of the big tech firms."

Fortune • 22h ago

---

**[Opinion | The Hunt for a Job Has Never Been Worse. These Applicants Are Fighting Back.](https://www.nytimes.com/2026/07/18/opinion/job-market-ai-employees.html)**

The New York Times • 1d ago

---

**[San Francisco restaurant gets angry backlash for AI menu images](https://www.sfgate.com/food/article/grind-unwind-ai-images-22348931.php)**

SFGATE • 9h ago

---

**[Meet the little-known companies behind America’s data center boom](https://www.nbcnews.com/tech/tech-news/data-center-developer-ai-boom-backlash-who-build-rcna353391)**

AI demand has brought billions in financing to little-known developers, while putting them at the center of fights over electricity, pollution and land.

NBC News • 9h ago

---

**[China’s Latest A.I. Breakthrough Threatens America’s Lead](https://www.nytimes.com/2026/07/17/business/china-ai-moonshot-kimi.html)**

The New York Times • 2d ago

---

**[Moonshot Plans IPO in Six Months After China AI Breakthrough](https://www.bloomberg.com/news/articles/2026-07-19/china-s-moonshot-plans-ipo-in-six-months-after-ai-breakthrough)**

Bloomberg.com • 4h ago

---

**[China’s Questionable Tech Strategy](https://www.theatlantic.com/international/2026/07/china-tech-sector-ai/687938/)**

Keeping out the world’s best tools promises to stymie innovation.

The Atlantic • 8h ago

---

---

## HackerNews: "ai"

**[Kaiser nurses say AI, surveillance are making their jobs and patient care worse](https://news.ycombinator.com/item?id=48952880)**

⬆️ 557 • 💬 376 • 1d ago • [localnewsmatters.org](https://localnewsmatters.org/2026/07/15/kaiser-nurses-say-ai-workplace-surveillance-are-making-their-jobs-and-patient-care-worse/)

---

**[NYC may require landlords and realtors to disclose the use of AI in listings](https://news.ycombinator.com/item?id=48962983)**

No more AI-edited listings without disclosures.

⬆️ 555 • 💬 256 • 22h ago • [PetaPixel](https://petapixel.com/2026/07/16/mayor-mamdani-says-landlords-cant-secretly-use-ai-images-to-advertise-properties/)

---

**[The state of open source AI](https://news.ycombinator.com/item?id=48947825)**

⬆️ 480 • 💬 354 • 2d ago • [stateofopensource.ai](https://stateofopensource.ai/)

---

**[Why do AI company logos look like buttholes? (2025)](https://news.ycombinator.com/item?id=48956924)**

A humorous exploration of the uncanny resemblance between AI company logos and human anatomy. Discover why circular, gradient-based designs dominate the AI industry, and what this design convergence tells us about branding in tech.

⬆️ 438 • 💬 145 • 1d ago • [VelvetShark](https://velvetshark.com/ai-company-logos-that-look-like-buttholes)

---

**[What AI did to stackoverflow in a graph](https://news.ycombinator.com/item?id=48956949)**

⬆️ 435 • 💬 520 • 1d ago • [data.stackexchange.com](https://data.stackexchange.com/stackoverflow/query/1953768#graph)

---

**[AI Mania Is Eviscerating Global Decision-Making](https://news.ycombinator.com/item?id=48964185)**

⬆️ 363 • 💬 207 • 19h ago • [ludic.mataroa.blog](https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/#fnref:3)

---

**[FAA lets Boeing sign off on 737 MAX, 787 airworthiness certificates again](https://news.ycombinator.com/item?id=48952439)**

The move is a vote of confidence in Boeing from the U.S. government.

⬆️ 196 • 💬 118 • 1d ago • [CNBC](https://www.cnbc.com/2026/07/17/faa-boeing-737-max-787.html)

---

**[Moonshot AI suspends new subscriptions due to Kimi K3 demand](https://news.ycombinator.com/item?id=48969291)**

Kimi K3 has received far more love than we expected, and our GPUs are feeling it.

Over the past 48 hours, demand has pushed close to the limits of our current capacity. To protect the experience of existing subscribers, we're temporarily pausing new subscriptions and

⬆️ 126 • 💬 45 • 4h ago • [X (formerly Twitter)](https://twitter.com/kimi_moonshot/status/2078855608565207130)

---

**[AI Meets Cryptography 2: What AI Found in OpenVM's ZkVM](https://news.ycombinator.com/item?id=48947714)**

We turned zkao (our AI auditor) on OpenVM, a state-of-the-art zkVM, and it found a critical soundness bug: the pairing check accepted a prover-supplied witness without proper subfield checking, which lets a malicious prover forge any pairing equality. It is fixed in OpenVM 1.6.0 and tracked as CVE-2026-46669. This is the second post in our series on bugs our agents found across open source cryptography.

⬆️ 99 • 💬 9 • 2d ago • [ZK/SEC Quarterly](https://blog.zksecurity.xyz/posts/openvm-bugs/)

---

**[VulnHunter: Capital One's agentic AI code security tool](https://news.ycombinator.com/item?id=48946692)**

Announcing the release of VulnHunter, an open-source AI code security tool with an agentic reasoning workflow developed by Capital One.

⬆️ 77 • 💬 35 • 2d ago • [Capital One](https://www.capitalone.com/tech/open-source/announcing-vulnhunter/)

---

---

## YouTube Videos: "ai"

**[Open Source AI Is Getting Too Big to Run](https://www.youtube.com/watch?v=qW5UDpHZBPw)**

Two major open-model releases arrived this week from very different directions. Both geographically and conceptually. Kimi K3 is ...

📺 Turing Post TV

👁️ 18K • 👍 667 • 💬 96 • ⏱️ 18:08 • 1d ago

---

**[Urgent Update- AI Sputnik Moment: Kimi K3 Released w/ Emad Mostaque | Ep. 272](https://www.youtube.com/watch?v=pSUyLfirP8Y)**

The mates chat with Emad Mostaque on an urgent update regarding the AI Sputnik Moment of Kimi K3 being released. Get access ...

📺 Peter H. Diamandis

👁️ 33K • 👍 2K • 💬 540 • ⏱️ 2:07:31 • 6h ago

---

**[AI Expert WARNS: Mass Job Loss Is Coming By 2027 - Tristan Harris](https://www.youtube.com/watch?v=GSoqVsdkvNA)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Tristan Harris warns that mass AI ...

📺 Neural Nutshell

👁️ 8K • 👍 220 • 💬 45 • ⏱️ 17:41 • 2d ago

---

**[China&#39;s AI just shocked Wall Street](https://www.youtube.com/watch?v=_fNhzoiZdNI)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 134K • 👍 7K • 💬 2K • ⏱️ 14:15 • 1d ago

---

**[I Cut the Internet and Let AI Read the File I Could Never Upload. It Caught the Leak.](https://www.youtube.com/watch?v=5slsNizN6MQ)**

Full post with a guide to clean sensitive documents: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 15K • 👍 498 • 💬 63 • ⏱️ 14:04 • 15h ago

---

**[China World AI Conference Mocked: No Western Nations Attend, Turns Into A “Beggar’s Fair”](https://www.youtube.com/watch?v=B1ThwmDJmn0)**

On July 17, the Shanghai Pudong World Expo Center hosted a heavily promoted event by Chinese authorities — the 2026 World ...

📺 China Observer

👁️ 27K • 👍 1K • 💬 323 • ⏱️ 16:56 • 20h ago

---

**[Is This the Biggest AI Release of 2026? (China’s New DeepSeek Moment)](https://www.youtube.com/watch?v=V0RsocRqjIU)**

China's Moonshot AI just released Kimi K3, the world's largest open-weight AI model. It rivals leading American systems, ...

📺 AI Revolution

👁️ 53K • 👍 2K • 💬 191 • ⏱️ 14:29 • 1d ago

---

**[China just beat Claude AI: Kimi K3](https://www.youtube.com/watch?v=2wDXtzIE7qw)**

Kimi K3 AI just beat Claude AI at coding. Join my private group https://techleadpro.com Your Community for Crypto, Stocks, ...

📺 TechLead

👁️ 69K • 👍 3K • 💬 474 • ⏱️ 8:08 • 1d ago

---

**[The Non-NVIDIA AI Card Everyone’s Ignoring](https://www.youtube.com/watch?v=NtYoTt-RB1s)**

This AI card isn't really a GPU, isn't NVIDIA, and its strangest feature may be the reason it matters. Try out ChatLLM ...

📺 Alex Ziskind

👁️ 23K • 👍 1K • 💬 91 • ⏱️ 13:06 • 6h ago

---

**[Meta’s AI Just Exposed the Whole Sh*tshow](https://www.youtube.com/watch?v=9BArC9Q39MI)**

Meta's AI-powered Ray-Ban glasses could transform everyday life for blind and visually impaired people, translating text, ...

📺 House of El: AI

👁️ 141K • 👍 11K • 💬 2K • ⏱️ 20:09 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 13,462 • ❤️ 1,136 • 3h ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 338,945 • ❤️ 782 • 1d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,262,894 • ❤️ 484 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 536,177 • ❤️ 4,161 • 17d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,118,995 • ❤️ 2,337 • 5d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 417 • 1d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 10,647 • ❤️ 455 • 9d ago

---

**[OvisOCR2](https://huggingface.co/ATH-MaaS/OvisOCR2)**

*ATH-MaaS*

OvisOCR2 is a compact 0.8B multimodal model for end-to-end document parsing, generating Markdown from document images. It excels at extracting text, formulas, tables, and visual regions in natural reading order, achieving state-of-the-art performance on benchmarks like OmniDocBench.

`image-text-to-text` `853.0M`

⬇️ 14,587 • ❤️ 188 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 2,084,530 • ❤️ 2,893 • 3mo ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 2,122,848 • ❤️ 2,119 • 16d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 29 • 💬 3 • ⭐ 13,258 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 93,667 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 9,275 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 12 • 💬 0 • ⭐ 9,233 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,304 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 17 • 💬 2 • ⭐ 20,945 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 257 • 💬 4 • ⭐ 13,153 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 44 • 💬 1 • ⭐ 1,305 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 75,104 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 60 • 💬 3 • ⭐ 1,473 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.0k • 🔱 1.0k • 2d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.0k • 🔱 223 • 7h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.6k • 🔱 365 • 2d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.3k • 🔱 269 • 11d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 991 • 🔱 17 • 11d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 948 • 🔱 59 • 5d ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 906 • 🔱 203 • 8d ago

---

**[HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC)**

OpenOPC: Build Your Personal AI-Native Company — Self-Built, Self-Run, Self-Grown

`Python`

⭐ 905 • 🔱 145 • 4d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 897 • 🔱 38 • 18d ago

---

**[ai4s-research/open-science](https://github.com/ai4s-research/open-science)**

Open Science Desktop — local-first, model-agnostic AI research workbench for macOS, Windows & Linux. Open-source Claude Science desktop alternative built on Tauri + MCP + agent skills.

`TypeScript` `ai-agent` `ai-for-science` `ai-scientist` `ai4s` `claude-science`

⭐ 834 • 🔱 96 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
