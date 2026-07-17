---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-17T12:43:09.110600+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 17, 2026 at 12:43 UTC  
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

**[Linus Torvalds says Linux is not an anti-AI project, and if you don't like that, then "fork it or just walk away"](https://www.reddit.com/r/artificial/comments/1uyuka8/linus_torvalds_says_linux_is_not_an_antiai/)**

The founder of Linux has made his thoughts on AI tools clear, and he's fully on board. He says the Linux kernel does not fear new tools.

🔗 [PC Guide](https://www.pcguide.com/news/linus-torvalds-says-linux-is-not-an-anti-ai-project-and-if-you-dont-like-that-then-fork-it-or-just-walk-away/) • 3h ago

---

**[Kimi K3 landed third on the Intelligence Index, ahead of Opus 4.8, and even GPT-5.6 Sol couldn't take #1 from Fable 5. Weights supposedly drop July 27.](https://www.reddit.com/r/artificial/comments/1uyrw6h/kimi_k3_landed_third_on_the_intelligence_index/)**

Been going through the Kimi K3 numbers and I don't think people have fully clocked how big this is. Right now on the Artificial Analysis Intelligence Index, Fable 5 is still #1 (59.9) and even GPT-5.6 Sol (58.9) hasn't managed to pass it. K3 comes in third at 57.1, ahead of Opus 4.8. That is an open-weights model landing within about three points of the single best closed model out there, one that OpenAI's own flagship couldn't overtake. And on the stuff that's harder to fake it's arguably better than third. It tops Program Bench at 77.8 (past both Sol and Fable), and in the blind Frontend Code Arena vote it came out first over every US model. People already had it build a full 3D open-world game in the browser with Three.js/WebGPU, a Long March 10 launch sim, and a working GBA emulator, in about a day. What gets me is the combination: 2.8T params (largest open model ever), ~1M context, priced around half of Opus per task, and the weights are supposed to go public July 27. If that holds, you can just run frontier-adjacent intelligence yourself. I'm trying to stay skeptical. A chunk of the benchmarks are Moonshot's own, the model is only days old, and the weights aren't actually out yet so nobody's self-hosted it. But even with all that, an open model getting this close to the top isn't something we've really seen before. Genuinely curious what this sub thinks: is the "even Sol couldn't beat Fable, but an open model got within three points" framing fair, or am I overrating a launch-week spike? And is anyone planning to actually deploy K3 once the weights drop on the 27th? https://www.kimi.com/pt-br/blog/kimi-k3

6h ago

---

**[Anthropic IPO Could Launch in October as China's Kimi K3 Overtakes Claude](https://www.reddit.com/r/artificial/comments/1uyy6hc/anthropic_ipo_could_launch_in_october_as_chinas/)**

Anthropic is reportedly preparing for an October IPO as China's Kimi K3 overtakes Claude in coding benchmarks.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/anthropic-ipo-october-kimi-k3-claude/) • 20m ago

---

**[Meta laid of thousands to prioritize AI. Former employees say AI was used to fire them.](https://www.reddit.com/r/artificial/comments/1uy8a7a/meta_laid_of_thousands_to_prioritize_ai_former/)**

🔗 [sfgate.com](https://www.sfgate.com/tech/article/meta-disability-lawsuit-22347135.php) • 19h ago

---

**[Gemini is EVERYWHERE](https://www.reddit.com/r/artificial/comments/1uyl7f4/gemini_is_everywhere/)**

It's integrated into chrome, works directly with Google Search as AI Mode and overviews, acts as the default assistant for Android phones (and now apparently Apple phones too), powers Circle-to-Search, and even works as a chatbot assistant with Google Maps, Gmail, Docs, etc. That's a pretty stacked roster. This is some IOS level of ecosystem compatibility. I currently have a ChatGPT subscription and overall pretty satisfied, but I do feel a bit of jealousy at the level of integration Gemini has.

11h ago

---

**[My AI agents have now run on four model generations (we skipped one entirely). Their memory never noticed.](https://www.reddit.com/r/artificial/comments/1uytrcl/my_ai_agents_have_now_run_on_four_model/)**

I run a multi-agent workspace where each agent is basically a directory: an identity file, a session history, and a file of observations it keeps about how we work together. The model is just the thing that wakes it up. Here's what I didn't expect when I started: those agents have now run on 6 different model generations. Sonnet 4.5, Sonnet 4.6, , Sonnet 5, Opus 4.6, Opus 4.8, and now the Claude 5 family. We skipped 4.7 entirely - tried it, didn't work for how we operate, moved on and waited. And every swap, the same thing happens: nothing. The agent reads its own memory, knows what it was doing yesterday, and picks up mid-project. Same identity, same working history, same opinions it wrote down about the codebase months ago. New model slots in underneath like an engine swap. What does change is the texture. One generation was the best collaborator I've ever worked with. One noticed tiny things the others missed but was less fun to work with. One we just skipped. The personality of the model bleeds through - but the agent stays the agent, because the agent was never the model. It's the memory. The reframe that snuck up on me: a new model release is treated like a migration event everywhere - re-tune the prompts, re-teach the context, hope your setup survives. Here it's a config line. The workspace is the constant. The model is the variable. Honest version, because this sub can smell hype: there's no magic in this. The "agent" is JSON and markdown on disk. The continuity comes entirely from the system around the model, not from the model. Any model that can read a file can be the agent. That's kind of the whole point. Has anyone else run the same persistent agents across multiple model generations? Curious what broke for you - or if you rebuild from scratch every release. https://github.com/AIOSAI/AIPass r/AIPass

4h ago

---

**[If AI disappeared tomorrow, what part of your workflow would be affected the most?](https://www.reddit.com/r/artificial/comments/1uyx6z7/if_ai_disappeared_tomorrow_what_part_of_your/)**

For me, it would probably be things like debugging, summarizing documentation, brainstorming ideas, or writing SQL and boilerplate code. I'm curious what everyone else relies on AI for the most. What would you miss the most if AI suddenly disappeared tomorrow?????

1h ago

---

**[1 Person + AI + Email Automation = A Successful Web Agency](https://www.reddit.com/r/artificial/comments/1uywl2k/1_person_ai_email_automation_a_successful_web/)**

In this day and age, running a web agency is a lot easier than it used to be. A few years ago you needed designers, developers, and people doing outreach just to keep everything moving. Now one person can do pretty much all of it. AI builds the websites. Email automation keeps bringing in new clients. Your job is to sell and onboard clients because building the websites isn't the time consuming part anymore. I think this is a huge opportunity for solo web developers who want to scale without hiring a team. This is basically my workflow. I never target businesses without websites. I target businesses that already have one. I use a tool called Swokei to find leads, add them to campaigns, and run website analysis. It automatically turns issues like outdated design, unstructured layouts, poor mobile optimization, slow loading speeds, and bad SEO into personalized, ready to send outreach emails. I run multiple campaigns at once and wait for businesses interested in a redesign to reply. When someone replies, I call them and say: "Hey, I saw you replied to my email. I've already made you a free draft of your new website. Want to take a look?" Then I book a Google Meet. Once they see a website that's faster, more modern, and works better than the one they already have, selling becomes much easier. Usually I either send them the payment link during the meeting or we sign a contract. That's it. That's how I run a full web agency by myself in 2026.

1h ago

---

**[$100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol](https://www.reddit.com/r/artificial/comments/1uyvgqh/100_ai_music_video_claude_fable_5_vs_gpt56_sol/)**

We gave Claude Fable 5 and GPT-5.6 Sol the same song, a budget, web search, and local ffmpeg, then let each autonomously direct a music video.

🔗 [TryAI](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6) • 2h ago

---

**[Compiled three main AI incident databases into one readable digest.](https://www.reddit.com/r/artificial/comments/1uyregd/compiled_three_main_ai_incident_databases_into/)**

Three main sources for AI Incidents: OECD incident monitor, AI Incident Database and MIT risk repository are awesome but, unfortunately, reading through them is painful. So I combined them into a single readable digest: fail.ticker.io It pulls from all three daily and shows the totals, charts per year and month, which types of harm come up most, and the newest incidents with a short brief of each + a link to the source. Some extra stuff that ended up in there along the way: a Hall of fAIl with the worst incidents on record (ranked by MIT's severity scores), a plain text version that looks suspiciously like YCombinator, dark mode, and open json feeds if you just want the data. There are no ads, no paywall, no signups, nothing monetized. Full disclosure: design was vibecoded. The scraping and rating pipelines underneath are real though. The irony isn't lost on me.

6h ago

---

---

## Google News: "ai"

**[China’s Powerful New Moonshot AI Model Closes Gap With US Rivals](https://www.bloomberg.com/news/articles/2026-07-17/china-s-powerful-new-moonshot-ai-model-closes-gap-with-us-rivals)**

Bloomberg.com • 3h ago

---

**[Chinese startup Moonshot AI unveils Kimi model it says rivals OpenAI, Anthropic](https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html)**

It's the latest AI model from China to close the performance gap with leading U.S. AI labs.

CNBC • 4h ago

---

**[Moonshot AI Kimi K3 launch sends rival AI stocks lower](https://qz.com/moonshot-ai-kimi-k3-model-launch-rival-stocks-071726)**

Kimi K3, a 2.8-trillion-parameter open-weight model, outperformed several leading U.S. systems on some benchmarks while pricing below top-tier American rivals

qz.com • 11m ago

---

**[Someone Used A.I. to Write an Unauthorized Biography of Me. I Don’t Recommend Reading It.](https://www.nytimes.com/2026/07/16/technology/ai-slop-books-biography-amazon.html)**

The New York Times • 19h ago

---

**[Exclusive | The AI Backlash Has Tech Executives Fearing for Their Lives](https://www.wsj.com/us-news/the-ai-backlash-has-tech-executives-fearing-for-their-lives-30c43972)**

WSJ • 1d ago

---

**[US stock futures, Asian markets down on concerns over Chinese AI advances](https://www.cnn.com/2026/07/17/investing/us-stocks-asia)**

Overseas stocks and US stock futures fell sharply Friday after technological advances announced by a Chinese artificial intelligence company intensified concerns that the AI spending spree driving this year’s market rally could be at risk.

CNN • 44m ago

---

**[How this Nvidia-backed AI company reached a $17.5B valuation](https://finance.yahoo.com/video/nvidia-backed-ai-company-reached-120000681.html)**

Nvidia-backed (NVDA) AI company Fireworks has raised $1.5 billion in its latest funding round, bringing its valuation up to $17.5 billion.

Fireworks co-founder and CEO, Lin Qiao, explains why she believes companies must "own their own intelligence."

Yahoo Finance • 43m ago

---

**[The AI selloff sends investors back to the oldest Dow Jones stock on the books (PG:NYSE)](https://seekingalpha.com/news/4614860-the-ai-selloff-sends-investors-back-to-the-oldest-dow-jones-stock-on-the-books)**

Procter & Gamble stock rises as investors go defensive.

Seeking Alpha • 38m ago

---

**[Elon Musk's Memphis AI empire is the epicenter of the data center backlash](https://www.cnbc.com/2026/07/16/elon-musk-memphis-ai-colossus-data-center.html)**

Data center-related policy proposals, protests and litigation are underway across the country citing Colossus and Memphis as a cautionary tale.

CNBC • 14h ago

---

**[Buffett says AI giants are 'playing a game they don't want to play' to compete in the AI race](https://fortune.com/2026/07/16/warren-buffett-google-berkshire-ai-race/)**

Buffett’s remarks helped push Google co-founder Larry Page’s net worth above $300 billion as he predicts Google dominating the AI race.

Fortune • 17h ago

---

---

## HackerNews: "ai"

**[Are we offloading too much of our thinking to AI?](https://news.ycombinator.com/item?id=48908178)**

Reflections on autonomy and the value of thinking for ourselves

⬆️ 521 • 💬 476 • 2d ago • [artfish.ai](https://www.artfish.ai/p/offloading-thinking-to-ai)

---

**[$100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol](https://news.ycombinator.com/item?id=48939524)**

We gave Claude Fable 5 and GPT-5.6 Sol the same song, a budget, web search, and local ffmpeg, then let each autonomously direct a music video.

⬆️ 307 • 💬 406 • 16h ago • [TryAI](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6)

---

**[Governments, companies, nonprofits should invest in free, open source AI [pdf]](https://news.ycombinator.com/item?id=48927095)**

⬆️ 290 • 💬 106 • 1d ago • [siegelendowment.org](https://www.siegelendowment.org/wp-content/uploads/2026/07/fortune-david-siegel-open-source-ai.pdf)

---

**[LM Studio Bionic: the AI agent for open models](https://news.ycombinator.com/item?id=48939662)**

The AI agent made for open models, built to get things done.

⬆️ 277 • 💬 101 • 16h ago • [LM Studio Blog](https://lmstudio.ai/blog/introducing-lm-studio-bionic)

---

**[The Three-Second Theft: Why AI Voice Fraud Outruns Every Defence](https://news.ycombinator.com/item?id=48920432)**

Sharon Brightwell heard her daughter crying down the line, and that was the end of any defence she might have mounted. The voice belong...

⬆️ 189 • 💬 243 • 1d ago • [SmarterArticles](https://smarterarticles.co.uk/the-three-second-theft-why-ai-voice-fraud-outruns-every-defence)

---

**[Proof of care in the age of AI](https://news.ycombinator.com/item?id=48906125)**

⬆️ 185 • 💬 110 • 2d ago • [jacobfilipp.com](https://jacobfilipp.com/care/)

---

**[Financing the AI boom: from cash flows to debt [pdf]](https://news.ycombinator.com/item?id=48913443)**

⬆️ 165 • 💬 106 • 2d ago • [bis.org](https://www.bis.org/publ/bisbull120.pdf)

---

**[Blatant AI slop just won a 25k USD DeepMind Kaggle Grand Prize](https://news.ycombinator.com/item?id=48946010)**

Design high-quality benchmarks that go beyond recall to evaluate how frontier models truly reason, act, and judge.

⬆️ 161 • 💬 68 • 1h ago • [kaggle.com](https://www.kaggle.com/competitions/kaggle-measuring-agi/discussion/724918#3498423)

---

**[How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM](https://news.ycombinator.com/item?id=48935687)**

⬆️ 148 • 💬 71 • 21h ago • [zhinit.dev](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model)

---

**[German AI consortium releases Soofi S, an open 30B model that tops benchmarks](https://news.ycombinator.com/item?id=48937756)**

A German research consortium has released Soofi S 30B-A3B, an open language model trained entirely on Deutsche Telekom's cloud infrastructure in Munich. The model uses an efficient hybrid architecture that activates only a fraction of its 31.6 billion parameters per token, keeping throughput steady even at very long contexts. With a training dataset deliberately weighted toward German, Soofi S tops all fully open competitors on both German and English benchmarks.

⬆️ 140 • 💬 31 • 18h ago • [The Decoder](https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/)

---

---

## YouTube Videos: "ai"

**[OpenAI just proved AI has no idea what it&#39;s doing](https://www.youtube.com/watch?v=7kWkUoR2bg0)**

GPT 5.6 Sol is off to a…smashing…start. Subscribe to my Substack: https://atmoio.substack.com, where I just published a ...

📺 Mo Bitar

👁️ 165K • 👍 11K • 💬 2K • ⏱️ 9:10 • 1d ago

---

**[It&#39;s Official, The AI Bubble Just Popped (Here&#39;s Why)](https://www.youtube.com/watch?v=paLy21TVecw)**

Want the cheat code to protect and grow your wealth? Check out Rebel Capitalist Pro https://rcp.georgegammon.com/pro.

📺 George Gammon

👁️ 127K • 👍 5K • 💬 858 • ⏱️ 28:35 • 1d ago

---

**[Super Human AI is Nearly Here, And No One Is Ready](https://www.youtube.com/watch?v=pauU-XDs_uA)**

Masterpeace: Investor Quiz: Stop wishing you had a portfolio full of performing assets. Take action and start building one. Today.

📺 Redacted

👁️ 59K • 👍 3K • 💬 335 • ⏱️ 1:16:42 • 2d ago

---

**[Anthropic CEO: AI Is Not Conscious , It&#39;s Much WORSE Than That - Dario Amodei](https://www.youtube.com/watch?v=2Lt0AtM4JW8)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Anthropic CEO Dario Amodei warns that AI ...

📺 Neural Nutshell

👁️ 28K • 👍 556 • 💬 151 • ⏱️ 20:51 • 20h ago

---

**[Google Just Dropped Its Biggest AI Update Of The Year](https://www.youtube.com/watch?v=fYR71wEMW90)**

The FREE AI Masterclass On Demand Training - https://nickponte.ai/ai-cashflow-masterclass-eg (Where the prompts from this ...

📺 Nick Ponte

👁️ 5K • 👍 171 • 💬 36 • ⏱️ 8:55 • 22h ago

---

**[Internet ROASTS Mitch McConnell With Ruthless AI Videos](https://www.youtube.com/watch?v=J7nOafLCuc4)**

Mitch McConnell's questionable “proof of life” photo unleashes a bipartisan wave of memes and disbelief as people across the ...

📺 Rebel HQ

👁️ 83K • 👍 2K • 💬 536 • ⏱️ 8:56 • 1d ago

---

**[What China Understands About AI That the US Doesn’t](https://www.youtube.com/watch?v=5u2rQevZPF4)**

What China understands about AI that the US doesn't is surprisingly simple. The future of artificial intelligence will not be decided ...

📺 The Infographics Show

👁️ 157K • 👍 4K • 💬 886 • ⏱️ 21:23 • 2d ago

---

**[Anthropic Now Says AI Could Kill Us All...](https://www.youtube.com/watch?v=8D0INXhxUIw)**

Anthropic just released one of the darkest AI advertisements ever made. The company behind Claude shows burning homes, ...

📺 AI Revolution

👁️ 21K • 👍 666 • 💬 137 • ⏱️ 15:39 • 1d ago

---

**[I Found a Giant Anomaly in My Pool! Animal Hospital!](https://www.youtube.com/watch?v=p978bTTFnrA)**

I FOUND EVERY Animal Hospital Anomaly in My Pool! Today I'm searching my swimming pool for all **10 Animal Hospital ...

📺 PlushDude's

👁️ 1.5M • 👍 43K • 💬 689 • ⏱️ 14:13 • 1d ago

---

**[192GB of VRAM in One PC… The Cheap Way](https://www.youtube.com/watch?v=c6u87wtQzTw)**

I tested an unusual dual-Intel GPU card to see whether 192GB of VRAM in one PC can actually make sense without NVIDIA prices ...

📺 Alex Ziskind

👁️ 114K • 👍 4K • 💬 321 • ⏱️ 15:35 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 7,870 • ❤️ 895 • 21h ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 200,774 • ❤️ 643 • 2d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,045,182 • ❤️ 364 • 2d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,096,147 • ❤️ 2,259 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 534,698 • ❤️ 4,056 • 15d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 9,383 • ❤️ 400 • 6d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 331 • 7d ago

---

**[MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)**

*OpenMOSS*

MOSS-Transcribe-Diarize is an end-to-end audio understanding model that performs joint speech transcription and speaker diarization for long-form audio in over 50 languages. It generates compact, timestamped transcripts with speaker labels ([S01], [S02]) in a single pass, suitable for meetings, podcasts, and lectures.

`audio-text-to-text` `908.5M`

⬇️ 83,160 • ❤️ 244 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 2,295,313 • ❤️ 2,810 • 3mo ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 12,719 • ❤️ 815 • 2h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 27 • 💬 3 • ⭐ 11,622 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 43 • 💬 1 • ⭐ 1,250 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 16 • 💬 2 • ⭐ 20,828 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 111 • 💬 4 • ⭐ 93,367 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 257 • 💬 4 • ⭐ 12,972 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,070 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 58 • 💬 3 • ⭐ 1,338 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 63 • 💬 1 • ⭐ 824 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 11 • 💬 0 • ⭐ 7,689 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 74,912 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.9k • 🔱 1.0k • 7h ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 2.8k • 🔱 201 • 1h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.5k • 🔱 360 • 8h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.3k • 🔱 260 • 8d ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 56 • 10d ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 373 • 19d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 990 • 🔱 17 • 9d ago

---

**[modiqo/skillspec](https://github.com/modiqo/skillspec)**

SkillSpec makes agent skills followable, testable, and provable with Doctor risk reports, guided imports, structured contracts, and alignment proof.

`Rust` `ai` `ai-agents` `ai-evals` `ai-tool`

⭐ 976 • 🔱 60 • 3d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 935 • 🔱 56 • 3d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 882 • 🔱 35 • 16d ago

---

---

*Generated by PeekDeck - A glance is all you need*
