---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-17T11:06:47.141574+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 17, 2026 at 11:06 UTC  
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

🔗 [PC Guide](https://www.pcguide.com/news/linus-torvalds-says-linux-is-not-an-anti-ai-project-and-if-you-dont-like-that-then-fork-it-or-just-walk-away/) • 1h ago

---

**[Kimi K3 landed third on the Intelligence Index, ahead of Opus 4.8, and even GPT-5.6 Sol couldn't take #1 from Fable 5. Weights supposedly drop July 27.](https://www.reddit.com/r/artificial/comments/1uyrw6h/kimi_k3_landed_third_on_the_intelligence_index/)**

Been going through the Kimi K3 numbers and I don't think people have fully clocked how big this is. Right now on the Artificial Analysis Intelligence Index, Fable 5 is still #1 (59.9) and even GPT-5.6 Sol (58.9) hasn't managed to pass it. K3 comes in third at 57.1, ahead of Opus 4.8. That is an open-weights model landing within about three points of the single best closed model out there, one that OpenAI's own flagship couldn't overtake. And on the stuff that's harder to fake it's arguably better than third. It tops Program Bench at 77.8 (past both Sol and Fable), and in the blind Frontend Code Arena vote it came out first over every US model. People already had it build a full 3D open-world game in the browser with Three.js/WebGPU, a Long March 10 launch sim, and a working GBA emulator, in about a day. What gets me is the combination: 2.8T params (largest open model ever), ~1M context, priced around half of Opus per task, and the weights are supposed to go public July 27. If that holds, you can just run frontier-adjacent intelligence yourself. I'm trying to stay skeptical. A chunk of the benchmarks are Moonshot's own, the model is only days old, and the weights aren't actually out yet so nobody's self-hosted it. But even with all that, an open model getting this close to the top isn't something we've really seen before. Genuinely curious what this sub thinks: is the "even Sol couldn't beat Fable, but an open model got within three points" framing fair, or am I overrating a launch-week spike? And is anyone planning to actually deploy K3 once the weights drop on the 27th? https://www.kimi.com/pt-br/blog/kimi-k3

4h ago

---

**[Meta laid of thousands to prioritize AI. Former employees say AI was used to fire them.](https://www.reddit.com/r/artificial/comments/1uy8a7a/meta_laid_of_thousands_to_prioritize_ai_former/)**

🔗 [sfgate.com](https://www.sfgate.com/tech/article/meta-disability-lawsuit-22347135.php) • 18h ago

---

**[Gemini is EVERYWHERE](https://www.reddit.com/r/artificial/comments/1uyl7f4/gemini_is_everywhere/)**

It's integrated into chrome, works directly with Google Search as AI Mode and overviews, acts as the default assistant for Android phones (and now apparently Apple phones too), powers Circle-to-Search, and even works as a chatbot assistant with Google Maps, Gmail, Docs, etc. That's a pretty stacked roster. This is some IOS level of ecosystem compatibility. I currently have a ChatGPT subscription and overall pretty satisfied, but I do feel a bit of jealousy at the level of integration Gemini has.

9h ago

---

**[My AI agents have now run on four model generations (we skipped one entirely). Their memory never noticed.](https://www.reddit.com/r/artificial/comments/1uytrcl/my_ai_agents_have_now_run_on_four_model/)**

I run a multi-agent workspace where each agent is basically a directory: an identity file, a session history, and a file of observations it keeps about how we work together. The model is just the thing that wakes it up. Here's what I didn't expect when I started: those agents have now run on 6 different model generations. Sonnet 4.5, Sonnet 4.6, , Sonnet 5, Opus 4.6, Opus 4.8, and now the Claude 5 family. We skipped 4.7 entirely - tried it, didn't work for how we operate, moved on and waited. And every swap, the same thing happens: nothing. The agent reads its own memory, knows what it was doing yesterday, and picks up mid-project. Same identity, same working history, same opinions it wrote down about the codebase months ago. New model slots in underneath like an engine swap. What does change is the texture. One generation was the best collaborator I've ever worked with. One noticed tiny things the others missed but was less fun to work with. One we just skipped. The personality of the model bleeds through - but the agent stays the agent, because the agent was never the model. It's the memory. The reframe that snuck up on me: a new model release is treated like a migration event everywhere - re-tune the prompts, re-teach the context, hope your setup survives. Here it's a config line. The workspace is the constant. The model is the variable. Honest version, because this sub can smell hype: there's no magic in this. The "agent" is JSON and markdown on disk. The continuity comes entirely from the system around the model, not from the model. Any model that can read a file can be the agent. That's kind of the whole point. Has anyone else run the same persistent agents across multiple model generations? Curious what broke for you - or if you rebuild from scratch every release. https://github.com/AIOSAI/AIPass r/AIPass

2h ago

---

**[Compiled three main AI incident databases into one readable digest.](https://www.reddit.com/r/artificial/comments/1uyregd/compiled_three_main_ai_incident_databases_into/)**

Three main sources for AI Incidents: OECD incident monitor, AI Incident Database and MIT risk repository are awesome but, unfortunately, reading through them is painful. So I combined them into a single readable digest: fail.ticker.io It pulls from all three daily and shows the totals, charts per year and month, which types of harm come up most, and the newest incidents with a short brief of each + a link to the source. Some extra stuff that ended up in there along the way: a Hall of fAIl with the worst incidents on record (ranked by MIT's severity scores), a plain text version that looks suspiciously like YCombinator, dark mode, and open json feeds if you just want the data. There are no ads, no paywall, no signups, nothing monetized. Full disclosure: design was vibecoded. The scraping and rating pipelines underneath are real though. The irony isn't lost on me.

4h ago

---

**[$100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol](https://www.reddit.com/r/artificial/comments/1uyvgqh/100_ai_music_video_claude_fable_5_vs_gpt56_sol/)**

We gave Claude Fable 5 and GPT-5.6 Sol the same song, a budget, web search, and local ffmpeg, then let each autonomously direct a music video.

🔗 [TryAI](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6) • 1h ago

---

**[Genie 3 Isn't About Soulless Games, It's About Whether Creative Craft Careers Survive the 'Vibes' Metric](https://www.reddit.com/r/artificial/comments/1uyrbgq/genie_3_isnt_about_soulless_games_its_about/)**

Google Genie 3 generating explorable worlds from a text prompt is genuinely strange to watch, and the tech demo framing actually undersells what's happening. Even in its rough state, it's compressing something that used to take hundreds of people years of work into a single prompt. Most of the conversation lands on whether games will look better or worse, whether it feels soulless, that kind of thing. But the more interesting question is what happens to the people who currently build this stuff for a living. Level designers, environmental artists, narrative designers who do worldbuilding. These aren't lowskill jobs that were always going to get automated eventually. They're craft jobs people spent years training for. The cost efficiency argument keeps coming up with robotics and physical labor, but it's starting to apply to creative industries in a way that feels different because the output is harder to measure. With a factory robot you can count units. With AIgenerated game content the metric is engagement and vibes, basically. Is there a version of this where the tools just expand what small teams can build, or does the trajectory pretty clearly lead toward massive headcount cuts at studios the moment the quality clears a certain bar? Genuinely not sure how to read it.

4h ago

---

**[American Communities Are Coming Together To Destroy Flock Surveillance Cameras](https://www.reddit.com/r/artificial/comments/1uxg3p4/american_communities_are_coming_together_to/)**

Thirty-nine Flock contracts were terminated in the first five months of 2026.

🔗 [Military.com](https://www.military.com/flock-surveillance-cameras-face-another-blow-lapd-wont-renew-contract) • 1d ago

---

**[Are there any serious AI developers here that might want to help me create an intuitive AI assisted filmmaking plugin/app](https://www.reddit.com/r/artificial/comments/1uysonn/are_there_any_serious_ai_developers_here_that/)**

I'm 40, I've done 3dcg since the late 90s, went to school at SCAD for animation, the guy who animated mufasa was one of my professors, I've been working on creating a totally independent animation/film professional pipeline to youtube for over a decade now. blah blah I don't think it's necessary to reinvent the wheel with this, so it would function basically as a plugin for existing AI film creation systems. To my knowledge there is no existing existing publicly available intuitive AI video creation software that goes beyond text prompts or crude image input. I'm an artist, but I know enough about AI and the technical side to know that what I envision with this plugin would be very much technically possible given current technology. All I'm talking about here is really just a way to have greater intuitive control over specific parameters in AI video production and greatly reduce the amount of computation required for preliminary work. Something where the user has more direct control over AI image creation beyond just text prompts. Basic sliders, image inputs. Let's say you need a scene of a revolutionary war battle. The user provides a rough sketch of the composition, something you would see in the storyboarding or thumbnail phase. The AI gives a very low burden computational creation of it, maybe very low rez or whatever. You then further define the environment, characters, etc. Instead of saying "make the sky slightly grayer" there is just a simple slider that you can adjust tone/tint/hue etc like in photoshop or similar products. Instead of saying "make me a fight scene!" you either build the assets yourself, or define them specifically with concept art/reference images. Direction is handled directly with animatics an storyboards. These are capabilities that I know probably exist somewhere, but they are not being shared with the public and would be relatively easy for random collaborators on the internet to create. What I'm talking about here from my understanding requires very little to basically no actual direct AI development, just a way to more intuitively and efficiently use existing capabilities. If people here want me to I can edit this original post an describe in excruciating detail exactly the features I would want down to the UI, specific functions, everything but the actual technical implementation. It might ultimately require some basic cooperation with an existing AI system, but that would be in the latest stages of development. Let me stress this is not a "do this for me" thing and this could even be an open source effort. I have a very very specific very extensive description of exactly the features it would need. Everything, including UI, functionality, literally everything but the technical implementation. Also to be specific, what I'm describing here is a professional level plugin. It's not meant for people who know nothing about filmmaking. Basically people at a graduate level from film school in terms of knowledge. Nor about creating new capabilities of AI, it's about using capabilities that I know exist within AI systems in an intuitive way with minimal computational burden on the systems.

3h ago

---

---

## Google News: "ai"

**[China's Moonshot unveils world's largest open AI model, closing in on US rivals](https://finance.yahoo.com/technology/ai/articles/chinas-moonshot-unveils-worlds-largest-020622030.html)**

At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rates that help you manage your financial life.

Yahoo Finance • 9h ago

---

**[China’s Powerful New Moonshot AI Model Closes Gap With US Rivals](https://www.bloomberg.com/news/articles/2026-07-17/china-s-powerful-new-moonshot-ai-model-closes-gap-with-us-rivals)**

Bloomberg.com • 1h ago

---

**[China just erased America's AI lead](https://www.axios.com/2026/07/17/china-ai-kimi-k3-open-source-anthropic-opus)**

Axios • 1h ago

---

**[Xi Promises AI for All in Debut at China’s Top Tech Summit](https://www.bloomberg.com/news/articles/2026-07-17/xi-vows-to-make-ai-for-all-in-debut-at-china-s-top-tech-summit)**

Bloomberg.com • 5h ago

---

**[Xi pitches China as AI partner to developing world, warns against risks and security overreach](https://www.cnbc.com/2026/07/17/x-china-ai-summit-risks-security.html)**

China will provide developing countries with 5,000 opportunities in AI training and seminar programs, as well as develop AI cooperation with various blocs.

CNBC • 5h ago

---

**[China’s Leader Pitches ‘Openness’ in Push to Shape the Path of A.I.](https://www.nytimes.com/2026/07/17/business/xi-jinping-china-ai.html)**

The New York Times • 45m ago

---

**[Exclusive | The AI Backlash Has Tech Executives Fearing for Their Lives](https://www.wsj.com/us-news/the-ai-backlash-has-tech-executives-fearing-for-their-lives-30c43972)**

WSJ • 1d ago

---

**[San Francisco Demands Apple and Google Delete AI ‘Nudify’ Apps From App Stores](https://www.wired.com/story/san-francisco-demands-apple-and-google-delete-ai-nudify-apps-from-app-stores/)**

The City Attorney’s Office sent the tech giants cease-and-desist letters this week telling them to stop profiting from 13 “face-swap” apps that are overwhelmingly used to target women and girls.

WIRED • 1h ago

---

**[EXCLUSIVE: Indonesia's copyright rewrite puts Google, AI platforms on notice](https://www.reuters.com/legal/litigation/indonesias-copyright-rewrite-puts-google-ai-platforms-notice-2026-07-17/)**

Reuters • 56m ago

---

**[Brunswick’s AutoCaptain Takes Over Boat Docking With AI Help](https://www.forbes.com/sites/edgarsten/2026/07/17/brunswicks-autocaptain-takes-over-boat-docking-with-ai-help/)**

Brunswick Corp's Simrad AutoCaptain is taking the scare out of docking and undocking recreational boats by doing the task autonomously using AI and other technology.

Forbes • 6m ago

---

---

## HackerNews: "ai"

**[Are we offloading too much of our thinking to AI?](https://news.ycombinator.com/item?id=48908178)**

Reflections on autonomy and the value of thinking for ourselves

⬆️ 521 • 💬 476 • 2d ago • [artfish.ai](https://www.artfish.ai/p/offloading-thinking-to-ai)

---

**[Governments, companies, nonprofits should invest in free, open source AI [pdf]](https://news.ycombinator.com/item?id=48927095)**

⬆️ 290 • 💬 106 • 1d ago • [siegelendowment.org](https://www.siegelendowment.org/wp-content/uploads/2026/07/fortune-david-siegel-open-source-ai.pdf)

---

**[$100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol](https://news.ycombinator.com/item?id=48939524)**

We gave Claude Fable 5 and GPT-5.6 Sol the same song, a budget, web search, and local ffmpeg, then let each autonomously direct a music video.

⬆️ 288 • 💬 382 • 15h ago • [TryAI](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6)

---

**[LM Studio Bionic: the AI agent for open models](https://news.ycombinator.com/item?id=48939662)**

The AI agent made for open models, built to get things done.

⬆️ 264 • 💬 91 • 14h ago • [LM Studio Blog](https://lmstudio.ai/blog/introducing-lm-studio-bionic)

---

**[The Three-Second Theft: Why AI Voice Fraud Outruns Every Defence](https://news.ycombinator.com/item?id=48920432)**

Sharon Brightwell heard her daughter crying down the line, and that was the end of any defence she might have mounted. The voice belong...

⬆️ 188 • 💬 242 • 1d ago • [SmarterArticles](https://smarterarticles.co.uk/the-three-second-theft-why-ai-voice-fraud-outruns-every-defence)

---

**[Proof of care in the age of AI](https://news.ycombinator.com/item?id=48906125)**

⬆️ 185 • 💬 110 • 2d ago • [jacobfilipp.com](https://jacobfilipp.com/care/)

---

**[Financing the AI boom: from cash flows to debt [pdf]](https://news.ycombinator.com/item?id=48913443)**

⬆️ 165 • 💬 106 • 2d ago • [bis.org](https://www.bis.org/publ/bisbull120.pdf)

---

**[How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM](https://news.ycombinator.com/item?id=48935687)**

⬆️ 139 • 💬 67 • 19h ago • [zhinit.dev](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model)

---

**[German AI consortium releases Soofi S, an open 30B model that tops benchmarks](https://news.ycombinator.com/item?id=48937756)**

A German research consortium has released Soofi S 30B-A3B, an open language model trained entirely on Deutsche Telekom's cloud infrastructure in Munich. The model uses an efficient hybrid architecture that activates only a fraction of its 31.6 billion parameters per token, keeping throughput steady even at very long contexts. With a training dataset deliberately weighted toward German, Soofi S tops all fully open competitors on both German and English benchmarks.

⬆️ 139 • 💬 30 • 17h ago • [The Decoder](https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/)

---

**[We don't use AI in any of our design or production processes](https://news.ycombinator.com/item?id=48927373)**

⬆️ 107 • 💬 113 • 1d ago • [mass-driver.com](https://mass-driver.com/article/from-human-hands)

---

---

## YouTube Videos: "ai"

**[OpenAI just proved AI has no idea what it&#39;s doing](https://www.youtube.com/watch?v=7kWkUoR2bg0)**

GPT 5.6 Sol is off to a…smashing…start. Subscribe to my Substack: https://atmoio.substack.com, where I just published a ...

📺 Mo Bitar

👁️ 160K • 👍 10K • 💬 2K • ⏱️ 9:10 • 1d ago

---

**[It&#39;s Official, The AI Bubble Just Popped (Here&#39;s Why)](https://www.youtube.com/watch?v=paLy21TVecw)**

Want the cheat code to protect and grow your wealth? Check out Rebel Capitalist Pro https://rcp.georgegammon.com/pro.

📺 George Gammon

👁️ 123K • 👍 5K • 💬 827 • ⏱️ 28:35 • 1d ago

---

**[I saw the future of AI... it scared me](https://www.youtube.com/watch?v=BIrQa_BH6AE)**

LinkedIn: https://www.linkedin.com/in/charles-broomfield/ Apply to work with me: https://forms.gle/XDEWyVhPeqhzEy2V8 I began ...

📺 Charles Level Up

👁️ 6K • 👍 348 • 💬 72 • ⏱️ 19:36 • 1d ago

---

**[Anthropic CEO: AI Is Not Conscious , It&#39;s Much WORSE Than That - Dario Amodei](https://www.youtube.com/watch?v=2Lt0AtM4JW8)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Anthropic CEO Dario Amodei warns that AI ...

📺 Neural Nutshell

👁️ 27K • 👍 529 • 💬 149 • ⏱️ 20:51 • 18h ago

---

**[Internet ROASTS Mitch McConnell With Ruthless AI Videos](https://www.youtube.com/watch?v=J7nOafLCuc4)**

Mitch McConnell's questionable “proof of life” photo unleashes a bipartisan wave of memes and disbelief as people across the ...

📺 Rebel HQ

👁️ 82K • 👍 2K • 💬 528 • ⏱️ 8:56 • 1d ago

---

**[Google Just Dropped Its Biggest AI Update Of The Year](https://www.youtube.com/watch?v=fYR71wEMW90)**

The FREE AI Masterclass On Demand Training - https://nickponte.ai/ai-cashflow-masterclass-eg (Where the prompts from this ...

📺 Nick Ponte

👁️ 5K • 👍 171 • 💬 35 • ⏱️ 8:55 • 20h ago

---

**[Anthropic Now Says AI Could Kill Us All...](https://www.youtube.com/watch?v=8D0INXhxUIw)**

Anthropic just released one of the darkest AI advertisements ever made. The company behind Claude shows burning homes, ...

📺 AI Revolution

👁️ 20K • 👍 659 • 💬 136 • ⏱️ 15:39 • 1d ago

---

**[3 FREE AI Video Generators 😱 | Best Free AI Video Generator 2026 | Text to Video AI](https://www.youtube.com/watch?v=QchMSh-xvfE)**

3 FREE AI Video Generators | Best Free AI Video Generator 2026 | Text to Video AI Instagram Link: ...

📺 AK - Educate 

👁️ 12K • 👍 543 • 💬 86 • ⏱️ 10:16 • 1d ago

---

**[Super Human AI is Nearly Here, And No One Is Ready](https://www.youtube.com/watch?v=pauU-XDs_uA)**

Masterpeace: Investor Quiz: Stop wishing you had a portfolio full of performing assets. Take action and start building one. Today.

📺 Redacted

👁️ 58K • 👍 3K • 💬 333 • ⏱️ 1:16:42 • 2d ago

---

**[China and Russia Are Behind the War on AI Data Centers](https://www.youtube.com/watch?v=Ug4nsMLQ0oc)**

Helix Sleep - Visit https://helixsleep.com/ben for this exclusive offer. Here's a good rule for life: if Xi Jinping and Vladimir Putin want ...

📺 Ben Shapiro

👁️ 22K • 👍 1K • 💬 633 • ⏱️ 16:31 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 7,870 • ❤️ 870 • 19h ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 200,774 • ❤️ 633 • 2d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,045,182 • ❤️ 361 • 2d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,096,147 • ❤️ 2,253 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 534,698 • ❤️ 4,048 • 15d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 9,383 • ❤️ 397 • 6d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 327 • 7d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 12,719 • ❤️ 815 • 1d ago

---

**[MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)**

*OpenMOSS*

MOSS-Transcribe-Diarize is an end-to-end audio understanding model that performs joint speech transcription and speaker diarization for long-form audio in over 50 languages. It generates compact, timestamped transcripts with speaker labels ([S01], [S02]) in a single pass, suitable for meetings, podcasts, and lectures.

`audio-text-to-text` `908.5M`

⬇️ 83,160 • ❤️ 239 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 2,295,313 • ❤️ 2,800 • 3mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 43 • 💬 1 • ⭐ 1,205 • 9d ago

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

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 63 • 💬 1 • ⭐ 811 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

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

▲ 83 • 💬 7 • ⭐ 80,973 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 58 • 💬 3 • ⭐ 1,338 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

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

▲ 11 • 💬 0 • ⭐ 7,613 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 74,845 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 67 • 💬 2 • ⭐ 61,017 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.9k • 🔱 1.0k • 5h ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 2.8k • 🔱 199 • 2h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.5k • 🔱 360 • 6h ago

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

⭐ 1.1k • 🔱 374 • 19d ago

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

⭐ 880 • 🔱 35 • 16d ago

---

---

*Generated by PeekDeck - A glance is all you need*
