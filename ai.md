---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-12T19:30:14.422012+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 12, 2026 at 19:30 UTC  
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

**[Datacenter & AI water use is overblown](https://www.reddit.com/r/artificial/comments/1u4128s/datacenter_ai_water_use_is_overblown/)**

This keeps coming up over and over; for those interfacing with the anti-AI / anti-DC crowd, this article has some good talking points, about water, but also jobs and power. Data centers certainly do use water. They are basically warehouses of tightly packed, high-powered computers, and when computers run, they get hot. Most data centers—though not all—use water for cooling. But many of them use a “closed loop,” which doesn’t actually waste much, because the water is recycled repeatedly for the same purpose. And many statistics about data centers’ water use are misleading in that they include “indirect” water use too. The Substack writer Andy Masley found one particularly absurd example: In a widely cited paper, the amount of water that AI supposedly “wastes” includes the water that naturally evaporates off rivers and lakes in Washington State. Why? Because those rivers and lakes are dammed for hydroelectric plants, which generate electricity, which is then used by (among other things) a data center. The water-quality issue AOC pointed out in Georgia is not a general feature of data-center construction and appears to have affected only four households.

🔗 [The Atlantic](https://www.theatlantic.com/ideas/2026/06/ai-data-center-electricity-water/687521/) • 2h ago

---

**[Continual learning in mid-2026. A map of everyone trying to crack it: memory layers, "dreaming" agents, and the Post-Transformer models that learn inside the network](https://www.reddit.com/r/artificial/comments/1u40uys/continual_learning_in_mid2026_a_map_of_everyone/)**

Llion Jones said “2026 is the continual learning year” in the recent Post-Transformer debate. Sutton/Silver call the next phase the "era of experience”. What’s continual learning? Simply put, it’s a model’s ability to continuously improve as it gains experience – without exhibiting catastrophic forgetting. Essentially the stability-plasticity tradeoff for a reasoning model. Essentially it comes down to: where does the memory live? Outside the model. Memory files, vector dbs, graphs. Text is retrieved and pasted back into context. The model stays frozen. In the model's running state. Hidden states or fast weights that change while the model processes input. In the model's weights. What it actually knows. Encoded within the model weights to improve decision making patterns without forgetting. Dev docs today hint at #1 - memory outside the model. But the “2026 is continual learning year” notion does not come from it. Why? Part 1: The Memento stack (today’s stack) There are engineering fixes for the LLM’s memory problem. Julian Togelius & a16z compared it to Memento. In the movie, Leonard functions with his Polaroid and notes. But everyday he is the same man as day 0. Progress around these include: Anthropic's Dreaming: an async job to manage “memories”, explicitly modeled on sleep consolidation. Long context as memory: Visibly good, but with 3 problems. a) Position bias and "lost in the middle" challenge. b) Longer LLM windows come with bigger costs and we’re already discussing “token economics”. c). KV cache bottleneck, and everything evaporates when the request ends. Mem0, Letta, Zep: the popular memory-layer products from startups. AGENTS.md and git-style memory files: But, in this ETH Zurich paper (arXiv 2602.11988) it showed that LLM-generated context files actually reduce task success by about 3% while raising cost over 20%. And human-written ones barely helped too. Part 2: Continual learning, memory within the model (the big bet) Weight updates in large networks trigger catastrophic forgetting. A January 2026 paper tried continual fine-tuning on LRMs (arXiv 2601.18699) but catastrophic forgetting didn’t fade but rather increased. Promising directions that could solve this: TTT layers (arXiv 2407.04620, ICML 2025): the hidden state of the sequence layer is a small model, updated by gradient descent on tokens as they stream in. Matches or beats Transformer / Mamba baselines upto 1.3B params. Titans & Atlas: Titans add a neural long-term memory that decides what to store using a surprise signal. Atlas upgrades the memory's learning rule. Nested Learning + HOPE: Architecture updates different blocks at different frequencies. RNNs are also coming closer to Transformers via viral Memory Caching papers. Dragon Hatchling (BDH): From AI lab Pathway (arXiv 2509.26507). Working memory lives in Hebbian synapses rather than in a KV cache, allowing for an "infinite context window" without quadratic cost. AMI Labs, LFMs, etc. also mention continual learning but I didn’t find much specific info on them in this front. Current State and Future Outlook Where is continual learning in mid-2026? Solved with public access: nothing. Shipping in production: only the dossier stack, all frozen models. Demonstrated at research scale (< 2B params): TTT, Titans, Memory Caching, HOPE, and BDH. What would move the needle imo: Ship memory within the model with forgetting measurably controlled. Two questions though: What OpenAI is brewing in all of this? What’s the blocker to adoption for continual learning models: the missing breakthrough itself, or evals, serving economics, etc?

2h ago

---

**["Talk Show Host" [ft. Jibaro's Sara Silkin ] - Is this the future of motion capture? + Breakdown](https://www.reddit.com/r/artificial/comments/1u43wvs/talk_show_host_ft_jibaros_sara_silkin_is_this_the/)**

choreography and performance by: Sara Silkin vfx: myself In collaboration with Sara, I transformed an iPhone recording of this beautiful performance, into this multi-angle audiovisual piece. I managed to do in using no ultra-expensive equipment, nor full-production budget. All in a single platform + editing software. [A few years ago, this would have costed several thousand bucks.] Breakdown: I started from the original dance/performance video and split it into 3-10s clips if I wanted to use the camera angle present in reference image, or up until 30s if I wanted to preserve original camera angle from video source. Then I used Uisato Studio’s Kling Motion Control mode for generating the interventions. Inputs were: the original performance video as the reference video a target image with the robot / bio-tech aesthetic as the reference image for each section. You can use the "capture frame" function to intervene one of input video's frames using Gemini, or you can bring your own intervened [reference] images. As I said before, here's the place in which you can introduce different point-of-view for the interevened scene. a brief [balanced] prompt describing what I wanted beyond the motion transfer; "an avant-garde humanoid android performer dancing (...)" / "you might introduce subtle robotic precision while still following the original dance (...)" while standard the "std" kling-3 model performs really well, I went with "pro" for that tiny, but noticeable overall improvement In all sections I added some [10] overlapping frames at the start and the end between each, just in case I wanted to have some room for later transitioning between section on editing. For some particular parts of the piece, I created duplicated sections for having variations of a single shot. Once everything has been set I generated the clips in a single go, and then assembled the final piece in editing. Voilá, single-character motion capture on-a-budget²

47m ago

---

**[Google's Genie 3 turns a text prompt into a playable open world you can explore. It's rough now. Future of games, or a tech demo?](https://www.reddit.com/r/artificial/comments/1u3jlw6/googles_genie_3_turns_a_text_prompt_into_a/)**

Google's Project Genie went global this week and I have not stopped thinking about it. You type a sentence, or upload an image, and it generates an open world you can actually walk around in, in real time. No code, no game engine. Someone made a GTA-style open world of Istanbul and just strolled through it, with pedestrians and traffic reacting around them. The reality check: it is rough. Low framerate, laggy response, visible bugs. Right now it is a tech demo, not a game you would sit down and play. But the trajectory is the whole conversation. I keep going back and forth. One side: this is the beginning of the end for the traditional pipeline. If a sentence can spin up an explorable world, the engine, the assets, the studio, all of that stops being the gate. Anyone gets to make a world. The other side: interactive world models hit a wall fast. Consistency, object permanence, holding a world together for more than a few minutes, framerate. It could stay an impressive demo that never becomes a real game for years. My honest guess is the "walk around a generated world" part is genuinely new, but the gap from explorable demo to a game you would actually play is huge and might not close as fast as the hype says. Where do you land, real threat to game engines in a year or two, or a plateau? And what is the first world you would generate?

16h ago

---

**[This 2000s photo is 100% AI-generated. Be honest: how many details did you check before scrolling?](https://www.reddit.com/r/artificial/comments/1u3lmrn/this_2000s_photo_is_100_aigenerated_be_honest_how/)**

14h ago

---

**[Claude Fable made me realize I don't need a better model](https://www.reddit.com/r/artificial/comments/1u3acx4/claude_fable_made_me_realize_i_dont_need_a_better/)**

Hi everyone, I think I’ve reached a point where new LLM releases don’t really change much for me anymore. I tried Anthropic’s new Mythos-lite model, Fable, and played around with it for a while. I tested it on some security-related research for my own scripts and projects, and also used it for a few work-related tasks. And yes, it may have more parameters, a larger context window, better benchmarks, and all the usual improvements. But personally, I almost immediately switched back to Claude Opus for coding and Haiku for everyday work. For what I actually do, that combination is already more than enough. These models, my skills and prompting makes me more productive then 3 years ago, but it's more than enough. It reminds me of having an iPhone 14 while the iPhone 17 is coming out. You can see that the newer version is technically better, but you still think: “Nah, I’m good.” Curious if anyone else feels the same.

23h ago

---

**[What project are you working on and what problem does it solve?](https://www.reddit.com/r/artificial/comments/1u3xwkz/what_project_are_you_working_on_and_what_problem/)**

Hi all, Just curious, I've been noticing lately that a lot of people have some secret project that will change the industry and so on. Please share a bit if you're working on something

4h ago

---

**[How accurate are LLM's right now?](https://www.reddit.com/r/artificial/comments/1u43l5q/how_accurate_are_llms_right_now/)**

I've had people tell me that LLM's like ChatGPT and GROK aren't trustworthy or accurate. Lately, it feels like ChatGPT is more accurate about heavily discussed topics than most other sources, but that's just a feeling I have. Where can I find good information on just how accurate LLM's really are?

59m ago

---

**[Google DeepMind releases DiffusionGemma, a model that runs local AI 4x faster | Diffusion AI is most common in image generation, but it can make text outputs much faster.](https://www.reddit.com/r/artificial/comments/1u373y6/google_deepmind_releases_diffusiongemma_a_model/)**

🔗 [arstechnica.com](https://arstechnica.com/google/2026/06/googles-latest-diffusiongemma-open-ai-model-comes-with-a-4x-speed-boost/) • 1d ago

---

**[OpenAI, Visa Team Up to Let AI Agents Make Purchases Online](https://www.reddit.com/r/artificial/comments/1u42v64/openai_visa_team_up_to_let_ai_agents_make/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-06-10/openai-visa-team-up-to-let-ai-agents-make-purchases-online) • 1h ago

---

---

## Google News: "ai"

**[After SpaceX’s huge IPO, Americans’ financial future will be bound to AI](https://www.theguardian.com/business/2026/jun/12/ai-ipos-stock-market)**

They’re about to get more AI rammed down their throats, stuck into their pension plans and investment portfolios

The Guardian • 1h ago

---

**[Google Says Chinese Cybercrime Group Used Its A.I. in Scams](https://www.nytimes.com/2026/06/12/technology/google-lawsuit-china-ai-scams.html)**

The New York Times • 10h ago

---

**[Coinbase layoffs fuel debate over AI's role in job cuts](https://www.axios.com/local/san-francisco/2026/06/12/coinbase-layoffs-ai-job-losses-san-francisco-tech-workers)**

Axios • 24m ago

---

**[Tokenminimizing: Meta Moves to Curb Employee AI Usage as AI Costs Reach Billions](https://www.theinformation.com/articles/tokenminimizing-meta-moves-curb-employee-ai-usage-ai-costs-reach-billions)**

Meta Platforms plans to clamp down on skyrocketing AI costs inside the company by imposing limits on employees’ token usage, the company told staff in a memo on Tuesday, just weeks after it pushed them to adopt AI tools in their work. The company is building an internal platform to track ...

The Information • 33m ago

---

**[AI Watchdog: Free Music Archive](https://www.theatlantic.com/technology/2026/06/dataset-free-music-archive/687336/)**

None

The Atlantic • 1h ago

---

**[Capitol agenda: What Schumer told us about AI - Live Updates](https://www.politico.com/live-updates/2026/06/12/congress/chuck-schumer-ai-congress-00960335)**

Politico • 7h ago

---

**[SpaceX Rented Out Computing After Own Teams Had Trouble Using It](https://www.bloomberg.com/news/articles/2026-06-12/spacex-rented-out-computing-after-own-teams-had-trouble-using-it)**

Bloomberg.com • 59m ago

---

**[Introducing Claude Corps](https://www.anthropic.com/news/claude-corps)**

We’re launching Claude Corps, a national fellowship program for people early in their careers who are passionate about extending the benefits of AI to communities across America.

Anthropic • 1d ago

---

**[Opinion | Battery breakthroughs will lessen AI’s demand on the electricity grid](https://www.washingtonpost.com/opinions/2026/06/12/battery-breakthroughs-will-lessen-ais-demand-electricity-grid/)**

Pivoting from lithium to sodium-ion will reduce reliance on China.

The Washington Post • 53m ago

---

**[South Shore News: AI-generated newsletter has a paid audience](https://www.bostonglobe.com/2026/06/12/business/south-shore-local-news-ai/)**

While the audience is still small, it’s a sign that despite skepticism about the technology, there could be a larger audience for AI-generated local news — albeit with a limited focus.

The Boston Globe • 14h ago

---

---

## HackerNews: "ai"

**[AI agent bankrupted their operator while trying to scan DN42](https://news.ycombinator.com/item?id=48500012)**

⬆️ 1321 • 💬 475 • 14h ago • [Lan Tian @ Blog](https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian/)

---

**[German ruling declares Google liable for false answers in AI Overviews](https://news.ycombinator.com/item?id=48470248)**

A German regional court has ruled that Google is directly liable for the content of its AI search overviews. According to the court, previous limited liability protections for search engine operators don't apply to AI overviews. In this case, Google's AI had falsely linked two publishers to fraud and made claims that didn't appear in any of the linked sources. The ruling could set a precedent for AI-generated content liability worldwide.

⬆️ 1010 • 💬 537 • 2d ago • [The Decoder](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/)

---

**[AI agent runs amok in Fedora and elsewhere](https://news.ycombinator.com/item?id=48484584)**

Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user [...]

⬆️ 547 • 💬 242 • 1d ago • [LWN.net](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

---

**[Why AI hasn't replaced software engineers, and won't](https://news.ycombinator.com/item?id=48487540)**

Coding agents as normal technology

⬆️ 304 • 💬 348 • 1d ago • [normaltech.ai](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers)

---

**[Workers are spending over 6 hours a week botsitting AI, fueling job frustration](https://news.ycombinator.com/item?id=48490057)**

Workers are spending an average of 6.4 hours a week — almost a full working day — "botsitting" AI, pushing some to look for an exit, researchers say.

⬆️ 274 • 💬 220 • 1d ago • [Business Insider](https://www.businessinsider.com/botsitting-ai-hidden-human-labor-at-work-2026-6)

---

**[Apache Burr: Build reliable AI agents and applications](https://news.ycombinator.com/item?id=48477400)**

Apache Burr (Incubating) - develop AI applications that make decisions. Pure Python, no magic.

⬆️ 244 • 💬 114 • 2d ago • [burr.apache.org](https://burr.apache.org/)

---

**[Rich Sutton on AI creativity and discovery](https://news.ycombinator.com/item?id=48470581)**

A new and possibly controversial perspective:
In this video, I explain the sense in which generative AI trained by supervised learning is incapable of making novel discoveries.
https://t.co/LhAU6AyDkh

The text of the speech:

AI Creativity and Discovery

Good day ladies and

⬆️ 209 • 💬 124 • 2d ago • [X (formerly Twitter)](https://twitter.com/RichardSSutton/status/2061216087744946656)

---

**[A €0.01 bank transfer could compromise a banking AI agent](https://news.ycombinator.com/item?id=48476136)**

Blue41 helps regulated organizations monitor AI agent behavior, detect manipulation and misuse, and prove that sensitive workflows stay within safe boundaries.

⬆️ 206 • 💬 199 • 2d ago • [blue41.com](https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/)

---

**[Shall we play a game? My AI nuclear simulation](https://news.ycombinator.com/item?id=48495575)**

My AI nuclear simulation is out now, and it's a WOPR.

⬆️ 203 • 💬 193 • 23h ago • [kennethpayne.uk](https://www.kennethpayne.uk/p/shall-we-play-a-game)

---

**[Policy on the AI Exponential](https://news.ycombinator.com/item?id=48480719)**

⬆️ 167 • 💬 249 • 2d ago • [darioamodei.com](https://darioamodei.com/post/policy-on-the-ai-exponential)

---

---

## YouTube Videos: "ai"

**[Are We About to Lose Control of AI? (*sighs*)](https://www.youtube.com/watch?v=mbxuS6wlVR0)**

Cal Newport takes a critical look at recent AI News. More from Cal Download Cal's FREE guide to cultivating a deeper life: ...

📺 Cal Newport

👁️ 16K • 👍 595 • 💬 189 • ⏱️ 20:38 • 1d ago

---

**[Anthropic begged the world to stop AI… then shipped this](https://www.youtube.com/watch?v=1PBRhm5ZnjU)**

Render is the easiest place to ship full-stack apps and agents. The first 2000 people to use the code RENDER-FIRESHIP will get ...

📺 Fireship

👁️ 602K • 👍 22K • 💬 1K • ⏱️ 5:09 • 1d ago

---

**[OpenAI Slashing Prices for AI - OpenAI is Dead](https://www.youtube.com/watch?v=tZWLOPkpVvQ)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 24K • 👍 956 • 💬 224 • ⏱️ 17:22 • 19h ago

---

**[&quot;AI............is inevitable.&quot;](https://www.youtube.com/watch?v=M0-kPte_Erc)**

Nebula: https://go.nebula.tv/mancarryingthing Letterboxd: https://letterboxd.com/ManCarrying/ Twitter: ...

📺 Man Carrying Thing

👁️ 233K • 👍 23K • 💬 2K • ⏱️ 1:37 • 21h ago

---

**[The AI Breakthrough That Will Change Everything (Google DeepMind CEO Interview)](https://www.youtube.com/watch?v=HaZaFCHdkuk)**

Subscribe Demis Hassabis is the co-founder and CEO of Google DeepMind and Isomorphic Labs. He believes AI will help cure ...

📺 New Frontier

👁️ 14K • 👍 407 • 💬 50 • ⏱️ 13:45 • 1d ago

---

**[AI Did This.](https://www.youtube.com/watch?v=QGC40AfmgY0)**

ZTNA gives you the control you want in your network. Try it today with Threatlocker @ https://go.lowlevel.tv/threatlocker2026 ...

📺 Low Level

👁️ 80K • 👍 5K • 💬 373 • ⏱️ 11:00 • 6h ago

---

**[Anthropic Just Dropped Fable 5 And It’s Terrifying](https://www.youtube.com/watch?v=8TjCwdnZSp8)**

Anthropic just released Claude Fable 5, its first publicly available Mythos-class AI model, and the whole launch feels different.

📺 AI Revolution

👁️ 69K • 👍 2K • 💬 344 • ⏱️ 11:30 • 2d ago

---

**[I Asked AI to Build a Square Four Engine… Then I Made It Real](https://www.youtube.com/watch?v=x2-N50rQN-g)**

What started as an AI-generated concept turned into a real, running Square Four engine. From designing the crankshaft and ...

📺 Lets Learn Something

👁️ 55K • 👍 3K • 💬 326 • ⏱️ 41:56 • 1d ago

---

**[Prometheus CO-CEO Jeff Bezos: AI will result in labor scarcity, will raise standard of living](https://www.youtube.com/watch?v=NG0GoX0zMxQ)**

Prometheus Co-Founders and Co-CEOs Jeff Bezos and Vik Bajaj sits down with CNBC's David Faber to talk Prometheus' strategy ...

📺 CNBC Television

👁️ 35K • 👍 378 • 💬 185 • ⏱️ 2:45 • 1d ago

---

**[Do You Remember Me Before AI?](https://www.youtube.com/watch?v=0Af8LDWJzjc)**

I really created the T3 stack because I'm lazy but let me break down why that's important Want to sponsor a video? Learn more ...

📺 Theo - t3․gg

👁️ 536 • 👍 21 • 💬 2 • ⏱️ 0:56 • 29m ago

---

---

## HuggingFace Models: 🔥 Trending

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 20,669 • ❤️ 596 • 2d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 149,206 • ❤️ 1,916 • 8h ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 911,544 • ❤️ 961 • 8d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 4,054 • ❤️ 330 • 1d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 0 • ❤️ 296 • 9h ago

---

**[higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**

*Boson AI*

Higgs Audio v3 TTS is a 4B parameter autoregressive text-to-speech model supporting over 100 languages with zero-shot voice cloning. It offers fine-grained control over speech characteristics like emotion, style, and prosody via inline tokens, making it suitable for expressive conversational AI and voice agents.

`text-to-speech` `4.7B`

⬇️ 29,347 • ❤️ 383 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,393,894 • ❤️ 1,720 • 1mo ago

---

**[Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)**

*OBLITERATUS*

Gemma-4-12B-OBLITERATED is a text-generation model modified via weight surgery to achieve zero refusals while maintaining stock benchmark performance. It's designed for alignment research, red-teaming, and safety evaluation by removing safety guardrails.

`text-generation` `12.0B`

⬇️ 43,578 • ❤️ 250 • 3d ago

---

**[ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)**

*Ideogram*

Ideogram 4 (fp8) is a state-of-the-art, open-weight text-to-image foundation model trained from scratch. It excels in multilingual text rendering, layout control, and native 2k resolution image generation, making it ideal for design-oriented applications.

`text-to-image`

⬇️ 4,987 • ❤️ 501 • 9d ago

---

**[diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)**

*Unsloth AI*

DiffusionGemma-26B-A4B-it-GGUF is a 26B MoE multimodal generative model that produces text output from text, image, and video inputs using discrete diffusion. Optimized for speed and deployability, it leverages Gemma 4 architecture advancements for efficient token generation.

`image-text-to-text` `25.3B`

⬇️ 17,666 • ❤️ 208 • 4h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 92 • 💬 4 • ⭐ 85,422 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SIA: Self Improving AI with Harness & Weight Updates](https://huggingface.co/papers/2605.27276)**

*Prannay Hebbar, Yogendra Manawat, Samuel Verboomen et al. (7 authors)*

🏢 Hexo AI

A self-improving AI framework simultaneously updates both model weights and task-specific agent architecture through a language-model feedback agent across legal classification, GPU optimization, and biological data denoising tasks.

▲ 13 • 💬 2 • ⭐ 1,585 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27276) • [💻 code](https://github.com/hexo-ai/sia) • [🔗 project](https://hexolabs.com/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 16 • 💬 1 • ⭐ 81,931 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 227 • 💬 3 • ⭐ 6,004 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[InterleaveThinker: Reinforcing Agentic Interleaved Generation](https://huggingface.co/papers/2606.13679)**

*Dian Zheng, Harry Lee, Manyuan Zhang et al. (7 authors)*

InterleaveThinker enables interleaved generation capabilities for image generators through a multi-agent pipeline with planner and critic agents, achieving performance comparable to state-of-the-art models while enhancing reasoning benchmarks.

▲ 71 • 💬 1 • ⭐ 76 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2606.13679) • [💻 code](https://github.com/zhengdian1/InterleaveThinker) • [🔗 project](https://zhengdian1.github.io/InterleaveThinker-proj/)

---

**[Agents' Last Exam](https://huggingface.co/papers/2606.05405)**

*Yiyou Sun, Xinyang Han, Weichen Zhang et al. (308 authors)*

🏢 UC Berkeley

Agents' Last Exam (ALE) is a benchmark for evaluating AI agents on long-term, economically valuable real-world tasks across 13 industry clusters with 1K+ tasks, revealing significant gaps between benchmark performance and practical deployment.

▲ 323 • 💬 3 • ⭐ 592 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.05405) • [💻 code](https://github.com/rdi-berkeley/agents-last-exam) • [🔗 project](https://agents-last-exam.org/)

---

**[Robust-U1: Can MLLMs Self-Recover Corrupted Visual Content for Robust Understanding?](https://huggingface.co/papers/2606.08063)**

*Jiaqi Tang, Jianmin Chen, Youyang Zhai et al. (9 authors)*

Robust-U1 enhances multimodal large language models' robustness against visual corruptions through self-recovery capabilities that improve both visual quality and reasoning performance.

▲ 70 • 💬 2 • ⭐ 72 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2606.08063) • [💻 code](https://github.com/jqtangust/Robust-U1) • [🔗 project](https://huggingface.co/spaces/Jiaqi-hkust/Robust-U1)

---

**[Rethinking the Divergence Regularization in LLM RL](https://huggingface.co/papers/2606.09821)**

*Jiarui Yao, Xiangxin Zhou, Penghui Qi et al. (6 authors)*

🏢 Tencent-Hunyuan-Multimodal-RL

DRPO improves LLM reinforcement learning stability by replacing hard masks with smooth regularization that provides continuous gradient corrections beyond trust-region boundaries.

▲ 32 • 💬 4 • ⭐ 539 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.09821) • [💻 code](https://github.com/Tencent-Hunyuan/UniRL)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 166 • 💬 2 • ⭐ 67,332 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning](https://huggingface.co/papers/2606.10804)**

*Wenhao Yan, Fengjia Guo, Zhuoyi Yang et al. (4 authors)*

🏢 Z.ai

SCAIL-2 enables end-to-end character animation by directly transferring motion from driving videos without intermediate representations, using unified task decomposition and synthetic data generation.

▲ 40 • 💬 2 • ⭐ 311 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.10804) • [💻 code](https://github.com/zai-org/SCAIL-2) • [🔗 project](https://teal024.github.io/SCAIL-2/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 69.2k • 🔱 8.7k • 6h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 3.9k • 🔱 341 • 1d ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 3.5k • 🔱 364 • 7d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.2k • 🔱 338 • 1d ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 2.9k • 🔱 340 • 1d ago

---

**[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)**

Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP.

`TypeScript` `baas` `backend-as-a-service` `mcp` `open-source` `postgres`

⭐ 2.0k • 🔱 143 • 4h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 1.9k • 🔱 179 • 3d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.8k • 🔱 138 • 7d ago

---

**[Helvesec/rmux](https://github.com/Helvesec/rmux)**

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

`Rust` `agent` `ai` `cli` `linux` `macos`

⭐ 1.7k • 🔱 83 • 7d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.5k • 🔱 131 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
